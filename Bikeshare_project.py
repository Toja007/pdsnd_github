# importing libraries
import pandas as pd
import numpy as np

# load all data
df1 = pd.read_csv("chicago.csv")
df2 = pd.read_csv("new_york_city.csv")
df3 = pd.read_csv("washington.csv")

# drop null values
df1.dropna(axis = 0, inplace = True)
df2.dropna(axis = 0, inplace = True)
df3.dropna(axis = 0, inplace = True)

# coverting start time and end time to datetime
df1["Start Time"] = pd.to_datetime(df1['Start Time'])
df1["End Time"] = pd.to_datetime(df1['End Time'])

df2["Start Time"] = pd.to_datetime(df2['Start Time'])
df2["End Time"] = pd.to_datetime(df2['End Time'])

df3["Start Time"] = pd.to_datetime(df3['Start Time'])
df3["End Time"] = pd.to_datetime(df3['End Time'])

# extracting months and days
df1['month'] = df1['Start Time'].dt.month_name()
df1['day'] = df1['Start Time'].dt.day_name()
df1['Hour'] = df1['Start Time'].dt.hour

df2['month'] = df2['Start Time'].dt.month_name()
df2['day'] = df2['Start Time'].dt.day_name()
df2['Hour'] = df2['Start Time'].dt.hour

df3['month'] = df3['Start Time'].dt.month_name()
df3['day'] = df3['Start Time'].dt.day_name()
df3['Hour'] = df3['Start Time'].dt.hour

# function for city statistics
def city(df1, df2, df3):
    #creating user interaction
    name = str(input("Please enter your name: ")).lower()
    print("\U0001f600", f"Welcome {name} lets explore bikeshare data")

    while True:
        city = str(input("Please enter the city name : ")).lower()
        if city not in ("Chicago", "New York City", "Washington"):
            print("Sorry, we only have three cities \n Chicago, New york city and Washington.")
        else:
            print("looks like you want to learn about ", city)
            break
    while True:
        month = str(input("What month would you like to explore? ")).lower()
        if month not in ("January", "February", "March", "April", "May", "June"):
            print("we only have six months of data, January - June \n Try again!")
        else:
            break
    while True:
        day = str(input("what day? ")).lower()
        if day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
            print("Enter day in words \n Try again!")
        else:
            break

    n = int(input("How many rows of data do you wish to see? "))

    if city == "Chicago":
        print("\U0001f600", "okay, let us explore", city)
        mask_month = df1['month'] == month
        mask_day = df1['day'] == day
        df1 = df1[mask_month & mask_day]
        print(df1.head(n))
        print("Enter yes for more and no to skip ")
        while True:
            more = str(input("would like to see more data? ")).lower()
            n += 5
            if more == "Yes":
                print(df1.head(n))
            elif more == "No":
                print("Alright!")
                break



    elif city == "New York City":
        print("\U0001f600", "okay, let us explore", city)
        mask_month = df2['month'] == month
        mask_day = df2['day'] == day
        df2 = df2[mask_month & mask_day]
        print(df2.head(n))
        print("Enter yes for more and no to skip ")
        while True:
            more = str(input("would like to see more data? ")).lower()
            n += 5
            if more == "Yes":
                print(df2.head(n))
            elif more == "No":
                print("Alright!")
                break

    elif city == "Washington":
        print("\U0001f600", "okay, let us explore", city)
        mask_month = df3['month'] == month
        mask_day = df3['day'] == day
        df3 = df3[mask_month & mask_day]
        print(df3.head())
        print("Enter yes for more and no to skip ")
        while True:
            more = str(input("would like to see more data? ")).lower()
            n += 5
            if more == "Yes":
                print(df3.head(n))
            elif more == "No":
                print("Alright!")
                break

city(df1, df2, df3)

# function for time statistics
def time_stats():
    while True:
        city = str(input("Please enter the city name : ")).lower()
        if city not in ("Chicago", "New York City", "Washington"):
            print("Sorry, we only have three cities \n Chicago, New york city and Washington.")
        else:
            break
    if city == "Chicago":
        print(f"The most common month is: ", df1["month"].mode()[0])
        print(f"The most common day is: ", df1["day"].mode()[0])
        print(f"The most comon hour is: ", df1["Hour"].mode()[0])

    elif city == "New York City":
        print(f"The most common month is: ", df2["month"].mode()[0])
        print(f"The most common day is: ", df2["day"].mode()[0])
        print(f"The most comon hour is: ", df2["Hour"].mode()[0])

    elif city == "Washington":
        print(f"The most common month is: ", df3["month"].mode()[0])
        print(f"The most common day is: ", df3["day"].mode()[0])
        print(f"The most comon hour is: ", df3["Hour"].mode()[0])

time_stats()

# function for station statistics
def station_stats():
    while True:
        city = str(input("Please enter the city name : ")).lower()
        if city not in ("Chicago", "New York City", "Washington"):
            print("Sorry, we only have three cities \n Chicago, New york city and Washington.")
        else:
            break
    if city == "Chicago":
        print(f"The most common start station is: ", df1["Start Station"].mode()[0])
        print(f"The most common end station is: ", df1["End Station"].mode()[0])
        print(f"The most frequent combination of start station and end station trip is: ", df1.groupby(["Start Station", "End Station"]).size().idxmax())

    elif city == "New York City":
        print(f"The most common start station is: ", df2["Start Station"].mode()[0])
        print(f"The most common end station is: ", df2["End Station"].mode()[0])
        print(f"The most frequent combination of start station and end station trip is: ", df2.groupby(["Start Station", "End Station"]).size().idxmax())

    elif city == "Washington":
        print(f"The most common month is: ", df3["Start Station"].mode()[0])
        print(f"The most common day is: ", df3["End Station"].mode()[0])
        print(f"The most frequent combination of start station and end station trip is: ", df3.groupby(["Start Station", "End Station"]).size().idxmax())

station_stats()

# function for trip statistics
def trip_stats():
    while True:
        city = str(input("Please enter the city name : ")).lower()
        if city not in ("Chicago", "New York City", "Washington"):
            print("Sorry, we only have three cities \n Chicago, New york city and Washington.")
        else:
            break
    if city == "Chicago":
        total_minutes = df1["Trip Duration"].sum()
        average_minute = df1["Trip Duration"].mean()
        # Get hours with floor division
        hours = total_minutes // 60
        a_hour = average_minute // 60

        # Get additional minutes with modulus
        minutes = total_minutes % 60
        a_minute = average_minute % 60

        # Create time as a string
        time_string = "{}:{}".format(hours, minutes)
        a_time_string = "{}:{}".format(a_hour, a_minute)

        print("Total trip: ", time_string)
        print("Average trip: ", a_time_string)

    elif city == "New York City":
        total_minutes = df2["Trip Duration"].sum()
        average_minute = df2["Trip Duration"].mean()
        # Get hours with floor division
        hours = total_minutes // 60
        a_hour = average_minute // 60

        # Get additional minutes with modulus
        minutes = total_minutes % 60
        a_minute = average_minute % 60

        # Create time as a string
        time_string = "{}:{}".format(hours, minutes)
        a_time_string = "{}:{}".format(a_hour, a_minute)

        print("Total trip: ", time_string)
        print("Average trip: ", a_time_string)

    elif city == "Washington":
        total_minutes = df3["Trip Duration"].sum()
        average_minute = df3["Trip Duration"].mean()
        # Get hours with floor division
        hours = total_minutes // 60
        a_hour = average_minute // 60

        # Get additional minutes with modulus
        minutes = total_minutes % 60
        a_minute = average_minute % 60

        # Create time as a string
        time_string = "{}:{}".format(hours, minutes)
        a_time_string = "{}:{}".format(a_hour, a_minute)

        print("Total trip: ", time_string)
        print("Average trip: ", a_time_string)

trip_stats()

# function for user statistics
def user_stats():
    while True:
        city = str(input("Please enter the city name : ")).lower()
        if city not in ("Chicago", "New York City", "Washington"):
            print("Sorry, we only have three cities \n Chicago, New york city and Washington.")
        else:
            break
    if city == "Chicago":
        print(df1["User Type"].value_counts())
        print(df1["Gender"].value_counts())
        print("The earliest birth year is: ", df1["Birth Year"].min())
        print("The latest birth year is: ", df1["Birth Year"].max())
        print("The most common birth year is: ", df1["Birth Year"].mode()[0])

    if city == "New York City":
        print(df2["User Type"].value_counts())
        print(df2["Gender"].value_counts())
        print("The earliest birth year is: ", df2["Birth Year"].min())
        print("The latest birth year is: ", df2["Birth Year"].max())
        print("The most common birth year is: ", df2["Birth Year"].mode()[0])

    if city == "Washington":
        print(df3["User Type"].value_counts())
        print(df3["Gender"].value_counts())
        print("The earliest birth year is: ", df3["Birth Year"].min())
        print("The latest birth year is: ", df3["Birth Year"].max())
        print("The most common birth year is: ", df3["Birth Year"].mode()[0])


user_stats()

def main():
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart != "yes":
            print("\U0001f600 Thank you!, see you some other time")
            break
        city(df1, df2, df3)
        time_stats()
        station_stats()
        trip_stats()
        user_stats()

main()
