from apple_search_ad.rest_authentications import CsrfExemptSessionAuthentication

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from campaign.serializers import *
from campaign.models import *
from campaign.db_manager import get_model_manager, get_bundle_id, clean_data

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
        bundle_id, message = get_bundle_id(data)
        if not bundle_id:
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        if data.get('attribution'):
            # app_user, created = AppUser.objects.get_or_create(identifier=data.get('user_identifier'))
            # campaign = Campaign.objects.get(campaign_id=data.get('campaign_id'))
            app_user, created = get_model_manager(AppUser, bundle_id).get_or_create(identifier=data.get('user_identifier'))
            campaign = get_model_manager(Campaign, bundle_id).get(campaign_id=data.get('campaign_id'))
            # fix the below line later
            # app = App.objects.first()
            app = get_model_manager(App, bundle_id).first()
            data['app_user'] = app_user
            data['campaign'] = campaign
            data['app'] = app
            data = clean_data(data)
            try:
                get_model_manager(UserConversionEvent, bundle_id).create(**data)
                return Response("Saved data Successfully.", status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        get_model_manager(OrganicUserData, bundle_id).create(data=data)
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
        bundle_id, message = get_bundle_id(data)
        if not bundle_id:
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        app_user, created = get_model_manager(AppUser, bundle_id).get_or_create(identifier=data.get("user_identifier"))
        user_conversion_event = get_model_manager(UserConversionEvent, bundle_id).filter(app_user=app_user).first()
        campaign = user_conversion_event.campaign
        # fix the below line later
        app = get_model_manager(App, bundle_id).first()
        data['app_user'] = app_user
        data["campaign"] = campaign
        data['app'] = app
        data = clean_data(data)
        # serializer = UserSubscriptionEventSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        try:
            get_model_manager(UserSubscriptionEvent, bundle_id).create(**data)
            return Response("Saved data Successfully.", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BulkUserDataCreateAPIView(APIView):
    """
    Create Any user event API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        data = request.data
        logger.info("...............................Logging bulk user data...................................")
        logger.info(str(data))
        bundle_id, message = get_bundle_id(data)
        if not bundle_id:
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        user_identifier = data.get("user_identifier")
        get_model_manager(BulkUserData, bundle_id).create(user_identifier=user_identifier, data=data)
        return Response("Saved data successfully.", status=status.HTTP_201_CREATED)


class BulkAttributionDataCreateAPIView(APIView):
    """
    Create Any user event API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request, *args, **kwargs):
        data = request.data
        logger.info("...............................Logging bulk attribution data...................................")
        logger.info(str(data))
        bundle_id, message = get_bundle_id(data)
        if not bundle_id:
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        user_identifier = data.get("user_identifier")
        get_model_manager(BulkAttributionData, bundle_id).create(user_identifier=user_identifier, data=data)
        return Response("Saved data successfully.", status=status.HTTP_201_CREATED)
