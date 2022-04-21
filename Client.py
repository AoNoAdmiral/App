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

class Client:

    def __init__(self,master):
        self.myFont = font.Font(family='Courier', weight='bold')
        self.master = master
        self.counter = 0
        self.trI = 0
        self.listTime=[]
        self.listHeat=[]
        self.listEarth=[]
        self.listHumd=[]
        self.master.geometry('2000x1000')
        self.master.attributes('-fullscreen', True)
        self.page1 = Frame(master,bg='black',width = 3000,height = 1000)
        self.page2 = Frame(master,bg='black',width = 3000,height = 1000)
        self.page3 = Frame(master,bg='black',width = 3000,height = 1000)
        self.page4 = Frame(master,bg='black',width = 3000,height = 1000)
        self.switch(3)
        self.canvas = Canvas(self.page1, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.initOption()
        threading.Thread(target=self.update).start()
    
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
        DuLieu = db.child("Minute").get()
        for x, y in DuLieu.val().items():
            self.listTime.insert(0,x)
            self.listHeat.insert(0,y['Heat'])
            self.listHumd.insert(0,y['Humd'])
            self.listEarth.insert(0,y['Earth'])
        data1 = {'Time':self.listTime,'Heat':self.listHeat}
        data2 = {'Time':self.listTime,'Humd':self.listHeat}
        data3 = {'Time':self.listTime,'Earth':self.listHeat}
        
        # TEST
        # data1 = {'Time': ['8:15','8:20','8:25','8:30','8:35','8:40','8:45','8:50','8:55','8:60','9:05','9:10','9:15','9:20','9:25'],
        #  'Heat': [31,33,31,32,31,33,35,35,32,31,36,33,34,31,32]
        # }
        # data2 = {'Time': ['8:15','8:20','8:25','8:30','8:35','8:40','8:45','8:50','8:55','8:60','9:05','9:10','9:15','9:20','9:25'],
        #  'Humd': [80,85,83,81,84,89,86,87,81,80,82,82,85,80,83]
        # }
        # data3 = {'Time': ['8:15','8:20','8:25','8:30','8:35','8:40','8:45','8:50','8:55','8:60','9:05','9:10','9:15','9:20','9:25'],
        #  'Earth': [54,53,52,51,50,52,54,53,56,53,54,54,51,51,54]
        # }
        df1 = DataFrame(data1,columns=['Time','Heat'])
        figure1 = plt.Figure(figsize=(6,5), dpi=100)
        ax1 = figure1.add_subplot(111)
        self.bar1 = FigureCanvasTkAgg(figure1, self.canvasP2)
        self.bar1.get_tk_widget().place(x=450,y=10)
        df1 = df1[['Time','Heat']].groupby('Time').sum()
        df1.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
        ax1.set_title('Recorded temperature')
        # bar1.get_tk_widget().place(x=-1000,y=-1000)
        df2 = DataFrame(data2,columns=['Time','Humd'])
        figure2 = plt.Figure(figsize=(6,5), dpi=100)
        ax2 = figure2.add_subplot(111)
        self.bar2 = FigureCanvasTkAgg(figure2, self.canvasP2)
        self.bar2.get_tk_widget().place(x=450,y=10)
        df2 = df2[['Time','Humd']].groupby('Time').sum()
        df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
        ax2.set_title('Recorded air humidity')
        self.bar2.get_tk_widget().place(x=-1000,y=-1000)
        df3 = DataFrame(data3,columns=['Time','Earth'])
        figure3 = plt.Figure(figsize=(6,5), dpi=100)
        ax3 = figure3.add_subplot(111)
        self.bar3 = FigureCanvasTkAgg(figure3, self.canvasP2)
        self.bar3.get_tk_widget().place(x=450,y=10)
        df3 = df3[['Time','Earth']].groupby('Time').sum()
        df3.plot(kind='line', legend=True, ax=ax3, color='r',marker='o', fontsize=10)
        ax3.set_title('Recorded earth humidity')
        self.bar3.get_tk_widget().place(x=-1000,y=-1000)
        

    def switch(self,a):
        for frame in (self.page1, self.page2,self.page3,self.page4):
            frame.pack(fill='both', expand=True)
        if a == 1:
            self.page2.pack_forget()
            self.page3.pack_forget()
            self.page4.pack_forget()
        elif a==2: 
            self.page1.pack_forget()
            self.page3.pack_forget()
            self.page4.pack_forget()
        elif a==3:
            self.page1.pack_forget()
            self.page2.pack_forget()
            self.page4.pack_forget()
        else:
            self.page1.pack_forget()
            self.page2.pack_forget()
            self.page3.pack_forget()
            
    def update(self):
        AIO_USERNAME = "Airforce"
        AIO_KEY = "aio_Qcan99Ot2yY7cMOLDjlyHeNhbm1t"

        def connected ( client ) :
            print ("Ket noi thanh cong ...")
            client.subscribe("Heat")
            client.subscribe("Humd")
            client.subscribe("Earth")
            client.subscribe("Watering")
        def subscribe ( client , userdata , mid , granted_qos ):
            print (" Subcribe thanh cong ...")
        def disconnected ( client ) :
            print (" Ngat ket noi ...")
            sys . exit (1)
        def message ( client , feed_id , payload ):
            print (" Nhan du lieu : " + payload )
            if feed_id=="Heat":
                self.canvas2.itemconfig(self.box["temp"], text=str(payload)+"oC")
            if feed_id=="Humd":
                self.canvas2.itemconfig(self.box["humid"], text=str(payload)+"%")
            if feed_id=="Earth":
                self.canvas2.itemconfig(self.box["earth"], text= str(payload)+"%")
            if feed_id=="Watering":
                self.canvas2.itemconfig(self.box["led"], text= "on" if payload == 1 else "off")
        while(self.trI==0):
            pass
        client = MQTTClient ( AIO_USERNAME , AIO_KEY )
        client . on_connect = connected
        client . on_disconnect = disconnected
        client . on_message = message
        client . on_subscribe = subscribe
        client . connect ()
        client . loop_background ()
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
        self.counter =self.counter+1
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
        def handleInputString(input, length):
            o1 = ''
            o2 = ''
            for i in range(length):
                if input[i] != '-':
                    o1 += input[i]
                if input[i] == '-':
                    i = i+1
                    while(i < len(input)):
                        o2 += input[i]
                        i = i + 1
                    break
            return (o1, o2)
        
        def handleInputTime(input, length):
            o1 = ''
            o2 = ''
            for i in range(length):
                if input[i] != ':':
                    o1 += input[i]
                if input[i] == ':':
                    i = i+1
                    while(i < len(input)):
                        o2 += input[i]
                        i = i + 1
                    break
            return (o1, o2)
        
        def checkInput(input1, input2, input):
            if input <= input2 and input >= input1: return 
            aver_input = (input1 + input2)/2
            if (abs(aver_input - input) > 2):
                print("Tuoi nuoc trong vong 5ph")
            elif (abs(aver_input - input) > 5):
                print("Tuoi nuoc trong vong 10ph")
            else:
                print("Canh bao den nguoi dung!!!")
            
        def handleAutoWatering():
            self.temperature = inputTemperature.get(1.0, "end-1c")
            self.humidity = inputDoamKK.get(1.0, "end-1c")
            self.earth = inputDoamdat.get(1.0, "end-1c")
            self.LED = inputAnhsang.get(1.0, "end-1c")
            (self.temperature1,self.temperature2) = handleInputString(self.temperature, len(self.temperature))
            
            (self.humidity1, self.humidity2) = handleInputString(self.humidity, len(self.humidity))
            
            (self.earth1,self.earth2) = handleInputString(self.earth, len(self.earth))
            
            (self.LED1, self.LED2) = handleInputString(self.LED, len(self.LED))
            realtime_temperature =  15 # json.loads(value["temperature"])["value"]
            realtime_humidity = 15 # json.loads(value["humidity"])["value"]
            realtime_earth = 15 # json.loads(value["earth"])["value"]
            realtime_LED = 15 # json.loads(value["LED"])["value"]
            checkInput(int(self.temperature1),int(self.temperature2), realtime_temperature)
            checkInput(int(self.humidity1),int(self.humidity2), realtime_humidity)
            checkInput(int(self.earth1),int(self.earth2), realtime_earth)
            checkInput(int(self.LED1),int(self.LED2), realtime_LED)
            
        def timeWatering():
            self.time1 = inputHour1.get(1.0, "end-1c")
            self.time2 = inputHour2.get(1.0, "end-1c")
            (h1, m1) = handleInputTime(self.time1, len(self.time1))
            (h2, m2) = handleInputTime(self.time2, len(self.time2))
            hour_realtime = 6
            minus_realtime = 0
            if (hour_realtime == int(h1) and minus_realtime == int(m1)) or (hour_realtime == int(h2) and minus_realtime == int(m2)):
                print("Tuoi nuoc")
        def switchSetting():
            self.switch(4)
        def switchHome():
            self.switch(1)
        def exit():
            self.master.destroy()
        def switchGraph1():
            self.bar3.get_tk_widget().place(x=-1000,y=-1000)
            self.bar2.get_tk_widget().place(x=-1000,y=-1000)
            self.bar1.get_tk_widget().place(x=400,y=10)
        def switchGraph2():
            self.bar3.get_tk_widget().place(x=-1000,y=-1000)
            self.bar1.get_tk_widget().place(x=-1000,y=-1000)
            self.bar2.get_tk_widget().place(x=400,y=10)
        def switchGraph3():
            self.bar2.get_tk_widget().place(x=-1000,y=-1000)
            self.bar1.get_tk_widget().place(x=-1000,y=-1000)
            self.bar3.get_tk_widget().place(x=400,y=10)

        # Page 1
        
        self.weather = Image.open("image/Sunny.png") 
        self.weather = ImageTk.PhotoImage(self.weather.resize((240,200), Image.ANTIALIAS))
        self.canvas.create_image(10,7, anchor=NW, image=self.weather)    
        self.canvas.image = self.weather   
        
        self.frame1 = Frame(self.page1,bg="#2B2B2B",width=1800,height=300)
        self.frame1.place(x=0,y=440)
        self.canvas2 = Canvas(self.frame1,bg="#2B2B2B",width=1800,height=300,highlightthickness=0)
        self.scroll = ttk.Scrollbar(self.frame1,orient='horizontal',command=self.canvas2.yview)
        self.scroll.pack(side = RIGHT, fill = Y)
        self.canvas2.configure(yscrollcommand=self.scroll.set)
        self.canvas2.bind('<Configure>',lambda e : self.canvas2.configure(scrollregion=self.canvas2.bbox('all')))
        self.canvas2.bind("<Key>", key)
        self.canvas2.bind("<Button-1>", callback)
        self.canvas2.pack(fill='both', expand=True)
        self.frame2 = Frame(self.frame1,bg="#2B2B2B",width=1800,height=300)
        self.canvas3 = Canvas(self.frame2,bg="#2B2B2B",highlightthickness=0)
        self.canvas2.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas3.pack(fill='both', expand=True)
        
        self.canvas2.create_window((0,0),window=self.frame2,anchor="nw")
        for i in range(0,5):
            Button(self.canvas3,text=i,width = 1,bg='black',highlightthickness = 0,borderwidth = 0).pack()
        self.box = self.createBox()
        
        self.canvas.create_text(150,400, text="GLASSHOUSE:", fill="white", font=('Helvetica 20 bold'))

        self.label2 = self.canvas.create_text(500,70, text="Thứ 3, Ngày 14 Tháng 2 Năm 2022", fill="white", font=('Helvetica 20 bold'))
        self.label21 = self.canvas.create_text(390,130, text="SUNNY", fill="white", font=('Helvetica 50 bold'))
    
        self.round_rectangle(self.canvas,200, 190, 800, 350,fill="white")
        self.label31 = self.canvas.create_text(225,230, text="Humidity", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.label32 = self.canvas.create_text(410,230, text="Temperature", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.label33 = self.canvas.create_text(605,230, text="Precipitation", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.humidity = self.canvas.create_text(245,300, text="50%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.temp = self.canvas.create_text(440,300, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.prep = self.canvas.create_text(625,300, text="0.5 cm", fill="black", font=('Helvetica 20 bold'),anchor=NW)

        # Page 2
        # data1 = {'Time': ['8:15','8:20','8:25','8:30','8:35','8:40','8:45','8:50','8:55','8:60','9:05','9:10','9:15','9:20','9:25'],
        #  'Heat': [45000,42000,52000,49000,47000,45000,42000,52000,49000,47000,45000,42000,52000,49000,47000]
        # }
        self.canvasP2= Canvas(self.page2, bg='black', highlightthickness=0)
        self.canvasP2.pack(fill='both', expand=True) 
        threading.Thread(target=self.updateGraph).start()
        # df1 = DataFrame(data1,columns=['Time','Heat'])
        # figure1 = plt.Figure(figsize=(6,5), dpi=100)
        # ax1 = figure1.add_subplot(111)
        # bar1 = FigureCanvasTkAgg(figure1, self.canvasP2)
        # bar1.get_tk_widget().place(x=400,y=10)
        # df1 = df1[['Time','Heat']].groupby('Time').sum()
        # df1.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=10)
        # ax1.set_title('Country Vs. GDP Per Capita')
        # bar1.get_tk_widget().place(x=-1000,y=-1000)

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
        
        # Login
        
        # Layout Setting
        self.canvasP4= Canvas(self.page4, bg='black', highlightthickness=0)
        self.canvasP4.pack(fill='both', expand=True) 
        self.canvasP4.create_text(50,50, text="Thiết lập chế độ tự động tưới nước", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(50,100, text="Vui lòng điền vào nhiệt độ (Vd: 25-27): ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(50,150, text="Vui lòng điền vào độ ẩm không khí (): ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(50,200, text="Vui lòng điền vào độ ẩm của đất mong muốn: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(50,250, text="Vui lòng điền vào ánh sáng mong muốn: ", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        inputTemperature = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputTemperature.place(x=800,y=100)
        
        inputDoamKK = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputDoamKK.place(x=800,y=150)
        
        inputDoamdat = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputDoamdat.place(x=800,y=200)
        
        inputAnhsang = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputAnhsang.place(x=800,y=250)
        
        self.save = Button(self.page4, width=5, height = 2,text="Lưu",font=('Helvetica 20 bold'), command=handleAutoWatering)
        self.save.place(x=650, y=350)
        
        self.canvasP4.create_text(50,500, text="Cài đặt giờ tự động tưới nước (Vui lòng nhập theo dạng hh:mm)", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(50,550, text="Giờ tưới lần thứ 1:", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP4.create_text(50,600, text="Giờ tưới lần thứ 2:", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        inputHour1 = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputHour1.place(x=800,y=550)
        
        inputHour2 = Text(self.page4,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputHour2.place(x=800,y=600)
        
        self.save1 = Button(self.page4, width=5, height = 2,text="Lưu",font=('Helvetica 20 bold'), command=timeWatering)
        self.save1.place(x=650, y=650)
        
        self.Button1 = Image.open("image/Home.png") 
        self.Button1 = ImageTk.PhotoImage(self.Button1.resize((80,100), Image.ANTIALIAS)) 
        self.master.image = self.Button1 
        
        self.home1 = Button(self.page4, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchHome)
        self.home1.place(x=300, y=700)
        
        
        self.canvasP3= Canvas(self.page3, bg='black', highlightthickness=0)
        self.canvasP3.pack(fill='both', expand=True) 
        self.canvasP3.create_text(450,400, text="Username", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP3.create_text(450,500, text="Password", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.login = Image.open("image/276156773_395766165713386_5796930991960104386_n.png") 
        self.login = ImageTk.PhotoImage(self.login.resize((250,100), Image.ANTIALIAS)) 
        self.master.imageL = self.login 
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

        self.home = Button(self.page2, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchHome,borderwidth=0)
        self.home.place(x=500, y=770)

        self.option = Button(self.page2, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchSetting,borderwidth=0)
        self.option.place(x=700, y=770)
        
        self.user = Button(self.page2, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",borderwidth=0)
        self.user.place(x=900, y=770)
        
        self.option = Button(self.page2, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchGraph1,borderwidth=0)
        self.option.place(x=500, y=600)
        
        self.user = Button(self.page2, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchGraph2,borderwidth=0)
        self.user.place(x=700, y=600)
        
        self.user = Button(self.page2, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchGraph3,borderwidth=0)
        self.user.place(x=900, y=600)
        
        
        
        self.home = Button(self.page1, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchHome,borderwidth=0)
        self.home.place(x=500, y=770)

        self.option = Button(self.page1, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchSetting,borderwidth=0)
        self.option.place(x=700, y=770)
        
        self.user = Button(self.page1, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",borderwidth=0)
        self.user.place(x=900, y=770)
        
        self.home = Button(self.page4, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchHome,borderwidth=0)
        self.home.place(x=500, y=770)

        self.option = Button(self.page4, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=switchSetting,borderwidth=0)
        self.option.place(x=700, y=770)
        
        self.user = Button(self.page4, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",borderwidth=0)
        self.user.place(x=900, y=770)
        
        self.quit = Button(self.master, width=100, height = 100,image =self.buttq,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",command=exit,borderwidth=0)
        self.quit.place(x=1400, y=50)


