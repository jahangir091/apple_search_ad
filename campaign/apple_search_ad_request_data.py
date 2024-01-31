from django.conf import settings

search_ad_api_requests = {}
for key, value in settings.APP_INFO.items():
    request_info = {
        'token': {
            "url": "https://appleid.apple.com/auth/oauth2/token?",
            "params": {
                "grant_type": "client_credentials",
                "client_secret": value['client_secret'],
                'client_id': value['client_id'],
                'scope': 'searchadsorg'
            }
        },
        'campaign_list': {
            "url": "https://api.searchads.apple.com/api/v4/reports/campaigns",
            "body": {
                "startTime": "2020-01-04",
                "endTime": "2030-12-05",
                "selector": {
                    "orderBy": [
                        {
                            "field": "countryOrRegion",
                            "sortOrder": "ASCENDING"
                        }
                    ],
                    "conditions": [
                    ],
                    "pagination": {
                        "offset": 0,
                        "limit": 1000
                    }
                },
                "groupBy": [
                    "countryOrRegion"
                ],
                "timeZone": "UTC",
                "returnRecordsWithNoMetrics": False,
                "returnRowTotals": True,
                "returnGrandTotals": True
            },
            "headers": {
                "X-AP-Context": "orgId={0}".format(value['org_id']),
                "Content-Type": "application/json",
                "Authorization": ""
            }
        }
    }
    search_ad_api_requests[value['bundle_id']] = request_info
