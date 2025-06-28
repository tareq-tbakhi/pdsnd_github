# bikeshare.py
# Author: Tareq Tbakhi
# Project: Explore US Bikeshare Data
# Description: Interactive terminal program to analyze bikeshare data from three U.S. cities.
# Created for Udacity Programming for Data Science with Python Nanodegree
import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """Asks user to specify a city, month, and day to analyze."""
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').strip().lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please try again.")

    while True:
        filter_type = input('Would you like to filter the data by month, day, or not at all? Type "none" for no filter.\n').strip().lower()
        if filter_type in ['month', 'day', 'none']:
            break
        else:
            print("Invalid filter type. Try again.")

    month = day = 'all'
    if filter_type == 'month':
        while True:
            month = input('Which month - January, February, March, April, May, or June?\n').strip().lower()
            if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print("Invalid month. Try again.")
    elif filter_type == 'day':
        while True:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').strip().lower()
            if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                print("Invalid day. Try again.")

    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable."""
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start = time.time()

    print('Most Common Month:', df['month'].mode()[0].title())
    print('Most Common Day:', df['day_of_week'].mode()[0].title())
    print('Most Common Start Hour:', df['hour'].mode()[0])

    print(f"\nThis took {time.time() - start:.2f} seconds.")


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start = time.time()

    print('Most Common Start Station:', df['Start Station'].mode()[0])
    print('Most Common End Station:', df['End Station'].mode()[0])
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    print('Most Common Trip:', df['trip'].mode()[0])

    print(f"\nThis took {time.time() - start:.2f} seconds.")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start = time.time()

    print('Total Travel Time (s):', df['Trip Duration'].sum())
    print('Average Travel Time (s):', df['Trip Duration'].mean())

    print(f"\nThis took {time.time() - start:.2f} seconds.")


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start = time.time()

    print('\nUser Types:\n', df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print('\nGender Breakdown:\n', df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print('\nEarliest Birth Year:', int(df['Birth Year'].min()))
        print('Most Recent Birth Year:', int(df['Birth Year'].max()))
        print('Most Common Birth Year:', int(df['Birth Year'].mode()[0]))

    print(f"\nThis took {time.time() - start:.2f} seconds.")


def display_raw_data(df):
    """Displays raw data 5 rows at a time upon user request."""
    i = 0
    while True:
        view = input('\nWould you like to view 5 rows of raw data? Enter yes or no.\n').strip().lower()
        if view != 'yes':
            break
        print(df.iloc[i:i+5])
        i += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart != 'yes':
            print('\nThank you for using the Bikeshare Data Explorer. Goodbye!\n')
            break


if __name__ == "__main__":
    main()
