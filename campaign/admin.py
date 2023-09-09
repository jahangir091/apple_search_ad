from django.contrib import admin

from campaign.models import *

admin.site.register(AppUser)
admin.site.register(App)
admin.site.register(Campaign)
admin.site.register(UserConversionEvent)
admin.site.register(UserSubscriptionEvent)
admin.site.register(OrganicUserData)