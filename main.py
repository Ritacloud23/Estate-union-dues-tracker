from chairman_book.members import register_member, get_members
import chairman_book.payments as payments
from chairman_book.storage import load_data, save_data
from chairman_book import logger


def main():
    while True:
        print("\n=== CHAIRMAN ADE'S MONEY BOOK ===")
        print("1. Register member")
        print("2. View members")
        print("3. Record payment")
        print("4. View payment history")
        print("5. Check payment status")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # Register member
        if choice == "1":
            name = input("Enter member's name: ")
            phone = input("Enter member's phone number: ")

            member = register_member(name, phone)

            print("\nMember registered successfully!")
            print(f"Name: {member['name']}")
            print(f"Phone: {member['phone']}")

        # View members
        elif choice == "2":
            members = get_members()

            if not members:
                print("\nNo members registered yet.")
            else:
                print("\n=== REGISTERED MEMBERS ===")

                for number, member in enumerate(members, start=1):
                    print(
                        f"{number}. {member['name']} - "
                        f"{member['phone']}"
                    )

        # Record payment
        elif choice == "3":
            member_name = input("Enter member's name: ")
            amount = input("Enter amount paid: ")
            month = input("Enter payment month: ")

            try:
                amount = float(amount)
            except ValueError:
                print("\nInvalid amount. Please enter a number.")
                continue

            payment = payments.record_payment(
                member_name,
                amount,
                month
            )

            if payment is None:
                print("\nMember not found.")
                print("Please register the member first.")
            else:
                print("\nPayment recorded successfully!")
                print(f"Member: {payment['member']}")
                print(f"Amount: ₦{payment['amount']:,.2f}")
                print(f"Month: {payment['month']}")

        # View payment history
        elif choice == "4":
            member_name = input("Enter member's name: ")

            history = payments.get_payment_history(member_name)

            if not history:
                print("\nNo payment history found.")
            else:
                print(f"\n=== PAYMENT HISTORY: {member_name} ===")

                total = 0

                for number, payment in enumerate(history, start=1):
                    print(
                        f"{number}. "
                        f"{payment['month']} - "
                        f"₦{payment['amount']:,.2f}"
                    )
                    total += payment["amount"]

                print(f"\nTotal paid: ₦{total:,.2f}")

        # Check payment status
        elif choice == "5":
            member_name = input("Enter member's name: ")
            month = input("Enter month to check: ")

            status = payments.check_payment_status(
                member_name,
                month
            )

            if status is None:
                print("\nMember not found.")
                print("Please register the member first.")
            elif status["status"] == "Paid":
                print("\n=== PAYMENT STATUS ===")
                print(f"Member: {member_name}")
                print(f"Month: {month}")
                print("Status: PAID")
                print(f"Amount: ₦{status['amount']:,.2f}")
            else:
                print("\n=== PAYMENT STATUS ===")
                print(f"Member: {member_name}")
                print(f"Month: {month}")
                print("Status: OWING")

        # Exit
        elif choice == "6":
            print("\nThank you for using Chairman Ade's Money Book.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()