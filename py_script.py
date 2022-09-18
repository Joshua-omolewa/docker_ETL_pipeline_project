#created by Joshua Omolewa

#Importing libraries
import pandas as pd , glob,os

#Assessing  the  local environment variable created in the docker container and store them as paths 
#os.environ method return the vlaue of the environment variable created in the container
input_path = os.environ['INPUT_DIR']
output_path = os.environ['OUTPUT_DIR']

#Defining file name
filename = 'all_years.csv'


"""
using glob to to retrieve files/pathnames matching a specified pattern with os.path.join() method
os.path.join: This method concatenates various path components with exactly one directory separator (‘/’) following each non-empty part except the last path component
os.path.join method returns a string which represents the concatenated path components. 
glob. glob() method returns a list of files or folders that matches the path specified in the pathname argument. 
"""
csvs = glob.glob(os.path.join(input_path , "*.csv"))


#creating an empty list
li = []

"""
looping through the list of matching files returned in csvs variable and reading the csv file using pandas and then appending it to the empty li list
csv file is separated with spaces hence we add \t to use tab as delimiter, header =None is stating csv files do not have headers i.e titles
engine = python is to declare Parser engine to be used
"""
for f in csvs:
    df = pd.read_csv(f, index_col=None, header=None, sep = "\t", engine = "python")
    li.append(df)
    
    
"""
Concatenating the data frames in the li list, axis =0 is to concatenate data frames along the row, 
ignore_index= True is to  prevent the use of  index values along the concatenation axis i.e. exluding the use default pandas axis along the 
row and creating a new axis when combining files. This prevent axis values duplication in pandas frame
"""
df_concat = pd.concat(li,axis=0, ignore_index=True)



"""
ouputing the concatenating data as a csv file with a specific file name, index =false is to  ignore pandas default index when outputting the file 
header=False is to remove pandas default headers
"""
df_concat.to_csv(output_path+"/"+filename, index= False, header=False)


#message to print if script runs successfully
print("File is created sucessfully!")
