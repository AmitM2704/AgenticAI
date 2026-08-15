from agent.history import add_message
from agent.planner import plan
from mcp.client import call_tool
from services.pdf_extractor import extract_trip_info
from services.itinerary_service import generate_itinerary
#from agent.history import add_message
#from agent.planner import plan

#from mcp.client import call_tool

from models.llm import generate_response
from prompts.prompts import RESPONSE_PROMPT


def chat(user_query, trip_info):

    add_message("user", user_query)

    task = plan(user_query, trip_info)

    tool = task["tool"]

    if tool == "followup":
        return {
            "response": task["question"]
        }

    elif tool == "weather":

        if "parameters" in task:
            response = call_tool("weather", task["parameters"])
        else:
            response = call_tool(
                "weather",
                {"city": trip_info["destination"]}
            )

    elif tool == "calendar":
        response = call_tool("calendar", trip_info)
    elif tool == "email":

        trip_info.update(task.get("parameters", {}))

        if "recipient" not in trip_info:
            return {
                "response": "Sure! What email address would you like me to send your itinerary to?"
            }

        response = call_tool("email", trip_info)
    elif tool == "trip_planner":

        
        response = generate_itinerary(user_query,trip_info)
        print("TYPE:", type(response))
        print(response)
        print("========== ITINERARY ==========")
        print(response)
        print("===============================")
        
        new_trip = extract_trip_info(response)
        trip_info["itinerary"] = response

        
        trip_info.update(new_trip)

        print("Updated Trip Info:")
        print(trip_info)

        add_message("assistant", response)

        return {
            "response": response
        }
    elif tool == "flights":
        response = trip_info["flight"]

    elif tool == "hotels":
        response = trip_info["hotel"]

    else:
        return {
            "response": "Sorry, I couldn't understand your request."
        }

    
    prompt = RESPONSE_PROMPT.format(
        query=user_query,
        result=response
    )

    final_response = generate_response(prompt)

    add_message("assistant", final_response)

    return {
        "response": final_response
    }