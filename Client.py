from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import tkinter.font as font
from turtle import color
from PIL import Image, ImageTk
from tkinter import PhotoImage
import threading
import paho.mqtt.client as mqtt
import time
import json
import geocoder

class Client:

    def __init__(self,master):
        self.myFont = font.Font(family='Courier', weight='bold')
        self.master = master
        self.counter = 0
        self.trI = 0
        self.master.protocol("WM_DELETE_WINDOW", self.handler)
        self.master.attributes('-fullscreen', True)
        self.page1 = Frame(master,bg='#2B2B2B',width = 3000,height = 1000)
        self.page2 = Frame(master,bg='#2B2B2B',width = 3000,height = 1000)
        self.page3 = Frame(master,bg='#2B2B2B',width = 3000,height = 1000)
        self.switch(3)
        self.canvas = Canvas(self.page1, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.initOption()
        threading.Thread(target=self.update).start()
        
    def switch(self,a):
        for frame in (self.page1, self.page2,self.page3):
            frame.pack(fill='both', expand=True)
        if a == 1:
            self.page2.pack_forget()
            self.page3.pack_forget()
        elif a==2: 
            self.page1.pack_forget()
            self.page3.pack_forget()
        else:
            self.page1.pack_forget()
            self.page2.pack_forget()
            
    def update(self):
        THINGSBOARD_HOST = "demo.thingsboard.io"
        ACCESS_TOKEN = 'LyoSMl8n9Yoki1fBpJoj'   
        request = {"method": "gettelemetry", "params": {}}

# MQTT on_connect callback function
        def on_connect(client, userdata, flags, rc):
            print("rc code:", rc)
            self.switch(1)
            client.subscribe('v1/devices/me/rpc/response/+')
            
        def check(a):
            if a == 1:
                return "on"
            return "off" 

# MQTT on_message caallback function
        def on_message(client, userdata, msg):
            value = json.loads(msg.payload.decode("utf-8"))
            print(value)
            self.canvas2.itemconfig(self.box["temp"], text=str(json.loads(value["temperature"])["value"])+"oC")
            self.canvas2.itemconfig(self.box["humid"], text=str(json.loads(value["humidity"])["value"])+"%")
            self.canvas2.itemconfig(self.box["pump"], text= check(json.loads(value["PUMP"])["value"]))
            self.canvas2.itemconfig(self.box["led"], text=  check(json.loads(value["LED"])["value"]))
            print(json.loads(value["temperature"])["value"])
        while(self.trI==0):
            pass
        client = mqtt.Client()

        client.loop_start()
        client.on_connect = on_connect
        client.on_message = on_message

        client.username_pw_set(ACCESS_TOKEN)
        client.connect(THINGSBOARD_HOST, 1883,60)
        while True:
            client.publish('v1/devices/me/rpc/request/1',json.dumps(request), 1)
            time.sleep(5)
            

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
        
        self.gh1 = Image.open("image/Sun.png") 
        self.gh1 = ImageTk.PhotoImage(self.gh1.resize((50,50), Image.ANTIALIAS))
        self.canvas2.create_image(195,200, anchor=NW, image=self.gh1)    
        self.canvas2.imageG2 = self.gh1
        
        self.gh2 = Image.open("image/Temp.jpg") 
        self.gh2 = ImageTk.PhotoImage(self.gh2.resize((50,50), Image.ANTIALIAS))
        self.canvas2.create_image(340,200, anchor=NW, image=self.gh2)    
        self.canvas2.imageG3 = self.gh2
        
        self.gh3 = Image.open("image/Drop.jpg") 
        self.gh3 = ImageTk.PhotoImage(self.gh3.resize((50,50), Image.ANTIALIAS))
        self.canvas2.create_image(475,200, anchor=NW, image=self.gh3)    
        self.canvas2.imageG4 = self.gh3
        
        self.gh4 = Image.open("image/Wind.png") 
        self.gh4 = ImageTk.PhotoImage(self.gh4.resize((50,50), Image.ANTIALIAS))
        self.canvas2.create_image(600,200, anchor=NW, image=self.gh4)    
        self.canvas2.imageG4 = self.gh4
        
        x["humid"]=self.canvas2.create_text(195,250, text="59%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        x["temp"]=self.canvas2.create_text(340,250, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        x["pump"]=self.canvas2.create_text(475,250, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
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
            self.username = inputtxt.get(1.0, "end-1c")
            self.pw = inputPW.get(1.0, "end-1c")
            self.trI = 1
            print(self.username)
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
            Button(self.canvas3,text=i,width = 1,bg='#2B2B2B',highlightthickness = 0,borderwidth = 0).pack()
        self.box = self.createBox()
        
        self.canvas.create_text(150,400, text="GLASSHOUSE:", fill="white", font=('Helvetica 20 bold'))

        self.label2 = self.canvas.create_text(500,70, text="Thứ 3, Ngày 14 Tháng 2 Năm 2022", fill="white", font=('Helvetica 20 bold'))
        self.label21 = self.canvas.create_text(390,130, text="SUNNY", fill="white", font=('Helvetica 50 bold'))
    
        self.round_rectangle(self.canvas,200, 190, 800, 350,fill="white")
        self.label31 = self.canvas.create_text(225,230, text="Humidity", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.label32 = self.canvas.create_text(425,230, text="SUNNY", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.label33 = self.canvas.create_text(605,230, text="Precipitation", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.humidity = self.canvas.create_text(245,300, text="54%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.temp = self.canvas.create_text(440,300, text="11oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.prep = self.canvas.create_text(625,300, text="0.5 cm", fill="black", font=('Helvetica 20 bold'),anchor=NW)

        # Page 2
        self.canvasP2= Canvas(self.page2, bg='black', highlightthickness=0)
        self.canvasP2.pack(fill='both', expand=True) 
        self.img = Image.open("image/Greenhouse1.png") 
        self.img = ImageTk.PhotoImage(self.img.resize((1200,450), Image.ANTIALIAS))
        self.canvasP2.create_image(180,10, anchor=NW, image=self.img)    
        self.canvasP2.image = self.img   
        self.round_rectangle(self.canvasP2,240,500, 440, 700,fill="white")
        self.round_rectangle(self.canvasP2,540,500, 740, 700,fill="white")
        self.round_rectangle(self.canvasP2,840,500, 1040, 700,fill="white")
        self.round_rectangle(self.canvasP2,1140,500, 1340, 700,fill="white")
        self.back = Image.open("image/Back.png") 
        self.back = ImageTk.PhotoImage(self.back.resize((100,100), Image.ANTIALIAS)) 
        self.master.bbk = self.back 
        
        Button(self.canvasP2,width = 100, height = 100,command = switchBack,image = self.back).place(x=25,y=25)
        
        self.canvasP2.create_text(268,600, text="Lightning", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(568,600, text="Temperature", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(868,600, text="Humidity", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(1168,600, text="CO2", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        
        self.canvasP2.create_text(268,650, text="59%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(568,650, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(868,650, text="60%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP2.create_text(1168,650, text="", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        
        # Login
        self.canvasP3= Canvas(self.page3, bg='black', highlightthickness=0)
        self.canvasP3.pack(fill='both', expand=True) 
        self.canvasP3.create_text(450,400, text="Username", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.canvasP3.create_text(450,500, text="Password", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        self.login = Image.open("image/Home.png") 
        self.login = ImageTk.PhotoImage(self.login.resize((80,100), Image.ANTIALIAS)) 
        self.master.imageL = self.login 
        inputtxt = Text(self.page3,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputtxt.place(x=600,y=400)
        inputPW = Text(self.page3,height = 1,width = 20,font=('Helvetica 20 bold'))
        inputPW.place(x=600,y=500)
        self.login = Button(self.page3, width=100, height = 100,image =self.login,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black",text="LOGIN",command=connect)
        self.login.place(x=650, y=600)
        
        
        # Bottom bar
        
        self.Button1 = Image.open("image/Home.png") 
        self.Button1 = ImageTk.PhotoImage(self.Button1.resize((80,100), Image.ANTIALIAS)) 
        self.master.image = self.Button1 
        
        self.Button2 = Image.open("image/Setting.png") 
        self.Button2 = ImageTk.PhotoImage(self.Button2.resize((80,100), Image.ANTIALIAS)) 
        self.master.image1 = self.Button2    
        
        self.Button3 = Image.open("image/User.png") 
        self.Button3 = ImageTk.PhotoImage(self.Button3.resize((80,100), Image.ANTIALIAS)) 
        self.master.image2 = self.Button3    

        self.home = Button(self.page2, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.home.place(x=500, y=750)

        self.option = Button(self.page2, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.option.place(x=700, y=750)
        
        self.user = Button(self.page2, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.user.place(x=900, y=750)
        
        self.home = Button(self.page1, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.home.place(x=500, y=750)

        self.option = Button(self.page1, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.option.place(x=700, y=750)
        
        self.user = Button(self.page1, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.user.place(x=900, y=750)



    def exitClient(self):
        pass

    def handler(self):
        """Handler on explicitly closing the GUI window."""
        if tkMessageBox.askokcancel("Quit?", "Are you sure you want to quit?"):
            self.exitClient()
