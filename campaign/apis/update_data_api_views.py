import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apple_search_ad.rest_authentications import CsrfExemptSessionAuthentication

from campaign.serializers import *
from campaign.models import *
from campaign.apple_search_ad_request_data import search_ad_api_requests
import logging

log = logging.getLogger(__name__)


def get_token():
    url = search_ad_api_requests['token']['url']
    params = search_ad_api_requests['token']['params']
    response = requests.post(url, params=params)
    return response.json()['access_token']


class UpdateCampaignListAPIView(APIView):
    """
    Create UserCampaign API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get(self, request, *args, **kwargs):
        log.debug("...............................Logging update campaign ids api...................................")
        log.debug('logger is working fine')
        access_token = get_token()
        url = search_ad_api_requests['campaign_list']['url']
        body = search_ad_api_requests['campaign_list']['body']
        headers = search_ad_api_requests['campaign_list']['headers']
        headers["Authorization"] = "Bearer " + access_token
        response = requests.post(url, json=body, headers=headers)

        for campaign_data in  response.json()['data']['reportingDataResponse']['row']:
            cmd = campaign_data['metadata']
            adamId = cmd["app"]["adamId"]
            app = App.objects.get(adamId=adamId)
            campaign, created = Campaign.objects.get_or_create(campaign_id=cmd['campaignId'], app=app)
            campaign.name = cmd['campaignName']
            campaign.deleted = cmd['deleted']
            campaign.status = cmd['campaignStatus']
            campaign.serving_status = cmd['servingStatus']
            campaign.country = cmd['countryOrRegion']
            campaign.modification_time = cmd['modificationTime']
            campaign.total_budget = cmd['totalBudget']
            campaign.daily_budget = cmd['dailyBudget']['amount']
            campaign.display_status = cmd['displayStatus']
            campaign.supply_sources = cmd['supplySources']
            campaign.add_channel_type = cmd['adChannelType']
            campaign.org_id = cmd['orgId']
            campaign.billing_event = cmd['billingEvent']
            campaign.save()

        return Response("Updated all the campaign details info", status=status.HTTP_200_OK)



