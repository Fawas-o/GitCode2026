#Absolutely 0 help just me, myself and I
import pandas as pd
import matplotlib.pyplot as plt
#^ for data visualisation ^
from time import sleep

print("---Loading---")

try:
    table = pd.read_csv('lung_cancer.csv')
    print("These are the total number of missing values in this table:")
    print(table.isna().sum())
    sleep(3)
    print(f"---Numbers of rows and columns {table.shape}---")
    sleep(2)

    print(f"---These are the Data types ---\n{table.info}")

    sleep(2)

    print("---A quick preview will be printed soon---")

    time = 0
    while time <= 0:
        try:
            time = int(input("How much rows would you like to get printed: "))
            if time <= 0:
                print("You must input a number above 0")
        except ValueError:
            print("You must input a number over 0")
            time = 0

    for i in range (3,0,-1):
        print(i)
        sleep(1)
    
    print(table.head(time))

    drop = ""
    cln_tbl = table.dropna()

    stats = table['gender'].value_counts()
    race = table['race'].value_counts()
    tmr_lction = table['tumor_location'].value_counts()
    death = table['death01'].value_counts()

    print(stats)
    print()
    print(race)
    print()
    print(tmr_lction)
    print()
    print(death)

    print(f"The oldest person in this data is {table['age_at_initial_pathologic'].max()} \nThe youngest person is {table['age_at_initial_pathologic'].min()}\nthe average age is {round(table['age_at_initial_pathologic'].mean(), 2)}")

    while drop != "Y" and drop != "N":
        drop = input("Would you like to drop any rows with missing data? Y/N ").upper()

    if drop == "Y":
        print(cln_tbl)
    #axis = 0 means rows, axis = 1 means columns
    #printing amount of men and ladies
    table['age_at_initial_pathologic'].plot(kind = 'hist')
    plt.savefig('Age_histogram.png')
    plt.show()
    # print("The ") something with mean etc
except FileNotFoundError:
    print("File couldn't be found")
