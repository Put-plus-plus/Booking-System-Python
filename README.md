## Description 
This a booking system to be used for booking laboratory equiptment, as costly equiptment is often shared across research groups in academic departments. The system allows the user to book a day’s worth of use for up to 14 days in advance. The booked and available dates are displayed for the user to view, and the user will then select their name, department, and date from drop down menues to make a booking. As the user makes the booking, the user is provided with a unique booking references which can be used to cancel the booking. 

The `BookingDatabase` class has a `sql_initiate_database()` method to create a table in an SQLite3 database, a `sql_maintain_database()` for adding bookable days, a `sql_make_booking()` method for making bookings, a `sql_display_bookings()` method for extracting slot information, a `sql_cancel_booking()` method for deleting slots, and a `sql_display_bookings()` method for viewing slots. The `BookingGUi` class has a tkinter GUI a `launch_gui()` method for initating the widgets, a `initiate_database()` method for creating slots at the initiation of the database, a `maintain_database()` method for maintaining the number of slots, a `generate_book_ref()` methof for creating a unique user booking reference, a `make_booking()` for the user to make a booking, a `cancel_booking()` method for the user to cancel a booking, and a `display_bookings()` method for displaying bookings visually. The `BookingLogger` class has a `log_message()` method for logging booking events, cancellations, and errors.  


## Dependencies
* Microsoft Windows version 10.0.19045
* Python version 3.9.1
* Sqlite3 ???, Time, Datetime, Logging, Tkinter, Random, String, Numpy, Calendar

## Execution - laboratory booking system example
```python
first_bookable_date = '2003-05-02'
equipment_name = 'TSQQuantum'
users = ['Dr J Watson', 'Dr F Crick', 'Dr L Pauling', 'Dr E Schrödinger'] 
user_departments = ['Ornithology', 'Physics', 'Chemistry'] 
BookingSystem(equipment_name, users, user_departments, first_bookable_date)
```

## Animation - laboratory booking system example 
remember to add the link to the GIF, which I must also make sure to add to the repo, see stackoverflow 
