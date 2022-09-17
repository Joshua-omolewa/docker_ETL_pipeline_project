#Importing libraries
import pandas as pd
import glob
import os

#Assessing  the  local environment variable created in the docker file as paths  
input_path = os.environ['INPUT_DIR']
output_path = os.environ['OUTPUT_DIR']

#Defining file name
filename = 'all_years.csv'

#using glob to to retrieve files/pathnames matching a specified pattern with os.path.join() method
#os.path.join: This method concatenates various path components with exactly one directory separator (‘/’) following each non-empty part except the last path component
#os.path.join method returns a string which represents the concatenated path components. 
#glob. glob() method returns a list of files or folders that matches the path specified in the pathname argument. 
csvs = glob.glob(os.path.join(input_path , "*.csv"))

#creating an empty list
li = []

#looping through the list of matching files returned in csvs variable and reading the csv file using pandas and then appending it to the empty li list
for f in csvs:
    df = pd.read_csv(f, index_col=None, header=0)
    li.append(df)

#Concatenating the data frame in the li list ignoring pandas index
df_concat = pd.concat(li,axis=0, ignore_index=True)

#otuputing the concatenating data as a csv file with a specific file name
df_concat.to_csv(output_path+"/"+filename)

#message to print if successful
print("File is created sucessfully!")