## Description 
The project is a booking system to be used for laboratory apparatuses, motivation for instance a FACS sorter machine as such experiments would require in advance planning with a python tkinter GUI and a sqlite database, prevents experiments to go to waste. The system allows the user to book a day’s worth of use for up to 14 days in advance. Upon making the booking the user gets a booking reference, which also allows the user to cancel the booking.  

The `BookingDatabase` class has a `create_table()` method to create an SQLite3 database, a `` for adding slots, a `` method for making bookings, a `` method for extracting slot information, a `` method for deleting slots, and a `` method for viewing slots. The `BookingGUi` class has a ``  method for initating the widgets, a `` method for creating slots at the initiation of the database, a `` method for maintaining the number of slots, a `` methof for creating a unique user booking reference, a `` method for cancelling a booking, and a `` method for displaying bookings visually. The `BookingLogger` class has a `` method for logging booking events, cancellations, and errors.  

## Dependencies
* Microsoft Windows version 10.0.19045
* Python version 3.9.1
* Sqlite3 ???, Time, Datetime, Logging, Tkinter, Random, String, Numpy, Calendar

## Execution - X flow sorter booking system 
```python
Flashcards() #replace this 
# OUTPUT: something
```

## Animation - X flow sorter booking system 
remember to add the link to the GIF, which I must also make sure to add to the repo, see stackoverflow 
