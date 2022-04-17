from pandas import DataFrame
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyrebase
root= tk.Tk() 
 
data1 = {'Time': ['8:15','8:20','8:25','8:30','8:35','8:40','8:45','8:50','8:55','8:60','9:05','9:10','9:15','9:20','9:25'],
         'Heat': [45000,42000,52000,49000,47000,45000,42000,52000,49000,47000,45000,42000,52000,49000,47000]
        }

df1 = DataFrame(data1,columns=['Time','Heat'])
  
figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Time','Heat']].groupby('Time').sum()
df1.plot(kind='line', legend=True, ax=ax1, color='r',marker='o', fontsize=8)
ax1.set_title('Country Vs. GDP Per Capita')
# bar1.get_tk_widget().pack_forget()

root.mainloop()