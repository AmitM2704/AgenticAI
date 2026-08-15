from flask import Blueprint, request, jsonify

from agent.controller import chat

from services.pdf_reader import read_pdf
from services.pdf_extractor import extract_trip_info

chat_bp = Blueprint("chat", __name__)


PDF_PATH = "data/travel_database_sample.pdf"

pdf_text = read_pdf(PDF_PATH)
trip_info = extract_trip_info(pdf_text)

print("Trip Info:")
print(trip_info)


@chat_bp.route("/chat", methods=["POST"])
def chatbot():

    data = request.get_json()
    query = data["message"]

    response = chat(query, trip_info)

    return jsonify(response)