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


def import_members(filename):
    imported = 0
    skipped = 0

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 2:
                    skipped += 1
                    continue

                name = parts[0].strip()
                phone = parts[1].strip()

                if not name or not phone:
                    skipped += 1
                    continue

                register_member(name, phone)
                imported += 1

    except FileNotFoundError:
        return None, 0, 0

    return True, imported, skipped    