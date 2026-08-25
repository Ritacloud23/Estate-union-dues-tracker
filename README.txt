CHAIRMAN ADE'S MONEY BOOK
=========================

Estate Union Dues Tracker

Author: Rita Nnenna
Project Type: Python Package Application


1. PROJECT OVERVIEW
===================

Chairman Ade's Money Book is a Python-based estate dues tracking system.

The system was created to solve a real problem faced by a housing estate
residents' association. The chairman needs to keep track of estate members,
their monthly dues payments, payment history, and members who are still owing.

Previously, the records could easily be lost because they were kept in the
chairman's head or on his phone. This application provides a more reliable
way to store and manage those records.

The most important requirement of the system is DATA PERSISTENCE.

When the program is closed and opened again, previously saved members and
payments must still be available.

The system also maintains a readable diary file that records important events,
such as member registration and payments, together with the date and time
that each event happened.


2. PROJECT GOALS
================

The main goals of this project are:

- Register new estate members.
- Store each member's name and phone number.
- View all registered members.
- Record monthly dues payments.
- Record who made the payment.
- Record how much was paid.
- Record which month the payment was for.
- View a member's complete payment history.
- Check whether a member has paid for a particular month.
- Identify whether a member is paid or owing.
- Keep all information after the program is closed.
- Maintain a readable diary of important activities.
- Handle missing or corrupted data files gracefully.
- Organize the application as a proper Python package instead of one large
  script.


3. PROJECT FOLDER STRUCTURE
===========================

The project is organized as follows:

Chairman-estate-record/
|
|-- main.py
|-- data.json
|-- diary.txt
|-- Readme.txt
|
|-- chairman_book/
    |
    |-- __init__.py
    |-- members.py
    |-- payments.py
    |-- storage.py
    |-- logger.py


4. WHY THE PROJECT IS A PACKAGE
================================

The assignment specifically requires the application to be built as a
package rather than putting everything inside one Python file.

The chairman_book folder is the Python package.

The __init__.py file tells Python that chairman_book is a package.

The package is divided into different modules, with each module having a
specific responsibility.

This approach makes the project easier to understand, maintain, test, and
expand.

Instead of putting member registration, payment processing, file handling,
and logging into one large file, each responsibility has its own module.

This follows the principle of separation of concerns.


5. main.py
==========

main.py is the entry point of the application.

It is the only file that the user runs directly.

The main responsibility of main.py is to display the menu and receive the
user's choices.

It then calls the appropriate functions from the chairman_book package.

The menu includes options such as:

1. Register member
2. View members
3. Record payment
4. View payment history
5. Check payment status
6. Exit

The reason for keeping the main program simple is to prevent business logic
from being mixed with the user interface.

The actual work is performed by functions inside the package.

This makes the program easier to maintain because changes to storage,
payments, members, or logging can be made without putting all the code inside
main.py.


6. members.py
=============

The members.py module is responsible for member-related operations.

Its responsibilities include:

- Registering new members.
- Retrieving all registered members.
- Finding a particular member.

The main functions include:

register_member()
    Adds a new member to the saved data.

get_members()
    Retrieves all registered members.

find_member()
    Searches for a member by name.

A member is stored as a dictionary containing information such as:

{
    "name": "John Doe",
    "phone": "08012345678"
}

The reason for keeping these functions inside members.py is that they all
deal specifically with members.

This makes it easier to locate and modify member-related functionality.


7. payments.py
==============

The payments.py module handles all payment-related operations.

Its responsibilities include:

- Recording payments.
- Viewing payment history.
- Checking payment status.

The main functions include:

record_payment()
    Records a member's payment.

get_payment_history()
    Retrieves all payments belonging to a particular member.

check_payment_status()
    Checks whether a member has paid for a particular month.

A payment is stored as a dictionary such as:

{
    "member": "John Doe",
    "amount": 5000,
    "month": "August 2026"
}

The payment module first checks whether the member exists before recording
the payment.

This prevents the system from recording payments for people who are not
registered members.

The module also compares both the member name and the month when checking
payment status.

This is important because a member may have paid for one month but still owe
another month.


8. storage.py
============

The storage.py module is responsible for saving and loading the chairman's
data.

This module is very important because the chairman's biggest requirement is
that his records must survive after the program is closed.

The application uses a JSON file called:

data.json

JSON was chosen because it is simple, human-readable, and works naturally
with Python dictionaries and lists.

The storage module handles operations such as:

- Loading saved data.
- Saving updated data.
- Handling the situation where the data file does not exist.
- Handling corrupted JSON data.

Instead of putting file-handling code throughout the project, all storage
operations are kept in storage.py.

This means the other modules can simply request the data they need without
having to worry about how the data is physically stored.


9. DATA PERSISTENCE
===================

Data persistence means that information remains available even after the
program has been closed.

This is one of the most important features of the project.

For example:

The chairman registers:

John Doe
08012345678

The program saves the information to data.json.

If the chairman closes the program and opens it again, John Doe is still
available.

The same applies to payment records.

The basic process is:

User enters information
        |
        v
Python function processes it
        |
        v
storage.py saves the information
        |
        v
data.json
        |
        v
Program can load it again later

This prevents the chairman from losing his financial history whenever the
program is closed or the computer is restarted.


10. FIRST-RUN HANDLING
======================

The assignment requires that the program must not crash the first time it
runs.

On the first run, data.json may not exist yet.

The program handles this situation gracefully by starting with an empty
record instead of displaying a traceback.

This means the chairman can start using the application immediately without
having to manually create the data file.

The application creates the necessary saved data when information is first
added.


11. CORRUPTED DATA HANDLING
===========================

The assignment specifically states that the saved data may be deliberately
tampered with before marking.

For this reason, the program uses exception handling when reading the JSON
file.

If data.json contains invalid or corrupted JSON, the program does not expose
a Python traceback to the user.

Instead, it gives a simple message explaining that the saved data appears to
be corrupted.

This demonstrates the use of Python exceptions and defensive programming.

The purpose is not only to prevent the program from crashing but also to
make the application easier for a normal user to understand.


12. logger.py
=============

The logger.py module is responsible for maintaining the chairman's diary.

The diary is stored in:

diary.txt

The diary records important events such as:

- Member registration.
- Payment registration.

Each event includes the date and time.

For example:

[2026-08-25 04:20:55] Registered member: John Doe - 08012345678

[2026-08-25 04:25:12] Payment recorded: John Doe - ₦5,000.00 - August 2026


13. WHY THE DIARY USES APPEND MODE
==================================

The diary is opened using append mode:

"a"

Append mode means that new information is added to the end of the existing
file instead of deleting the previous information.

This is important because the chairman wants a history of what has happened.

For example, if the diary already contains:

[2026-08-25 04:20:55] Registered member: John Doe

and another member is registered, the old entry must remain.

The new entry is added underneath it.

This creates a chronological history of activities.


14. WHY THE DIARY IS A TEXT FILE
================================

The assignment requires the diary to be readable without the program.

For this reason, diary.txt is a normal plain-text file.

The chairman can open it using:

- Notepad
- VS Code
- Any other text editor

He does not need the Python program to be running to read the diary.

This gives the chairman direct access to his activity history.


15. IMPORTS
===========

The project demonstrates two different Python import styles.

The first style is:

from chairman_book.members import register_member, get_members

This imports specific functions from the members module.

It allows main.py to call the functions directly:

register_member()
get_members()

The second style is:

import chairman_book.payments as payments

This imports the payments module and gives it the name "payments".

Functions can then be accessed through the module:

payments.record_payment()
payments.get_payment_history()
payments.check_payment_status()

The different import styles demonstrate that Python modules can be imported
in different ways depending on how they are going to be used.

Using module imports can also make it clearer where a function belongs.


16. EXCEPTIONS
=============

Exception handling is used to prevent the program from crashing when
unexpected problems occur.

For example, when the program converts the amount entered by the user into a
number, it uses exception handling to deal with invalid input.

If the user enters:

five thousand

instead of:

5000

the program can respond with a friendly message instead of crashing.

Exception handling is also important when reading data.json.

If the JSON file is corrupted, the program handles the error gracefully.


17. USER INPUT VALIDATION
=========================

The program receives information from the user through input().

Examples include:

- Member name
- Phone number
- Payment amount
- Payment month

The payment amount is converted into a number before being saved.

If the user enters an invalid amount, the program informs the user that the
amount is invalid and asks them to try again.

This makes the application safer and prevents invalid data from being
stored accidentally.


18. MEMBER VALIDATION BEFORE PAYMENT
=====================================

A payment cannot be recorded unless the member already exists.

When a payment is being recorded, the program first searches for the member.

If the member cannot be found, the function returns None.

The menu then informs the user:

"Member not found. Please register the member first."

This prevents payments from being connected to unknown members.

It also demonstrates how functions can communicate results back to the part
of the program that called them.


19. PAYMENT STATUS
==================

The application can check whether a member has paid for a specific month.

For example:

John Doe
August 2026

If a matching payment exists, the system reports:

PAID

If there is no payment for that month, the system reports:

OWING

The program uses both the member name and the month when checking.

This prevents a payment for July from incorrectly being treated as a payment
for August.


20. PAYMENT HISTORY
===================

The payment history feature allows the chairman to see all recorded payments
for a particular member.

For example:

John Doe

June 2026 - ₦5,000
July 2026 - ₦5,000
August 2026 - ₦5,000

The system also calculates the total amount paid by that member based on the
records returned.

This gives the chairman a quick way to understand an individual member's
payment history.


21. WHY DICTIONARIES AND LISTS WERE USED
=========================================

The project uses Python dictionaries and lists because they are suitable for
representing structured information.

A member is represented using a dictionary:

{
    "name": "John Doe",
    "phone": "08012345678"
}

Multiple members are stored inside a list.

Payments are also represented using dictionaries:

{
    "member": "John Doe",
    "amount": 5000,
    "month": "August 2026"
}

Multiple payments are stored in a list.

This structure is simple to understand and can easily be converted to JSON.


22. WHY JSON WAS USED
=====================

JSON was chosen as the storage format because:

- It is easy to read.
- It is easy for Python to work with.
- It supports dictionaries and lists.
- It can be opened manually.
- It does not require a database server.
- It is suitable for a small application like this.

For this project, using JSON keeps the application simple while still
providing persistent storage.


23. PROJECT IMPACT
==================

This application has several practical benefits for the estate.

First, it reduces the risk of losing financial records.

Instead of keeping the information only in someone's memory or phone, the
records are stored in a persistent file.

Second, it improves accountability.

The chairman can see who paid, how much they paid, and which month the payment
was for.

Third, it makes it easier to identify outstanding payments.

Instead of manually remembering who owes money, the chairman can check the
payment status.

Fourth, the payment history provides a record that can be reviewed later.

Fifth, the diary creates an additional activity record showing when members
were registered and when payments were recorded.

Overall, the application changes the dues process from a memory-based system
into a simple digital record-keeping system.


24. SOFTWARE ENGINEERING PRINCIPLES USED
=========================================

The project demonstrates several important programming and software
engineering concepts.

1. Functions
   Reusable pieces of code are used for specific tasks.

2. Modules
   Related functions are grouped into separate Python files.

3. Packages
   The chairman_book directory groups the application's modules together.

4. Separation of concerns
   Members, payments, storage, and logging have different responsibilities.

5. File handling
   The application reads and writes persistent files.

6. Exception handling
   The program handles unexpected situations without crashing.

7. Data persistence
   Records survive after the application is closed.

8. Logging
   Important events are recorded with timestamps.

9. User input validation
   Invalid input is handled instead of allowing it to break the program.

10. Imports
    Modules and functions are imported where they are needed.


25. HOW TO RUN THE APPLICATION
==============================

Requirements:

- Python 3
- A terminal or command prompt

Step 1:
Open the project folder in the terminal.

Step 2:
Make sure the terminal is in the same folder as main.py.

Step 3:
Run:

python main.py

Step 4:
Use the menu to interact with the application.


26. IMPORTANT FILES
===================

main.py
    The entry point and menu interface.

chairman_book/__init__.py
    Identifies chairman_book as a Python package.

chairman_book/members.py
    Handles member registration and member searching.

chairman_book/payments.py
    Handles payment records, payment history, and payment status.

chairman_book/storage.py
    Handles loading and saving persistent data.

chairman_book/logger.py
    Handles the activity diary.

data.json
    Stores members and payment records.

diary.txt
    Stores a readable history of important activities.

Readme.txt
    Explains the project, structure, design decisions, and usage.


27. RESTART TEST
================

The application was designed to pass the restart requirement.

Example:

1. Start the program.
2. Register two members.
3. Record a payment.
4. Exit the program.
5. Start the program again.
6. View the members.
7. View the payment history.

The members and payment records remain available because they were saved to
data.json instead of being kept only in memory.


28. CONCLUSION
==============

Chairman Ade's Money Book was designed to provide a simple but reliable
solution for managing estate union dues.

The project combines the Python concepts learned during the course,
including functions, dictionaries, lists, loops, conditional statements,
modules, packages, file handling, imports, and exception handling.

The most important lesson from the project is that writing code that works is
only one part of building a useful application.

The code also needs to be organized, maintainable, reliable, and capable of
handling real-world problems such as missing files, invalid input, corrupted
data, and unexpected program restarts.

This project applies those concepts to a practical problem and provides the
chairman with a system that can keep his records safe and accessible.