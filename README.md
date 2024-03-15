## Description 
This a booking system to be used for booking laboratory equiptment. The system allows the user to book a day’s worth of use for up to 14 days in advance. Consists of two classes: `BookingWindow` and  `BookingDatabase`. The `BookingWindow` class accepts first_slot_date_admin_input to set up the booking system including an error log for the BookingDatabase and BookingWindow classes, and 14 all-day slots the very first time the sqlite database is initialised. Creates all-day booking slots to maintain the number of bookable slots in the database, so that as time passes the user will always be able to book a slot for up to 14 days ahead. Creates a booking reference unique to the booking of an all-day slot. A graphical user interfaced with labels with user instructions on how to use the book system (that instruct the user how to use the boooking system), drop down menues from from which the user selects their name, deparmental affiliation, and an available all-day slot when making a booking, and buttons with which with which the user submits bookings and cancellations of bookings of all-day slots, as well as an entry widget where the user enters a unique booking reference when cancelling a booking of an all-day slot. Displays a calendar of the next 14 all-day slots to the user.

The `BookingDatabase` class has a `create_log()` method that launches an error log for the BookingDatabase and BookingWindow classes.`create_table()` method that Creates an empty sqlite database table for holding bookings of all-day slots. The table has the columns: slot_id_no, a key unique to an all-day slot; slot_created_ts, the date the all-day slot was added to the table; booking_name, the name of the person making a booking of an all-day slot; booking_department, the booker's departmental affiliation; slot_date, the date of the all-day slot; and booking_reference, an identifier unique to a booking. `create_slots()` method that Creates bookable all-day slots in the sqlite database table. `create_booking()` method that Creates a booking by updating the columns booking_name, booking_department, and booking_reference of an existing available all-day slot in the sqlite database table, thus rendering the slot unavailable for booking to other users. `delete_booking()` method that Deletes a booking by updating the columns booking_name, booking_department, and booking_reference of a booked all-day slot in the sqlite database table, thus making the slot available for booking again. `get_slots_available()` method that Returns a list of tuples that represents the last n available all-day slots in the sqlite database table. `get_slots_calendar_display()` Returns a list of tuples the represents the last n all-day slots in the sqlite database table. `get_slots_all()` method Returns a list of tuples that represents all all-day slots in the sqlite database table. `get_slots_last()` Returns a tuple that represents the last (most recently created) all-day slot in the sqlite database table. `is_booking_reference_unique()` Returns a tuple with the booking reference if it is already in use in the sqlite database table, and None when the booking reference is unique.  


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




