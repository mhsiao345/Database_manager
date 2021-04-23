# import sqlite3 for querying and tkinter for GUI
import sqlite3
from tkinter import *
from tkinter import ttk, messagebox


# ---------- EMPLOYEE ----------- #
# function to show all existing employees
def show_all():
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve all employees from database
    c.execute("select * from employees")
    items = c.fetchall()

# iterate through retrieved items and save desired fields
    employees_list = [(row[0], row[1], row[2], row[3], row[14]) for row in items]

# result display setup
    employees = Tk()
    employees.title('All Current Employees')
    table = ttk.Treeview(employees, columns=(1, 2, 3, 4, 5), show='headings')
    table.pack()
    table.column(1, width=60)
    table.column(2, width=100)
    table.column(3, width=100)
    table.column(4, width=150)
    table.column(5, width=200)
    table.heading(1, text='Employee ID', anchor=W)
    table.heading(2, text='First Name', anchor=W)
    table.heading(3, text='Last Name', anchor=W)
    table.heading(4, text='Title', anchor=W)
    table.heading(5, text='Email', anchor=W)

# display result
    for row in employees_list:
        table.insert('', 'end', values=row)

# close database connection
    conn.close()


# function to show specific employee
def find_employee(number):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select employees from database
    c.execute("select * from employees where EmployeeId = (?)", (number,))
    row = c.fetchall()

# close database connection
    conn.close()

# display result
    try:
        messagebox.showinfo(title='Employee Details',
                            message=f'Employee ID: {row[0][0]}\n'
                                    f'First Name: {row[0][1]}\n'
                                    f'Last Name: {row[0][2]}\n'
                                    f'Title: {row[0][3]}\n'
                                    f'Birth Date: {row[0][5].split()[0]}\n'
                                    f'Hire Date: {row[0][6].split()[0]}\n'
                                    f'Address: {row[0][7]}\n'
                                    f'         {row[0][8]}, {row[0][9]} {row[0][10]} {row[0][11]}\n'
                                    f'Phone: {row[0][12]}\n'
                                    f'Email: {row[0][14]}')
# display error if not found
    except IndexError:
        messagebox.showerror(title='Employee Not Found',
                             message=f'Employee ID entered not found. Try again.')


# ---------- CUSTOMER ----------- #
# function to find customer by id
def find_customer_by_id(number):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select customer from database
    c.execute("select * from customers where CustomerId = (?)", (number,))
    row = c.fetchall()

# close database connection
    conn.close()

# display result
    try:
        messagebox.showinfo(title='Customer Details',
                            message=f'Customer ID: {row[0][0]}\n'
                                    f'First Name: {row[0][1]}\n'
                                    f'Last Name: {row[0][2]}\n'
                                    f'Company: {row[0][3]}\n'
                                    f'Address: {row[0][4]}\n'
                                    f'         {row[0][5]}, {row[0][6]} {row[0][7]} {row[0][8]}\n'
                                    f'Phone: {row[0][9]}\n'
                                    f'Email: {row[0][10]}')
# display error if not found
    except IndexError:
        messagebox.showerror(title='Customer Not Found',
                             message=f'Customer ID entered not found. Try again.')


# function to find customer by name
def find_customer_by_name(fn, ln):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select customer database
    c.execute("select * from customers where FirstName = (?) and LastName = (?)", (fn, ln,))
    row = c.fetchall()

# close database connection
    conn.close()

# display result
    try:
        messagebox.showinfo(title='Customer Details',
                            message=f'Customer ID: {row[0][0]}\n'
                                    f'First Name: {row[0][1]}\n'
                                    f'Last Name: {row[0][2]}\n'
                                    f'Company: {row[0][3]}\n'
                                    f'Address: {row[0][4]}\n'
                                    f'         {row[0][5]}, {row[0][6]} {row[0][7]} {row[0][8]}\n'
                                    f'Phone: {row[0][9]}\n'
                                    f'Email: {row[0][10]}')
# display error if not found
    except IndexError:
        messagebox.showerror(title='Customer Not Found',
                             message=f'Try again. Re-enter first and last name.')


# ---------- ARTIST ----------- #
# function to show all albums by artist
def show_all_albums_by_artist(artis_id, artist_name):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select album database
    c.execute("select * from albums where ArtistId = (?)", (artis_id,))
    items = c.fetchall()

# close database connection
    conn.close()

# display error if not found
    if len(items) == 0:
        messagebox.showerror(title='None Available',
                             message=f'Store has 0 albums by {artist_name}.')

# iterate through retrieved items and save desired fields
    else:
        albums_list = [(row[0], row[1]) for row in items]

# result display setup
        albums = Tk()
        albums.title(f'Available Albums in Store by {artist_name}')
        table = ttk.Treeview(albums, columns=(1, 2), show='headings')
        table.pack()
        table.column(1, width=60)
        table.column(2, width=500)
        table.heading(1, text='Album ID', anchor=W)
        table.heading(2, text='Album Title', anchor=W)

# display result
        for row in albums_list:
            table.insert('', 'end', values=row)


# function to find artist by id
def find_artist_by_id(number):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select artist from database
    c.execute("select * from artists where ArtistId = (?)", (number,))
    row = c.fetchall()

# close database connection
    conn.close()

# retrieve artist name
    try:
        artist_name = row[0][1]
# display error if not found
    except IndexError:
        messagebox.showerror(title='Artist Not Found',
                             message=f'Artist ID entered not found. Try again.')
# call display function
    else:
        show_all_albums_by_artist(number, artist_name)


# function to find artist by name
def find_artist_by_name(art_name):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select artist from database
    c.execute("select * from artists where Name like (?)", (art_name+'%',))
    row = c.fetchall()

# close database connection
    conn.close()

# retrieve artist id and name
    try:
        artist_id = row[0][0]
        artist_name = row[0][1]
# display error if not found
    except IndexError:
        messagebox.showerror(title='Artist Not Found',
                             message=f'Artist name entered not found. Try again.')
# call display function
    else:
        show_all_albums_by_artist(artist_id, artist_name)


# ---------- ALBUM ----------- #
# function to find album by id
def find_album_by_id(number):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select album
    c.execute("select * from albums where AlbumId = (?)", (number,))
    row = c.fetchall()

# retrieve artist id and album title
    try:
        artist_id = row[0][2]
        album_title = row[0][1]

# retrieve select artist from database
        c.execute("select * from artists where ArtistId = (?)", (artist_id,))
        row = c.fetchall()

# display result
        messagebox.showinfo(title='Album Found in Store',
                            message=f'Album ID: {number}\n'
                                    f'Album Title: {album_title}\n'
                                    f'Artist Name: {row[0][1]}')
# display error if not found
    except IndexError:
        messagebox.showerror(title='Album Not Found',
                             message=f'Album ID entered not found. Try again.')

# close database connection
    conn.close()


# function to find album by name
def find_album_by_name(alb_name):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select album from database
    c.execute("select * from albums where Title like (?)", ('%'+alb_name+'%',))
    row = c.fetchall()

# retrieve artist id and album id and title
    try:
        artist_id = row[0][2]
        album_id = row[0][0]
        album_title = row[0][1]

# retrieve select artist from database
        c.execute("select * from artists where ArtistId = (?)", (artist_id,))
        row = c.fetchall()

# display result
        messagebox.showinfo(title='Album Found in Store',
                            message=f'Album ID: {album_id}\n'
                                    f'Album Title: {album_title}\n'
                                    f'Artist Name: {row[0][1]}')
# display error if not found
    except IndexError:
        messagebox.showerror(title='Album Not Found',
                             message=f'Album name entered not found. Try again.')

# close database connection
    conn.close()


# ---------- TRACK ----------- #
# function to album tracks by id
def find_album_tracks_by_id(number):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select album from database
    c.execute("select * from albums where AlbumId = (?)", (number,))
    row = c.fetchall()

# retrieve album title
    try:
        album_title = row[0][1]
# display error if not found
    except IndexError:
        messagebox.showerror(title='Album Not Found',
                             message=f'Album ID entered not found. Try again.')

# retrieve select track from database
    else:
        c.execute("select * from tracks where AlbumId = (?)", (number,))
        items = c.fetchall()

# iterate through retrieved items and save desired fields
        album_tracks_list = [(row[2], row[0], row[1], row[5], row[8]) for row in items]

# result display setup
        albums_tracks = Tk()
        albums_tracks.title(f'Tracks List for Album Title: {album_title}')
        table = ttk.Treeview(albums_tracks, columns=(1, 2, 3, 4, 5), show='headings')
        table.pack()
        table.column(1, width=60)
        table.column(2, width=60)
        table.column(3, width=300)
        table.column(4, width=300)
        table.column(5, width=80)
        table.heading(1, text='Album ID', anchor=W)
        table.heading(2, text='Track ID', anchor=W)
        table.heading(3, text='Track Name', anchor=W)
        table.heading(4, text='Track Composer', anchor=W)
        table.heading(5, text='Price ($)', anchor=W)

# display result
        for row in album_tracks_list:
            table.insert('', 'end', values=row)

# close database connection
    conn.close()


# function to find album tracks by name
def find_album_tracks_by_name(track_name):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select track from database
    c.execute("select * from tracks where Name like (?)", ('%'+track_name+'%',))
    row = c.fetchall()

# close database connection
    conn.close()

# display error if not found
    if len(row) == 0:
        messagebox.showerror(title='Track Not Found',
                             message=f'Track name entered not found. Try again.')
# display result
    else:
        messagebox.showinfo(title='Track Found Available in Store',
                            message=f'Album ID: {row[0][2]}\n'
                                    f'Track ID: {row[0][0]}\n'
                                    f'Track Name: {row[0][1]}\n'
                                    f'Track Composer: {row[0][5]}\n'
                                    f'Price ($) {row[0][8]}')


# ---------- INVOICE ----------- #
# function to display invoice items
def invoice_display(items, first_name, last_name):
    invoices_list = [(first_name, last_name, row[1], row[0], row[2].split()[0], row[8]) for row in items]

# result display setup
    invoices = Tk()
    invoices.title(f'Customer Invoice Record')
    table = ttk.Treeview(invoices, columns=(1, 2, 3, 4, 5, 6), show='headings')
    table.pack()
    table.column(1, width=100)
    table.column(2, width=100)
    table.column(3, width=80)
    table.column(4, width=80)
    table.column(5, width=100)
    table.column(6, width=100)
    table.heading(1, text='First Name', anchor=W)
    table.heading(2, text='Last Name', anchor=W)
    table.heading(3, text='Customer ID', anchor=W)
    table.heading(4, text='Invoice ID', anchor=W)
    table.heading(5, text='Invoice Date', anchor=W)
    table.heading(6, text='Total ($)', anchor=W)

# display result
    for row in invoices_list:
        table.insert('', 'end', values=row)


# function to find invoice by id
def find_invoice_by_id(number):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select invoice from database
    c.execute("select * from invoices where InvoiceId = (?)", (number,))
    row = c.fetchall()

# display error if not found
    if len(row) == 0:
        messagebox.showerror(title='Invoice Not Found',
                             message=f'Invoice ID entered not found. Try again.')

# retrieve select customer from database
    else:
        c.execute("select * from customers where CustomerId = (?)", (row[0][1],))
        name = c.fetchall()

# call function to dsplay result
        invoice_display(row, name[0][1], name[0][2])

# close database connection
    conn.close()


# function to find invoice by customer
def find_invoice_by_customer_id(number):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select invoice from database
    c.execute("select * from invoices where CustomerId = (?)", (number,))
    row = c.fetchall()

# display error if not found
    if len(row) == 0:
        messagebox.showerror(title='None Found',
                             message=f'No invoices found for Customer ID: {number}. Try again.')

# retrieve select customer from database
    else:
        c.execute("select * from customers where CustomerId = (?)", (row[0][1],))
        name = c.fetchall()

# call function to display result
        invoice_display(row, name[0][1], name[0][2])

# close database connection
    conn.close()


# function to find invoice by customer name
def find_invoice_by_name(fn, ln):
    conn = sqlite3.connect('chinook.db')
    c = conn.cursor()

# retrieve select customer from database
    c.execute("select * from customers where FirstName = (?) and LastName = (?)", (fn, ln,))
    row = c.fetchall()

# display error if not found
    if len(row) == 0:
        messagebox.showerror(title='Customer Not Found',
                             message=f'Try again. Re-enter first and last name.')

# retrieve select invoice from database
    else:
        c.execute("select * from invoices where CustomerId = (?)", (row[0][0],))
        row = c.fetchall()

# call function to display result
        invoice_display(row, fn, ln)

# close database connection
    conn.close()
