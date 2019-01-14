## TODO: import all necessary packages and functions
import pandas as pd 
import numpy as np
import calendar
import datetime
import pprint
import time

## Filenames
#chicago = 'chicago.csv'
#new_york_city = 'new_york_city.csv'
#washington = 'washington.csv'

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n').lower()
    # TODO: handle raw input and complete function
    if city == 'chicago':
        chicago = pd.read_csv('chicago.csv')
        return chicago
    if city == 'washington':
        washington = pd.read_csv('washington.csv')
        return washington
    if city == 'new york':
        nyc = pd.read_csv('new_york_city.csv')
        return new_york_city

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n').lower()
    # TODO: handle raw input and complete function
    month = 0
    day = 0
    if time_period == 'day' or time_period == 'month':
        month = get_month()
        if time_period == 'day':
            day = get_day(month)
    else:
        time_period = 'none'

    return {
        "type": time_period,
        "month": month,
        "day": day
    }


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    # TODO: handle raw input and complete function
    month_num = 0
    while month_num == 0:
        month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
        switch = {
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6
        }
        month_num = switch.get(month, 0)
    return month_num

    

def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    # TODO: handle raw input and complete function
    day_num = 0
    week_day, last_day = calendar.monthrange(2017, month)
    while day_num == 0:
        try:
            day = int(input('\nWhich day? Please type your response as an integer.\n'))
        except:
            day = 0
        if (day >= 1 or day <= last_day):
            day_num = day
    return day


def popular_month(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What month occurs most often in the start time?
    '''
    # TODO: complete function
    switch = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June"
    }
    return switch.get(city['month'].value_counts().index[0])
    


def popular_day(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?
    '''
    # TODO: complete function
    return city['day'].value_counts().index[0]


def popular_hour(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What hour of the day (0, 2, ... 22, 23) occurs most often in the start time?
    '''
    # TODO: complete function
    return city['hour'].value_counts().index[0]


def trip_duration(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    return city['duration'].sum(), city['duration'].mean()

def popular_stations(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most frequently used start station and most frequently
    used end station?
    '''
    # TODO: complete function
    return city['startStation'].value_counts().index[0], city['endStation'].value_counts().index[0]


def popular_trip(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?
    '''
    # TODO: complete function
    grouped = city.groupby(['startStation', 'endStation']).agg('count').idxmax()
    return str(grouped[0])


def users(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    return city['userType'].value_counts()


def gender(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    return len(city[city['Gender'] == 'Male']), len(city[city['Gender'] == 'Female'])


def birth_years(city, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    '''
    # TODO: complete function
    return (city['yearsOld'].max()), (city['yearsOld'].min())


def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    counter = 5
    while display == 'yes':
        return pprint.pprint(city.head(counter))
    counter += 5


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    city.rename(columns={'Start Time': 'startTime', 'End Time': 'endTime', 'Trip Duration': 'tripDuration', 
                        'Start Station': 'startStation', 'End Station': 'endStation', 'User Type': 'userType',
                       'Birth Year': 'birthYear'}, inplace=True)
    city['startTime'] = pd.to_datetime(city.startTime)
    city['endTime'] = pd.to_datetime(city.endTime)
    city['month'] = pd.to_datetime(city.startTime).map(lambda d: d.month)
    city['year'] = pd.to_datetime(city.startTime).map(lambda d: d.year)
    city['day'] = pd.to_datetime(city.startTime).map(lambda d: d.day)
    city['hour'] = pd.to_datetime(city.startTime).map(lambda d: d.hour)
    city['yearsOld'] = city['year'] - city['birthYear']
    city['duration'] = (city['endTime'] - city['startTime']).astype('timedelta64[s]')

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if (time_period['month'] > 0):
        city = city[city['month'] == time_period['month']]
    if (time_period['day'] > 0):
        city = city[city['day'] == time_period['day']]
    print(city.head())

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period['type'] == 'none':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        print('Most popular month: %s' % popular_month(city, time_period))

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period['type'] == 'none' or time_period['type'] == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        print('Most popular day of month: %s' % popular_day(city, time_period))

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    print('Most popular hour of day: %s' % popular_hour(city, time_period))


    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    totalDuration, averageDuration = trip_duration(city, time_period)
    print('The total trip duration is: %s minutes' % round((totalDuration / 60), 2))
    print('Average trip duration: %s minutes' % round((averageDuration / 60), 2))


    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    startStation, endStation = popular_stations(city, time_period)
    print('The most popular start station is: %s' % startStation)
    print('The most popular end station is: %s' % endStation)



    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    print("The most popular trip: %s" % popular_trip(city, time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    print(users(city, time_period))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    male, female = gender(city, time_period)
    print('There are %s males and %s females' % (male, female))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    oldest, youngest = birth_years(city, time_period)
    print('The oldest user is: %s' % oldest)
    print('The youngest user is: %s' % youngest)

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
