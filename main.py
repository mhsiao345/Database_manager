# import actions.py which contains database access functions and tkinter for GUI
import actions
from tkinter import *

# fonts definition used in GUI
FONT1 = ('Arial', 18, 'bold')
FONT2 = ('Arial', 12, 'bold')
FONT3 = ('Arial', 10, 'bold')

# empty list variable to hold display elements to be cleared
display = []


# ---------- CLEAR ----------- #
# function to clears all displayed elements on GUI
def clear():
    global display
    for element in display:
        element.grid_remove()

# sets display once again to an empty list
    display = []


# ---------- ALBUMS ----------- #
# albums GUI interface
def albums():
    clear()

# display title for this screen
    screen_label = Label(text='Album Details\n', font=FONT1, fg='green')
    screen_label.grid(column=0, row=0, columnspan=3)

# display elements for this screen
    album_id = Label(text='Album ID: ', font=FONT2)
    album_id.grid(column=0, row=1, pady=10)
    entry_album_id = Entry(width=18)
    entry_album_id.focus()
    entry_album_id.grid(column=1, row=1)
    album_name = Label(text='Album Name: ', font=FONT2)
    album_name.grid(column=0, row=2)
    entry_album_name = Entry(width=18)
    entry_album_name.grid(column=1, row=2)

# get album id entered and trigger corresponding database action
    def search_id():
        number = entry_album_id.get()
        actions.find_album_by_id(number)

# get album name entered and trigger corresponding database action
    def search_name():
        alb_name = entry_album_name.get()
        actions.find_album_by_name(alb_name)

# display available functions for this screen
    search_id_button = Button(text='Search by Album ID', width=20, font=FONT3, command=search_id)
    search_id_button.grid(column=2, row=1, padx=20)
    search_name_button = Button(text='Search by Album Name', width=20, font=FONT3, command=search_name)
    search_name_button.grid(column=2, row=2)
    home_button = Button(text='Home', width=10, font=FONT2, command=home)
    home_button.grid(column=0, row=4, pady=50)

# save all displayed elements to list
    global display
    display = [screen_label, album_id, entry_album_id, album_name, entry_album_name,
               search_id_button, search_name_button, home_button]


# ---------- ARTISTS ----------- #
# artists GUI interface
def artists():
    clear()

# display title for this screen
    screen_label = Label(text='Artist Details\n', font=FONT1, fg='green')
    screen_label.grid(column=0, row=0, columnspan=3)

# display elements for this screen
    artist_id = Label(text='Artist ID: ', font=FONT2)
    artist_id.grid(column=0, row=1, pady=10)
    entry_artist_id = Entry(width=18)
    entry_artist_id.focus()
    entry_artist_id.grid(column=1, row=1)
    artist_name = Label(text='Artist Name: ', font=FONT2)
    artist_name.grid(column=0, row=2)
    entry_artist_name = Entry(width=18)
    entry_artist_name.grid(column=1, row=2)

# get artist id entered and trigger corresponding database action
    def search_id():
        number = entry_artist_id.get()
        actions.find_artist_by_id(number)

# get artist name entered and trigger corresponding database action
    def search_name():
        art_name = entry_artist_name.get()
        actions.find_artist_by_name(art_name)

# display available functions for this screen
    search_id_button = Button(text='Search by Artist ID', width=20, font=FONT3, command=search_id)
    search_id_button.grid(column=2, row=1, padx=20)
    search_name_button = Button(text='Search by Artist Name', width=20, font=FONT3, command=search_name)
    search_name_button.grid(column=2, row=2)
    home_button = Button(text='Home', width=10, font=FONT2, command=home)
    home_button.grid(column=0, row=4, pady=50)

# save all displayed elements to list
    global display
    display = [screen_label, artist_id, entry_artist_id, artist_name, entry_artist_name,
               search_id_button, search_name_button, home_button]


# ---------- CUSTOMERS ----------- #
# customers GUI interface
def customers():
    clear()

# display title for this screen
    screen_label = Label(text='Customer Details\n', font=FONT1, fg='green')
    screen_label.grid(column=0, row=0, columnspan=3)

# display elements for this screen
    customer_id = Label(text='Customer ID: ', font=FONT2)
    customer_id.grid(column=0, row=1, pady=10)
    entry_customer_id = Entry(width=13)
    entry_customer_id.focus()
    entry_customer_id.grid(column=1, row=1)
    customer_fn = Label(text='First Name: ', font=FONT2)
    customer_fn.grid(column=0, row=2)
    entry_customer_fn = Entry(width=13)
    entry_customer_fn.grid(column=1, row=2)
    customer_ln = Label(text='Last Name: ', font=FONT2)
    customer_ln.grid(column=0, row=3)
    entry_customer_ln = Entry(width=13)
    entry_customer_ln.grid(column=1, row=3)

# get customer id entered and trigger corresponding database action
    def search_id():
        number = entry_customer_id.get()
        actions.find_customer_by_id(number)

# get customer name entered and trigger corresponding database action
    def search_name():
        first_name = entry_customer_fn.get().title()
        last_name = entry_customer_ln.get().title()
        actions.find_customer_by_name(first_name, last_name)

# display available functions for this screen
    search_id_button = Button(text='Search by Customer ID', width=20, font=FONT3, command=search_id)
    search_id_button.grid(column=2, row=1, padx=20)
    search_name_button = Button(text='Search by Name', width=20, font=FONT3, command=search_name)
    search_name_button.grid(column=2, row=3)
    home_button = Button(text='Home', width=10, font=FONT2, command=home)
    home_button.grid(column=0, row=4, pady=50)

# save all displayed elements to list
    global display
    display = [screen_label, customer_id, entry_customer_id, customer_fn, entry_customer_fn,
               customer_ln, entry_customer_ln, search_id_button, search_name_button, home_button]


# ---------- EMPLOYEE DETAILS ----------- #
# employee details GUI interface
def employee_details():
    clear()

# display title for this screen
    screen_label = Label(text='Employee Details\n', font=FONT1, fg='green')
    screen_label.grid(column=0, row=0, columnspan=3)

# display elements for this screen
    employee_id = Label(text='Enter Employee ID: ', font=FONT2)
    employee_id.grid(column=0, row=1)
    entry_id = Entry(width=8)
    entry_id.focus()
    entry_id.grid(column=1, row=1)

# get employee id entered and trigger corresponding database action
    def get_info():
        number = entry_id.get()
        actions.find_employee(number)

# display available functions for this screen
    get_button = Button(text='Get Details', width=16, font=FONT3, command=get_info)
    get_button.grid(column=2, row=1)
    home_button = Button(text='Home', width=16, font=FONT2, command=home)
    home_button.grid(column=0, row=3, pady=50)
    back_button = Button(text='Back', width=16, font=FONT2, command=employees)
    back_button.grid(column=2, row=3, pady=30)

# save all displayed elements to list
    global display
    display = [screen_label, employee_id, entry_id, get_button, home_button, back_button]


# ---------- EMPLOYEES ----------- #
# employees GUI interface
def employees():
    clear()

# display title for this screen
    screen_label = Label(text='Employees Database\n', font=FONT1, fg='green')
    screen_label.grid(column=0, row=0, columnspan=3)

# display available functions for this screen
    employee_button = Button(text='Employee Details', width=16, height=2, font=FONT2, command=employee_details)
    employee_button.grid(column=0, row=1)
    see_all_button = Button(text='All Employees', width=16, height=2, font=FONT2, command=actions.show_all)
    see_all_button.grid(column=0, row=2, padx=20, pady=20)
    home_button = Button(text='Home', width=16, height=2, font=FONT2, command=home)
    home_button.grid(column=2, row=2)

# save all displayed elements to list
    global display
    display = [screen_label, employee_button, see_all_button, home_button]


# ---------- HOME ----------- #
# home GUI interface
def home():
    clear()

# display title for this screen
    welcome = Label(text='\n\nStore Database Management\n\n', font=FONT1, fg='green')
    welcome.grid(column=0, row=1, columnspan=3)

# display available functions for this screen
    artists_button = Button(text='Artists', width=16, height=2, font=FONT2, command=artists)
    artists_button.grid(column=0, row=0)
    albums_button = Button(text='Albums', width=16, height=2, font=FONT2, command=albums)
    albums_button.grid(column=1, row=0)
    tracks_button = Button(text='Tracks', width=16, height=2, font=FONT2, command=tracks)
    tracks_button.grid(column=2, row=0)
    customers_button = Button(text='Customers', width=16, height=2, font=FONT2, command=customers)
    customers_button.grid(column=0, row=2)
    invoices_button = Button(text='Invoices', width=16, height=2, font=FONT2, command=invoices)
    invoices_button.grid(column=1, row=2)
    employees_button = Button(text='Employees', width=16, height=2, font=FONT2, command=employees)
    employees_button.grid(column=2, row=2)

# save all displayed elements to list
    global display
    display = [welcome, artists_button, albums_button, tracks_button,
               customers_button, invoices_button, employees_button]


# ---------- INVOICES ----------- #
# invoices GUI interface
def invoices():
    clear()

# display title for this screen
    screen_label = Label(text='Invoice Details\n', font=FONT1, fg='green')
    screen_label.grid(column=0, row=0, columnspan=3)

# display elements for this screen
    invoice_id = Label(text='Invoice ID: ', font=FONT2)
    invoice_id.grid(column=0, row=1)
    entry_invoice_id = Entry(width=13)
    entry_invoice_id.focus()
    entry_invoice_id.grid(column=1, row=1)
    customer_id = Label(text='Customer ID: ', font=FONT2)
    customer_id.grid(column=0, row=2, pady=10)
    entry_customer_id = Entry(width=13)
    entry_customer_id.grid(column=1, row=2)
    customer_fn = Label(text='First Name: ', font=FONT2)
    customer_fn.grid(column=0, row=3)
    entry_customer_fn = Entry(width=13)
    entry_customer_fn.grid(column=1, row=3)
    customer_ln = Label(text='Last Name: ', font=FONT2)
    customer_ln.grid(column=0, row=4)
    entry_customer_ln = Entry(width=13)
    entry_customer_ln.grid(column=1, row=4)

# get invoice id entered and trigger corresponding database action
    def search_invoice():
        number = entry_invoice_id.get()
        actions.find_invoice_by_id(number)

# get customer id entered and trigger corresponding database action
    def search_id():
        number = entry_customer_id.get()
        actions.find_invoice_by_customer_id(number)

# get customer name entered and trigger corresponding database action
    def search_name():
        first_name = entry_customer_fn.get().title()
        last_name = entry_customer_ln.get().title()
        actions.find_invoice_by_name(first_name, last_name)

# display available functions for this screen
    search_invoice_id_button = Button(text='Search by Invoice ID', width=20, font=FONT3, command=search_invoice)
    search_invoice_id_button.grid(column=2, row=1, padx=20)
    search_id_button = Button(text='Search by Customer ID', width=20, font=FONT3, command=search_id)
    search_id_button.grid(column=2, row=2)
    search_name_button = Button(text='Search by Customer', width=20, font=FONT3, command=search_name)
    search_name_button.grid(column=2, row=3)
    home_button = Button(text='Home', width=10, font=FONT2, command=home)
    home_button.grid(column=0, row=5, pady=30)

# save all displayed elements to list
    global display
    display = [screen_label, invoice_id, entry_invoice_id, customer_id, entry_customer_id,
               customer_fn, entry_customer_fn, customer_ln, entry_customer_ln,
               search_invoice_id_button, search_id_button, search_name_button, home_button]


# ---------- TRACKS ----------- #
# tracks GUI interface
def tracks():
    clear()

# display title for this screen
    screen_label = Label(text='Track Details\n', font=FONT1, fg='green')
    screen_label.grid(column=0, row=0, columnspan=3)

# display elements for this screen
    album_id = Label(text='Album ID: ', font=FONT2)
    album_id.grid(column=0, row=1, pady=10)
    entry_album_id = Entry(width=18)
    entry_album_id.focus()
    entry_album_id.grid(column=1, row=1)
    track_name = Label(text='Track Name: ', font=FONT2)
    track_name.grid(column=0, row=2)
    entry_track_name = Entry(width=18)
    entry_track_name.grid(column=1, row=2)

# get album id entered and trigger corresponding database action
    def search_id():
        number = entry_album_id.get()
        actions.find_album_tracks_by_id(number)

# get track name id entered and trigger corresponding database action
    def search_name():
        name = entry_track_name.get()
        actions.find_album_tracks_by_name(name)

# display available functions for this screen
    search_id_button = Button(text='Get Tracks for Album by ID', width=25, font=FONT3, command=search_id)
    search_id_button.grid(column=2, row=1, padx=20)
    search_name_button = Button(text='Search for Tracks by Name', width=25, font=FONT3, command=search_name)
    search_name_button.grid(column=2, row=2)
    home_button = Button(text='Home', width=10, font=FONT2, command=home)
    home_button.grid(column=0, row=4, pady=50)

# save all displayed elements to list
    global display
    display = [screen_label, album_id, entry_album_id, track_name, entry_track_name,
               search_id_button, search_name_button, home_button]


# ---------- GUI SETUP ----------- #
window = Tk()
window.title('Chinook Database Manager')
window.config(padx=50, pady=50)
window.geometry('700x350')

home()

window.mainloop()
