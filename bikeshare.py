import pandas as pd
import time
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             
             'new york city': 'new_york_city.csv',
             
             'washington': 'washington.csv'}


def get_filters():
    print(' this is US bikeshare , get some data :  ')
# getter function to filtter data

    city = input('please enter City name : ').lower()
    # get the city name if valid
    
    while city not in ['chicago', 'new york', 'washington']:
        city = input("enter valid City name : (chicago, new york,                                           washington)").lower()
        #check for the city name

    month = input('please enter moth: all, january,february, ..,')
    # get the month name if valid
    while month not in ['all', 'january', 'february', 'march', 'april', 'may','june']:
        month = input('enter valid month name').lower()
        #check for the month name

        # get user input for month (all, january, february, ... , june)
    day = input('please enter : all, monday, tuesday, ... ')
    while day not in ['all', 'saturday', 'sunday', 'monday',
                      'tuesday', 'wednesday', 'thursday', 'friday']:
     #check for the day name   
        day = input('enter valid day name').lower()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    # function to load (city, month, day)
    f_name = CITY_DATA[city]
    # list  of cities names to make operation
    df = pd.read_csv(f_name)
    # read the file
    # then convert date (string) to date datatype
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # creae new 2 columns called month ,day_of_week from Start Time column
    # using built in function dt.month , dt.day_name()
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    df['hour'] = df['Start Time'].dt.hour
    # first , import Start date by to_datetime Function
    # we split the column of 'Start Time' into 'month' and 'day_of_week'
    # filter by month if applicable
    if month != 'all':
        # list of month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        #
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    ######
    # popular_hour = df['hour'].mode()[0]
    # can't assin to varaible
    print('hourrrrrrrrrr : ', df['hour'].mode()[0])
    # TO DO: display the most common month

    # month = df['month'].mode()[0]
    # can't assin to varaible
    print(df['month'].mode()[0])
    # TO DO: display the most common day of week

    # popular_day = df['day_of_week'].mode()[0]
    # can't assin to varaible
    print(df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    # function to calculate most commonly used (start ,end) station ,combination of start station       #and end  station
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # star2_station = df['Start Station'].mode()[0]
    # can't assin to varaible
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly end end station
    # end2_station = df['End Station'].mode()[0]
    # can't assin to varaible
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['combin_start_end'] = df['Start Station'] + ' ' + df['End Station']
    combin_start_end2 = df['combin_start_end'].mode()[0]

    print('starttttttttttt : ', df['combin_start_end'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    # function to Calculate total travel time,mean travel time 
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # total_travel = df['Trip Duration'].sum()
    # can't assin to varaible
    print(round((df['Trip Duration'].sum())
                / 3600, 2))

    # TO DO: display mean travel time
    # mean_travel = df['Trip Duration'].mean()
    # can't assin to varaible
    print(round((df['Trip Duration'].mean())
                / 3600, 2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    # function to display user types,counts of gender , 
    # earliest_year ,recent_year , common_year
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # user_counts = df['User Type'].value_counts()
    # can't assin to varaible
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # gender_counts = df['Gender'].value_counts()
    # can't assin to varaible
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print('not found')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
   # check statment for Birth Year
        common_year = int(df['Birth Year'].mode())
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        print('the earliest year: ', earliest_year, 'the recent year:   ',recent_year ,
              'the common year: ', common_year)
    else:
        print('not found')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    
    # function to view top 5 rows from data to user
    get_data = input(" to displays the first 5 rows ,press yes :  ").lower()
    first_location = 0
    while (get_data.lower() == "yes"):
        # using iloc() to print data by index begin location to end location
        print(df.iloc[first_location:first_location + 5])
        first_location += 5
        get_data = input(" get more 5 rows press yes : ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
         # pass the arguments to the functions
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\n to restart- Enter yes command \n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
    