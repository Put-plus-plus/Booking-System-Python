## Description 
This a booking system to be used for booking laboratory equiptment, as equiptment is often shared across research groups in academic departments. The system allows the user to book a day’s worth of use for up to 14 days in advance. The booked and available dates are visually displayed for the user to view, and the user will then select their name, department, and date from drop down menues to make a booking. As the user makes the booking, the user is provided with a unique booking references which can be used to cancel the booking. 

The `BookingDatabase` class has a `sql_initiate_database()` method to create a table in an SQLite3 database, a `sql_maintain_database()` for adding bookable days, a `sql_make_booking()` method for making bookings, a `sql_display_bookings()` method for extracting slot information, a `sql_cancel_booking()` method for deleting slots, and a `sql_display_bookings()` method for viewing slots. The `BookingGUi` class has a tkinter GUI a `launch_gui()` method for initating the widgets, a `initiate_database()` method for creating slots at the initiation of the database, a `maintain_database()` method for maintaining the number of slots, a `generate_book_ref()` methof for creating a unique user booking reference, a `make_booking()` for the user to make a booking, a `cancel_booking()` method for the user to cancel a booking, and a `display_bookings()` method for displaying bookings visually. The `BookingLogger` class has a `log_message()` method for logging booking events, cancellations, and errors.  


## Dependencies
* Microsoft Windows 10.0.19045
* Python 3.9.1
* sqlite3 3.33.0, datetime (built-in), logging (built-in), tkinter (built-in), random (built-in), string (built-in), calendar (built-in), re (built-in)
 
## Execution - cell sorter booking system example   
```python
from booking_system import *

cell_sorter_apparatus_name = 'BDFACSMelody'
cell_sorter_booking_name =  ['Dr E Chargaff', 'Dr F Crick', 'Dr M Delbrück', 'Dr L Pauling', 'Dr J Watson'] 
cell_sorter_booking_department = ['Ornithology', 'Physics', 'Biochemistry', 'Chemistry']
cell_sorter_first_slot_date = '2024-08-21'
BookingWindow(cell_sorter_apparatus_name, cell_sorter_booking_name, cell_sorter_booking_department, cell_sorter_first_slot_date)
```

## Animation - cell sorter booking system example
remember to add the link to the GIF, which I must also make sure to add to the repo, see stackoverflow 
