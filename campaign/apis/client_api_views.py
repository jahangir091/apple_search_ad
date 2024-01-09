from apple_search_ad.rest_authentications import CsrfExemptSessionAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from campaign.serializers import *
from campaign.models import *

from logging import getLogger

logger = getLogger(__name__)


class UserConversionEventCreateAPIView(APIView):
    """
    Create UserConversionEvent API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        data = request.data
        logger.info("...............................Logging user conversion event...................................")
        logger.info(str(data))
        if data.get('attribution'):
            app_user, created = AppUser.objects.get_or_create(identifier=data.get('user_identifier'))
            campaign = Campaign.objects.get(campaign_id=data.get('campaign_id'))
            # fix the below line later
            app = App.objects.first()
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
        logger.info("...............................Logging user subscription event...................................")
        logger.info(str(data))
        app_user, created = AppUser.objects.get_or_create(identifier=data.get("user_identifier"))
        user_conversion_event = UserConversionEvent.objects.filter(app_user=app_user).first()
        campaign = user_conversion_event.campaign
        # fix the below line later
        app = App.objects.first()
        data['app_user'] = app_user.pk
        data["campaign"] = campaign.pk
        data['app'] = app.pk
        serializer = UserSubscriptionEventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Saved data successfullly", status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BulkUserDataCreateAPIView(APIView):
    """
    Create Any user event API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        data = request.data
        logger.info("...............................Logging bulk user data...................................")
        logger.info(str(data))
        user_identifier = data.get("user_identifier")
        BulkUserData.objects.create(user_identifier=user_identifier, data=data)
        return Response("Saved data successfully.", status=status.HTTP_201_CREATED)
