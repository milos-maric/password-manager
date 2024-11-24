from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
	pass_entry.delete(0, END)

	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = []
	password_symbols = []
	password_numbers = []

	password_letters = [choice(letters) for _ in range(randint(8, 10))]
	password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
	password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

	password_list = password_letters + password_symbols + password_numbers
	shuffle(password_list)

	password = "".join(password_list)
	pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

	website = website_entry.get()
	email = email_entry.get()
	password = pass_entry.get()
	new_data = {website: {
		"email": email,
		"password": password,
	}}

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="Ooops", message="Don't leave any fields empty.")
	else:
			try:
				with open("data.json", mode="r") as file:
					#Reading old data
					data = json.load(file)
			except FileNotFoundError:
				with open("data.json", mode="w") as file:
					json.dump(new_data, file, indent=4)
			else:
				#Updating old data with new data
				data.update(new_data)

				with open("data.json", mode="w") as file:
					#Saving updated data
					json.dump(data, file, indent=4)
			finally:
				website_entry.delete(0, END)
				pass_entry.delete(0, END)
				website_entry.focus()

# ---------------------------- SEARCH --------------------------------- #

def search_password():
	website = website_entry.get()

	try:
		with open("data.json", mode="r") as file:
			data = json.load(file)
	except FileNotFoundError:
		messagebox.showinfo(title="Error", message="No data file found.")
	else:
		if website in data:
			data_email = data[website]["email"]
			data_password = data[website]["password"]
			messagebox.showinfo(title=f"{website}", message=f"Email: {data_email}\nPassword: {data_password}")
		else:
			messagebox.showinfo(title="Error", message=f"No details for the {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=24)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "any-email@gmail.com")

pass_entry = Entry(width=24)
pass_entry.grid(row=3, column=1)

#Buttons
add_button = Button(text="Add", width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(row=3, column=2)

search_button = Button(text="Search", width=7, command=search_password)
search_button.grid(row=1, column=2)

window.mainloop()