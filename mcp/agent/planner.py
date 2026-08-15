import json

from models.llm import generate_response
from prompts.prompts import PLANNER_PROMPT
from agent.history import get_history_text


def plan(user_query, trip_info=None):

    history = get_history_text()

    prompt = f"""
{PLANNER_PROMPT}
 
Conversation History:
{history}

Trip Information:
{trip_info}

Current User Query:
{user_query}

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json.
"""

    response = generate_response(prompt).strip()

    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    print(response)

    return json.loads(response)