import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk

# ===========================
# Define parameters
figurePath = './nba_court.jpg'
global coords
coords=[]

# Get Data from Excel Files
# Open a file
path = "./Data/"
dirs = os.listdir(path)
print('>>> Original Database Data')
for filename in dirs:
    filepath = './Data/' + filename
    if (filename == 'data_Curry_all.xlsx'):
        df_Curry = pd.read_excel(filepath)
        data_Curry = np.matrix(df_Curry)
        print(data_Curry)
    elif (filename == 'data_Durant_all.xlsx'):
        df_Durant = pd.read_excel(filepath)
        data_Durant = np.matrix(df_Durant)
        print(data_Durant)
    elif (filename == 'data_Thompson_all.xlsx'):
        df_Thompson = pd.read_excel(filepath)
        data_Thompson = np.matrix(df_Thompson)
        print(data_Thompson)

# ===========================
# Define functions
def function_Record():
    # Record Shooting
    fig = plt.figure()
    img = plt.imread(figurePath)
    plt.imshow(img)
    global coords
    coords = []  # initialize

    if (val_Curry.get() == 1):
        plt.title('Record Interface for Curry')
    elif (val_Durant.get() == 1):
        plt.title('Record Interface for Durant')
    elif (val_Thompson.get() == 1):
        plt.title('Record Interface for Thompson')

    def onclick(event):
        global ix, iy
        ix, iy = event.xdata, event.ydata
        print('x = %d, y = %d' % (ix, iy))
        plt.plot(ix, iy, 'co')
        plt.draw()

        global coords
        temp_coords = [ix, iy]
        coords = np.append(coords, temp_coords)

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    return

def function_SaveToExcel():
    global coords
    coords = np.matrix(coords)
    coords = np.transpose(coords)
    (m, n) = np.shape(coords)
    x = []
    y = []
    for i in range(0, m):
        if (i%2 == 0):
            x = np.append(x, coords[i, 0])
        elif (i%2 == 1):
            y = np.append(y, coords[i, 0])

    x = np.transpose(np.matrix(x))
    y = np.transpose(np.matrix(y))
    pos = np.hstack((x, y))

    if (val_Curry.get() == 1):
        pos = np.vstack((data_Curry, pos))
        pos = pd.DataFrame(pos)
        print(pos)
        writer = pd.ExcelWriter('./Data/data_Curry_all.xlsx')
        pos.to_excel(writer, 'Sheet1')
        writer.save()
        print('Successfully Saved into Curry Excel!')
    elif (val_Durant.get() == 1):
        pos = np.vstack((data_Durant, pos))
        pos = pd.DataFrame(pos)
        print(pos)
        writer = pd.ExcelWriter('./Data/data_Durant_all.xlsx')
        pos.to_excel(writer, 'Sheet1')
        writer.save()
        print('Successfully Saved into Durant Excel!')
    elif (val_Thompson.get() == 1):
        pos = np.vstack((data_Thompson, pos))
        pos = pd.DataFrame(pos)
        print(pos)
        writer = pd.ExcelWriter('./Data/data_Thompson_all.xlsx')
        pos.to_excel(writer, 'Sheet1')
        writer.save()
        print('Successfully Saved into Thompson Excel!')

    return

def plot_Point(x_val, y_val, colr):
    # put a red dot, size 40, at 2 locations:
    if (colr == 'red'):
        plt.scatter(x=x_val, y=y_val, c='r', s=20)
    elif (colr == 'green'):
        plt.scatter(x=x_val, y=y_val, c='g', s=20)
    elif (colr == 'blue'):
        plt.scatter(x=x_val, y=y_val, c='b', s=20)
    return

def function_Plot():

    # Get Data from Excel Files (Data could be updated.)
    # Open a file
    path = "./Data/"
    dirs = os.listdir(path)
    print('>>> Updated Database Data')
    for filename in dirs:
        filepath = './Data/' + filename
        if (filename == 'data_Curry_all.xlsx'):
            df_Curry = pd.read_excel(filepath)
            data_Curry = np.matrix(df_Curry)
            print(data_Curry)
        elif (filename == 'data_Durant_all.xlsx'):
            df_Durant = pd.read_excel(filepath)
            data_Durant = np.matrix(df_Durant)
            print(data_Durant)
        elif (filename == 'data_Thompson_all.xlsx'):
            df_Thompson = pd.read_excel(filepath)
            data_Thompson = np.matrix(df_Thompson)
            print(data_Thompson)

    # ===========================
    # Plot Shooting
    img = plt.imread(figurePath)
    plt.imshow(img)

    x_val_Curry = np.squeeze(np.asarray(np.transpose(data_Curry[:, 0])))
    y_val_Curry = np.squeeze(np.asarray(np.transpose(data_Curry[:, 1])))
    x_val_Durant = np.squeeze(np.asarray(np.transpose(data_Durant[:, 0])))
    y_val_Durant = np.squeeze(np.asarray(np.transpose(data_Durant[:, 1])))
    x_val_Thompson = np.squeeze(np.asarray(np.transpose(data_Thompson[:, 0])))
    y_val_Thompson = np.squeeze(np.asarray(np.transpose(data_Thompson[:, 1])))


    if ((val_Curry.get()==1) and (val_Durant.get()==0) and (val_Thompson.get()==0)):
        plot_Point(x_val_Curry, y_val_Curry, 'red')
        plt.title('Field Goals Made')
        plt.legend(['Stephen Curry'])
        print('Successfully Plotted Curry Data!')
        plt.show()

    elif ((val_Curry.get()==0) and (val_Durant.get()==1) and (val_Thompson.get()==0)):
        plot_Point(x_val_Durant, y_val_Durant, 'green')
        plt.title('Field Goals Made')
        plt.legend(['Kevin Durant'])
        print('Successfully Plotted Durant Data!')
        plt.show()

    elif ((val_Curry.get()==0) and (val_Durant.get()==0) and (val_Thompson.get()==1)):
        plot_Point(x_val_Thompson, y_val_Thompson, 'blue')
        plt.title('Field Goals Made')
        plt.legend(['Klay Thompson'])
        print('Successfully Plotted Thompson Data!')
        plt.show()

    elif ((val_Curry.get() == 1) and (val_Durant.get() == 1) and (val_Thompson.get() == 0)):
        plot_Point(x_val_Curry, y_val_Curry, 'red')
        plot_Point(x_val_Durant, y_val_Durant, 'green')
        plt.title('Field Goals Made')
        plt.legend(['Stephen Curry', 'Kevin Durant'])
        print('Successfully Plotted Curry and Durant Data!')
        plt.show()

    elif ((val_Curry.get() == 1) and (val_Durant.get() == 0) and (val_Thompson.get() == 1)):
        plot_Point(x_val_Curry, y_val_Curry, 'red')
        plot_Point(x_val_Thompson, y_val_Thompson, 'blue')
        plt.title('Field Goals Made')
        plt.legend(['Stephen Curry', 'Klay Thompson'])
        print('Successfully Plotted Curry and Thompson Data!')
        plt.show()

    elif ((val_Curry.get() == 0) and (val_Durant.get() == 1) and (val_Thompson.get() == 1)):
        plot_Point(x_val_Durant, y_val_Durant, 'green')
        plot_Point(x_val_Thompson, y_val_Thompson, 'blue')
        plt.title('Field Goals Made')
        plt.legend(['Kevin Durant', 'Klay Thompson'])
        print('Successfully Plotted Durant and Thompson Data!')
        plt.show()

    elif ((val_Curry.get() == 1) and (val_Durant.get() == 1) and (val_Thompson.get() == 1)):
        plot_Point(x_val_Curry, y_val_Curry, 'red')
        plot_Point(x_val_Durant, y_val_Durant, 'green')
        plot_Point(x_val_Thompson, y_val_Thompson, 'blue')
        plt.title('Field Goals Made')
        plt.legend(['Stephen Curry', 'Kevin Durant', 'Klay Thompson'])
        print('Successfully Plotted Curry, Durant and Thompson Data!')
        plt.show()

    return


# =======================================================
# GUI Starts Here.
master = tk.Tk()
master.title('NBA Player Shooting Position')
master.geometry('280x120')

# Label
label_Player = tk.Label(master, text='Select Player(s)', bg='cyan')
label_Player.place(x=5, y=5)

# Checkbuttons
val_Curry = tk.IntVar()
checkbutton_Curry = tk.Checkbutton(master, text='Stephen Curry', variable=val_Curry)
checkbutton_Curry.place(x=5, y=25)
val_Durant = tk.IntVar()
checkbutton_Durant = tk.Checkbutton(master, text='Kevin Durant', variable=val_Durant)
checkbutton_Durant.place(x=5, y=55)
val_Thompson = tk.IntVar()
checkbutton_Thompson = tk.Checkbutton(master, text='Klay Thompson', variable=val_Thompson)
checkbutton_Thompson.place(x=5, y=85)

# Buttons
button_Record = tk.Button(master, text='Record Shooting Position!', command=function_Record)
button_Record.place(x=120, y=25)
button_Save = tk.Button(master, text='Save into Excel!', command=function_SaveToExcel)
button_Save.place(x=120, y=55)
button_Plot = tk.Button(master, text='Plot Shooting Position!', command=function_Plot)
button_Plot.place(x=120, y=85)

master.mainloop()

