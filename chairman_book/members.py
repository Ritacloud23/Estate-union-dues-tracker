from chairman_book.storage import load_data, save_data
from chairman_book.logger import log_event


def register_member(name, phone):
    data = load_data()

    member = {
        "name": name,
        "phone": phone
    }

    data["members"].append(member)
    save_data(data)

    log_event(
        f"Registered member: {name} - {phone}"
    )

    return member


def get_members():
    data = load_data()
    return data["members"]


def find_member(name):
    members = get_members()

    for member in members:
        if member["name"].lower() == name.lower():
            return member

    return None