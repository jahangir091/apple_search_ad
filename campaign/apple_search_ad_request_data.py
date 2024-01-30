search_ad_api_requests = {
    'com.secure.universalRemote': {
        'token': {
            "url": "https://appleid.apple.com/auth/oauth2/token?",
            "params": {
                "grant_type": "client_credentials",
                "client_secret": "eyJhbGciOiJFUzI1NiIsImtpZCI6IjRjZTQ2ZTIzLTYyYjktNGYxOC04NGU0LTA3Yzk4NzY4N2I5NCIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJTRUFSQ0hBRFMuZDc0MGFhYWItYzhmOS00MjUyLWEyN2QtNGQ1NTdiMWU3OWI3IiwiYXVkIjoiaHR0cHM6Ly9hcHBsZWlkLmFwcGxlLmNvbSIsImlhdCI6MTcwNDg0NTQxMCwiZXhwIjoxNzIwMzk3NDEwLCJpc3MiOiJTRUFSQ0hBRFMuZDc0MGFhYWItYzhmOS00MjUyLWEyN2QtNGQ1NTdiMWU3OWI3In0.Ifp6WvCzXHZK1KJ5ia25l3ePLlfBSDcP2Cj4J6Mbxpx4AMmBQia4sZB41-BXpJ8PzlJx_SAEAaoxOyG2RXSong",
                'client_id': "SEARCHADS.d740aaab-c8f9-4252-a27d-4d557b1e79b7",
                'scope': 'searchadsorg'
            }
        },
        'campaign_list': {
            "url": "https://api.searchads.apple.com/api/v4/reports/campaigns",
            "body": {
                "startTime": "2023-01-04",
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
                "X-AP-Context": "orgId=6536270",
                "Content-Type": "application/json",
                "Authorization": ""
            }
        }
    },
    'com.bitmorpher.apps.logomaker': {
        'token': {
            "url": "https://appleid.apple.com/auth/oauth2/token?",
            "params": {
                "grant_type": "client_credentials",
                "client_secret": "eyJhbGciOiJFUzI1NiIsImtpZCI6ImRmMjk4ZDQ0LWQ2M2MtNDM1OS1iZGUzLWE2OTkzM2YzMDgyNyIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJTRUFSQ0hBRFMuOGM0NmM1YjMtNTk4My00YzBlLTgxM2EtMTZiMTZlNDkwZTZiIiwiYXVkIjoiaHR0cHM6Ly9hcHBsZWlkLmFwcGxlLmNvbSIsImlhdCI6MTcwNTU2NDk1MiwiZXhwIjoxNzIxMTE2OTUyLCJpc3MiOiJTRUFSQ0hBRFMuOGM0NmM1YjMtNTk4My00YzBlLTgxM2EtMTZiMTZlNDkwZTZiIn0.rTryMCVADgT_bj8FfVHkq4F9kwiprv0kMzs_nYDCTx9K3Vqq5VGsAGBje48EWNkrJgkD9n_oIr2ldE-0frcbeQ",
                'client_id': "SEARCHADS.8c46c5b3-5983-4c0e-813a-16b16e490e6b",
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
                "X-AP-Context": "orgId=1678650",
                "Content-Type": "application/json",
                "Authorization": ""
            }
        }
    }
}