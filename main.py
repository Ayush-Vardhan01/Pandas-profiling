import pandas as pd
from pandas_profiling import ProfileReport

# Load the dataset
df = pd.read_csv('train.csv')

# Generate the profiling report
prof = ProfileReport(df)
prof.to_file(output_file='output.html')
