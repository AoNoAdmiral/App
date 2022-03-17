from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import tkinter.font as font
from turtle import color
from PIL import Image, ImageTk
from tkinter import PhotoImage


class Client:

    def __init__(self,master):
        self.myFont = font.Font(family='Courier', weight='bold')
        self.master = master
        self.counter = 0
        self.master.protocol("WM_DELETE_WINDOW", self.handler)
        self.master.attributes('-fullscreen', True)
        self.page1 = Frame(master,bg='black',width = 3000,height = 1000)
        self.page2 = Frame(master,bg='black',width = 3000,height = 1000)
        self.switch(1)
        self.canvas = Canvas(self.page1, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        self.initOption()
        
    def switch(self,a):
        for frame in (self.page1, self.page2):
            frame.pack(fill='both', expand=True)
        if a == 1:
            self.page2.pack_forget()
        else: 
            self.page1.pack_forget()

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
        
        self.canvas2.create_text(195,250, text="59%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvas2.create_text(340,250, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvas2.create_text(475,250, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        self.canvas2.create_text(600,250, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        
        self.round_rectangle(self.canvas2,110,10, 300, 50,fill="green")
        self.canvas2.create_text(120,15, text="Glasshouse 1", fill="white", font=('Helvetica 20 bold'),anchor=NW)
        
        # x = self.round_rectangle(self.canvas2,100,400, 700, 700,fill="white")
        # self.canvas2.create_rectangle(110,10+400, 690, 150+400,fill="white")
        # self.canvas2.create_text(195,250+400, text="59%", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        # self.canvas2.create_text(340,250+400, text="30oC", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        # self.canvas2.create_text(475,250+400, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        # self.canvas2.create_text(600,250+400, text="off", fill="black", font=('Helvetica 20 bold'),anchor=NW)
        # self.round_rectangle(self.canvas2,100,400, 700, 700,fill="white")
        # self.canvas2.create_rectangle(110,410, 690, 550,fill="white")
        # return x
    
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
        self.createBox()
        
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
        
        # im = im.resize((1000,300))
        # self.renderimage(self.canvasP2,im.load(),im.size[0],im.size[1])
        
        
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

        self.home = Button(self.master, width=100, height = 100,image =self.Button1,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.home.place(x=500, y=750)

        self.option = Button(self.master, width=100, height = 100,image =self.Button2,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.option.place(x=700, y=750)
        
        self.user = Button(self.master, width=100, height = 100,image =self.Button3,highlightthickness=0,bg='black', fg='black', activeforeground="black",
                            activebackground="black")
        self.user.place(x=900, y=750)



    def exitClient(self):
        pass

    def handler(self):
        """Handler on explicitly closing the GUI window."""
        if tkMessageBox.askokcancel("Quit?", "Are you sure you want to quit?"):
            self.exitClient()
