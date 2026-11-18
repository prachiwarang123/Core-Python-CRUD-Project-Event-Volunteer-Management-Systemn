events = {}

while True:
    print("\n===== Corporate Event & Exhibition Management System =====")
    print("1. Add Event")
    print("2. Display All Events")
    print("3. Search Event")
    print("4. Update Event")
    print("5. Delete Event")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    match choice :
        case "1" :
            # Add Event
            print("=========Add Event=========")

            event_id = input("Enter Event ID: ")

            if event_id in events:
                print("Event ID already exists. Please use a unique ID.")
            else:
                event_name = input("Enter Event Name: ")
                event_type = input("Enter Event Type: ")
                event_date = input("Enter Event Date (DD-MM-YYYY): ")
                event_venue = input("Enter Event Venue: ")

                events[event_id] = {
                    "name": event_name,
                    "type": event_type,
                    "date": event_date,
                    "venue": event_venue
                }
                print("Event added successfully.")

        case "2" :
            # Display All Events

            print("=========Display All Events=========")

            if len(events) == 0:
                print("No events found.")
            else:
                print("=========All Registered Events=========")
                print("Total Events :", len(events))
                for event_id, event_details in events.items():
                    print(f"\nEvent ID : {event_id}")
                    print(f"Event Name : {event_details['name']}")
                    print(f"Event Type : {event_details['type']}")
                    print(f"Event Date : {event_details['date']}")
                    print(f"Event Venue : {event_details['venue']}")

        case "3" :
            # Search Event
            print("=========Search Event=========")

            event_id = input("Enter Event ID to search :")

            if event_id in events:
                event_details = events[event_id]
                print(f"\nEvent ID : {event_id}")
                print(f"Event Name : {event_details['name']}")
                print(f"Event Type : {event_details['type']}")
                print(f"Event Date : {event_details['date']}")
                print(f"Event Venue : {event_details['venue']}")
            else:
                print("Event Not Found")

        case "4" :
            # Update Event

            print("=========Update Event=========")

            event_id = input("Enter Event ID to Update :")

            if event_id in events:
                print("Enter a new details for the event ")
                new_event_name = input("Enter New Event Name :")
                new_event_date = input("Enter New Event Date (DD-MM-YYYY) :")
                new_event_venue = input("Enter New Event Venue :")

                events[event_id]["name"] = new_event_name
                events[event_id]["date"] = new_event_date
                events[event_id]["venue"] = new_event_venue
                print("Event Updated Successfully!.... ")
            else:
                print("Event Not Found")

        case "5" :
            # Delete Event

            print("=========Delete Event=========")

            event_id = input("Enter Event ID  To Delete :")

            if event_id in events:
                del events[event_id]
                print("Event Deleted Sucessfully!....")
            else:
                print("Event Not Found")


        case "6" :
            # Exit

            print("Exiting the program. Goodbye!")
            break

        case _ :
            print("Invalid choice. Please enter a number between 1 and 6.")





            




