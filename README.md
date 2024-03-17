## Description 
This is a laboratory equiptment booking system for the booking of all-day slots for up to 14 days in advance. The system consists of the `BookingWindow` class that holds the graphical user interface, and the `BookingDatabase` class that holds the SQLite database. The system is set up by passing the name of the eqiptment, a list of users, a list of the users' departmental affiliations, and the the date of the first bookable all-day slot into `BookingWindow`. `BookingWindow` has eleven methods: `create_log()`creates an error log for the system; `create_initial_slots()` creates 14 all-day slots the first time the system is initialised; `create_additional_slots()` maintains the number of bookable slots in the database, so that as time passes the user is always able to book an all-day slot for up to 14 days ahead; `display_calendar()` displays a calendar to the user so to provide an overview of the next 14 all-day slots; `launch_labels()`, `launch_menus()`, and `launch_buttons()` and `launch_entries()` launch widgets for user interaction; `create_booking_ref()` creates a booking reference unique to a booking; `make_booking()` creates a booking after accepting user input and the unique booking reference, and displays the unique booking reference to the user; `cancel_booking()` cancels a booking by accepting the unique booking reference as input from the user. 

    

The methods of the `BookingDatabase` class are called from `BookingWindow`. `create_table()` creates an empty SQLite database table for holding bookings of all-day slots; `create_slots()` creates available all-day slots in the table; `create_booking()` creates a booking in the table by updating of an existing available all-day slot, thus rendering the slot unavailable by booking to other users; `delete_booking()` deletes a booking by updating a booked all-day slot in the table, thus making the slot available for booking again; `get_slots_available()` returns the last n available all-day slots in the table; `get_slots_calendar_display()` returns the last n all-day slots in the table; `get_slots_all()` returns all all-day slots in the table; `get_slots_last()` returns the last (most recently created) all-day slot in the table; and `is_booking_reference_unique()` returns None when the booking reference is unique.  


## Dependencies
* Microsoft Windows 10.0.19045
* Python 3.9.1
* sqlite3 3.33.0, datetime (built-in), logging (built-in), tkinter (built-in), random (built-in), string (built-in), calendar (built-in), re (built-in)
 
## Execution - booking system example   
```python
from booking_system import *

sorter_apparatus_name = 'BDFACSMelody'
sorter_booking_name =  ['Dr E Chargaff', 'Dr F Crick', 'Dr M Delbrück', 'Dr L Pauling', 'Dr J Watson'] 
sorter_booking_department = ['Ornithology', 'Physics', 'Biochemistry', 'Chemistry']
sorter_first_slot_date = '2024-08-21'
BookingWindow(sorter_apparatus_name, sorter_booking_name, sorter_booking_department, sorter_first_slot_date)
```

## Animation - booking system example
https://github.com/Put-plus-plus/Booking-System-Python/assets/153921921/d29e0f5b-c854-4679-bd4e-9a4a3369f24d




