## Description 
This a booking system to be used for booking laboratory equiptment. The system allows the user to book a day’s worth of use for up to 14 days in advance. The booked and available dates are visually displayed for the user to view, and the user will then select their name, department, and date from drop down menues to make a booking. As the user makes the booking, the user is provided with a unique booking references which can be used to cancel the booking. Consists of two classes: `BookingWindow` and  `BookingDatabase`.

The `BookingWindow` class accepts apparatus_name_admin_input, booking_name_admin_input, booking_department_admin_input, first_slot_date_admin_input to set up the booking system. `create_log()` Launches an error log for the BookingDatabase and BookingWindow classes. `launch_labels()` method Launches tkinter label widgets that instruct the user how to use the boooking system. `launch_menus()` Launches tkinter option menu widgets (drop-down menus) from which the user selects their name, deparmental affiliation, and an available all-day slot when making a booking. `launch_buttons()` Launches tkinter button widgets with which the user submits bookings and cancellations of bookings of all-day slots. `launch_entries()` Launches a tkinter entry widget where the user enters a unique booking reference when cancelling a booking of an all-day slot. `create_initial_slots()` Creates 14 all-day slots the very first time the sqlite database is initialised. `create_additional_slots()` Creates all-day booking slots to maintain the number of bookable slots in the database, so that as time passes the user will always be able to book a slot for up to 14 days ahead. `create_booking_ref()` Creates a booking reference unique to the booking of an all-day slot. `make_booking()` Allows for the user to make a booking of an all-day slot. `cancel_booking()` Allows for the user to cancel a booking of an all-day slot. `display_calendar()` Displays a calendar of the next 14 all-day slots to the user.

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
https://github.com/Put-plus-plus/Booking-System-Python/assets/153921921/7f7c2d79-730a-4976-bfc1-e75354772728



