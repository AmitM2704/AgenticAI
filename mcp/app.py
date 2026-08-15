import streamlit as st

from agent.controller import chat
from services.pdf_reader import read_pdf
from services.pdf_extractor import extract_trip_info

PDF_PATH = "data/travel_database_sample.pdf"


@st.cache_resource
def load_trip():
    pdf_text = read_pdf(PDF_PATH)
    return extract_trip_info(pdf_text)


if "trip_info" not in st.session_state:
    st.session_state.trip_info = load_trip()


if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("✈️ AI Travel Assistant")


# Display previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


query = st.chat_input("Ask me about your trip...")


if query:

    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.markdown(query)

    result = chat(
        query,
        st.session_state.trip_info
    )

    response = result["response"]

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)