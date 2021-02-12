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
    print()
    print('Hello! Let\'s explore some US bikeshare data!')
    print()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city =  input('Would you like to see data for Chicago, New York City, or Washington?\n\n').lower().strip()
        print()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('That\s not a valid city')
            print()
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to filter the data by?\nSelect a month from January to June or type "all" if not applicable.\n\n').title().strip()
        print()
        if month in ['All','January', 'February', 'March', 'April', 'May', 'June']:
            break
        else:
            print('That\'s not a valid month.')
            print()
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day would you like to filter the data by? Type "all" if not applicable.\n\n').title().strip()
        print()
        if day in ['All','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            break
        else:
            print('That\'s not a valid day')
            print()
            continue

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
        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # filter by month if applicable
    if month != 'All':
        months = ['All','January', 'February', 'March', 'April', 'May', 'June']

        month = months.index(month)

        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    print()
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()

    print("The most common month based on the given filtered data:\n\n", popular_month[0])
    print()
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()
    print('The most common day based on on the given filtered data:\n\n' , popular_day[0])
    print()

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()
    print('The most common start hour based on the given filtered data:\n\n' ,str(popular_start_hour[0]))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    print()
    start_time = time.time()

        # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()
    print("The most commonly used start station based on the given filtered data:\n\n",popular_start_station[0])
    print()

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()
    print("The most commonly used end station based on the given filtered data:\n\n",popular_end_station[0])
    print()

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = ('From: ' + df['Start Station'] + ' To: ' + df['End Station']).mode()
    print('The most most frequent combination of start station and end station trip based on the given filtered data: ')
    print()
    print(frequent_combination[0])
    print()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    print()
    start_time = time.time()

    """takes the sum of -numpy.64int array and retarun str- total travel time in(day:hour:min:sec)format"""

    seconds = df['Trip Duration'].sum()
    day = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    total_travel_time = "%02d:%02d:%02d:%02d" % (day,hour, minutes, seconds)
    print('The total travel time based on the given filtered data:\n')
    print(total_travel_time)
    print('days:hours:min:sec')


    print()

    """takes the mean of -numpy.64int array and retarun str- average travel time in(hour:min:sec)format"""

    seconds = df['Trip Duration'].mean()
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    average_travel_time = "%02d:%02d:%02d" % (hour, minutes, seconds)

    print()
    print('The average travel time based on the given filtered data:\n')
    print(average_travel_time)
    print('hours:min:sec')


    print()



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    print()
    start_time = time.time()

       # TO DO: Display counts of user types
    print('The count of user types based on the given filtered data:\n\n', df['User Type'].value_counts().to_string())
    print()

    # TO DO: Display counts of gender

    if 'Gender' in df:
        print('The count of user gender based on the given filtered data:\n\n', df['Gender'].value_counts().to_string())
        print()
    else:
        pass
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('The earliest birth year based on the given filtered data:\n\n', int(df['Birth Year'].min()))
        print()
        print('The most recent birth year based on the given filtered data:\n\n', int(df['Birth Year'].max()))
        print()
        print('The most common birth year based on the given filtered data:\n\n', int(df['Birth Year'].mode()[0]))
        print()
    else:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()

def row_data(df):
    """Display the row input based on the user input"""
    start = 0
    end = 5
    while True:
        user_row_data = input('Would you like to see row data?\n\n').lower().strip()
        if user_row_data == 'yes':
            print(df.iloc[start:end])
            start += 5
            end += 5
        elif user_row_data not in ['yes', 'no']:
            print('That\'s not a valid answer, please type "yes" or "no"')
        elif user_row_data == 'no':
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data(df)
        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n\n')
            if restart.lower().strip() == 'no':
                exit()
            elif restart.lower().strip() == 'yes':
                main()
            else:
                print()
                print('That invalid input, enter yes or no.\n')
                print()
                continue

if __name__ == "__main__":
	main()
