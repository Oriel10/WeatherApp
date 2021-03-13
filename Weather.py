import tkinter as tk
from tkinter import font
import requests

# window size:
HEIGHT = 500
WIDTH = 600

# entry window:
ENTRY_FONT = 'Century'
ENTRY_SIZE = 18

# button:
BUTTON_FONT = 'Century'
BUTTON_SIZE = 13

# res window:
RES_FONT = 'Century'
RES_SIZE =  18

# frames:
U_FRAME_COLOR = '#80d4ff' # light blue
L_FRAME_COLOR = '#80d4ff' # light blue
   

def test(text):
    print("the text is: ",text)

# 489f2af5f5b132b49edcfcb2eff36305
# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        feelslike = weather['main']['feels_like']
        final_str = 'City: %s \nConditions: %s\nTemperature: %s celsius\nFeels Like: %s celsius' % (name, desc, temp, feelslike) 
    except:
        final_str = 'There was a problem retrieving that information'
    return final_str

def get_weather(city):
    weather_key = '489f2af5f5b132b49edcfcb2eff36305'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city,'appid': weather_key, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

# main window
window = tk.Tk()
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

#resize image
background_image = tk.PhotoImage(file = 'weather_resized.png')
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

# entry and button frame
entry_frame = tk.Frame(window, bg=U_FRAME_COLOR, bd=5)
entry_frame.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)# represents relative part of screen that will be colored

#entry window
entry = tk.Entry(entry_frame, font = (ENTRY_FONT,ENTRY_SIZE))
entry.place(relwidth=0.65, relheight=1)

#button
#explanation of command:
#lambda is an inline function that is defined at run time and can change at run time as well.
#entry.get() returns what is in the entry at any moment
#command gets a function as parameter
button = tk.Button(entry_frame, text="Get Weather", font=(BUTTON_FONT, BUTTON_SIZE), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

#result frame
lower_frame = tk.Frame(window, bg=L_FRAME_COLOR, bd=10)
lower_frame.place(relx=0.1, rely=0.25, relwidth=0.75, relheight=0.6)

#result label
label = tk.Label(lower_frame, font=(RES_FONT, RES_SIZE), anchor='nw', justify='left')
label.place(relwidth=1,relheight=1)

#makes the window keep running
window.mainloop() 