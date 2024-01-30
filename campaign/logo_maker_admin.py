from django.conf import settings

from campaign.models import *
from campaign.base_admin import *


class LogoAdminSite(admin.AdminSite):
    site_header = "Logo maker search ad admin site"


logo_admin_site = LogoAdminSite(name="logo_admin")


# this class is common for all the models in this database section
class LogoDbSectionAdmin(MultiDBModelAdmin):
    # logo database alias from settings
    using = settings.LOGO_APP_DATABASE_ALIAS


# -------Custom Django admin classes for Logo DB models(tables)--------------------------------
class LogoAppModelCustomAdmin(LogoDbSectionAdmin, AppModelAdmin):
    pass


class LogoCampaignModelCustomAdmin(LogoDbSectionAdmin, CampaignModelAdmin):
    pass


class LogoAppUserModelCustomAdmin(LogoDbSectionAdmin, AppUserModelAdmin):
    pass


class LogoUserConversionEventModelCustomAdmin(LogoDbSectionAdmin, UserConversionEventModelAdmin):
    pass


class LogoUserSubscriptionEventModelCustomAdmin(LogoDbSectionAdmin, UserSubscriptionEventModelAdmin):
    pass


class LogoOrganicUserDataModelCustomAdmin(LogoDbSectionAdmin, OrganicUserDataModelAdmin):
    pass


class LogoBulkUserDataModelCustomAdmin(LogoDbSectionAdmin, BulkUserDataModelAdmin):
    pass


# ---------register all the admin classes -----------------------------------
logo_admin_site.register(App, LogoAppModelCustomAdmin)
logo_admin_site.register(Campaign, LogoCampaignModelCustomAdmin)
logo_admin_site.register(AppUser, LogoAppUserModelCustomAdmin)
logo_admin_site.register(UserConversionEvent, LogoUserConversionEventModelCustomAdmin)
logo_admin_site.register(UserSubscriptionEvent, LogoUserSubscriptionEventModelCustomAdmin)
logo_admin_site.register(OrganicUserData, LogoOrganicUserDataModelCustomAdmin)
logo_admin_site.register(BulkUserData, LogoBulkUserDataModelCustomAdmin)
