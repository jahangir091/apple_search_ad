
from django.urls import path

from campaign.apis.client_api_views import *
from campaign.apis.update_data_api_views import *
from campaign.apis.test_apis import TestAPIView


urlpatterns = [
    path('search-ad/v1/user-conversion-event', UserConversionEventCreateAPIView.as_view()),
    path('search-ad/v1/user-subscription-event', UserSubscriptionEventCreateAPIView.as_view()),
    path('search-ad/v1/update-campaigns-info', UpdateCampaignListAPIView.as_view()),
    path('server_test', TestAPIView.as_view()),
]
