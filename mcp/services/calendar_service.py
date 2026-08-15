from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dateutil import parser

SCOPES = [
    "https://www.googleapis.com/auth/calendar"
]


def convert_date(date_str):
    if not date_str:
        return ""

    dt = parser.parse(date_str, fuzzy=True)
    return dt.strftime("%Y-%m-%d")


def add_to_calendar(destination, start_date, end_date):

    # Validate dates
    if not start_date or not end_date:
        return {
            "status": "error",
            "message": "Trip dates are missing. Please provide departure and return dates."
        }

    # Convert dates to YYYY-MM-DD
    start_date = convert_date(start_date)
    end_date = convert_date(end_date)
    
    flow = InstalledAppFlow.from_client_secrets_file(
        "services/creds.json",
        SCOPES
    )

    creds = flow.run_local_server(port=0)

    service = build(
        "calendar",
        "v3",
        credentials=creds
    )

    event = {
        "summary": f"Trip to {destination}",
        "start": {
            "date": start_date
        },
        "end": {
            "date": end_date
        }
    }

    created_event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    return {
        "status": "success",
        "message": "Trip added to Google Calendar successfully.",
        "link": created_event["htmlLink"]
    }