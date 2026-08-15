from services.calendar_service import add_to_calendar

def run(trip_info):

    destination = trip_info["destination"]
    start_date = trip_info["departure_date"]
    end_date = trip_info["return_date"]

    return add_to_calendar(
        destination,
        start_date,
        end_date
    )