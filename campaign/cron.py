
# python manage.py crontab add
# python manage.py crontab show
# python manage.py crontab remove
# https://pypi.org/project/django-crontab/

import random
import string
import datetime

from django.contrib.auth.models import User

from campaign.apple_search_ad_reporting import AppleSearchAdReporting


def my_scheduled_job():
    username = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits, k=10))
    u = User(username=username)
    u.save()
    print("cron is running fine!")


def daily_campaign_data_update_cron():
    today_date = str(datetime.datetime.today().date())
    start_date = today_date
    end_date = today_date
    report = AppleSearchAdReporting()
    try:
        response = report.get_campaign_list()
    except Exception as e:
        print("Could not update campaign data for date {0}. {1}".format(str(today_date), str(e)))
    else:
        for campaign_data in response.json()['data']['reportingDataResponse']['row']:
            cmd = campaign_data['metadata']
            adamId = cmd["app"]["adamId"]
            app = App.objects.get(adamId=adamId)
            campaign, created = Campaign.objects.get_or_create(campaign_id=cmd['campaignId'], app=app)
            campaign.name = cmd['campaignName']
            campaign.deleted = cmd['deleted']
            campaign.status = cmd['campaignStatus']
            campaign.serving_status = cmd['servingStatus']
            campaign.country = cmd['countryOrRegion']
            campaign.modification_time = cmd['modificationTime']
            campaign.total_budget = cmd['totalBudget']
            campaign.daily_budget = cmd['dailyBudget']['amount']
            campaign.display_status = cmd['displayStatus']
            campaign.supply_sources = cmd['supplySources']
            campaign.add_channel_type = cmd['adChannelType']
            campaign.org_id = cmd['orgId']
            campaign.billing_event = cmd['billingEvent']
            campaign.save()


def daily_keywords_data():
    pass


def daily_adgroup_data():
    pass
