## Description 
The project is a booking system to be used for laboratory apparatuses, motivation for instance a FACS sorter machine as such experiments would require in advance planning with a python tkinter GUI and a sqlite database, prevents experiments to go to waste. The system allows the user to book a day’s worth of use for up to 14 days in advance. Upon making the booking the user gets a booking reference, which also allows the user to cancel the booking. The bookable slots are day long, bookable dates referred to as slots.  

The `BookingDatabase` class has a `sql_initiate_database()` method to create a table in an SQLite3 database, a `sql_maintain_database()` for adding bookable days, a `sql_make_booking()` method for making bookings, a `sql_display_bookings()` method for extracting slot information, a `sql_cancel_booking()` method for deleting slots, and a `sql_display_bookings()` method for viewing slots. The `BookingGUi` class has a `launch_gui()` method for initating the widgets, a `initiate_database()` method for creating slots at the initiation of the database, a `maintain_database()` method for maintaining the number of slots, a `generate_book_ref()` methof for creating a unique user booking reference, a `make_booking()` for the user to make a booking, a `cancel_booking()` method for the user to cancel a booking, and a `display_bookings()` method for displaying bookings visually. The `BookingLogger` class has a `log_message()` method for logging booking events, cancellations, and errors.  


## Dependencies
* Microsoft Windows version 10.0.19045
* Python version 3.9.1
* Sqlite3 ???, Time, Datetime, Logging, Tkinter, Random, String, Numpy, Calendar

## Execution - laboratory booking system example
```python
example_db_start_date = '2003-05-02'
example_apparatus_name = 'TSQQuantum'
example_users = ['Dr J Watson', 'Dr F Crick', 'Dr L Pauling', 'Dr E Schroedinger'] 
example_user_departments = ['Ornithology', 'Physics', 'Chemistry'] 
BookingGUI(example_apparatus_name, example_users, example_user_departments, example_db_start_date)
```

## Animation - laboratory booking system example 
remember to add the link to the GIF, which I must also make sure to add to the repo, see stackoverflow 
