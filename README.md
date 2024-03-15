## Description 
This a laboratory equiptment booking system designed for a user to be able to book all-day slots for up to 14 days in advance. The booking system consists of two classes: `BookingWindow` and  `BookingDatabase`. When the booking system is set up for the first time, the `BookingWindow` class accepts first_slot_date_admin_input, a list of userss, the users departmental afflication, and the aparatus name. There is an x method that creates 14 all-day slots the very first time the sqlite database is initialised, and an x method that creates all-day booking slots to maintain the number of bookable slots in the database, so that as time passes the user will always be able to book a slot for up to 14 days ahead. The x method creates a visual representation provding an overview calendar of the next 14 all-day slots to the user, and x,y,z methods labels with user instructions on how to use the book system (that instruct the user how to use the boooking system), drop down menues from from which the user selects their name, deparmental affiliation, and an available all-day slot when making a booking, along with The x method reference unique to the booking of an all-day slot. The x method is called with which with which the user submits bookings and cancellations of bookings of all-day slots. (MENTION TKINTER NAD SQLITE),  a `create_log()` method including an error log for the BookingDatabase and BookingWindow classes. 

The methods of the `BookingDatabase` class are called from `BookingWindow`. `create_table()` creates an empty SQLite database table for holding bookings of all-day slots; `create_slots()` creates bookable all-day slots in the table; `create_booking()` creates a booking in the table by updating of an existing available all-day slot, thus rendering the slot unavailable by booking to other users; `delete_booking()` deletes a booking by updating a booked all-day slot in the table, thus making the slot available for booking again; `get_slots_available()` returns the last n available all-day slots in the table; `get_slots_calendar_display()` returns the last n all-day slots in the table; `get_slots_all()` returns all all-day slots in the sqlite database table; `get_slots_last()` returns the last (most recently created) all-day slot in the table; and `is_booking_reference_unique()` returns None when the booking reference is unique.  


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




