from campaign.models import *
from campaign.base_admin import *


class LogoAdminSite(admin.AdminSite):
    site_header = "Logo maker search ad admin site"


logo_admin_site = LogoAdminSite(name="logo_admin")


# this class is common for all the models in this database section
class LogoDbSectionAdmin(MultiDBModelAdmin):
    # other database identifier from settings
    using = 'logo'


# -----custom proxy models for django admin panel for all the models of logo database------------------

class LogoApp(App):
    # used this custom class for Campaign model in logo database
    class Meta:
        proxy = True


class LogoCampaign(Campaign):
    # used this custom class for Campaign model in logo database
    class Meta:
        proxy = True


class LogoAppUser(AppUser):
    # used this custom class for logo AppUser model in logo database
    class Meta:
        proxy = True


class LogoUserConversionEvent(UserConversionEvent):
    # used this custom class for logo UserConversionEvent model in logo database
    class Meta:
        proxy = True


class LogoUserSubscriptionEvent(UserSubscriptionEvent):
    # used this custom class for logo UserSubscriptionEvent model in logo database
    class Meta:
        proxy = True


class LogoOrganicUserData(OrganicUserData):
    # used this custom class for logo OrganicUserData model in logo database
    class Meta:
        proxy = True


# -------Custom Django admin classes for Logo Proxy models--------------------------------
class LogoAppAdmin(LogoDbSectionAdmin, AppModelAdmin):
    pass


class LogoCampaignAdmin(LogoDbSectionAdmin, CampaignModelAdmin):
    pass


class LogoAppUserAdmin(LogoDbSectionAdmin, AppUserModelAdmin):
    pass


class LogoUserConversionEventAdmin(LogoDbSectionAdmin, UserConversionEventModelAdmin):
    pass


class LogoUserSubscriptionEventAdmin(LogoDbSectionAdmin, UserSubscriptionEventModelAdmin):
    pass


class LogoOrganicUserDataAdmin(LogoDbSectionAdmin, OrganicUserDataModelAdmin):
    pass


# ---------register all the admin classes -----------------------------------
logo_admin_site.register(LogoApp, LogoAppAdmin)
logo_admin_site.register(LogoCampaign, LogoCampaignAdmin)
logo_admin_site.register(LogoAppUser, LogoAppUserAdmin)
logo_admin_site.register(LogoUserConversionEvent, LogoUserConversionEventAdmin)
logo_admin_site.register(LogoUserSubscriptionEvent, LogoUserSubscriptionEventAdmin)
logo_admin_site.register(LogoOrganicUserData, LogoOrganicUserDataAdmin)
