import tkinter as tk
import tkinter.messagebox as messagebox
import requests
from twilio.rest import Client

account_sid = 'ACb72aee305173ceb5f91e586307758224'
auth_token = 'a4a18bc7324bc856dc0907afb9ebfecc'

# Create a Twilio client
client = Client(account_sid, auth_token)

import geocoder

# Get your current location using the "ipinfo.io" service
g = geocoder.ip('me')

# Print the latitude and longitude of your current location

# Define the main window
root = tk.Tk()
root.title("Doctor Messenger")

# Define the input fields
message_label = tk.Label(root, text="Message to Doctor:")
message_label.grid(row=0, column=0, padx=5, pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.grid(row=0, column=1, padx=5, pady=5)

location_label = tk.Label(root, text="Share Your Location:")
location_label.grid(row=1, column=0, padx=5, pady=5)


def share_location():
    phone_number = phone_entry.get()
    try:
        # Use the geocoder library to get the user's location
        g = geocoder.ip('me')
        location_str = f"{g.city}, {g.state}, {g.country}, Latitude: {g.lat}, Longitude: {g.lng}"

        # Display the user's location in a message box
        messagebox.showinfo("Location", location_str)
    except:
        messagebox.showerror("Error", "Unable to get location data.")

    message = client.messages.create(
        to=phone_number,
        from_='+18885217093',
        body=location_str
    )

location_button = tk.Button(root, text="Share", command=share_location)
location_button.grid(row=1, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Call Your Doctor:")
phone_label.grid(row=2, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root, width=50)
phone_entry.grid(row=2, column=1, padx=5, pady=5)


def call_doctor():
    # Get the phone number from the user input
    phone_number = phone_entry.get()
    # Create the Twilio call
    call = client.calls.create(
        to=phone_number,
        from_='+18885217093',
        url='http://demo.twilio.com/docs/voice.xml'
    )
    # Show a message to the user that the call is being made
    messagebox.showinfo("Calling", f"Calling {phone_number}...")

# Create the tkinter window and widgets
root = tk.Tk()
phone_label = tk.Label(root, text="Enter phone number:")
phone_label.grid(row=0, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=0, column=1, padx=5, pady=5)
call_button = tk.Button(root, text="Call", command=call_doctor)
call_button.grid(row=1, column=1, padx=5, pady=5)


# Define the send button
def send_message():
    # Get the message content from the user input
    message = message_entry.get()
    # Get the phone number from the user input
    phone_number = phone_entry.get()
    # Create the Twilio message
    message = client.messages.create(
        to=phone_number,
        from_='+18885217093',
        body=message
    )
    # Show a message to the user that the message has been sent
    messagebox.showinfo("Sent", f"Your message: {message} has been sent to your doctor.")
    # Clear the message entry field
    message_entry.delete(0, tk.END)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=4, column=1, padx=5, pady=5)

# Start the application
root.mainloop()

print(f'Latitude: {g.lat}')
print(f'Longitude: {g.lng}')