
from django.urls import path

from campaign.apis.client_api_views import *
from campaign.apis.update_data_api_views import *


urlpatterns = [
    path('search-ad/v1/user-conversion-event', UserConversionEventCreateAPIView.as_view()),
    path('search-ad/v1/user-subscription-event', UserSubscriptionEventCreateAPIView.as_view()),
    path('search-ad/v1/update-campaigns-info', UpdateCampaignListAPIView.as_view()),
    path('search-ad/v1/bulk-user-info', BulkUserDataCreateAPIView.as_view()),

]
