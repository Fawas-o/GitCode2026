#Absolutely 0 help just me, myself and I
import pandas as pd
import matplotlib.pyplot as plt
#^ for data visualisation ^
from time import sleep

print("---Loading---")

try:
    table = pd.read_csv('lung_cancer.csv')
    print(f"---Numbers of rows and columns {table.shape}---")
    sleep(3)

    print(f"---These are the Data types {table.info}---")
    sleep(2)

    print("---A quick preview will be printed soon---")
    time = int(input("How much rows would you like to get printed: "))

    for i in range (3,0):
        print(i)
        sleep(1)
    
    print(table.head(time))

    drop = ""
    while drop != "Y" and drop != "N":
        drop = input("Would you like to drop any rows with missing data? Y/N ").upper()

    if drop == "Y":
        print(table.dropna())
    #axis = 0 means rows, axis = 1 means columns
except FileNotFoundError:
    print("File couldn't be found")