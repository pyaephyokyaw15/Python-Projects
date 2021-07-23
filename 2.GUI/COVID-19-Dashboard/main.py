from tkinter import *
from PIL import ImageTk, Image
import requests
import json
import datetime
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from tkinter import ttk
import numpy as np



# ========================== Getting Started ===========================

# Creat window
root = Tk()
root.title("COVID-19")
root.wm_iconbitmap('covid.ico')

# To get fit on screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry("{}x{}+0+0".format(window_width, window_height))

# change background color
root.configure(background='white')

# title
Label(root,text='COVID-19 Dashboard', font=('Arial', 20), pady=30, bg='#95bbe6', foreground='black').place(relx=0, rely=0, relwidth=1, relheight=0.05)





# ============================== varibales =======================================

c_country = StringVar()
background_color = '#86bfa1'

# ================================= World Data ==============================================

        
world_url = "https://disease.sh/v3/covid-19/all"
world_data = requests.get(world_url)
world_data = world_data.json()
updated = datetime.datetime.fromtimestamp((world_data['updated'])/1000)
updated = str(updated).split('.')[0]
updated = updated.split()
updated = updated[0]+'                                                           '+updated[1]
world_cases = world_data['cases']
world_deaths = world_data['deaths']
world_recovered = world_data['recovered']


today_world_cases = world_data['todayCases']
today_world_deaths = world_data['todayDeaths']
today_world_recovered = world_data['todayRecovered']






    



# ==============================================functions==============================

def world():
    global global_dates
    world_btn.config(bg='#aadfe3')
    country_btn.config(bg='#e6f4f5')
    

    total_cases_box_data.config(text=f"{world_cases:,}")
    total_deaths_box_data.config(text=f"{world_deaths:,}") 
    total_recovered_box_data.config(text=f"{world_recovered:,}")

    today_cases_box_data.config(text=f"{today_world_cases:,}")
    today_deaths_box_data.config(text=f"{today_world_deaths:,}") 
    today_recovered_box_data.config(text=f"{today_world_recovered:,}")

    world_bar_url = "https://disease.sh/v3/covid-19/historical/all?lastdays=31"
    bar = requests.get(world_bar_url)
    bar  = bar .json()  
    cases = bar['cases']
    global_dates = [date for date in cases.keys()][1:]
    piechart(world_recovered, world_deaths)
    barchart(world_bar_url)

    try:
        c_country1.destroy()
        c_search1.destroy()
   
    
    except:
        pass

    

def country():
    world_btn.config(bg='#e6f4f5')
    country_btn.config(bg='#aadfe3')
    
    

    
    global c_country1
    global c_search1

    
    c_country1=ttk.Entry(headline,font=('Arial',15, 'bold'), textvariable=c_country)
    c_country1.place(relx=0.8, rely =0.5, relwidth=0.15, anchor=CENTER)
    c_search1 = Button(headline,font=('Arial',12, 'bold'), text='Search', command=country_search)
    c_search1.place(relx=0.9, rely =0.5, relwidth=0.04,relheight=0.6, anchor=CENTER)
    

   
  





  
   


def country_search():
    
    
    base_url = "https://disease.sh/v3/covid-19/countries/"+str(c_country.get())
    page = requests.get(base_url)

    data = page.json() # turn page into a python object
        
    total_cases_box_data.config(text=f"{data['cases']:,}")
    total_deaths_box_data.config(text=f"{data['deaths']:,}") 
    total_recovered_box_data.config(text=f"{data['recovered']:,}")

    today_cases_box_data.config(text=f"{data['todayCases']:,}")
    today_deaths_box_data.config(text=f"{data['todayDeaths']:,}") 
    today_recovered_box_data.config(text=f"{data['todayRecovered']:,}")

    country_bar_url = "https://disease.sh/v3/covid-19/historical/{}?lastdays=31".format(str(c_country.get()))

    piechart(data['recovered'], data['deaths'])
    
    try:
        bar = requests.get(country_bar_url)
        bar  = bar .json()  

        cases = bar['timeline']['cases']
        dates = [date for date in cases.keys()][1:]
        total_cases = [case for case in cases.values()]
        cases = []
        cases.extend([total_cases[i+1]-total_cases[i] for i in range(len(total_cases)-1)])
    except:
        cases = [0 for i in range(30)]
        dates = global_dates


    fig = plt.figure(figsize=(12, 5), dpi=80)

    labelpos = np.arange(len(dates))


    ##This section formats the barchart for output

    plt.bar(labelpos, cases, align='center', alpha=1.0)
    plt.xticks(labelpos, dates, rotation=90)


    plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
    plt.xticks( horizontalalignment="center")

    #Applies the values on the top of the bar chart
    offset = min(cases)//10
    if offset != 0:
        for index, datapoints in enumerate(cases):
            plt.text(x=index, y=datapoints + offset, s=f"{datapoints}", fontdict=dict(fontsize=10), ha='center', va='bottom', rotation=90)



    ## This section draws a canvas to allow the barchart to appear in it
    canvasbar = FigureCanvasTkAgg(fig, master=root)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.33, rely=0.54, anchor=CENTER)












def piechart(recovered_num, death_num):
    # ======= Pie Chart =======



    #### Plot pie chart #####
    fig = plt.figure(figsize=(4, 4), dpi=100)
    fig.set_size_inches(4, 4)

    # Data to plot
    
    y = np.array([recovered_num, death_num])
    mylabels = ["Recovered", "Deaths"]
    mycolors = ["#4fd170", "#cf4f1d"]


    # Plot pie chart


    my_circle = plt.Circle((0, 0), 0.7, color='white')
    plt.pie(y, labels = mylabels, colors = mycolors, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
    plt.gca().add_artist(my_circle)
    # plt.show() 

    canvasbar = FigureCanvasTkAgg(fig, master=root)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.85, rely=0.54, anchor=CENTER)  # show the barchart on the ouput window
    

def barchart(bar_url):
    
    bar = requests.get(bar_url)
    bar  = bar .json()  

    cases = bar['cases']
    dates = [date for date in cases.keys()][1:]
    total_cases = [case for case in cases.values()]
    cases = []
    cases.extend([total_cases[i+1]-total_cases[i] for i in range(len(total_cases)-1)])
   

    fig = plt.figure(figsize=(12, 5), dpi=80)

    labelpos = np.arange(len(dates))


    ##This section formats the barchart for output

    plt.bar(labelpos, cases, align='center', alpha=1.0)
    plt.xticks(labelpos, dates, rotation=90)


    plt.tight_layout(pad=2.2, w_pad=0.5, h_pad=0.1)
    plt.xticks( horizontalalignment="center")

    #Applies the values on the top of the bar chart
    for index, datapoints in enumerate(cases):
        plt.text(x=index, y=datapoints + 10000, s=f"{datapoints}", fontdict=dict(fontsize=10), ha='center', va='bottom', rotation=90)



    ## This section draws a canvas to allow the barchart to appear in it
    canvasbar = FigureCanvasTkAgg(fig, master=root)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(relx=0.33, rely=0.54, anchor=CENTER)  # show the barchart on the ouput window

    




# ============================ Layout =========================================

                    # ==========  buttons  ========

world_btn = Button(root,text='Global', font=('Arial', 15), command=world)
world_btn.place(relx=0, rely=0.05, relheight=0.03, relwidth=0.5)

country_btn = Button(root,text='Country', font=('Arial', 15), command=country)
country_btn.place(relx=0.5, rely=0.05, relheight=0.03, relwidth=0.5)


world_btn.config(bg='green')

        # ================= Data boxes =================

# Confirmed Cases
total_cases_box = Frame(root, borderwidth=0)
total_cases_box.place(relx=0.02, rely=0.13, relheight=0.15, relwidth=0.3)
total_cases_box_label = Label(total_cases_box, text='Cases', font=('Arial', 20),background=background_color, foreground="white")
total_cases_box_data = Label(total_cases_box, text=f"{world_cases:,}",font=('Arial', 30),background=background_color, foreground="#823d00")
total_cases_box_time = Label(total_cases_box, text=updated, font=('Arial', 13),background=background_color, foreground="white")

total_cases_box_label.pack(fill=BOTH, expand=TRUE)
total_cases_box_data.pack(fill=BOTH, expand=TRUE)
total_cases_box_time.pack(fill=BOTH, expand=TRUE)



# Deaths
total_deaths_box = Label(root, borderwidth=0)
total_deaths_box.place(relx=0.35, rely=0.13, relheight=0.15, relwidth=0.3)
total_deaths_box_label = Label(total_deaths_box, text='Deaths', font=('Arial', 20),background=background_color, foreground="white")
total_deaths_box_data = Label(total_deaths_box, text=f"{world_deaths:,}",font=('Arial', 30),background=background_color, foreground="#bd1a1a")
total_deaths_box_time = Label(total_deaths_box, text=updated, font=('Arial', 13),background=background_color, foreground="white")

total_deaths_box_label.pack(fill=BOTH, expand=TRUE)
total_deaths_box_data.pack(fill=BOTH, expand=TRUE)
total_deaths_box_time.pack(fill=BOTH, expand=TRUE)


# recovered
total_recovered_box = Label(root, borderwidth=0)
total_recovered_box.place(relx=0.68, rely=0.13, relheight=0.15, relwidth=0.3)
total_recovered_box_label = Label(total_recovered_box , text='Recovered', font=('Arial', 20),background=background_color, foreground="white")
total_recovered_box_data = Label(total_recovered_box , text=f"{world_recovered:,}",font=('Arial', 30),background=background_color, foreground="green")
total_recovered_box_time = Label(total_recovered_box , text=updated, font=('Arial', 13),background=background_color, foreground="white")

total_recovered_box_label.pack(fill=BOTH, expand=TRUE)
total_recovered_box_data.pack(fill=BOTH, expand=TRUE)
total_recovered_box_time.pack(fill=BOTH, expand=TRUE)


# Confirmed Cases
today_cases_box = Frame(root, borderwidth=0)
today_cases_box.place(relx=0.02, rely=0.8, relheight=0.15, relwidth=0.3)
today_cases_box_label = Label(today_cases_box, text='Cases', font=('Arial', 20),background=background_color, foreground="white")
today_cases_box_data = Label(today_cases_box, text=f"{today_world_cases:,}",font=('Arial', 30),background=background_color, foreground="#823d00")
today_cases_box_time = Label(today_cases_box, text=updated, font=('Arial', 13),background=background_color, foreground="white")

today_cases_box_label.pack(fill=BOTH, expand=TRUE)
today_cases_box_data.pack(fill=BOTH, expand=TRUE)
today_cases_box_time.pack(fill=BOTH, expand=TRUE)



# Deaths
today_deaths_box = Label(root, borderwidth=0)
today_deaths_box.place(relx=0.35, rely=0.8, relheight=0.15, relwidth=0.3)
today_deaths_box_label = Label(today_deaths_box, text='Deaths', font=('Arial', 20),background=background_color, foreground="white")
today_deaths_box_data = Label(today_deaths_box, text=f"{today_world_deaths:,}",font=('Arial', 30),background=background_color, foreground="#bd1a1a")
today_deaths_box_time = Label(today_deaths_box, text=updated, font=('Arial', 13),background=background_color, foreground="white")

today_deaths_box_label.pack(fill=BOTH, expand=TRUE)
today_deaths_box_data.pack(fill=BOTH, expand=TRUE)
today_deaths_box_time.pack(fill=BOTH, expand=TRUE)


# recovered
today_recovered_box = Label(root, borderwidth=0)
today_recovered_box.place(relx=0.68, rely=0.8, relheight=0.15, relwidth=0.3)
today_recovered_box_label = Label(today_recovered_box , text='Recovered', font=('Arial', 20),background=background_color, foreground="white")
today_recovered_box_data = Label(today_recovered_box , text=f"{today_world_recovered:,}",font=('Arial', 30),background=background_color, foreground="green")
today_recovered_box_time = Label(today_recovered_box , text=updated, font=('Arial', 13),background=background_color, foreground="white")

today_recovered_box_label.pack(fill=BOTH, expand=TRUE)
today_recovered_box_data.pack(fill=BOTH, expand=TRUE)
today_recovered_box_time.pack(fill=BOTH, expand=TRUE)


          # ========= headline widgets ==================

headline= Frame(root, bg='white')
headline.place(relx=0, rely=0.08, relheight=0.05, relwidth=1)







world()

# Execute Tkinter
root.mainloop()