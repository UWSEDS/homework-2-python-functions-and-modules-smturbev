# SAmi Turbeville
#Created 23 OCtober 2019
#CSE HW2
import pandas as pd

url="https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD"
#url1="https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

def test_create_dataframe(df, colNames):
    col = df.columns
    if len(col) != len(colNames):
        return False 
    #check if colNames is in df.columns (doesn't have to be in same order)
    for i in range(len(col)):
        for item in colNames:
            if item in col:
                continue
            else:
                return False
    #check that there are at least 10 rows in df
    nrows,ncols = df.shape
    if nrows <10:
        return False
    #check that all the columns have the same data types
    col_list = col.to_list()
    for i in col_list:
        #print("----------\n",i)
        column_values = df[i].to_list()
        column_types = [type(item) for item in column_values]
        numTypes = len(set(column_types))
        #print(numTypes)
        if numTypes > 1:
            return False
    return True


col_list= ['trip_id', 'starttime', 'stoptime', 'bikeid', 'tripduration','to_station_name','from_station_name','from_station_id','to_station_id','usertype','gender','birthyear' ]
col_list1=['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']

#print(test_create_dataframe(df,col_list1))

