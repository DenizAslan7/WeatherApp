import requests
import tkinter as tk
from tkinter import messagebox

# GUI
window = tk.Tk()
window.config(bg="deep sky blue")
window.title("Weather")
window.minsize(height=600,width=400)

# City label
city_label = tk.Label(text="City : ",
                      font=("Ariel",18,"normal"),
                      bg="Deep sky blue")
city_label.place(x=80,y=354)

# City Entry
city_entry = tk.Entry()
city_entry.place(x=145,y=360,
                 width=170,
                 height=22)
# Func
def get_city_info():
    city = city_entry.get()
    api_key = "Your api key !"
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        temp_c = str(float(temp) - 273.15)
        desc = data["weather"][0]["description"]
        global output_label
        output_label.config(text="{}".format(temp_c[0]))
        global city_name_label
        city_name_label.config(text=city.upper())
        global description_label
        description_label.config(text=desc)



    else:
        message = messagebox.showerror(title="Invalid City Name!",
                                       message="Please give valid city name.")



# Enter Button
city_button = tk.Button(text="Search",
                        command=get_city_info)
city_button.place(x=145,y=390)

# Output Label
output_label = tk.Label(text="5",
                        font=("Ariel",100,"normal"),
                        bg="Deep sky blue",
                        fg="white")
output_label.place(x=170,y=140)

# Celcius Label
celcius_label = tk.Label(text="°C",
                         font=("Ariel",40,"bold"),
                         bg="Deep sky blue",
                         fg="gold")
celcius_label.place(x=240,y=110)

# City Name Label
city_name_label = tk.Label(text="No Data",
                           font=("Ariel",26,"bold"),
                           bg="deep sky blue",
                           fg="white")
city_name_label.place(x=135,y=60)

# Description Label
description_label = tk.Label(text="No Data",
                             font=("Ariel",20,"normal"),
                             bg="deep sky blue",
                             fg="gray37")
description_label.place(x=150,y=290)




window.mainloop()

