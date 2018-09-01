import pandas as pd

path = "C:\\Users\\gv01\\Desktop\\googleSync\\LEarning\\Udacity\\Data Scientists Foundation\\python\\Resources\\"
filename = 'chicago.csv'
chicago_df  = pd.read_csv(path+filename)

# df.head(), df.columns, df.describe(), df.info()
# df['column_name'].value_counts(), df['column_name'].unique()

def print_generic_information(df):

    '''
    prints generic information like head, columns, describe and info for the given dataframe.

    INPUT
        df: dataframe
    OUTPUT 
        output by the methods head(), columns(), describe(), info() and shape respectively.

    '''
    print(df.head()) 
    print('---------------------------------------------------------------------------')
    print(df.columns)  
    print('---------------------------------------------------------------------------')
    print(df.describe())  
    print('---------------------------------------------------------------------------')
    print(df.info())  
    print('---------------------------------------------------------------------------')
    print(df.shape)
    

def print_each_column_value_counts(df): 
    '''
    print each coumn value count (count of each unique value in the column) for the given dataframe.

    INPUT
        df: dataframe
    OUTPUT 
          output by the method value_counts() for each column of the dataframe

    '''
    column_list  = list(chicago_df)
    for column in column_list:
        print('columne_name: {}, --> value_count: {}'.format(column,df[column].value_counts()))
        print('---------------------------------------------------------------------------')


def print_each_column_unique(df,print_unique): 
    '''
    prints each column's unique values and the count for the given dataframe.

    INPUT
        df: dataframe
        print_unique: true if you want to print both, the unique values and count; false if you want to only print the count
    OUTPUT 
        column name, unique value count and values (depending upon the value of print_unique)
        

    '''
    column_list  = list(chicago_df)
    for column in column_list:
        values = df[column].unique()
        unique_count = len(values)
        if print_unique:
            print('columne_name: {},---- Unique value count: {},---- values: {}'.format(column,unique_count,values))
            print('---------------------------------------------------------------------------')
        else:
            print('columne_name: {},---- Unique value count: {}'.format(column,unique_count))
            print('---------------------------------------------------------------------------')

# convert the Start Time column to datetime
chicago_df['Start Time'] = pd.to_datetime(chicago_df['Start Time'])
'''print('---------------------------Start time------------------------------------------------')
print(chicago_df['Start Time'])'''

# extract hour from the Start Time column to create an hour column
# chicago_df['hour'] = chicago_df['Start Time'].dt.hour
'''print('-----------------------------hour----------------------------------------------')
print(chicago_df['hour'])'''



# find the most popular hour
# popular_hour = chicago_df['hour'].mode()[0]
# print('-----------------------------Compute the Most Popular Start Hour----------------------------------------')
# print('Most popular start time is: {}'.format(popular_hour))
# print(chicago_df['Start Time'].dt.weekday)
# print('----------------------------MONTHS---------------------------------------')
# print(chicago_df['Start Time'].dt.month)

#print_each_column_value_counts(chicago_df)
#print_each_column_unique(chicago_df,False)


# print value counts for each user type
# user_types = chicago_df['User Type'].value_counts()
# print('------------------------------Display a Breakdown of User Types---------------------------------------------')
#print(user_types)

#print(pd.value_counts(chicago_df['User Type']).values)

# print('--------------------------------------------------------------------------')

#print(chicago_df['Gender'].value_counts())

# ypes = chicago_df['User Type'].value_counts().index.tolist()
# print(types)

# values = chicago_df['User Type'].value_counts().values.tolist()
# print(values)

chicago_df['month'] = chicago_df['Start Time'].dt.month
df_month = chicago_df[chicago_df['month'] == 1]
print(df_month.columns)
print("-"*50)

'''print('most common day of week')
print(df_month['day_of_week'].mode()[0])
print('\n')'''

print('user types')
print(df_month['User Type'].value_counts())
print('\n')


print('gender')
print(df_month['Gender'].value_counts())
print('\n')

chicago_df['day'] = chicago_df['Start Time'].dt.weekday
df_day = chicago_df[chicago_df['day'] == 0]
#print(df_day.columns)

