import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input('Would you like to see data for Chicago, New York, or Washington? ').lower()
        except KeyError:
            print('That is not a city! Try again!')
        if city in ['chicago', 'new york city', 'washington']:
            break
    #get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Which month - January, February, March, April, May, June or all? ').lower()
        except KeyError:
            print('That is not a month! Try again!')
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ').lower()
        except KeyError:
            print('That is not a month! Try again!')
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data from csv file
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #display the most common month
    print('the most common month: ')
    print(df['Start Time'].dt.month.mode()[0])
    
    #display the most common day of week
    print ('the most common day of week: ')
    print(df['Start Time'].dt.weekday_name.mode()[0])
    
    #display the most common start hour
    print('the most common start hour')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #display most commonly used start station
    print('The most commonly used start station: ')
    print((df['Start Station'].value_counts()).idxmax())

    #display most commonly used end station
    print('The most commonly used end station: ')
    print((df['End Station'].value_counts()).idxmax())

    #display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip: ')
    print(((df['Start Station']+df['End Station']).value_counts()).idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #display total travel time
    print('The total travel time: ')
    print(df['Trip Duration'].sum())
    
    #display mean travel time
    print('the mean travel time: ')
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #Display counts of user types
    print('The counts of user types: ')
    print(df['User Type'].value_counts())

    #Display counts of gender
    try:
        print('The counts of gender: ')
        print(df['Gender'].value_counts())
    except KeyError:
        print('no data about gender here')

#Display earliest, most recent, and most common year of birth
    try:
        print('The earliest year of birth: ')
        print(int(df['Birth Year'].min()))
        print('The most recent year of birth: ')
        print(int(df['Birth Year'].max()))
        print('The most common year of birth: ')
        print(int(df['Birth Year'].mode()[0]))
    except KeyError:
        print('no data about birth year here')
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        num_of_row = 5

        while True:
            display_data =input('\nWould you like to disply 5 row from data ? Enter yes or no.\n')
            if display_data.lower() == 'yes':
                print (df.head(num_of_row))
                num_of_row+=5
            elif display_data.lower() != 'yes':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
