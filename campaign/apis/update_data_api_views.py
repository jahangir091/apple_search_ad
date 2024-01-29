import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apple_search_ad.rest_authentications import CsrfExemptSessionAuthentication

from campaign.serializers import *
from campaign.models import *
from campaign.apple_search_ad_request_data import search_ad_api_requests
from campaign.db_manager import get_model_manager, exist_db, get_app_name_from_db_alias
from logging import getLogger

logger = getLogger(__name__)


def get_token(app_name):
    url = search_ad_api_requests[app_name]['token']['url']
    params = search_ad_api_requests[app_name]['token']['params']
    response = requests.post(url, params=params)
    return response.json()['access_token']


class UpdateCampaignListAPIView(APIView):
    """
    Create UserCampaign API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        logger.info("...............................Logging update campaign ids api...................................")
        data = request.data
        db_alias = data.get("db_alias")
        if not exist_db(db_alias):
            return Response("Database alias does not exist.", status=status.HTTP_404_NOT_FOUND)
        app_name = get_app_name_from_db_alias(db_alias)
        access_token = get_token(app_name)
        url = search_ad_api_requests[app_name]['campaign_list']['url']
        body = search_ad_api_requests[app_name]['campaign_list']['body']
        headers = search_ad_api_requests[app_name]['campaign_list']['headers']
        headers["Authorization"] = "Bearer " + access_token
        response = requests.post(url, json=body, headers=headers)

        for campaign_data in response.json()['data']['reportingDataResponse']['row']:
            cmd = campaign_data['metadata']
            adamId = cmd["app"]["adamId"]
            # app = App.objects.get(adamId=adamId)
            app = get_model_manager(App, db_alias).get(adamId=adamId)
            # campaign, created = Campaign.objects.get_or_create(campaign_id=cmd['campaignId'], app=app)
            campaign, created = get_model_manager(Campaign, db_alias).get_or_create(campaign_id=cmd['campaignId'], app=app)
            campaign.name = cmd.get('campaignName', '')
            campaign.deleted = cmd.get('deleted', False)
            campaign.status = cmd.get('campaignStatus', '')
            campaign.serving_status = cmd.get('servingStatus', '')
            campaign.country = cmd.get('countryOrRegion', '')
            campaign.modification_time = cmd.get('modificationTime', None)
            if cmd.get('totalBudget', None):
                campaign.total_budget = cmd.get('totalBudget').get('amount', 0)
            if cmd.get('dailyBudget', None):
                campaign.daily_budget = cmd.get('dailyBudget').get('amount', 0)
            campaign.display_status = cmd.get('displayStatus', '')
            campaign.supply_sources = cmd.get('supplySources', '')
            campaign.add_channel_type = cmd.get('adChannelType', '')
            campaign.org_id = cmd.get('orgId', '')
            campaign.billing_event = cmd.get('billingEvent', '')
            campaign.save()

        return Response("Updated all the campaign details info", status=status.HTTP_200_OK)



