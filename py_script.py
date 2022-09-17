import pandas as pd
import glob
import os

# ########### path to store input data extracted by year_wise_data function ############
# INPUT_FOLDER= os.system(`$(cd "$( dirname "${BASH_SOURCE:-$0}" )" && cd ../INPUT && pwd)`)


# ########### path to store output data extracted by year_wise_data function ############
# OUTPUT_FOLDER= os.system(`$(cd "$( dirname "${BASH_SOURCE:-$0}" )" && cd ../OUTPUT && pwd)`)

input_path = os.environ['INPUT_DIR']
output_path = os.environ['OUTPUT_DIR']
filename = 'all_years.csv'
csvs = glob.glob(os.path.join(input_path , "*.csv"))


li = []
for f in csvs:
    df = pd.read_csv(f, index_col=None, header=0)
    li.append(df)

df_concat = pd.concat(li,axis=0, ignore_index=True)

df_concat.to_csv(output_path+"/"+filename)

print("File is created sucessfully!")