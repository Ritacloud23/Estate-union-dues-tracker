from chairman_book import storage
from chairman_book.members import find_member
from chairman_book.logger import log_event
import chairman_book.storage as storage


def record_payment(member_name, amount, month):
    member = find_member(member_name)

    if member is None:
        return None

    data = storage.load_data()

    payment = {
        "member": member_name,
        "amount": amount,
        "month": month
    }

    data["payments"].append(payment)
    storage.save_data(data)

    log_event(
        f"Payment recorded: {member_name} - "
        f"₦{amount:,.2f} - {month}"
    )

    return payment


def get_payment_history(member_name):
    data = storage.load_data()

    history = []

    for payment in data["payments"]:
        if payment["member"].lower() == member_name.lower():
            history.append(payment)

    return history


def check_payment_status(member_name, month):
    member = find_member(member_name)

    if member is None:
        return None

    data = storage.load_data()

    for payment in data["payments"]:
        if (
            payment["member"].lower() == member_name.lower()
            and payment["month"].lower() == month.lower()
        ):
            return {
                "status": "Paid",
                "amount": payment["amount"]
            }

    return {
        "status": "Owing",
        "amount": 0
    }