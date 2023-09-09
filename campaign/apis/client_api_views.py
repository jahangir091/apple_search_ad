from apple_search_ad.rest_authentications import CsrfExemptSessionAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from campaign.serializers import *
from campaign.models import *


class UserConversionEventCreateAPIView(APIView):
    """
    Create UserConversionEvent API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        data = request.data
        if data.get('attribution'):
            app_user, created = AppUser.objects.get_or_create(identifier=data.get('user_identifier'))
            campaign = Campaign.objects.get(campaign_id=data.get('campaign_id'))
            app = App.objects.get(bundle_id=data.get('bundle_id'))
            data['app_user'] = app_user.pk
            data['campaign'] = campaign.pk
            data['app'] = app.pk
            serializer = UserConversionEventSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response("Saved data Successfully.", status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        OrganicUserData.objects.create(data=data)
        return Response("No attribution found. May be Organic user.", status=status.HTTP_201_CREATED)


class UserSubscriptionEventCreateAPIView(APIView):
    """
    Create UserSubscriptionEvent API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        data = request.data
        app_user, created = AppUser.objects.get_or_create(identifier=data.get("user_identifier"))
        user_conversion_event = UserConversionEvent.objects.filter(app_user=app_user).first()
        campaign = user_conversion_event.campaign
        app = App.objects.get(bundle_id=data.get("bundle_id"))
        data['app_user'] = app_user.pk
        data["campaign"] = campaign.pk
        data['app'] = app.pk
        serializer = UserSubscriptionEventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Saved data successfullly", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
