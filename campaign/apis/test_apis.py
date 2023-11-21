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
        return Response("OK, THANKS FOR CALLING ME.", status=status.HTTP_200_OK)



