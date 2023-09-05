from django.db import models


class BaseCategory(models.Model):
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    priority = models.IntegerField(default=0)
    is_pro = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class App(models.Model):
    name = models.CharField(max_length=100)
    adamId = models.CharField(max_length=50, blank=True, null=True)
    bundle_id = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class AppUser(models.Model):
    identifier = models.CharField(max_length=100, blank=True, null=True)


class Campaign(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    campaign_id = models.CharField(max_length=50, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    status = models.CharField(max_length=50, blank=True, null=True)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    serving_status = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    modification_time = models.DateTimeField(auto_now=True)
    total_budget = models.FloatField(default=0)
    daily_budget = models.FloatField(default=0)
    display_status = models.CharField(max_length=50, blank=True, null=True)
    supply_source = models.CharField(max_length=50, blank=True, null=True)
    add_channel_type = models.CharField(max_length=50, blank=True, null=True)
    org_id = models.IntegerField(default=0)
    billing_event = models.CharField(max_length=50, blank=True, null=True)


class DailyCampaignData(models.Model):
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
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

#
# created_at
# updated_at
# id
# campaign_id
# conversion_type
# country_region
# click_date
# org_id
# keyword_id
# ad_id
# ad_group_id
# user_id
# app_id
# attribution
# device_time
#
# for phone_ad_service_campaign table
#
#
#
#     created_at
#     updated_at
#     id
#     user_id
#     app_id
#     subscription_id
#     subscription_status
#     device_time
#
#     for subscription_events table


class UserEvent(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
