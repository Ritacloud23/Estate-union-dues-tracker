# 🏠 CHAIRMAN ADE'S MONEY BOOK

## Estate Union Dues Tracker

> A Python package-based application for managing estate members, monthly dues, payment history, persistent records, and activity logs.

**Author:** Rita Nnenna  
**Project Type:** Python Package Application  
**Language:** Python 3  
**Storage:** JSON  
**Logging:** Plain-text diary  

---

# 📖 Table of Contents

1. [Project Overview](#1-project-overview)
2. [The Client's Problem](#2-the-clients-problem)
3. [The Client's Requirements](#3-the-clients-requirements)
4. [Project Goals](#4-project-goals)
5. [Engineering Requirements](#5-engineering-requirements)
6. [Project Folder Structure](#6-project-folder-structure)
7. [Why the Project Is a Package](#7-why-the-project-is-a-package)
8. [Application Architecture](#8-application-architecture)
9. [main.py](#9-mainpy)
10. [__init__.py](#10-initpy)
11. [members.py](#11-memberspy)
12. [payments.py](#12-paymentspy)
13. [storage.py](#13-storagepy)
14. [logger.py](#14-loggerpy)
15. [Data Storage](#15-data-storage)
16. [Data Persistence](#16-data-persistence)
17. [First-Run Handling](#17-first-run-handling)
18. [Corrupted Data Handling](#18-corrupted-data-handling)
19. [The Activity Diary](#19-the-activity-diary)
20. [Why the Diary Uses Append Mode](#20-why-the-diary-uses-append-mode)
21. [Member Management](#21-member-management)
22. [Payment Management](#22-payment-management)
23. [Member Validation](#23-member-validation)
24. [Payment Status](#24-payment-status)
25. [Payment History](#25-payment-history)
26. [User Input Validation](#26-user-input-validation)
27. [Exception Handling](#27-exception-handling)
28. [Python Import Styles](#28-python-import-styles)
29. [Why Dictionaries and Lists Were Used](#29-why-dictionaries-and-lists-were-used)
30. [Why JSON Was Used](#30-why-json-was-used)
31. [Separation of Concerns](#31-separation-of-concerns)
32. [Software Engineering Concepts Demonstrated](#32-software-engineering-concepts-demonstrated)
33. [Program Workflow](#33-program-workflow)
34. [Data Flow](#34-data-flow)
35. [Example Member Data](#35-example-member-data)
36. [Example Payment Data](#36-example-payment-data)
37. [Example Diary Entries](#37-example-diary-entries)
38. [Menu Features](#38-menu-features)
39. [Restart Test](#39-restart-test)
40. [First Run Test](#40-first-run-test)
41. [Corrupted Data Test](#41-corrupted-data-test)
42. [Diary Test](#42-diary-test)
43. [Project Impact](#43-project-impact)
44. [Why This Project Matters](#44-why-this-project-matters)
45. [Bonus Features](#45-bonus-features)
46. [How to Run the Application](#46-how-to-run-the-application)
47. [Important Files](#47-important-files)
48. [What I Learned](#48-what-i-learned)
49. [Conclusion](#49-conclusion)

---

# 1. Project Overview

**Chairman Ade's Money Book** is a Python-based estate union dues tracking application.

The application was created for a housing estate residents' association where the chairman is responsible for collecting and managing monthly dues from residents.

The application allows the chairman to:

- Register estate members.
- Store member names and phone numbers.
- View registered members.
- Record monthly dues payments.
- Record the amount paid.
- Record the month the payment belongs to.
- View a member's payment history.
- Check whether a member has paid for a particular month.
- Identify members who are paid or owing.
- Keep records after the program has been closed.
- Maintain a readable activity diary.
- Handle missing data files.
- Handle corrupted data files gracefully.

The project was designed not just to demonstrate that Python code can work, but also to demonstrate how a Python application can be properly organized into **packages, modules, functions, file storage, imports, and exception handling**.

---

# 2. The Client's Problem

Chairman Ade currently manages his estate's financial records using unreliable methods.

Some information exists in his memory while other information exists on his phone.

This creates several problems.

### Problems with the old system

- Records can be forgotten.
- Records can be lost if the phone is damaged.
- It is difficult to know who has paid.
- It is difficult to know who is owing.
- It is difficult to remember which month someone paid for.
- There is no organized payment history.
- There is no proper record of when events happened.
- Financial information is not stored in a reliable system.

The client's biggest concern is that the records must survive even if the program is closed.

His requirement can be summarized as:

> **When I close this program and open it tomorrow, everything must still be there.**

The application was therefore designed around **persistent data storage**.

---

# 3. The Client's Requirements

The client wants a system that can:

### Member Management

- Register new members.
- Store member names.
- Store member phone numbers.
- View registered members.
- Find a specific member.

### Payment Management

- Record payments.
- Record who paid.
- Record how much was paid.
- Record the month the payment was for.
- View a member's payment history.
- Check whether a member has paid.
- Identify members who are owing.

### Data Management

- Save information permanently.
- Reload previous information when the application starts again.
- Start successfully even when no data file exists.
- Detect corrupted data.
- Handle corrupted data without crashing.

### Activity Diary

The client also wants a diary that records important events.

The diary must:

- Be a plain-text file.
- Be readable without the Python program.
- Include the date and time.
- Keep old records.
- Add new records to the end.
- Never overwrite previous records.

---

# 4. Project Goals

The main goals of the project are:

1. Create a reliable estate dues management system.
2. Organize the application using Python packages and modules.
3. Separate different responsibilities into different files.
4. Store data permanently using JSON.
5. Prevent data loss after restarting the application.
6. Handle missing files gracefully.
7. Handle corrupted files gracefully.
8. Record important events in a readable diary.
9. Validate user input.
10. Prevent payments from being recorded for unknown members.
11. Allow the chairman to check payment status.
12. Allow the chairman to view payment history.
13. Demonstrate different Python import styles.
14. Apply functions, dictionaries, lists, loops, conditions, file handling, and exceptions in a real-world application.

---

# 5. Engineering Requirements

The assignment has several engineering rules that determine how the application must be built.

## Requirement 1 — The Application Must Be a Package

The application must not be written as one large Python script.

It must contain:

- A package folder.
- `__init__.py`.
- At least three modules.
- Each module must have a clear responsibility.

The package created for this project is:

```text
chairman_book/
```

---

## Requirement 2 — `main.py` Must Be Outside the Package

`main.py` sits outside the package.

It is the only file that is run directly.

Its responsibility is mainly to:

- Display the menu.
- Receive user input.
- Call functions from the package.

The actual application logic belongs inside the package modules.

---

## Requirement 3 — Data Must Survive a Restart

The program must save information permanently.

For example:

```text
Run program
     ↓
Register John Doe
     ↓
Record John's August payment
     ↓
Exit program
     ↓
Start program again
     ↓
John Doe still exists
     ↓
August payment still exists
```

This is achieved using `data.json`.

---

## Requirement 4 — First Run Must Not Crash

When the program is run for the first time, `data.json` may not exist.

The program must not display a Python traceback.

Instead, it should start with an empty data structure.

---

## Requirement 5 — The Diary Must Grow

The diary must never delete previous entries.

New events must be added to the end of the file.

Every entry must contain a timestamp.

---

## Requirement 6 — Corrupted Data Must Be Handled

The marker may deliberately modify `data.json`.

If the JSON becomes invalid, the program must:

- Detect the problem.
- Display a simple message.
- Avoid showing a technical traceback.
- Continue running instead of completely crashing.

---

## Requirement 7 — README

The project must contain a README explaining:

- What the project does.
- The folder structure.
- What each module does.
- How to run the application.

This README provides documentation for another developer or user who wants to understand the project.

---

# 6. Project Folder Structure

The project is organized as follows:

```text
Chairman-estate-record/
│
├── main.py
├── data.json
├── diary.txt
├── Readme.txt
│
└── chairman_book/
    │
    ├── __init__.py
    ├── members.py
    ├── payments.py
    ├── storage.py
    └── logger.py
```

---

# 7. Why the Project Is a Package

The `chairman_book` directory is a Python package.

The package groups related functionality together.

Instead of having one large file containing everything, responsibilities are divided.

For example:

```text
members.py
    ↓
Member operations

payments.py
    ↓
Payment operations

storage.py
    ↓
Data saving and loading

logger.py
    ↓
Activity diary
```

This is called **separation of concerns**.

Each module focuses on one area of responsibility.

### Benefits

This makes the project:

- Easier to understand.
- Easier to maintain.
- Easier to debug.
- Easier to test.
- Easier to expand.
- More professional than one large script.

---

# 8. Application Architecture

The basic architecture of the application is:

```text
                    main.py
                       │
                       ↓
                 User Interface
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      members.py   payments.py   other functions
          │            │
          └──────┬─────┘
                 ↓
             storage.py
                 │
                 ↓
              data.json

                 payments.py
                      │
                      ↓
                  logger.py
                      │
                      ↓
                  diary.txt
```

The architecture separates the user interface from the application's actual functionality.

---

# 9. `main.py`

`main.py` is the entry point of the application.

It is the only file that the user runs directly.

Its main responsibility is to control the menu.

Example:

```python
from chairman_book.members import register_member, get_members
import chairman_book.payments as payments
```

The menu then calls the appropriate functions.

For example:

```text
1. Register member
2. View members
3. Record payment
4. View payment history
5. Check payment status
6. Exit
```

### Why `main.py` Does Not Contain Everything

Putting every function inside `main.py` would make the program difficult to maintain.

Instead:

```text
main.py
    ↓
calls members.py

main.py
    ↓
calls payments.py

members.py
    ↓
uses storage.py

payments.py
    ↓
uses storage.py

payments.py
    ↓
uses logger.py
```

This keeps the reception desk (`main.py`) separate from the actual office rooms.

---

# 10. `__init__.py`

The `__init__.py` file is located inside the `chairman_book` package.

```text
chairman_book/
└── __init__.py
```

Its main purpose is to identify the directory as a Python package.

The file does not need to contain the application's main functions.

Keeping it simple is intentional.

The actual functionality belongs in the individual modules.

---

# 11. `members.py`

The `members.py` module handles everything related to estate members.

### Responsibilities

- Register members.
- Retrieve members.
- Search for members.

### `register_member()`

This function creates a new member.

Example member:

```python
{
    "name": "John Doe",
    "phone": "08012345678"
}
```

The member is then added to the saved data.

---

### `get_members()`

This function loads the saved data and returns all registered members.

---

### `find_member()`

This function searches for a member by name.

The search is case-insensitive.

For example:

```text
john doe
John Doe
JOHN DOE
```

can all refer to the same member.

If the member is found, the member information is returned.

If the member does not exist:

```python
None
```

is returned.

This allows the program to respond appropriately instead of crashing.

---

# 12. `payments.py`

The `payments.py` module handles payment-related functionality.

### Responsibilities

- Record payments.
- Check payment status.
- Retrieve payment history.

---

## `record_payment()`

This function records:

- Member
- Amount
- Month

Example:

```python
{
    "member": "John Doe",
    "amount": 5000,
    "month": "August 2026"
}
```

Before recording the payment, the system checks whether the member exists.

If the member does not exist, no payment is recorded.

---

## `check_payment_status()`

This function checks whether a member has paid for a particular month.

For example:

```text
Member: John Doe
Month: August 2026
```

The system searches the payment records.

If a matching record is found:

```text
Status: Paid
```

If no matching payment exists:

```text
Status: Owing
```

---

## `get_payment_history()`

This function retrieves the complete payment history of a particular member.

Example:

```text
John Doe

June 2026   ₦5,000
July 2026   ₦5,000
August 2026 ₦5,000
```

This allows the chairman to see everything a member has paid.

---

# 13. `storage.py`

`storage.py` is responsible for persistent data storage.

This is one of the most important modules in the project.

The module handles:

- Loading data.
- Saving data.
- Missing data files.
- Corrupted JSON files.

The saved information is stored in:

```text
data.json
```

---

# 14. Data Storage

The project uses JSON to store application data.

The data contains members and payments.

A simplified structure is:

```json
{
    "members": [
        {
            "name": "John Doe",
            "phone": "08012345678"
        }
    ],
    "payments": [
        {
            "member": "John Doe",
            "amount": 5000,
            "month": "August 2026"
        }
    ]
}
```

This allows the program to save structured information.

---

# 15. Data Persistence

Data persistence means that data remains available even after the application has been closed.

This is the most important client requirement.

Without persistence:

```text
Start program
     ↓
Add members
     ↓
Add payment
     ↓
Close program
     ↓
Everything disappears
```

With persistence:

```text
Start program
     ↓
Add members
     ↓
Add payment
     ↓
Save to data.json
     ↓
Close program
     ↓
Open program again
     ↓
Load data.json
     ↓
Previous information returns
```

This ensures that Chairman Ade's records do not disappear whenever the program is closed.

---

# 16. First-Run Handling

The first time the program runs, there may be no `data.json`.

The application handles this situation gracefully.

Instead of crashing with:

```text
FileNotFoundError
```

the application starts with an empty data structure.

Conceptually:

```text
Does data.json exist?
       │
   ┌───┴───┐
   │       │
  YES      NO
   │       │
   ↓       ↓
Load     Start
data     fresh
```

This satisfies the assignment's first-run requirement.

---

# 17. Corrupted Data Handling

The application must also handle corrupted JSON data.

For example, valid JSON might look like:

```json
{
    "members": [],
    "payments": []
}
```

If someone changes it to invalid content such as:

```text
this is not valid json
```

the program should not crash with a traceback.

Instead, it should display a human-readable message such as:

```text
Sorry, the saved data appears to be corrupted.
```

This demonstrates defensive programming.

---

# 18. The Activity Diary

The activity diary is stored in:

```text
diary.txt
```

The diary records important events.

Examples include:

```text
Member registration
Payment registration
```

Each event includes the date and time.

Example:

```text
[2026-08-25 04:20:55] Registered member: John Doe - 08012345678

[2026-08-25 04:25:12] Payment recorded: John Doe - ₦5,000.00 - August 2026
```

---

# 19. Why the Diary Uses Append Mode

The diary must preserve previous information.

For this reason, the file is opened using append mode:

```python
"a"
```

Append mode adds new information to the end of the file.

It does not delete existing information.

For example:

```text
[2026-08-25 04:20:55] Registered member: John Doe
```

After another event:

```text
[2026-08-25 04:20:55] Registered member: John Doe
[2026-08-25 04:25:12] Registered member: Mary Jane
```

The first record remains.

This creates a chronological activity history.

---

# 20. Why the Diary Is a Plain Text File

The client specifically requested a diary that he can read without the program.

Therefore, `diary.txt` is a normal text file.

It can be opened with:

- Windows Notepad
- VS Code
- Any text editor

The chairman does not need Python or the application to read the diary.

This makes the activity history accessible independently of the program.

---

# 21. Member Management

Member management is one of the core features of the application.

The chairman can register a new resident by entering:

```text
Name
Phone number
```

Example:

```text
Name: John Doe
Phone: 08012345678
```

The system creates:

```python
{
    "name": "John Doe",
    "phone": "08012345678"
}
```

and saves it permanently.

---

# 22. Payment Management

The payment system allows the chairman to record monthly dues.

A payment contains:

```text
Member
Amount
Month
```

Example:

```text
Member: John Doe
Amount: ₦5,000
Month: August 2026
```

The information is stored in `data.json`.

---

# 23. Member Validation

The system does not allow a payment to be recorded for someone who is not registered.

For example, if the chairman enters:

```text
Member: David Smith
```

but David Smith is not registered, the system searches for the member.

If no member is found, the function returns:

```python
None
```

The user can then receive a message such as:

```text
Member not found. Please register the member first.
```

This prevents incorrect financial records.

---

# 24. Payment Status

The payment status feature answers a simple but important question:

> Has this member paid for this particular month?

For example:

```text
Member: John Doe
Month: August 2026
```

If the payment exists:

```text
PAID
```

If it does not:

```text
OWING
```

The system checks both the member and month.

This means:

```text
July payment ≠ August payment
```

A member who paid July can still owe August.

---

# 25. Payment History

The payment history feature allows the chairman to see every payment belonging to a particular member.

Example:

```text
Member: John Doe

June 2026   ₦5,000
July 2026   ₦5,000
August 2026 ₦5,000
```

This provides a clear financial history for each resident.

It can also be used to calculate the total amount paid.

---

# 26. User Input Validation

The program receives information using Python's `input()` function.

Examples include:

```text
Member name
Phone number
Payment amount
Payment month
```

User input cannot always be trusted.

For example, the chairman may enter:

```text
five thousand
```

when the program expects:

```text
5000
```

The application uses validation and exception handling to prevent invalid input from breaking the program.

---

# 27. Exception Handling

Exception handling is used to deal with unexpected situations.

Python's `try` and `except` mechanisms allow the program to handle errors gracefully.

For example:

```python
try:
    amount = float(input("Enter payment amount: "))
except ValueError:
    print("Invalid amount.")
```

Instead of crashing, the user receives a useful message.

Exception handling is especially important for:

- Invalid numbers
- Missing files
- Corrupted JSON
- Other unexpected file-related problems

---

# 28. Python Import Styles

The assignment requires at least **two different import styles**.

This project demonstrates both.

## Import Style 1 — Import Specific Functions

```python
from chairman_book.members import register_member, get_members
```

This imports specific functions.

They can then be called directly:

```python
register_member()
get_members()
```

### Why use this style?

It is useful when the program only needs a few functions from a module.

It also keeps the code concise.

---

## Import Style 2 — Import a Module

```python
import chairman_book.payments as payments
```

This imports the module itself.

Functions are accessed through the module:

```python
payments.record_payment()
payments.get_payment_history()
payments.check_payment_status()
```

### Why use this style?

It makes it clear that the functions belong to the `payments` module.

For example:

```text
payments.record_payment()
```

immediately tells another developer where `record_payment()` comes from.

---

# 29. Why Dictionaries and Lists Were Used

The project uses dictionaries to represent individual records.

A member:

```python
{
    "name": "John Doe",
    "phone": "08012345678"
}
```

A payment:

```python
{
    "member": "John Doe",
    "amount": 5000,
    "month": "August 2026"
}
```

Lists are used to store multiple records.

For example:

```python
members = [
    {
        "name": "John Doe",
        "phone": "08012345678"
    },
    {
        "name": "Mary Jane",
        "phone": "08087654321"
    }
]
```

This structure is simple and works naturally with JSON.

---

# 30. Why JSON Was Used

JSON was chosen because it is suitable for a small application like this.

### Advantages of JSON

- Human-readable
- Easy to edit
- Easy for Python to process
- Supports lists
- Supports dictionaries
- Does not require a database server
- Simple to implement
- Suitable for persistent storage

For this project, JSON provides enough storage functionality without introducing unnecessary complexity.

---

# 31. Separation of Concerns

One of the most important design principles used in this project is **separation of concerns**.

Each module has a specific responsibility.

```text
members.py
    → Member management

payments.py
    → Payment management

storage.py
    → Data persistence

logger.py
    → Activity diary

main.py
    → User interface/menu
```

This prevents unrelated functionality from becoming mixed together.

For example, `storage.py` should not decide whether a member has paid.

Its responsibility is simply:

```text
Save data
Load data
```

Similarly, `members.py` should focus on members.

This makes the project easier to maintain.

---

# 32. Software Engineering Concepts Demonstrated

This project demonstrates the following concepts:

## Functions

Reusable blocks of code that perform specific tasks.

## Modules

Separate Python files containing related functionality.

## Packages

A folder containing related Python modules.

## Separation of Concerns

Each part of the application has its own responsibility.

## File Handling

The application reads from and writes to files.

## JSON

Used for structured persistent data.

## Data Persistence

Information survives application restarts.

## Exception Handling

Unexpected problems are handled gracefully.

## Input Validation

Invalid user input is handled safely.

## Logging

Important events are recorded with timestamps.

## Imports

Different Python import styles are demonstrated.

## Dictionaries

Used to represent individual records.

## Lists

Used to store multiple records.

## Loops

Used for repeated operations such as displaying members and menu options.

## Conditional Statements

Used to make decisions based on user input and application state.

---

# 33. Program Workflow

The general workflow is:

```text
                 START
                   │
                   ↓
              Load data
                   │
                   ↓
             Display menu
                   │
          ┌────────┼────────┐
          ↓        ↓        ↓
      Members   Payments   Status
          │        │        │
          └────────┼────────┘
                   ↓
              Save changes
                   │
                   ↓
              Write diary
                   │
                   ↓
             Display menu
                   │
                   ↓
                 EXIT
```

The application continues displaying the menu until the user chooses to exit.

---

# 34. Data Flow

When a member is registered:

```text
User
 ↓
main.py
 ↓
members.py
 ↓
storage.py
 ↓
data.json
```

When a payment is recorded:

```text
User
 ↓
main.py
 ↓
payments.py
 ↓
members.py
 ↓
Check member
 ↓
storage.py
 ↓
data.json
 ↓
logger.py
 ↓
diary.txt
```

This demonstrates how the modules work together.

---

# 35. Example Member Data

Example:

```json
{
    "name": "John Doe",
    "phone": "08012345678"
}
```

Another member:

```json
{
    "name": "Mary Jane",
    "phone": "08087654321"
}
```

---

# 36. Example Payment Data

Example:

```json
{
    "member": "John Doe",
    "amount": 5000,
    "month": "August 2026"
}
```

This allows the program to know:

- Who paid
- How much was paid
- What month the payment belongs to

---

# 37. Example Diary Entries

The diary may contain entries such as:

```text
[2026-08-25 04:20:55] Registered member: John Doe - 08012345678
[2026-08-25 04:23:10] Registered member: Mary Jane - 08087654321
[2026-08-25 04:25:12] Payment recorded: John Doe - ₦5,000.00 - August 2026
```

Each line represents an event.

The timestamp allows the chairman to know when the event happened.

---

# 38. Menu Features

The application provides a menu for interacting with the system.

Example:

```text
========================================
       CHAIRMAN ADE'S MONEY BOOK
========================================

1. Register member
2. View members
3. Record payment
4. View payment history
5. Check payment status
6. Exit
```

### Option 1 — Register Member

Allows the chairman to add a new estate member.

### Option 2 — View Members

Displays all registered members.

### Option 3 — Record Payment

Records a member's monthly payment.

### Option 4 — Payment History

Displays previous payments for a selected member.

### Option 5 — Payment Status

Checks whether a member has paid for a particular month.

### Option 6 — Exit

Closes the application safely.

---

# 39. Restart Test

The restart test is one of the most important assignment requirements.

### Test Procedure

1. Start the program.
2. Register Member 1.
3. Register Member 2.
4. Record a payment.
5. Exit the application.
6. Start the application again.
7. View the members.
8. View the payment history.

### Expected Result

The previously entered information should still exist.

For example:

```text
Member 1 → Still available
Member 2 → Still available
Payment  → Still available
```

This works because the data is stored in:

```text
data.json
```

instead of only being stored temporarily in Python memory.

---

# 40. First Run Test

The application must also work when no data file exists.

### Test

Delete or move:

```text
data.json
```

Then run:

```bash
python main.py
```

### Expected Result

The program should start normally.

It should not display:

```text
FileNotFoundError
```

or a Python traceback.

Instead, it should start with an empty record.

This demonstrates graceful first-run handling.

---

# 41. Corrupted Data Test

The assignment requires the application to handle deliberately corrupted data.

### Test

Open:

```text
data.json
```

and replace its contents with invalid JSON.

For example:

```text
THIS IS NOT VALID JSON
```

Then run:

```bash
python main.py
```

### Expected Result

The program should detect the problem and display a human-readable message.

For example:

```text
Sorry, the saved data appears to be corrupted.
```

The program should not expose a long Python traceback to the user.

This demonstrates proper exception handling.

---

# 42. Diary Test

The diary must preserve previous entries.

### Test

1. Register a member.
2. Check `diary.txt`.
3. Register another member.
4. Check `diary.txt` again.
5. Record a payment.
6. Check `diary.txt` again.

### Expected Result

The previous entries should remain.

New entries should appear underneath them.

Example:

```text
[2026-08-25 04:20:55] Registered member: John Doe
[2026-08-25 04:25:10] Registered member: Mary Jane
[2026-08-25 04:30:15] Payment recorded: John Doe - ₦5,000.00 - August 2026
```

No previous diary entry should be deleted.

---

# 43. Project Impact

The application has several practical benefits.

## Reduced Risk of Data Loss

The chairman no longer depends on memory or a phone to store financial information.

The information is saved to persistent storage.

## Better Accountability

The chairman can see:

- Who paid
- How much they paid
- Which month they paid for

## Easier Identification of Debtors

The system can check whether a member has paid for a particular month.

This makes it easier to identify members who are owing.

## Better Financial History

The payment history allows the chairman to review previous payments.

## Activity Tracking

The diary provides a chronological record of important actions.

## Improved Organization

Instead of scattered information, the chairman has a structured system.

---

# 44. Why This Project Matters

This project demonstrates how programming can solve a practical real-world problem.

The problem is not simply:

> "How do I write Python code?"

The bigger problem is:

> "How do I design a reliable system that protects important information?"

The application addresses this by combining:

```text
Python
+
Packages
+
Modules
+
Functions
+
File Handling
+
JSON
+
Exception Handling
+
Logging
+
Data Persistence
```

The result is a small but functional record-management system.

---

# 45. Bonus Features

The assignment provides optional bonus features.

## Backup

A backup option could create a dated copy of `data.json`.

For example:

```text
backups/
├── data_2026-08-25.json
├── data_2026-08-26.json
└── data_2026-08-27.json
```

This would provide an additional layer of protection against data loss.

---

## Import Members

Another optional feature is importing members from:

```text
new_members.txt
```

The expected format is:

```text
John Doe, 08012345678
Mary Jane, 08087654321
```

The program should also be able to handle badly formatted lines without crashing.

For example:

```text
John Doe, 08012345678
Invalid line
Mary Jane, 08087654321
```

The valid records can be imported while the invalid lines are skipped or reported.

---

# 46. How to Run the Application

## Requirements

You need:

- Python 3
- A terminal or command prompt
- The project files

## Step 1

Open the project folder.

## Step 2

Open a terminal in the project folder.

You should be in the folder containing:

```text
main.py
```

## Step 3

Run:

```bash
python main.py
```

## Step 4

Use the menu to interact with the program.

---

# 47. Important Files

| File | Responsibility |
|---|---|
| `main.py` | Entry point and menu interface |
| `chairman_book/__init__.py` | Identifies the directory as a Python package |
| `chairman_book/members.py` | Member registration, retrieval, and searching |
| `chairman_book/payments.py` | Payment recording, history, and status |
| `chairman_book/storage.py` | Loading and saving persistent data |
| `chairman_book/logger.py` | Writing timestamped activity logs |
| `data.json` | Persistent member and payment records |
| `diary.txt` | Human-readable activity history |
| `Readme.txt` | Project documentation |

---

# 48. What I Learned

Building this project helped me understand how individual Python concepts can be combined to create a complete application.

### Functions

I learned how reusable functions can organize application logic.

### Modules

I learned that related functions can be placed in separate files.

### Packages

I learned how multiple modules can be grouped together into a Python package.

### Imports

I learned different ways to import functions and modules.

### Dictionaries

I used dictionaries to represent structured information such as members and payments.

### Lists

I used lists to store multiple members and payments.

### File Handling

I learned how programs can read from and write to files.

### JSON

I learned how Python data can be stored in JSON format.

### Persistence

I learned that data stored in memory disappears when a program closes, while data written to a file can survive a restart.

### Exception Handling

I learned how to prevent expected errors from crashing the application.

### Logging

I learned how to create a simple activity diary using a plain-text file.

### Separation of Concerns

I learned why different responsibilities should be placed in different modules instead of putting everything in one file.

---

# 49. Conclusion

## Final Summary

**Chairman Ade's Money Book** is a Python package-based estate dues tracking system designed to solve the problem of unreliable manual financial record keeping.

The application allows the chairman to:

- Register members.
- View members.
- Record monthly payments.
- Check payment status.
- View payment history.
- Store records permanently.
- Recover previously saved information after restarting.
- Handle missing data files.
- Handle corrupted data.
- Maintain a readable activity diary.

The project also demonstrates important Python and software engineering concepts, including:

- Functions
- Modules
- Packages
- Imports
- Dictionaries
- Lists
- Loops
- Conditional statements
- File handling
- JSON
- Data persistence
- Exception handling
- Input validation
- Logging
- Separation of concerns

The most important lesson from this project is that **building software is not only about making the code run**.

A good application must also be:

- Organized
- Reliable
- Maintainable
- Understandable
- Resilient to errors
- Capable of preserving important information

Chairman Ade's Money Book transforms the estate's dues process from a **memory-based system into a structured digital record-keeping system**.

The system provides the chairman with a more reliable way to manage residents, payments, payment history, and financial activity while ensuring that important records survive beyond a single program session.

---

# 🎯 Assignment Requirements Checklist

| Requirement | Status |
|---|---|
| Python package | ✅ |
| `__init__.py` included | ✅ |
| At least 3 modules | ✅ |
| `main.py` outside package | ✅ |
| `main.py` acts as entry point | ✅ |
| Persistent data | ✅ |
| JSON storage | ✅ |
| First-run handling | ✅ |
| Corrupted data handling | ✅ |
| Plain-text diary | ✅ |
| Timestamped diary entries | ✅ |
| Diary uses append behavior | ✅ |
| Two import styles | ✅ |
| Member registration | ✅ |
| Member searching | ✅ |
| Payment recording | ✅ |
| Payment status | ✅ |
| Payment history | ✅ |
| README documentation | ✅ |
| Backup | 🔲 Bonus |
| Import members | 🔲 Bonus |

---

# 👩🏽‍💻 Author

**Rita Nnenna**

Built with Python as part of a practical assignment on:

> **Modules, Packages, Files, Exceptions, and Data Persistence.**

---