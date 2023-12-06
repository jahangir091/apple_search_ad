import requests


def get_token():
    url = search_ad_api_requests['token']['url']
    params = search_ad_api_requests['token']['params']
    response = requests.post(url, params=params)
    return response.json()['access_token']


search_ad_api_requests = {
    'token': {
        "url": "https://appleid.apple.com/auth/oauth2/token?",
        "params": {
            "grant_type": "client_credentials",
            "client_secret": "eyJhbGciOiJFUzI1NiIsImtpZCI6IjRjZTQ2ZTIzLTYyYjktNGYxOC04NGU0LTA3Yzk4NzY4N2I5NCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJTRUFSQ0hBRFMuZDc0MGFhYWItYzhmOS00MjUyLWEyN2QtNGQ1NTdiMWU3OWI3IiwiYXVkIjoiaHR0cHM6Ly9hcHBsZWlkLmFwcGxlLmNvbSIsImlhdCI6MTY4OTIyNjMyMiwiZXhwIjoxNzA0Nzc4MzIyLCJpc3MiOiJTRUFSQ0hBRFMuZDc0MGFhYWItYzhmOS00MjUyLWEyN2QtNGQ1NTdiMWU3OWI3In0.aeWRPjiBI3bMvlJ75X85AJdP91YvQBe4sC9P9wHJnwvyOzZzJz9ES0m_t1o2ftIqXCESz2zPIWt80Jv3_VlI2w",
            'client_id': "SEARCHADS.d740aaab-c8f9-4252-a27d-4d557b1e79b7",
            'scope': 'searchadsorg'
        }
    },
    'campaign_list': {
        "url": "https://api.searchads.apple.com/api/v4/reports/campaigns",
        "body": {
            "startTime": "2023-01-04",
            "endTime": "2023-09-05",
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
            "X-AP-Context": "orgId=6536270",
            "Content-Type": "application/json",
            "Authorization": ""
        }
    }
}
