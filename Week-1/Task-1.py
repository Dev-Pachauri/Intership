#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install playsound


# In[ ]:


import tkinter as tk
from tkinter import messagebox
import datetime
import time
from playsound import playsound  # Make sure to install playsound using: pip install playsound

# Function to set the alarm
def set_alarm():
    alarm_time = entry.get()

    try:
        # Parsing the entered alarm time
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))

        # Validating the entered time
        if (0 <= alarm_hour < 24) and (0 <= alarm_minute < 60):
            now = datetime.datetime.now()
            alarm_datetime = datetime.datetime.combine(now.date(), datetime.time(alarm_hour, alarm_minute))

            # Checking if alarm time is in the past for today, then scheduling for tomorrow
            if alarm_datetime <= now:
                alarm_datetime += datetime.timedelta(days=1)  # Alarm time is tomorrow

            # Calculating the time difference until the alarms
            delta = alarm_datetime - now
            seconds = delta.total_seconds()

            # Informing user about the alarm setting
            messagebox.showinfo("Alarm Set", f"Alarm will ring in {int(seconds // 60)} minutes.")

            # Sleeping until the alarm time
            time.sleep(seconds)

            # Playing the alarm sound
            playsound('mixkit-retro-game-emergency-alarm-1000.wav')  # Replace 'mixkit-retro-game-emergency-alarm-1000.wavsv with your sound file

            # Showing a message when the alarm rings
            messagebox.showinfo("Wake Up", "Wake up!")

        else:
            # Error message for invalid time format
            messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format.")

    except Exception as e:
        # Generic error message for any exceptions
        messagebox.showerror("Error", f"An error occurred: {e}")

# Creating the GUI
root = tk.Tk()
root.title("Alarm Clock")

# Styling the GUI
root.geometry("300x200")
root.configure(bg='#e6e6e6')

# Label for instructions
label = tk.Label(root, text="Enter alarm time (HH:MM):", font=('Helvetica', 14), bg='#e6e6e6')
label.pack(pady=10)

# Entry field for alarm time
entry = tk.Entry(root, justify='center', font=('Arial', 16))
entry.pack()

# Button to set the alarm
button = tk.Button(root, text="Set Alarm", command=set_alarm, font=('Helvetica', 12), bg='#4CAF50', fg='white')
button.pack(pady=20)

# Running the GUI
root.mainloop()


# In[ ]:




