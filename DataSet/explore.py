#Absolutely 0 help just me, myself and I
import pandas as tb
from time import sleep

print("---Loading---")

try:
    table = tb.read_csv('lung_cancer.csv')
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

except FileNotFoundError:
    print("File couldn't be found")