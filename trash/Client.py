from tkinter import *
import sys
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import tkinter.font as font
from turtle import color
from PIL import Image, ImageTk
from tkinter import PhotoImage
import threading
from Adafruit_IO import MQTTClient
import time
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyrebase
from datetime import datetime
import re

class Client:

    def __init__(self,master):
        self.myFont = font.Font(family='Courier', weight='bold')
        self.master = master
        self.counter = 1
        self.current = 1
        self.listGraphHeat=["",""]
        self.listGraphHumd=["",""]
        self.listGraphEarth=["",""]
        self.trI = 0
        self.master.geometry('2000x1000')
        # self.master.attributes('-fullscreen', True)
        self.page1 = Frame(master,bg='black',width = 3000,height = 1000)
        self.page2 = Frame(master,bg='black',width = 3000,height = 1000)
        self.page3 = Frame(master,bg='black',width = 3000,height = 1000)
        self.page4 = Frame(master,bg='black',width = 3000,height = 1000)
        self.pageUser = Frame(master,bg='black',width = 3000,height = 1000)
        self.switch(3)
        self.canvas = Canvas(self.page1, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.initOption()
        threading.Thread(target=self.update).start()
    
    def updateS(self,n,i):
        print(i)
        config = {
            "apiKey": "AIzaSyBvSDvuuBcheDg6fZUpi30Il-MUogLKwV4",
            "authDomain": "chill-2ddd1.firebaseapp.com",
            "databaseURL": "https://chill-2ddd1-default-rtdb.firebaseio.com",
            "projectId": "chill-2ddd1",
            "storageBucket": "chill-2ddd1.appspot.com",
            "messagingSenderId": "62414238957",
            "appId": "1:62414238957:web:04d88c13d1ac0510a808e4",
            "measurementId": "G-ZG9Z0XL8MW"
        }       
        listTime=[]
        listHeat=[]
        listEarth=[]
        listHumd=[]
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        while True:
            DuLieu = db.child(n).get()
            for x, y in DuLieu.val().items():
                listTime.insert(0,x)
                listHeat.insert(0,y['Heat'])
                listHumd.insert(0,y['Humd'])
                listEarth.insert(0,y['Earth'])
            data1 = {'Time':listTime,'Heat':listHeat}
            data2 = {'Time':listTime,'Humd':listHumd}
            data3 = {'Time':listTime,'Earth':listEarth}
            df1 = DataFrame(data1,columns=['Time','Heat'])
            figure1 = plt.Figure(figsize=(6,5), dpi=100)
            ax1 = figure1.add_subplot(111)
            ax1.set_ylim(10,80)
            self.listGraphHeat[i] = FigureCanvasTkAgg(figure1, self.canvasP2)
            self.listGraphHeat[i].get_tk_widget().place(x=450,y=10)
            df1 = df1[['Time','Heat']].groupby('Time').sum()
            df1.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
            ax1.set_title('Recorded temperature '+n)
            # bar1.get_tk_widget().place(x=-1000,y=-1000)
            df2 = DataFrame(data2,columns=['Time','Humd'])
            figure2 = plt.Figure(figsize=(6,5), dpi=100)
            ax2 = figure2.add_subplot(111)
            ax2.set_ylim(30,80)
            self.listGraphHumd[i] = FigureCanvasTkAgg(figure2, self.canvasP2)
            self.listGraphHumd[i].get_tk_widget().place(x=450,y=10)
            df2 = df2[['Time','Humd']].groupby('Time').sum()
            df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
            
            ax2.set_title('Recorded air humidity '+n)
            self.listGraphHumd[i].get_tk_widget().place(x=-1000,y=-1000)
            df3 = DataFrame(data3,columns=['Time','Earth'])
            figure3 = plt.Figure(figsize=(6,5), dpi=100)
            ax3 = figure3.add_subplot(111)
            ax3.set_ylim(20,70)
            self.listGraphEarth[i] = FigureCanvasTkAgg(figure3, self.canvasP2)
            self.listGraphEarth[i].get_tk_widget().place(x=450,y=10)
            df3 = df3[['Time','Earth']].groupby('Time').sum()
            df3.plot(kind='line', legend=True, ax=ax3, color='r',marker='o', fontsize=10)
            ax3.set_title('Recorded earth humidity '+n)
            self.listGraphEarth[i].get_tk_widget().place(x=-1000,y=-1000)
            time.sleep(60)
    
    def updateGraph(self):
        config = {
            "apiKey": "AIzaSyBvSDvuuBcheDg6fZUpi30Il-MUogLKwV4",
            "authDomain": "chill-2ddd1.firebaseapp.com",
            "databaseURL": "https://chill-2ddd1-default-rtdb.firebaseio.com",
            "projectId": "chill-2ddd1",
            "storageBucket": "chill-2ddd1.appspot.com",
            "messagingSenderId": "62414238957",
            "appId": "1:62414238957:web:04d88c13d1ac0510a808e4",
            "measurementId": "G-ZG9Z0XL8MW"
        }       
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        Date = ["2022-04-16","2022-04-17"]
        i = 0
        for x in Date:
            threading.Thread(target=self.updateS,args =(x,i, )).start()
            i = i + 1
       
        

    def switch(self,a):
        for frame in (self.page1, self.page2,self.page3,self.page4, self.pageUser):
            frame.pack(fill='both', expand=True)
        if a == 1:
            self.page2.pack_forget()
            self.page3.pack_forget()
            self.page4.pack_forget()
            self.pageUser.pack_forget()
        elif a==2: 
            self.page1.pack_forget()
            self.page3.pack_forget()
            self.page4.pack_forget()
            self.pageUser.pack_forget()
        elif a==3:
            self.page1.pack_forget()
            self.page2.pack_forget()
            self.page4.pack_forget()
            self.pageUser.pack_forget()
        elif a==4:
            self.page1.pack_forget()
            self.page2.pack_forget()
            self.page3.pack_forget()
            self.pageUser.pack_forget()
        else:
            self.page1.pack_forget()
            self.page2.pack_forget()
            self.page3.pack_forget()
            self.page4.pack_forget()
            
    def update(self):
        AIO_USERNAME = "Airforce"
        AIO_KEY = "aio_Qcan99Ot2yY7cMOLDjlyHeNhbm1t"

        def connected (client ) :
            print ("Ket noi thanh cong ...")
            self.client.subscribe("Heat")
            self.client.subscribe("Humd")
            self.client.subscribe("Earth")
            self.client.subscribe("Watering")
        def subscribe ( client , userdata , mid , granted_qos ):
            print (" Subcribe thanh cong ...")
        def disconnected (client ) :
            print (" Ngat ket noi ...")
            sys . exit (1)
        def message (client , feed_id , payload ):
            print (" Nhan du lieu : " + payload )

            if feed_id=="Heat":
                self.canvas2.itemconfig(self.box["temp"], text=str(payload)+"oC")
                self.realtime_temperature =  int(str(payload))
            if feed_id=="Humd":
                self.canvas2.itemconfig(self.box["humid"], text=str(payload)+"%")
                self.realtime_humidity = int(str(payload))
            if feed_id=="Earth":
                self.canvas2.itemconfig(self.box["earth"], text= str(payload)+"%")
                self.realtime_earth = int(str(payload))
            if feed_id=="Watering":
                self.canvas2.itemconfig(self.box["led"], text= "on" if payload == 1 else "off")
        while(self.trI==0):
            pass
        self.client = MQTTClient ( AIO_USERNAME , AIO_KEY )
        self.client . on_connect = connected
        self.client . on_disconnect = disconnected
        self.client . on_message = message
        self.client . on_subscribe = subscribe
        self.client . connect ()
        self.client . loop_background ()
        while True:
            time . sleep (30)
      
    def round_rectangle(self,canvas,x1, y1, x2, y2, radius=25, **kwargs):      
        points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    def createBox(self):
        x = {}
        self.round_rectangle(self.canvas2,100,0, 700, 300,fill="white")
        self.gh = Image.open("image/Greenhouse1.png") 
        self.gh = ImageTk.PhotoImage(self.gh.resize((690-110,170), Image.ANTIALIAS))
        self.canvas2.create_image(110,10, anchor=NW, image=self.gh)    
        self.canvas2.imageG = self.gh 
        self.gh1 = Image.open("image/Drop.jpg")       
        self.gh3 = Image.open("image/Sun.png") 
        self.gh1 = ImageTk.PhotoImage(self.gh1.resize((50,50), Image.ANTIALIAS))
        self.canvas2.create_image(195,200, anchor=NW, image=self.gh1)    
        self.canvas2.imageG2 = self.gh1
        
        self.gh2 = Image.open("image/Temp.jpg") 
        self.gh2 = ImageTk.PhotoImage(self.gh2.resize((50,50), Image.ANTIALIAS))
        self.canvas2.create_image(340,200, anchor=NW, image=self.gh2)    
        self.canvas2.imageG3 = self.gh2
        
        self.gh3 = ImageTk.PhotoImage(self.gh3.resize((50,50), Image.ANTIALIAS))
        self.canvas2.create_image(475,200, anchor=NW, image=self.gh3)    
        self.canvas2.imageG4 = self.gh3
        
        self.gh4 = Image.open("image/Wind.png") 
        self.gh4 = ImageTk.PhotoImage(self.gh4.resize((50,50), Image.ANTIALIAS))
        self.canvas2.create_image(600,200, anchor=NW, image=self.gh4)    
        self.canvas2.imageG4 = self.gh4
        
        x["humid"]=self.canvas2.create_text(195,250, text="59%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        x["temp"]=self.canvas2.create_text(340,250, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        x["earth"]=self.canvas2.create_text(475,250, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        x["led"]=self.canvas2.create_text(600,250, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        
        self.round_rectangle(self.canvas2,110,10, 300, 50,fill="green")
        self.canvas2.create_text(120,15, text="Glasshouse 1", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        return x
    
    def createBox2(self):
        x = {}
        self.round_rectangle(self.canvasPageUser,700,0, 1300, 300,fill="white")
        self.gh = Image.open("image/Greenhouse1.png") 
        self.gh = ImageTk.PhotoImage(self.gh.resize((690-110,170), Image.ANTIALIAS))
        self.canvasPageUser.create_image(710,10, anchor=NW, image=self.gh)    
        self.canvasPageUser.imageG = self.gh 
        self.gh1 = Image.open("image/Drop.jpg")       
        self.gh32 = Image.open("image/Sun.png") 
        self.gh1 = ImageTk.PhotoImage(self.gh1.resize((50,50), Image.ANTIALIAS))
        self.canvasPageUser.create_image(795,200, anchor=NW, image=self.gh1)    
        self.canvasPageUser.imageG2 = self.gh1
        
        self.gh2 = Image.open("image/Temp.jpg") 
        self.gh2 = ImageTk.PhotoImage(self.gh2.resize((50,50), Image.ANTIALIAS))
        self.canvasPageUser.create_image(940,200, anchor=NW, image=self.gh2)    
        self.canvasPageUser.imageG3 = self.gh2
        
        self.gh32 = ImageTk.PhotoImage(self.gh32.resize((50,50), Image.ANTIALIAS))
        self.canvasPageUser.create_image(1075,200, anchor=NW, image=self.gh32)    
        self.canvasPageUser.imageG4 = self.gh32
        
        self.gh4 = Image.open("image/Wind.png") 
        self.gh4 = ImageTk.PhotoImage(self.gh4.resize((50,50), Image.ANTIALIAS))
        self.canvasPageUser.create_image(1200,200, anchor=NW, image=self.gh4)    
        self.canvasPageUser.imageG4 = self.gh4
        
        x["humid"]=self.canvasPageUser.create_text(795,250, text="59%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        x["temp"]=self.canvasPageUser.create_text(940,250, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        x["earth"]=self.canvasPageUser.create_text(1075,250, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        x["led"]=self.canvasPageUser.create_text(1200,250, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        
        self.round_rectangle(self.canvasPageUser,710,10, 900, 50,fill="green")
        self.canvasPageUser.create_text(720,15, text="Glasshouse 1", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        return x
    
    def _on_mousewheel(self, event):
        self.canvas2.yview_scroll(int(-1*(event.delta/120)), "units")

    def initOption(self):
        def key(event):
            print("pressed", repr(event.char))
        def callback(event):
            print("clicked at", event.x, event.y)
            if event.x >= 100 and event.x <= 700 and event.y >=0 and event.y <= 300:
                self.switch(2)
        def switchBack():
            self.switch(1)
        def connect():
            self.switch(1)
            self.username = inputtxt.get(1.0, "end-1c")
            self.pw = inputPW.get(1.0, "end-1c")
            self.trI = 1
            
        def checkInput(input1, input2, input):
            if input <= input2 and input >= input1: return 
            aver_input = (input1 + input2)/2
            if (abs(aver_input - input) > 2):
                self.client.publish("Watering",1) 
            else:
                self.client.publish("Watering",2) 
                
        def checkFormatInput(test):
            pat = re.compile(r"[0-9]+")
  
            # Checks whether the whole string matches the re.pattern or not
            if not re.fullmatch(pat, test):
                return False
            return True
                
        def timeWatering():
            self.canvasP4.delete(self.txtTime1)
            self.canvasP4.delete(self.txtTime2)
            self.txtTime1 = self.canvasP4.create_text(900,550,text="Vui l??ng nh???p gi??? t??? ?????ng t?????i", fill="black", font=('Helvetica 20 bold'),anchor=NW)
            self.txtTime2 = self.canvasP4.create_text(900,600,text="Vui l??ng nh???p gi??? t??? ?????ng t?????i", fill="black", font=('Helvetica 20 bold'),anchor=NW)
            
            self.time1 = inputHour1.get(1.0, "end-1c")
            self.time2 = inputHour2.get(1.0, "end-1c")
            if self.time1:
                pass
            else:
                self.canvasP4.itemconfig(self.txtTime1 ,fill="#8b0000")
            if self.time2:
                pass
            else:
                self.canvasP4.itemconfig(self.txtTime2 ,fill="#8b0000")
            
            if self.time1 and self.time2:
                h1 = self.time1.split(':')[0]
                m1 = self.time1.split(':')[1]
                h2 = self.time2.split(':')[0]
                m2 = self.time2.split(':')[1]
                if checkFormatInput(h1) and checkFormatInput(m1):
                    pass
                else:
                    self.canvasP4.itemconfig(self.txtTime1, text="Vui l??ng nh???p ????ng ?????nh d???ng")
                    self.canvasP4.itemconfig(self.txtTime1 ,fill="#8b0000")
                    
                if checkFormatInput(h2) and checkFormatInput(m2):
                    pass
                else:
                    self.canvasP4.itemconfig(self.txtTime2, text="Vui l??ng nh???p ????ng ?????nh d???ng")
                    self.canvasP4.itemconfig(self.txtTime2 ,fill="#8b0000")
                    
                now = datetime.now()
                if (now.hour == int(h1) and now.minute == int(m1)) or (now.hour == int(h2) and now.minute == int(m2)):
                    print("Tuoi nuoc")
                    self.client.publish("Watering",1) 
                    
        def handleAutoWatering():
            self.canvasP4.delete(self.txtTemp)
            self.canvasP4.delete(self.txtHumd)
            self.canvasP4.delete(self.txtEarth)
            self.txtTemp = self.canvasP4.create_text(900,150,text="Vui l??ng nh???p th??ng tin nhi???t ?????", fill="black", font=('Helvetica 20 bold'),anchor=NW)
            self.txtHumd = self.canvasP4.create_text(900,200, text="Vui l??ng nh???p th??ng tin ????? ???m", fill="black", font=('Helvetica 20 bold'),anchor=NW)
            self.txtEarth = self.canvasP4.create_text(900,250, text="Vui l??ng nh???p th??ng tin ????? ???m c???a ?????t", fill="black", font=('Helvetica 20 bold'),anchor=NW)
            self.temperature = self.inputTemperature.get(1.0, "end-1c")
            self.humidity = self.inputDoamKK.get(1.0, "end-1c")
            self.earth = self.inputDoamdat.get(1.0, "end-1c")
            if len(self.temperature) == 0:
                self.canvasP4.itemconfig(self.txtTemp, text="Vui l??ng nh???p th??ng tin nhi???t ?????")
                self.canvasP4.itemconfig(self.txtTemp ,fill="#8b0000")
                
            if len(self.humidity) == 0:
                self.canvasP4.itemconfig(self.txtHumd, text="Vui l??ng nh???p th??ng tin ????? ???m")
                self.canvasP4.itemconfig(self.txtHumd ,fill="#8b0000")
                
            if len(self.earth) == 0:
                self.canvasP4.itemconfig(self.txtEarth, text="Vui l??ng nh???p th??ng tin ????? ???m c???a ?????t")
                self.canvasP4.itemconfig(self.txtEarth ,fill="#8b0000")
                
            if (len(self.humidity) != 0 and len(self.earth) != 0 and len(self.temperature) != 0):
                temperature = self.temperature.split('-')
                temperature1 = temperature[0]
                temperature2 = temperature[1]
                
                if checkFormatInput(temperature1) and checkFormatInput(temperature2):
                    pass
                else:
                    self.canvasP4.itemconfig(self.txtTemp, text="Vui l??ng nh???p ????ng ?????nh d???ng")
                    self.canvasP4.itemconfig(self.txtTemp ,fill="#8b0000")
                
                humidity = self.humidity.split('-')
                humidity1 = humidity[0]
                humidity2 = humidity[1]
                
                if checkFormatInput(humidity1) and checkFormatInput(humidity2):
                    pass
                else:
                    self.canvasP4.itemconfig(self.txtHumd, text="Vui l??ng nh???p ????ng ?????nh d???ng")
                    self.canvasP4.itemconfig(self.txtHumd ,fill="#8b0000")
                    
                earth = self.earth.split('-')
                earth1 = earth[0]
                earth2 = earth[1]
                
                if checkFormatInput(earth1) and checkFormatInput(earth2):
                    pass
                else:
                    self.canvasP4.itemconfig(self.txtEarth, text="Vui l??ng nh???p ????ng ?????nh d???ng")
                    self.canvasP4.itemconfig(self.txtEarth ,fill="#8b0000")
                
                config = {
                    "apiKey": "AIzaSyBvSDvuuBcheDg6fZUpi30Il-MUogLKwV4",
                    "authDomain": "chill-2ddd1.firebaseapp.com",
                    "databaseURL": "https://chill-2ddd1-default-rtdb.firebaseio.com",
                    "projectId": "chill-2ddd1",
                    "storageBucket": "chill-2ddd1.appspot.com",
                    "messagingSenderId": "62414238957",
                    "appId": "1:62414238957:web:04d88c13d1ac0510a808e4",
                    "measurementId": "G-ZG9Z0XL8MW"
                }       
                firebase = pyrebase.initialize_app(config)

                db = firebase.database()
                DuLieu = db.child("User").get()
                db = firebase.database()
                db.child("User").child("ConditionHeat").set(self.temperature)
                db.child("User").child("ConditionHumd").set(self.humidity)
                db.child("User").child("ConditionEarth").set(self.earth)
                self.client.publish("ConditionHeat",self.temperature)
                self.client.publish("ConditionHumd",self.humidity)
                self.client.publish("ConditionEarth",self.earth)
                
                # checkInput(int(self.temperature1),int(self.temperature2), self.realtime_temperature)
                # checkInput(int(self.humidity1),int(self.humidity2), self.realtime_humidity)
                # checkInput(int(self.earth1),int(self.earth2), self.realtime_earth)
                    
        def switchSetting():
            self.switch(4)
        def switchHome():
            self.switch(1)
        def switchUser():
            self.switch(5)
        def exit():
            self.master.destroy()
        def switchCounter1():
            self.counter=0
            for x in self.listGraphEarth:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHumd:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHeat:
                x.get_tk_widget().place(x=-1000,y=-1000)
            if self.current == 1:
                self.listGraphHeat[self.counter].get_tk_widget().place(x=450,y=10)
            elif self.current == 2:
                self.listGraphHumd[self.counter].get_tk_widget().place(x=450,y=10)
            else:
                self.listGraphEarth[self.counter].get_tk_widget().place(x=450,y=10)
        def switchCounter2():
            self.counter=1
            for x in self.listGraphEarth:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHumd:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHeat:
                x.get_tk_widget().place(x=-1000,y=-1000)
            if self.current == 1:
                self.listGraphHeat[self.counter].get_tk_widget().place(x=450,y=10)
            elif self.current == 2:
                self.listGraphHumd[self.counter].get_tk_widget().place(x=450,y=10)
            else:
                self.listGraphEarth[self.counter].get_tk_widget().place(x=450,y=10)
        def switchGraph1():
            for x in self.listGraphEarth:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHumd:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHeat:
                x.get_tk_widget().place(x=-1000,y=-1000)
            self.listGraphHeat[self.counter].get_tk_widget().place(x=450,y=10)
            self.current=1
        def switchGraph2():
            for x in self.listGraphEarth:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHumd:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHeat:
                x.get_tk_widget().place(x=-1000,y=-1000)
            self.listGraphHumd[self.counter].get_tk_widget().place(x=450,y=10)
            self.current=2
        def switchGraph3():
            for x in self.listGraphEarth:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHumd:
                x.get_tk_widget().place(x=-1000,y=-1000)
            for x in self.listGraphHeat:
                x.get_tk_widget().place(x=-1000,y=-1000)
            self.listGraphEarth[self.counter].get_tk_widget().place(x=450,y=10)
            self.current=3

        # Page 1
        
        self.weather = Image.open("image/Sunny.png") 
        self.weather = ImageTk.PhotoImage(self.weather.resize((240,200), Image.ANTIALIAS))
        self.canvas.create_image(10,7, anchor=NW, image=self.weather)    
        self.canvas.image = self.weather   
        
        self.frame1 = Frame(self.page1,bg="black",width=1800,height=300)
        self.frame1.place(x=0,y=440)
        self.canvas2 = Canvas(self.frame1,bg="black",width=1800,height=300,highlightthickness=0)
        self.scroll = ttk.Scrollbar(self.frame1,orient='horizontal',command=self.canvas2.yview)
        self.scroll.pack(side = RIGHT, fill = Y)
        self.canvas2.configure(yscrollcommand=self.scroll.set)
        self.canvas2.bind('<Configure>',lambda e : self.canvas2.configure(scrollregion=self.canvas2.bbox('all')))
        self.canvas2.bind("<Key>", key)
        self.canvas2.bind("<Button-1>", callback)
        self.canvas2.pack(fill='both', expand=True)
        self.frame2 = Frame(self.frame1,bg="black",width=1800,height=300)
        self.canvas3 = Canvas(self.frame2,bg="black",highlightthickness=0)
        self.canvas2.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas3.pack(fill='both', expand=True)
        
        self.canvas2.create_window((0,0),window=self.frame2,anchor="nw")
        for i in range(0,5):
            Button(self.canvas3,text=i,width = 1,bg='black',highlightthickness = 0,borderwidth = 0).pack()
        self.box = self.createBox()
        
        self.canvas.create_text(150,400, text="GLASSHOUSE:", fill="white", font=('Helvetica 20 bold'))

        self.label2 = self.canvas.create_text(500,70, text="Th??? 3, Ng??y 14 Th??ng 2 N??m 2022", fill="white", font=('Helvetica 20 bold'))
        self.label21 = self.canvas.create_text(390,130, text="SUNNY", fill="white", font=('Helvetica 50 bold'))
    
        self.round_rectangle(self.canvas, 300, 190, 800, 350,fill="white")
        self.label31 = self.canvas.create_text(305,230, text="Humidity", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.label32 = self.canvas.create_text(440,230, text="Temperature", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.label33 = self.canvas.create_text(620,230, text="Precipitation", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.humidity = self.canvas.create_text(325,300, text="50%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.temp = self.canvas.create_text(500,300, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.prep = self.canvas.create_text(670,300, text="0.5 cm", fill="black", font=('Helvetica 20 bold'),anchor=NW)

        # Page 2
        # data1 = {'Time': ['8:15','8:20','8:25','8:30','8:35','8:40','8:45','8:50','8:55','8:60','9:05','9:10','9:15','9:20','9:25'],
        #  'Heat': [45000,42000,52000,49000,47000,45000,42000,52000,49000,47000,45000,42000,52000,49000,47000]
        # }
        self.canvasP2= Canvas(self.page2, bg='black', highlightthickness=0)
        self.canvasP2.pack(fill='both', expand=True) 
        threading.Thread(target=self.updateGraph).start()


        self.round_rectangle(self.canvasP2,140,100, 340, 300,fill="white")
        self.round_rectangle(self.canvasP2,140,400, 340, 600,fill="white")
        self.round_rectangle(self.canvasP2,1140,100, 1340, 300,fill="white")
        self.round_rectangle(self.canvasP2,1140,400, 1340, 600,fill="white")
        
        self.canvasP2.create_text(168,200, text="Humidity", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(168,500, text="Temperature", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(1168,200, text="Lightning", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(1168,500, text="CO2", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasP2.create_text(168,250, text="50%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(168,550, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(1168,250, text="on", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(1168,550, text="on", fill="black", font=('Helvetica 20 bold'),anchor=NW)
  
        self.canvasP2.create_image(168,120, anchor=NW, image=self.gh1)    
        self.canvasP2.imageG2 = self.gh1

        self.canvasP2.create_image(168,420, anchor=NW, image=self.gh2)    
        self.canvasP2.imageG3 = self.gh2

        self.canvasP2.create_image(1168,120, anchor=NW, image=self.gh3)    
        self.canvasP2.imageG4 = self.gh3

        self.canvasP2.create_image(1168,420, anchor=NW, image=self.gh4)    
        self.canvasP2.imageG4 = self.gh4
        
        self.nextDay = Button(self.page2, width=10, height = 5,text = "Next",command=switchCounter2)
        self.nextDay.place(x=1025, y=600)
        
        self.prevDay = Button(self.page2, width=10, height = 5,text = "Prev",command=switchCounter1)
        self.prevDay.place(x=400, y=600)
        
        
        # Login
        
        # Layout Setting
        self.canvasP4= Canvas(self.page4, bg='black', highlightthickness=0)
        self.canvasP4.pack(fill='both', expand=True) 
        self.txtTemp = self.canvasP4.create_text(900,150,text="Vui l??ng nh???p th??ng tin nhi???t ?????", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.txtHumd = self.canvasP4.create_text(900,200, text="Vui l??ng nh???p th??ng tin ????? ???m", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.txtEarth = self.canvasP4.create_text(900,250, text="Vui l??ng nh???p th??ng tin ????? ???m c???a ?????t", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.txtTime1 = self.canvasP4.create_text(900,550,text="Vui l??ng nh???p gi??? t??? ?????ng t?????i", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.txtTime2 = self.canvasP4.create_text(900,600,text="Vui l??ng nh???p gi??? t??? ?????ng t?????i", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(300,50, text="Thi???t l???p ch??? ????? t??? ?????ng t?????i n?????c (Vui l??ng nh???p theo d???ng aa-bb)", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasP4.create_text(150,150, text="Nhi???t ?????: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasP4.create_text(150,200, text="????? ???m kh??ng kh??: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasP4.create_text(150,250, text="????? ???m c???a ?????t: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.inputTemperature = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        self.inputTemperature.place(x=550,y=150)
        
        self.inputDoamKK = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        self.inputDoamKK.place(x=550,y=200)
        
        self.inputDoamdat = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        self.inputDoamdat.place(x=550,y=250)
        
        self.save = Button(self.page4, width=5, height = 2,text="L??u",font=('Helvetica 20 bold'), command=handleAutoWatering)
        self.save.place(x=650, y=300)
        
        self.canvasP4.create_text(300,500, text="C??i ?????t gi??? t??? ?????ng t?????i n?????c (Vui l??ng nh???p theo d???ng hh:mm)", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(150,550, text="Gi??? t?????i l???n th??? 1:", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(150,600, text="Gi??? t?????i l???n th??? 2:", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        inputHour1 = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputHour1.place(x=550,y=550)
        
        inputHour2 = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputHour2.place(x=550,y=600)
        
        self.save1 = Button(self.page4, width=5, height = 2,text="L??u",font=('Helvetica 20 bold'), command=timeWatering)
        self.save1.place(x=650, y=650)
        
        # Layout User
        self.canvasPageUser= Canvas(self.pageUser, bg='black', highlightthickness=0)
        self.canvasPageUser.pack(fill='both', expand=True) 
        self.canvasPageUser.create_text(400,50, text="C??i ?????t", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasPageUser.create_text(70,150, text="H??? v?? t??n: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasPageUser.create_text(70,200, text="Dob: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasPageUser.create_text(70,250, text="Gi???i t??nh: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasPageUser.create_text(70,300, text="?????a ch???: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasPageUser.create_text(70,350, text="S??? ??i???n tho???i:", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasPageUser.create_text(70,400, text="Gmail:", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasPageUser.create_text(70,450, text="Username:", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasPageUser.create_text(70,500, text="Password:", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        inputFullName = Text(self.pageUser,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputFullName.place(x=350,y=150)
        
        inputDob = Text(self.pageUser,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputDob.place(x=350,y=200)
        
        inputSex = Text(self.pageUser,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputSex.place(x=350,y=250)
        
        inputAddress = Text(self.pageUser,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputAddress.place(x=350,y=300)
        
        inputPhone = Text(self.pageUser,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputPhone.place(x=350,y=350)
        
        inputGmail = Text(self.pageUser,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputGmail.place(x=350,y=400)
        
        inputusername = Text(self.pageUser,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputusername.place(x=350,y=450)
        
        inputPassword = Text(self.pageUser,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputPassword.place(x=350,y=500)
        
        self.save1 = Button(self.pageUser, width=5, height = 2,text="L??u",font=('Helvetica 20 bold'))
        self.save1.place(x=450, y=600)
        
        # self.canvasPageUser.create_text(1000,300, text="GLASSHOUSE:", fill="white", font=('Helvetica 20 bold'))
        
        self.box = self.createBox2()
        # Layout Login
        self.canvasP3= Canvas(self.page3, bg='black', highlightthickness=0)
        self.canvasP3.pack(fill='both', expand=True) 
        self.canvasP3.create_text(450,400, text="Username", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP3.create_text(450,500, text="Password", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.login = Image.open("image/276156773_395766165713386_5796930991960104386_n.png") 
        self.login = ImageTk.PhotoImage(self.login.resize((250,100), Image.ANTIALIAS)) 
        self.master.imageL = self.login 
        
        self.logo = Image.open("image/277903344_390134799629988_4975759241260497395_n.png") 
        self.logo = ImageTk.PhotoImage(self.logo.resize((450,300), Image.ANTIALIAS)) 
        self.canvasP3.create_image(500,50, anchor=NW, image=self.logo) 
        self.master.logo = self.logo 
        
        inputtxt = Text(self.page3,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputtxt.place(x=600,y=400)
        inputPW = Text(self.page3,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputPW.place(x=600,y=500)
        self.login = Button(self.page3, width=250, height = 100,image =self.login,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",text="LOGIN",command=connect,borderwidth=0)
        self.login.place(x=600, y=600)
        # Bottom bar
        self.den = Image.open("image/Den.png") 
        self.den = ImageTk.PhotoImage(self.den.resize((800,200), Image.ANTIALIAS))
        self.master.den = self.den
        
        self.Button1 = Image.open("image/Home.png") 
        self.Button1 = ImageTk.PhotoImage(self.Button1.resize((80,100), Image.ANTIALIAS)) 
        self.master.image = self.Button1 
        
        self.Button2 = Image.open("image/Setting.png") 
        self.Button2 = ImageTk.PhotoImage(self.Button2.resize((80,100), Image.ANTIALIAS)) 
        self.master.image1 = self.Button2    
        
        self.Button3 = Image.open("image/User.png") 
        self.Button3 = ImageTk.PhotoImage(self.Button3.resize((80,100), Image.ANTIALIAS)) 
        self.master.image2 = self.Button3    
        
        self.buttq = Image.open("image/275769692_2055769447935399_2377188200629673018_n.jpg") 
        self.buttq = ImageTk.PhotoImage(self.buttq.resize((80,100), Image.ANTIALIAS)) 
        self.master.image2 = self.buttq    


        self.canvasP2.create_image(350,750, anchor=NW, image=self.den)   
        self.canvas.create_image(350,750, anchor=NW, image=self.den)    
        self.canvasP4.create_image(350,750, anchor=NW, image=self.den)     
        self.canvasPageUser.create_image(350,750, anchor=NW, image=self.den)     

        self.home = Button(self.page2, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchHome)
        self.home.place(x=500, y=770)

        self.option = Button(self.page2, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchSetting)
        self.option.place(x=700, y=770)
        
        self.user = Button(self.page2, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",borderwidth=0, command=switchUser)
        self.user.place(x=900, y=770)
        
        self.imgTemp = Image.open("image/Temp.jpg") 
        self.imgTemp = ImageTk.PhotoImage(self.imgTemp.resize((100,100), Image.ANTIALIAS)) 
        self.master.imgTemp = self.imgTemp 
        
        self.canvasP2.create_text(500,700, text="Nhi???t ?????", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.option = Button(self.page2, width=100, height = 100,image =self.imgTemp,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchGraph1,borderwidth=0)
        self.option.place(x=500, y=600)
        
        self.imgHumd = Image.open("image/Drop.jpg") 
        self.imgHumd = ImageTk.PhotoImage(self.imgHumd.resize((100,100), Image.ANTIALIAS)) 
        self.master.imgHumd = self.imgHumd 
        
        self.canvasP2.create_text(640,700, text="????? ???m kh??ng kh??", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.user = Button(self.page2, width=100, height = 100,image =self.imgHumd,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchGraph2,borderwidth=0)
        self.user.place(x=700, y=600)
        
        self.canvasP2.create_text(880,700, text="????? ???m c???a ?????t", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        self.imgEarth = Image.open("image/Wind.png") 
        self.imgEarth = ImageTk.PhotoImage(self.imgEarth.resize((100,100), Image.ANTIALIAS)) 
        self.master.imgEarth = self.imgEarth 
        
        self.user = Button(self.page2, width=100, height = 100,image =self.imgEarth,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchGraph3,borderwidth=0)
        self.user.place(x=900, y=600)
        
        
        
        self.home = Button(self.page1, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchHome,borderwidth=0)
        self.home.place(x=500, y=770)

        self.option = Button(self.page1, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchSetting,borderwidth=0)
        self.option.place(x=700, y=770)
        
        self.user = Button(self.page1, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",borderwidth=0, command=switchUser)
        self.user.place(x=900, y=770)
        
        self.home = Button(self.pageUser, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchHome,borderwidth=0)
        self.home.place(x=500, y=770)

        self.option = Button(self.pageUser, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchSetting,borderwidth=0)
        self.option.place(x=700, y=770)
        
        self.user = Button(self.pageUser, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",borderwidth=0, command=switchUser)
        self.user.place(x=900, y=770)
        
        self.home = Button(self.page4, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchHome,borderwidth=0)
        self.home.place(x=500, y=770)

        self.option = Button(self.page4, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchSetting,borderwidth=0)
        self.option.place(x=700, y=770)
        
        self.user = Button(self.page4, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",borderwidth=0, command=switchUser)
        self.user.place(x=900, y=770)
        
        self.quit = Button(self.master, width=100, height = 100,image =self.buttq,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=exit,borderwidth=0)
        self.quit.place(x=1400, y=50)


