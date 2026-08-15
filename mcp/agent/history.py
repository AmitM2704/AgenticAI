messages = []


def add_message(role, content):
    messages.append({
        "role": role,
        "content": content
    })


def get_history():
    return messages


def get_history_text():
    history = ""

    for msg in messages:
        history += f"{msg['role'].capitalize()}: {msg['content']}\n"

    return history