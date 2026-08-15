import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(prompt,
                      model="llama-3.3-70b-versatile",
                      temperature=0.3):

    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
def stream_response(prompt,
                    model="llama-3.3-70b-versatile",
                    temperature=0.3):

    stream = client.chat.completions.create(
        model=model,
        temperature=temperature,
        stream=True,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    for chunk in stream:

        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content