import pandas as pd 
from pandas import ExcelWriter
from pandas import ExcelFile 
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Graphing Application')


root.filename = filedialog.askopenfilename(initialdir="/Desktop", title="Select a File", filetypes=(("xlsm files", "*.xlsm"), ("all files", "*.*")))
my_label = Label(root, text=root.filename).pack()


root.mainloop() 


print("University of Maryland\n")
print("\n")
print("Welcome!")
print("\n")
print("You can use this application in order to print the graph of your data!\n")
print("Save the file in the same directory or folder where this program is.\n")
print("Enter the file name, as you saved it\n")
print("This program only takes Excel files\n")
print("please add the .xlsm or .xlsx at the end of your file name\n")
print("File name:")
filename = root.filename 

df = pd.read_excel(filename)


print("\n")
print("Enter the columns you want to graph: \n")
print("X-Axis: \n")
xAxis = input()
print("Y-Axis: \n")
yAxis = input()
print("Do you want to include error bars?")
print("Y/N")
check = input()
print("Enter the Units and Title of Axis:")
print("Enter the X-Axis title:")
xTitle = input()
print("Please enter the unit for the X-Axis now:")
xUnits = input()
print("Enter the Y-Axis title: ")
yTitle = input()
print("Please enter the unit for the Y-Axis now:")
yUnits = input()
print("Please enter the title of the Graph: ")
graph_title = input()

print("Graph loading ....")

for i in range(2,101):
    if i%2==0:
       print(i)

print("Done Loading graph.")
print("Do you want to see it, or just exit the program?")
print("Enter Y to continue, N to exit")
choice_to_continue = input()


if choice_to_continue == 'Y':

    if check == 'Y':
        print("Enter the error column you want")
        error = input()
    else:
        print("Graph without error bars.")



    print("Do you want to see them printed Y/N ?")
    choice = input()

    if choice == 'Y':
        if check == 'Y':
            print(" X Axis Column chosen:")
            print(xAxis)
            print("data:")
            for i in df.index:
                print(df[xAxis][i])
            print("\n")

            print(" Y Axis Column chosen:")
            print(yAxis)
            print("data:")
            for i in df.index:
                print(df[yAxis][i])
            print("\n")
            print("Error values:")
            print(error)
            for i in df.index:
                print(df[error][i])

        
        else:  
            print(" X Axis Column chosen:")
            print(xAxis)
            print("data:")
            for i in df.index:
                print(df[xAxis][i])
            print("\n")

            print(" Y Axis Column chosen:")
            print(yAxis)
            print("data:")
            for i in df.index:
                print(df[yAxis][i])
            print("\n")


    if check == 'Y':
        plt.scatter(df[xAxis],df[yAxis])
        plt.errorbar(df[xAxis], df[yAxis], yerr=error, linestyle="None")
        plt.title(graph_title)
        plt.xlabel(xTitle + " " + xUnits)
        plt.ylabel(yTitle + " " + yUnits)
        #plt.ylim(0,1.2E-06)
        #plt.yscale("log")
        #plt.xscale("log")
        plt.show()
    else:
        plt.scatter(df[xAxis],df[yAxis])
        plt.title(graph_title)
        plt.xlabel(xTitle + " " + xUnits)
        #plt.ylim(0,1.2E-06)
       # plt.xlim(600, 160000)
        plt.ylabel(yTitle + " " + yUnits)
        #plt.yscale("log")
        #plt.xscale("log")
        plt.show()
    print("Program has ended, please restart again to print another graph :)")
else:
    print("You chose to exit, program has ended, please restart again to print a graph:)")
