import base64
import os

from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apple_search_ad.rest_authentications import CsrfExemptSessionAuthentication


class TestAPIView(APIView):
    """
    Create UserCampaign API.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get(self, request, *args, **kwargs):
        with open(os.path.join(settings.BASE_DIR, 'h1.jpg'), "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return Response({"status" : "OK, THANKS FOR CALLING ME.", "image":encoded_string}, status=status.HTTP_200_OK)



