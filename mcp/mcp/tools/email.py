from services.email_service import send_email


def run(trip_info):

    recipient = trip_info["recipient"]

    itinerary = trip_info.get("itinerary", "")

    destination = trip_info.get("destination", "")

    departure = trip_info.get("departure_date", "")

    return_date = trip_info.get("return_date", "")

    subject = f"Your Trip to {destination}"

    body = f"""
Hello,

Here are your trip details.

Destination: {destination}

Departure: {departure}

Return: {return_date}

--------------------------------

{itinerary}

Have a great trip!
"""

    return send_email(
        recipient,
        subject,
        body
    )