from cgitb import text
from email.mime import image
import tkinter as tk
from tkinter.tix import IMAGE
from PIL import Image,ImageTk
from cv2 import convexityDefects
import requests

# api key = 38436b39a00b043e62639d08451a6bf1

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}




root=tk.Tk()

root.title("Weather App")
root.geometry("600x500")

def open_image(icon):
    size=int(second_frame.winfo_height()*0.35)
    img=ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img


def show_response(weather):
    try:
        City=weather['name']
        discription=weather['weather'][0]['description']
        temerature=weather['main']['temp']
        humidity=weather['main']['humidity']
        speed=weather['wind']['speed']
        final_result='City:%s\nCondition:%s\nTemperature:%s\N{DEGREE SIGN}C\nHumidity:%s%%\nWind speed:%s KMPH'%(City,discription,temerature,humidity,speed)
    except:
        final_result='Oops:Could Not Found data\nEnter the correct city name\n or Try again later'

    return final_result


def report(city):
    api_key='38436b39a00b043e62639d08451a6bf1'
    api_url='https://api.openweathermap.org/data/2.5/weather'
    data={'appid':api_key,'q':city,'units':'metric'}
    response=requests.get(api_url,data)
    # print(response.json())
    weather=response.json()
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'],chr(176),"C")
    # print(weather['main']['humidity'],"%")
    # print(weather['wind']['speed'],"KMPH")

    output['text']=show_response(weather)
    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)






root_img=Image.open(".\det.png","r")
resized_root_img=root_img.resize((600,500),Image.ANTIALIAS)
main_img=ImageTk.PhotoImage(resized_root_img)

bg_label=tk.Label(root,image=main_img)
bg_label.place(x=0,y=0,height=500,width=600)

first_frame=tk.Frame(bg_label,bg="#000fff000",bd=5)
first_frame.place(x=50,y=30,height=50,width=500)



city_name=tk.Entry(first_frame,font=('times new roman',25),width=20)
city_name.insert(0,'Enter the city')
city_name.bind()
city_name.grid(row=0,column=0,sticky='w')


but=tk.Button(first_frame,text='Get Weather',font=('times new roman',16,'bold'),fg="red",bg='white',command=lambda:report(city_name.get()))
but.grid(row=0,column=1,padx=8)

second_frame=tk.Frame(bg_label,bg="#000fff000",bd=5)
second_frame.place(x=50,y=110,height=350,width=500)


output=tk.Label(second_frame,font=40,bg='white',justify='left',anchor='nw')
output.place(relheight=1,relwidth=1)

weather_icon=tk.Canvas(output,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)





root.mainloop()