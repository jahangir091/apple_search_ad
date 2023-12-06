from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils.translation import gettext_lazy as _


class SearchAdCampaignBaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DailyData(SearchAdCampaignBaseModel):
    class DataType(models.TextChoices):
        CAMPAIGN = 'CM', _('Campaign')
        KEYWORD = 'KW', _('Keyword')
        AD_GROUP = 'AG', _('Ad Group')
        SEARCH_TERM = 'ST', _('Search Term')
        AD = 'AD', _('Ad')
    data_type = models.CharField(max_length=20, choices=DataType.choices, blank=True, null=True)
    impressions = models.IntegerField(default=0)
    taps = models.IntegerField(default=0)
    installs = models.IntegerField(default=0)
    new_downloads = models.IntegerField(default=0)
    re_downloads = models.IntegerField(default=0)
    lat_on_installs = models.IntegerField(default=0)
    lat_off_installs = models.IntegerField(default=0)
    ttr = models.FloatField(default=0)
    avg_cpa = models.FloatField(default=0)
    avg_cpt = models.FloatField(default=0)
    avg_cpm = models.FloatField(default=0)
    local_spend = models.FloatField(default=0)
    conversion_rate = models.FloatField(default=0)
    date = models.DateTimeField(blank=True,null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class App(SearchAdCampaignBaseModel):
    name = models.CharField(max_length=100)
    adamId = models.CharField(max_length=50, blank=True, null=True)
    bundle_id = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Campaign(SearchAdCampaignBaseModel):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, blank=True, null=True)
    campaign_id = models.CharField(max_length=50, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    status = models.CharField(max_length=50, blank=True, null=True)
    serving_status = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    modification_time = models.DateTimeField(blank=True, null=True)
    total_budget = models.FloatField(default=0, null=True)
    daily_budget = models.FloatField(default=0, null=True)
    display_status = models.CharField(max_length=50, blank=True, null=True)
    supply_sources = models.CharField(max_length=500, blank=True, null=True)
    add_channel_type = models.CharField(max_length=50, blank=True, null=True)
    org_id = models.CharField(max_length=20, blank=True, null=True)
    billing_event = models.CharField(max_length=50, blank=True, null=True)
    daily_data = GenericRelation(DailyData)

    def __str__(self):
        return f"{self.name}"


class AppUser(SearchAdCampaignBaseModel):
    identifier = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.identifier}"


class UserConversionEvent(SearchAdCampaignBaseModel):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    org_id = models.CharField(max_length=20, null=True, blank=True)
    keyword_id = models.CharField(max_length=20, null=True, blank=True)
    ad_id = models.CharField(max_length=20, null=True, blank=True)
    ad_group_id = models.CharField(max_length=20, null=True, blank=True)
    conversion_type = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    ad_click_date = models.DateTimeField(blank=True, null=True)
    attribution = models.BooleanField(default=True)
    device_time = models.DateTimeField(blank=True, null=True)
    device_type = models.CharField(max_length=20, blank=True, null=True)
    os_version = models.CharField(max_length=20, blank=True, null=True)


class UserSubscriptionEvent(SearchAdCampaignBaseModel):
    campaign = models.ForeignKey(Campaign, related_name="user_subscription_events", on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    subscription_id = models.CharField(max_length=20, blank=True, null=True)
    subscription_status = models.CharField(max_length=20, blank=True, null=True)
    device_time = models.DateTimeField(blank=True, null=True)


# subscription status: TRIAL, TRIAL_CANCEL, SUBSCRIBED, RENEWED, CANCELED

class OrganicUserData(SearchAdCampaignBaseModel):
    data = models.CharField(max_length=1000, blank=True, null=True)
