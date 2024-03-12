import sqlite3
import datetime
import logging
import tkinter as tk 
import tkinter.messagebox    
import random 
import string 
import calendar
import re





class BookingDatabase:  

    def __init__(self, database_name, table_name):    
        self.create_log(database_name)
        self.connection = sqlite3.connect(database_name,              
                             detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES)   
        self.cursor = self.connection.cursor() 

        self.create_table(table_name)


    def create_log(self, log_name):
        
        '''Launches an error log for the BookingDatabase and BookingWindow classes.'''

        self.logger = logging.getLogger(f'{log_name}_logger')
        self.logger.setLevel(logging.INFO) 
        handler = logging.FileHandler(f'{log_name}_log.log')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')  
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
 


    def create_table(self, table_name): 

        '''Creates an empty sqlite database table for holding bookings of all-day slots. Accepts table_name, a string that represents the name of an 
        sqlite database table. The table has the columns: slot_id_no, a key unique to an all-day slot; slot_created_ts, the date the all-day slot was 
        added to the table; booking_name, the name of the person making a booking of an all-day slot; booking_department, the booker's departmental 
        affiliation; slot_date, the date of the all-day slot; and booking_reference, an identifier unique to a booking.'''

        self.cursor.execute('''                                          
            CREATE TABLE IF NOT EXISTS {} (  
            slot_id_no INTEGER PRIMARY KEY,
            slot_created_ts TIMESTAMP,
            booking_name TEXT,               
            booking_department TEXT,
            slot_date TIMESTAMP,
            booking_reference TEXT 
        )
        '''.format(table_name))     
     


    
    def create_slots(self, table_name, slot_id_no, slot_created_ts, booking_name, booking_department, slot_date, booking_reference):  
        
        '''Creates bookable all-day slots in the sqlite database table. Accepts table_name (string), the name of the table; slot_id_no (integer), an 
        identifier unique to a slot; slot_created_ts (datetime.datetime), the date the slot was added to the table; booking_name (string), the 
        name of the person making a booking; booking_department (string), the booker's departmental affiliation; slot_date (datetime.datetime), 
        and booking_reference (string), an identifier unique to a booking.'''
        
        try:
            self.cursor.execute("""
                INSERT INTO {} VALUES 
                ({}, '{}', '{}', '{}', '{}', '{}')       
                """.format(table_name, slot_id_no, slot_created_ts, booking_name, booking_department, slot_date, booking_reference))
            self.connection.commit()
        except:
            self.logger.exception(f'The {BookingDatabase.create_slots.__name__} method could not create a slot.')




    def create_booking(self, table_name, booking_name, booking_department, slot_date, booking_reference):
        
        '''Creates a booking by updating the columns booking_name, booking_department, and booking_reference of an existing available all-day slot
        in the sqlite database table, thus rendering the slot unavailable for booking to other users. Accepts table_name (string), the name of the table; 
        booking_name (string), the name of the person making a booking; booking_department (string), the booker's departmental affiliation; 
        slot_date (datetime.datetime), the date of the slot, and booking_reference (string), an identifier unique to a booking.'''
        
        try:
            self.cursor.execute('''
                UPDATE {} SET booking_name = '{}', booking_department = '{}', booking_reference = '{}'
                WHERE slot_date = '{}'
                '''.format(table_name, booking_name, booking_department, booking_reference, slot_date))
            self.connection.commit()
        except:
            self.logger.exception(f'The {BookingDatabase.create_booking.__name__} method could not create a booking.')




    def delete_booking(self, table_name, booking_reference):  
        
        '''Deletes a booking by updating the columns booking_name, booking_department, and booking_reference of a booked all-day slot in the sqlite
        database table, thus making the slot available for booking again. Accepts table_name (string), the name of the table; and booking_reference (string), 
        an identifier unique to a booking.'''
        
        try:
            default = 'available'
            self.cursor.execute('''
                UPDATE {} SET booking_name = '{}', booking_department = '{}', booking_reference = '{}'
                WHERE booking_reference = '{}'
                '''.format(table_name, default, default, default, booking_reference))
            self.connection.commit()
        except:
            self.logger.exception(f'The {BookingDatabase.delete_booking.__name__} method could not delete a booking.')
             



    def get_slots_available(self, table_name, booking_name, n_slots):        
        
        '''Returns a list of tuples that represents the last n available all-day slots in the sqlite database table. Each tuple represents an all-day slot
        and contains data from one column of the table (slot_date) eg eg [(datetime.datetime(2003, 6, 29, 0, 0),), (datetime.datetime(2003, 6, 30, 0, 0),),...]. 
        Accepts table_name (string), the name of the table; booking_name (string), the name of the person making a booking and should be set to 'available'; 
        and n_slots (integer), the last n slots.'''     
        
        try:
            self.cursor.execute(""" 
                SELECT slot_date FROM (SELECT * FROM {} ORDER BY slot_id_no DESC LIMIT {})
                WHERE booking_name = '{}' ORDER BY slot_id_no ASC
                """.format(table_name, n_slots, booking_name))
            available_slot_dates = self.cursor.fetchall() 
            return(available_slot_dates)
        except:
            self.logger.exception(f'The {BookingDatabase.get_slots_available.__name__} method could not get the booking date.')



 
    def get_slots_calendar_display(self, table_name, n_slots):                             
        
        '''Returns a list of tuples the represents the last n all-day slots in the sqlite database table. Each tuple represents an all-day slot
        and contains data from two columns of the table (booking_name, slot_date). booking_name is either default 'available' or the
        name of the booker, and the slot_date is the date of the all all-day slot, eg eg [('available', datetime.datetime(2003, 6, 29, 0, 0)), 
        ('Dr J Watson', datetime.datetime(2003, 6, 30, 0, 0)),...]. Accepts table_name (string), the name of the table; and n_slots 
        (integer), the last n days.'''

        try:
            self.cursor.execute("SELECT booking_name, slot_date FROM (SELECT * FROM {} ORDER BY slot_id_no DESC LIMIT {}) ORDER BY slot_id_no ASC".format(table_name, n_slots))
            booking_names_slot_dates = self.cursor.fetchall()
            return(booking_names_slot_dates)
        except:
            self.logger.exception(f'The {BookingDatabase.get_slots_calendar_display.__name__} method could not get the user name and the booking date.')
                   
    


    def get_slots_all(self, table_name):     

        '''Returns a list of tuples that represents all all-day slots in the sqlite database table. Each tuple represents an all-day slot and contains
        data from all columns in the table (slot_id_no, slot_created_ts, booking_name, booking_department, slot_date, booking_reference), eg 
        [(1, datetime.datetime(2024, 3, 11, 13, 22, 59, 285635), 'available', available', datetime.datetime(2003, 6, 29, 0, 0), 'available'), 
        (2, datetime.datetime(2024, 3, 11, 13, 22, 59, 285635), 'Dr J Watson', 'Ornithology', datetime.datetime(2003, 6, 30, 0, 0), '6SKD4'),...]. 
        Accepts table_name (string), the name of the table.''' 

        try:
            self.cursor.execute("SELECT * FROM {}".format(table_name))
            all_slots = self.cursor.fetchall()
            return(all_slots)
        except:
            self.logger.exception(f'The {BookingDatabase.get_slots_all.__name__} method could not get all slots.')



            
    def get_slots_last(self, table_name):        

        '''Returns a tuple that represents the last (most recently created) all-day slot in the sqlite database table. The tuple contains
        data from all columns in the table (slot_id_no, slot_created_ts, booking_name, booking_department, slot_date, booking_reference), eg
        (143, datetime.datetime(2024, 3, 11, 13, 22, 59, 285635), 'available', 'available', datetime.datetime(2003, 7, 12, 0, 0), 'available'). 
        Accepts table_name (string), the name of the table.'''  

        try:
            self.cursor.execute("SELECT * FROM {}".format(table_name))
            last_slot = self.cursor.fetchall()[-1]
            return(last_slot)
        except:
            self.logger.exception(f'The {BookingDatabase.get_slots_last.__name__} method could not get the last slot.')




    def is_booking_reference_unique(self, table_name, booking_reference):  

        '''Returns a tuple with the booking reference if it is already in use in the sqlite database table, and None when the booking 
        reference is unique. Accepts table_name (string), the name of the table; and booking_reference (string), a booking reference.'''

        try:
            self.cursor.execute('''SELECT booking_reference FROM {} WHERE booking_reference = '{}' '''.format(table_name, booking_reference))
            booking_reference_query = self.cursor.fetchone()    
            return(booking_reference_query)
        except:
            self.logger.exception(f'The {BookingDatabase.is_booking_reference_unique.__name__} method could not check if the booking reference is unique.')





                      
class BookingWindow:   

    def __init__(self, apparatus_name_admin_input, booking_name_admin_input, booking_department_admin_input, first_slot_date_admin_input):   

        self.default_value = 'available'
        self.apparatus_name_admin_input = apparatus_name_admin_input 
        self.booking_name_admin_input = booking_name_admin_input                   
        self.booking_department_admin_input = booking_department_admin_input                                 

        self.create_log()

        self.root = tk.Tk()
        self.root.geometry('780x450')
        self.root.title(f'{self.apparatus_name_admin_input} Booking System')
        self.root.configure(bg = 'lightblue')

        self.booking_database = BookingDatabase(f'{self.apparatus_name_admin_input}_booking_system.db', self.apparatus_name_admin_input)

        self.create_initial_slots(first_slot_date_admin_input) 
        self.create_additional_slots()        
        self.launch_labels()
        self.launch_menus()
        self.launch_buttons()
        self.launch_entries()
        self.display_calendar()
        self.root.mainloop()




    def create_log(self):
        
        '''Launches an error log for the BookingDatabase and BookingWindow classes.'''

        self.logger = logging.getLogger(f'{self.apparatus_name_admin_input}_logger')
        self.logger.setLevel(logging.INFO) 
        handler = logging.FileHandler(f'{self.apparatus_name_admin_input}_log.log')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s') 
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)




    def launch_labels(self): 

        '''Launches tkinter label widgets that instruct the user how to use the boooking system.'''
        
        try:
            lbl_bg = 'lightblue'
            lbl_lrg_font = ('Calibri', 18) 
            lbl_sm_font = ('Calibri', 14)
            self.welcome_lbl = tk.Label(self.root, text = f'Welcome to the {self.apparatus_name_admin_input} Booking System', bg = lbl_bg, font = lbl_lrg_font)
            self.welcome_lbl.place(x = 155, y = 30)
            self.make_booking_lbl = tk.Label(self.root, text = 'To Make a Booking', bg = lbl_bg, font = lbl_sm_font)
            self.make_booking_lbl.place(x = 310, y = 240)
            self.cancel_booking_lbl = tk.Label(self.root, text = 'To Cancel a Booking', bg = lbl_bg, font = lbl_sm_font)
            self.cancel_booking_lbl.place(x = 305, y = 335)

        except Exception as Argument:
            self.logger.exception(f'The {BookingWindow.launch_labels.__name__} method could not launch label widgets.')




    def launch_menus(self):  
        
        '''Launches tkinter option menu widgets (drop-down menus) from which the user selects their name, deparmental affiliation, and an available all-day slot when making a booking.'''
        
        try:
            men_bg = 'white'
            men_wd = 10
            men_font = ('Calibri', 8)
            self.booking_name_var = tk.StringVar(self.root)
            self.booking_name_var.set('user name')
            self.booking_name_menu = tk.OptionMenu(self.root, self.booking_name_var, *self.booking_name_admin_input)
            self.booking_name_menu.config(bg = men_bg, width = men_wd, font = men_font, highlightthickness = 0)
            self.booking_name_menu.place(x = 150, y = 280)
            self.booking_department_var = tk.StringVar(self.root)
            self.booking_department_var.set('department') 
            self.booking_department_menu = tk.OptionMenu(self.root, self.booking_department_var, *self.booking_department_admin_input)
            self.booking_department_menu.config(bg = men_bg, width = men_wd, font = men_font, highlightthickness = 0)
            self.booking_department_menu.place(x = 270, y = 280) 
            available_slot_dates = self.booking_database.get_slots_available(self.apparatus_name_admin_input, self.default_value, 14)       
            available_slot_dates = [a_date.strftime('%d %B %Y') for a_tuple in available_slot_dates for a_date in a_tuple]
            self.available_slot_dates_var = tk.StringVar(self.root)      
            self.available_slot_dates_var.set('available date') 
            self.available_slot_dates_menu = tk.OptionMenu(self.root, self.available_slot_dates_var, *available_slot_dates)
            self.available_slot_dates_menu.config(bg = men_bg, width = men_wd, font = men_font, highlightthickness = 0)
            self.available_slot_dates_menu.place(x = 390, y = 280)

        except Exception as Argument:
            self.logger.exception(f'The {BookingWindow.launch_menus.__name__} method could not launch option menu widgets.')




    def launch_buttons(self): 
        
        '''Launches tkinter button widgets with which the user submits bookings and cancellations of bookings of all-day slots.'''
        
        try:
            btn_bg = 'white' 
            btn_wd = 17
            btn_font = ('Calibri', 8)
            self.make_booking_btn = tk.Button(self.root, text = 'submit booking', width = btn_wd, bg = btn_bg, font = btn_font, command = self.make_booking)
            self.make_booking_btn.place(x = 510, y = 280)  
            self.cancel_booking_btn = tk.Button(self.root, text = 'submit cancellation',  width = btn_wd, bg = btn_bg, font = btn_font, command = self.cancel_booking)
            self.cancel_booking_btn.place(x = 395, y = 375)

        except Exception as Argument:
            self.logger.exception(f'The {BookingWindow.launch_buttons.__name__} method could not launch button widgets.')




    def launch_entries(self): 

        '''Launches a tkinter entry widget where the user enters a unique booking reference when cancelling a booking of an all-day slot.'''

        try:
            ent_fg = 'grey'
            ent_wd = 19
            ent_font = ('Calibri 8')
            self.cancel_booking_var = tk.StringVar(self.root, value = 'enter booking reference')
            self.cancel_boooking_input = tk.Entry(self.root, textvariable = self.cancel_booking_var, width = ent_wd, fg = ent_fg, font = ent_font)
            self.cancel_boooking_input.place(x = 257, y = 375)

        except Exception as Argument:
            self.logger.exception(f'The {BookingWindow.launch_entries.__name__} method could not launch entry widget.')
        



    def create_initial_slots(self, first_slot_date):   

        '''Creates 14 all-day slots the very first time the sqlite database is initialised. Aceepts first_slot_date (string), which 
        should be the date of the first all-day slot available for booking. Calls BookingDatabase.get_slots_all() to check the the number of slots 
        in the sqlite database table, and only if there are no slots in the table ia BookingDatabase.create_slots() called to create 14 slots.'''

        try:
            no_slots = len(self.booking_database.get_slots_all(self.apparatus_name_admin_input))   
            if no_slots < 1:
                slot_id_no = 1
                valid_slot_date_format = '%Y-%m-%d'
                slot_date = datetime.datetime.strptime(first_slot_date, valid_slot_date_format)  
                slot_created_ts = datetime.datetime.now()
                for i in range(14):
                    self.booking_database.create_slots(self.apparatus_name_admin_input, slot_id_no, slot_created_ts, self.default_value, self.default_value, slot_date, self.default_value) 
                    slot_id_no += 1
                    slot_date += datetime.timedelta(days=1)
                self.logger.info('An sql database of bookable slots was created.')

        except Exception as Argument:
            self.logger.exception(f'The {BookingWindow.create_initial_slots.__name__} method could not add slots to the database as it was initialised for the first time.')




    def create_additional_slots(self):  

        '''Creates all-day booking slots to maintain the number of bookable slots in the database, so that as time passes the user will always 
        be able to book a slot for up to 14 days ahead. Calls BookingDatabase.get_slots_last() to check when the last slot was created and if the last
        slot was created more than a day ago, BookingDatabase.create_slots() is called to create slots. Eg if the last slot was created two days ago,
        two new slots will be created.'''

        try:    
            last_slot = self.booking_database.get_slots_last(self.apparatus_name_admin_input)    
            last_slot_created_ts = last_slot[1]
            last_slot_id_no = last_slot[0]
            last_slot_date = last_slot[4] 
            slot_created_ts = datetime.datetime.now()
            no_slots_needed = (slot_created_ts-last_slot_created_ts).days
            while no_slots_needed > 0:
                last_slot_date += datetime.timedelta(days=1)
                last_slot_id_no += 1
                self.booking_database.create_slots(self.apparatus_name_admin_input, last_slot_id_no, slot_created_ts, self.default_value, self.default_value, last_slot_date, self.default_value) 
                no_slots_needed -= 1
                self.logger.info('A new bookable slot was added to the sql database')

        except Exception as Argument:
            self.logger.exception(f'The {BookingWindow.create_additional_slots.__name__} method could not add additional slots to the database.')  

      


    def create_booking_ref(self):   

        '''Creates a booking reference unique to the booking of an all-day slot. booking_reference (string) is created, and 
        BookingDatabase.is_booking_reference_unique() is called to check if booking_reference is already in use the sqlite database table. 
        booking_reference is only returned if not already in use.'''

        try:
            booking_reference = ''.join(random.choice(string.ascii_uppercase) for x in range(3)) 
            booking_reference = booking_reference.join(str(random.randint(0, 9)) for x in range(2))  
            booking_reference_query = self.booking_database.is_booking_reference_unique(self.apparatus_name_admin_input, booking_reference)   

            if isinstance(booking_reference_query, tuple):
                self.logger.exception('The booking referenced generated was not unqiue.')
            else:     
                return(booking_reference)

        except Exception as Argument:
            self.logger.exception(f'The {BookingWindow.create_booking_ref.__name__} method could not create a booking reference.') 




    def make_booking(self):    

        '''Allows for the user to make a booking of an all-day slot. User input from user interactions with drop-down menus (tkinter.OptionMenu) is:
        booking_name_var (string), the name of the person making a booking; booking_department_var (string), the booker's departmental affiliation; 
        and available_slot_dates_var (datetime.datetime), an available slot date. Calls create_booking_ref() to create a unique booking reference (string). 
        Calls BookingDatabase.create_booking() to create the booking in the sqlite database table, accepting the user input and the booking reference.
        Then calls BookingDatabase.get_slots_available() to update self.available_slot_dates_menu, the drop-down menu of available slot dates. Finally 
        calls display_calendar() to update the calendar of available and booked slots displayed to the user.'''

        try:
            booking_reference = self.create_booking_ref()
            slot_date = self.available_slot_dates_var.get()   
            slot_date_valid_format = '%d %B %Y'   
            slot_date_formatted = datetime.datetime.strptime(slot_date, slot_date_valid_format)
            self.booking_database.create_booking(self.apparatus_name_admin_input, self.booking_name_var.get(), self.booking_department_var.get(), slot_date_formatted, booking_reference) 

            updated_available_slot_dates = self.booking_database.get_slots_available(self.apparatus_name_admin_input, self.default_value, 14) 
            updated_available_slot_dates = [a_date.strftime('%d %B %Y') for a_tuple in updated_available_slot_dates for a_date in a_tuple]
            self.available_slot_dates_menu['menu'].delete(0, 'end')
            for date in updated_available_slot_dates:
                self.available_slot_dates_menu['menu'].add_command(label=date, command=lambda: self.available_slot_dates_var.set(date))  # last self used to be menu

            self.logger.info(f'User {self.booking_name_var.get()}, Department of {self.booking_department_var.get()}, made booking {booking_reference} for {self.available_slot_dates_var.get()}') 

            self.booking_name_var.set('user name') 
            self.booking_department_var.set('department') 
            self.available_slot_dates_var.set('available date') 

            self.display_calendar()
            
            tkinter.messagebox.showinfo(f'{self.apparatus_name_admin_input} Booking System', f'Thank you for your booking.\nPlease make a note of your booking reference: {booking_reference}') 
            
        except Exception as Argument:
            tkinter.messagebox.showinfo(f'{self.apparatus_name_admin_input} Booking System','Sorry, your booking failed.')
            self.logger.exception(f'The {BookingWindow.make_booking.__name__} method failed to make booking.')




    def cancel_booking(self): 

        '''Allows for the user to cancel a booking of an all-day slot. User input from interation with the entry bar (tkinter.Entry) is booking_reference
        (string), the booking reference unique to a booking. Calls BookingDatabase.delete_booking() to delete the booking in the sqlite database table, 
        accepting booking_reference. Then calls BookingDatabase.get_slots_available() to update self.available_slot_dates_menu, the drop-down menu of 
        available slot dates. Finally calls display_calendar() to update the calendar of available and booked slots displayed to the user.'''

        try: 
            booking_reference = self.cancel_boooking_input.get()
            booking_reference_valid_format = re.compile(r'^\d{1}[A-Z]{3}\d{1}$')       
            if not re.match(booking_reference_valid_format, booking_reference):   
                raise Exception() 

            self.booking_database.delete_booking(self.apparatus_name_admin_input, booking_reference)
            updated_available_slot_dates = self.booking_database.get_slots_available(self.apparatus_name_admin_input, self.default_value, 14)
            updated_available_slot_dates = [a_date.strftime('%d %B %Y') for a_tuple in updated_available_slot_dates for a_date in a_tuple]
            self.available_slot_dates_menu['menu'].delete(0, 'end')
            for date in updated_available_slot_dates:
                self.available_slot_dates_menu['menu'].add_command(label=date, command=lambda: self.available_slot_dates_var.set(date))  
            self.cancel_booking_var.set('enter booking reference')

            self.display_calendar() 

            tkinter.messagebox.showinfo(f'{self.apparatus_name_admin_input} Booking System','Thank you for cancelling your booking.') 
            self.logger.info(f'User cancelled booking: booking reference {booking_reference}.')

        except Exception as Argument:
            tkinter.messagebox.showinfo(f'{self.apparatus_name_admin_input} Booking System','Sorry, your cancellation failed.') 
            self.logger.exception(f'The {BookingWindow.cancel_booking.__name__} method failed to cancel booking.') 




    def display_calendar(self):  

        '''Displays a calendar of the next 14 all-day slots to the user. Calls booking_database.get_slots_calendar_display() to retrieve: 
        booking_name (string), the name of the person who made a booking, or the default value 'available'; and slot_date (datetime.datetime), 
        the date of the slot. The slots are graphically displayed using tkinter.Labels in the format eg 'Friday\n3 November 2023\navailable' and 
        'bg' set to 'lightgreen' for available slots, and eg 'Friday\n3 November 2023\nDr J Watson' with 'bg' set to 'orange' for booked slots.'''

        try:
            cal_font = ('Calibri', 8)  
            cal_wd = 13
            cal_fg = 'black'
            x_coord = 50
            y_coord = 100
            slots = self.booking_database.get_slots_calendar_display(self.apparatus_name_admin_input, 14)
            for slot in slots:
                booking_name = slot[0]
                slot_date = slot[1]
                slot_date_day_name = calendar.day_name[slot_date.weekday()]
                slot_date_formatted = slot_date.strftime('%d %B %Y')   
                calendar_entry_text = f'{slot_date_day_name}\n{slot_date_formatted}\n{booking_name}'
                if booking_name == self.default_value:
                    calendar_entry = tk.Label(self.root, text = calendar_entry_text, font = cal_font, width = cal_wd, fg = cal_fg, bg = 'lightgreen')
                else:
                    calendar_entry = tk.Label(self.root, text = calendar_entry_text, font = cal_font, width = cal_wd, fg = cal_fg, bg = 'orange')
                calendar_entry.place(x = x_coord, y = y_coord) 
                x_coord +=100
                if x_coord > 700:
                    y_coord = 160
                    x_coord = 50
        except Exception as Argument:
            self.logger.exception(f'The {BookingWindow.display_calendar.__name__} method could not display the calendar')

        


