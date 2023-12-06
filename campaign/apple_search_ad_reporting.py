import requests


class AppleSearchAdReporting:
    APPLE_ACCOUNT_CLIENT_SECRET = "eyJhbGciOiJFUzI1NiIsImtpZCI6IjRjZTQ2ZTIzLTYyYjktNGYxOC04NGU0LTA3Yzk4NzY" \
                                  "4N2I5NCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJTRUFSQ0hBRFMuZDc0MGFhYWItYzhmOS00MjUy" \
                                  "LWEyN2QtNGQ1NTdiMWU3OWI3IiwiYXVkIjoiaHR0cHM6Ly9hcHBsZWlkLmFwcGxlLmNvbSIsImlh" \
                                  "dCI6MTY4OTIyNjMyMiwiZXhwIjoxNzA0Nzc4MzIyLCJpc3MiOiJTRUFSQ0hBRFMuZDc0MGFhYWItYz" \
                                  "hmOS00MjUyLWEyN2QtNGQ1NTdiMWU3OWI3In0.aeWRPjiBI3bMvlJ75X85AJdP91YvQBe4sC9P9wHJ" \
                                  "nwvyOzZzJz9ES0m_t1o2ftIqXCESz2zPIWt80Jv3_VlI2w"

    PARAMS = {
        "grant_type": "client_credentials",
        "client_secret": APPLE_ACCOUNT_CLIENT_SECRET,
        'client_id': "SEARCHADS.d740aaab-c8f9-4252-a27d-4d557b1e79b7",
        'scope': 'searchadsorg'
    }

    REQUEST_BODY = {
            "startTime": "2023-01-04",
            "endTime": "2023-09-05",
            "timeZone": "UTC",
            "returnRecordsWithNoMetrics": False,
            "returnRowTotals": True,
            "returnGrandTotals": True,
            "selector": {
                "orderBy": [
                ],
                "conditions": [
                ],
                "pagination": {
                    "offset": 0,
                    "limit": 1000
                }
            }
        }

    REQUEST_HEADERS = {
            "X-AP-Context": "orgId=6536270",
            "Content-Type": "application/json",
            "Authorization": ""
        }

    GET_BARER_TOKEN_URL = "https://appleid.apple.com/auth/oauth2/token?"
    GET_CAMPAIGN_LIST_URL = "https://api.searchads.apple.com/api/v4/reports/campaigns"

    def get_access_token(self):
        url = self.GET_BARER_TOKEN_URL
        params = self.PARAMS
        response = requests.post(url, params=params)
        return response.json()['access_token']

    def get_campaign_list(self):
        access_token = self.get_access_token()
        url = self.GET_CAMPAIGN_LIST_URL
        body = self.REQUEST_BODY
        headers = self.REQUEST_HEADERS
        headers["Authorization"] = "Bearer " + access_token
        response = requests.post(url, json=body, headers=headers)
        return response



import vastai