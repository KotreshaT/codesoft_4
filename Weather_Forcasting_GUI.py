from tkinter import *
import requests
root=Tk()
root.geometry("750x250")
root.title("weather forcast")

api_key = "0440a6f00336b7991fb55c5cb92ea7ba"

def get_weather(api_key, city_entry):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city=city_entry.get()
    print(city)
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit     # metric for celsies
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            l2=Label(root,text=f"Weather in {city_entry.get()}:",font="Helvetica 13 bold").grid(row=3,column=1)
            # print(f"Weather in {city_entry.get()}:")
            l3=Label(root,text=f"Temperature: {data['main']['temp']}°C",font="Helvetica 13 bold").grid(row=4,column=1)
            l4=Label(root,text=f"Description: {data['weather'][0]['description']}",font="Helvetica 13 bold").grid(row=5,column=1)
           
        else:
            l5=Label(root,text=f"Error: {data['message']}",font="Helvetica 13 bold").grid(row=5,column=1)
            
    except Exception as e:
        l3=Label(root,text=f"An error occurred: {e}",font="Helvetica 13 bold").grid(row=4,column=1)
        
def reset():
    root.after(500, root.destroy)
    

label1=Label(root,text=" WEATHER FORCASTING ",font="Helvetica 20 bold",background="skyblue",justify=LEFT).grid(row=0,column=1)
city_label=Label(root,text="Enter The City  Name: ",font="Helvetica 13 bold",pady=20,padx=20).grid(padx=20,row=1,column=0)

city_entry=StringVar()
city_entry.set("")

entry=Entry(root,textvariable=city_entry,font="Helvetica 13 bold",background="light yellow").grid(row=1,column=1)
s_btn=Button(root,text="SUBMIT",command=lambda:get_weather(api_key,city_entry),font="Helvetica 13 bold",background="light yellow",padx=10).grid(ipadx=20,row=2,column=1)
r_btn=Button(root,text="EXIT",command=reset,font="Helvetica 13 bold",background="light yellow",padx=15).grid(row=2,column=2,ipadx=10)

root.mainloop()