import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apple_search_ad.rest_authentications import CsrfExemptSessionAuthentication

from campaign.serializers import *
from campaign.models import *
from campaign.apple_search_ad_request_data import search_ad_api_requests

from campaign.apple_search_ad_reporting import AppleSearchAdReporting


class UpdateCampaignListAPIView(APIView):
    """
    Create UserCampaign API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get(self, request, *args, **kwargs):
        report = AppleSearchAdReporting()
        try:
            response = report.get_campaign_list()
        except Exception as e:
            return Response("Could not update campaign list. "+ str(e), status=status.HTTP_400_BAD_REQUEST)

        for campaign_data in response.json()['data']['reportingDataResponse']['row']:
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



