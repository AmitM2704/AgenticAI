import json

from models.llm import generate_response
from prompts.prompts import EXTRACTION_PROMPT


def extract_trip_info(pdf_text):

    prompt = EXTRACTION_PROMPT.format(pdf_text=pdf_text)

    response = generate_response(prompt)

    print("Extracted Trip Info:")
    print(response)

    # Remove markdown if present
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    return json.loads(response)