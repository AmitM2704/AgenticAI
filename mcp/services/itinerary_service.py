from agent.history import get_history_text
from models.llm import generate_response

def generate_itinerary(user_query, trip_info):

    history = get_history_text()

    prompt = f"""
You are an expert travel planner.

Conversation History:
{history}

Current Trip Information:
{trip_info}

Current User Request:
{user_query}

Instructions:

- If this is the first request, generate a new itinerary.
- If the user is modifying an existing itinerary, MODIFY the existing itinerary.
- Never change the destination unless the user explicitly asks.
- Never invent a new country or city.
- Preserve existing trip details unless the user requests changes.
- If the user changes the budget, adjust hotels, activities and transport to fit the new budget.
- If the user refers to "it", "there", "this trip", etc., assume they mean the current itinerary.

Return only the itinerary.
"""

    return generate_response(prompt)