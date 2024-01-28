from campaign.models import *
from campaign.base_admin import *


admin.site.register(App, AppModelAdmin)
admin.site.register(Campaign, CampaignModelAdmin)
admin.site.register(AppUser, AppUserModelAdmin)
admin.site.register(UserConversionEvent, UserConversionEventModelAdmin)
admin.site.register(UserSubscriptionEvent, UserSubscriptionEventModelAdmin)
admin.site.register(OrganicUserData, OrganicUserDataModelAdmin)
admin.site.register(BulkUserData, BulkUserDataModelAdmin)
admin.site.register(BulkAttributionData, BulkAttributionDataModelAdmin)
