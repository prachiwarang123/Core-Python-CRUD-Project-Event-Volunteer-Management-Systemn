# Event Volunteer Management System

A simple, menu-driven console application written in Python to manage corporate events and exhibitions. It runs in the terminal and keeps all records in a Python dictionary while the program is running.
This is a beginner-level project that uses only basic Python concepts. No libraries, files or databases are needed.

## Features

The program shows a menu and keeps running until you choose Exit.
 1. Add Event : Takes the event details and saves them. If the Event ID already exists, it shows a message instead.
 2. Display All Events : Shows every registered event, or a message if there are none. 
 3. Search Event : Finds an event by Event ID and shows its full details. 
 4. Update Event : Changes the name, date and venue of an existing event. 
 5. Delete Event : Removes an event by Event ID and shows a success or failure message. 
 6. Exit : Ends the program. 

## Event Details Stored

- Event ID
- Event Name
- Event Type (for example: Annual Business Summit, Product Launch, Technology Exhibition, Corporate Party, Business Conference)
- Event Date
- Event Venue

## Python Concepts Used

- Dictionary and nested dictionary
- `while` loop
- `match-case`
- `if-else` conditions
- `for` loop
- Dictionary methods such as `items()` and `len()`

## How to Run

1. Download or clone this repository.`
   git clone <your-repository-url>
2. Open the project folder in VS Code (or any terminal).
3. Run the program:
   python event.py
   On some systems, use `python3 event.py`.
4. Type the number of the option you want and press Enter. Choose `6` to exit.

## Sample Output

```
===== Corporate Event & Exhibition Management System =====
1. Add Event
2. Display All Events
3. Search Event
4. Update Event
5. Delete Event
6. Exit
Enter your choice (1-6): 5
=========Delete Event=========
Enter Event ID  To Delete :102
Event Deleted Sucessfully!....

===== Corporate Event & Exhibition Management System =====
1. Add Event
2. Display All Events
3. Search Event
4. Update Event
5. Delete Event
6. Exit
Enter your choice (1-6): 2
=========Display All Events=========
=========All Registered Events=========
Total Events : 1

Event ID : 101
Event Name : Tech Expo 2026
Event Type : Technology Exhibition
Event Date : 15-12-2026
Event Venue : Mumbai Convention Center
```

## Limitations
- Data is stored only in memory, so all records are lost when the program closes.
- The program works only in the terminal.
- Event ID and Event Type cannot be changed during an update.

## Future Enhancements
- Save data permanently using a file or SQLite database.
- Search by event name, date or type.
- Add input validation.
- Add a graphical or web interface.


## Author
Prachi Warang
