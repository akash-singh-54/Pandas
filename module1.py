import pandas as pd 

# PANDAS — MODULE 1: INTRODUCTION TO PANDAS


# 1. What is Pandas?
# Pandas is a Python library used to read, organize, clean, manipulate, and analyze data.
# For example, if you need to manage student data at CodeDesk—such as 
# Name, Course, and Fees — you can easily analyze it using Pandas.
# Main Uses of Pandas:
# Organizing data into rows and columns.
# Reading CSV and Excel files.
# Handling missing values.
# Removing duplicate data.
# Filtering and sorting data.
# Analyzing data.
# Preparing data for reports and visualizations.

 
# 2. How to Install Pandas?
# Run this command in your Terminal or Command Prompt:
# pip install pandas

# In a Jupyter Notebook:
# %pip install pandas
# Note: You generally only need to install Pandas once.


# 3. How to Import Pandas?
# Python: import pandas as pd
# print(pd.__version__)

# Explanation:import 
# — Used to include the library in your program.pandas 
# — The name of the library.as pd
# — Gives Pandas the short alias pd.pd.__version__ 
# — Displays the installed version of Pandas.Using the alias pd in Pandas examples is standard practice.

# 4. What is a Pandas Series?
# A Series is a one-dimensional labeled data structure. 
# In simple terms, it contains values along with an index.
# Example 1: Python List Python 

marks = [80, 75, 90, 85, 70]

print(marks)
# Output:Plaintext[80, 75, 90, 85, 70]

# Example 2: Pandas SeriesPythonimport pandas as pd

marks = [80, 75, 90, 85, 70]

s1 = pd.Series(marks)

print(s1)
# Output:Plaintext
# 0    80
# 1    75
# 2    90
# 3    85
# 4    70
# dtype: int64
# Explanation:0, 1, 2, 3, 4 — Index.
# 80, 75, 90, 85, 70 — Values.
# int64 — The data type of the integer values.
# By default, index numbering starts from 0.

# Example 3: Series with a Custom Index 

marks = [80, 75, 90]

s1 = pd.Series(
    marks,
    index=["Amit", "Priya", "Rahul"]
)

print(s1)
# Output:PlaintextAmit     80
# Priya    75
# Rahul    90
# dtype: int64

# Example 4: Extracting a Value Using an Index
print(s1["Priya"])
# Output:    75
# Here, "Priya" is the index label, and its corresponding value is 75.


# 5. What is a DataFrame?
# A DataFrame is a two-dimensional labeled data structure in Pandas. 
# It consists of rows and columns, and you can think of it like an Excel table.
# 
# Example:
# Name         Course               Fees
# Amit         Python               15000
# Priya        Data Analytics       25000
# Rahul        Python               15000
# Neha         Web Development      18000
# Vikas        Data Analytics       25000
# In this table:
# Rows: 5
# Columns: 3
# Name: Names of the students.
# Course: The student's course.
# Fees: Course fees.


# Example: Creating a DataFrame

data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Vikas"],
    "Course": [
        "Python",
        "Data Analytics",
        "Python",
        "Web Development",
        "Data Analytics"
    ],
    "Fees": [15000, 25000, 15000, 18000, 25000]
}

df = pd.DataFrame(data)

print(df)

# Output:Plaintext    Name           Course   Fees
# 0   Amit           Python  15000
# 1  Priya   Data Analytics  25000
# 2  Rahul           Python  15000
# 3   Neha  Web Development  18000
# 4  Vikas   Data Analytics  25000

# Explanation: data is a Python dictionary.
# The dictionary keys become the column names of the DataFrame.
# The list associated with each key provides the values for that column.
pd.DataFrame(data) 
# converts the dictionary into a DataFrame.
# The entire DataFrame is stored in the variable df.
# Note: When creating a DataFrame from a dictionary, 
# the lists for all columns must contain the exact same number of values.


# 6. Basic Information of a DataFrameUse the df created above for all the examples below.
# 6.1 Viewing the First 5 Rows — head()

print(df.head())
# This displays the first 5 rows of the DataFrame. 

# If there are fewer than 5 rows, it will display all available rows.

# 6.2 Viewing the First 3 Rows 
print(df.head(3))
# This displays the first 3 rows.

# 6.3 Viewing the Last 5 Rows — tail()

print(df.tail())
# This displays the last 5 rows.

# 6.4 Number of Rows and Columns — shape
print(df.shape)
# Output:Plaintext(5, 3)
# Explanation:5 — Number of rows.3 — Number of columns.
# Note: shape is a property (attribute), so do not write it with parentheses as df.shape().

# 6.5 Viewing Column Name
print(df.columns)
# This displays all column labels, such as Name, Course, and Fees.

# 6.6 Viewing Data Types
print(df.dtypes)
# This reveals the data type of each column.
# Example:
# Name — object or string dtype (depending on the Pandas version and data).
# Course — object or string dtype.
# Fees — int64.

# 6.7 Complete Information of the DataFrame — info()
df.info()
# This displays:
# Total number of rows.
# Total number of columns.
# Column names.
# Number of non-null values.
# Data type of each column.
# Memory usage information.
# info() usually displays the information directly; 
# you do not need to wrap it in a print() statement.

# 6.8 Numerical Summary — describe()
print(df.describe())
# This provides a statistical summary of numerical columns, including:
# count — Number of non-missing numerical values.
# mean — Average.
# std — Standard deviation.
# min — Minimum value.
# 25% — First quartile.
# 50% — Median.
# 75% — Third quartile.
# max — Maximum value.
# In this dataset, it will mainly provide a summary for the Fees column.


# 7. Selecting a Specific ColumnOnly the Name Column:
print(df["Name"])
# This returns a single Pandas Series.
# Only the Fees Column:
print(df["Fees"])
# Selecting Two Columns:
print(df[["Name", "Fees"]])
# Here, double square brackets are used because:
# The outer [] is for selecting from the DataFrame.
# The inner [] is a list of the column names to be selected.

# 8. Pandas Module 1 — Quick Revision Concept Code

# Import Pandas - import pandas as pd 
# Pandas version - pd.__version__ 
# Create a Series - pd.Series([10, 20, 30])
# Create a DataFrame - pd.DataFrame(data)
# First 5 rows - df.head()
# First 3 rows - df.head(3)
# Last 5 rows - df.tail()
# Rows and columns - df.shape
# Column names - df.columns
# Data types - df.dtypes
# DataFrame information - df.info()
# Numerical summary - df.describe()
# Single column - df["Name"]
# Multiple columns - df[["Name", "Fees"]]