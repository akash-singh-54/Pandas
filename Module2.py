# PANDAS — MODULE 2: DATA SELECTION & INDEXING1. 

# Creating a DataFrameWe will use this same dataset across all examples in this module.

import pandas as pd

data = {
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Vikas"],
    "Course": [
        "Python",
        "Data Analytics",
        "Python",
        "Web Development",
        "Data Analytics"
    ],
    "Fees": [15000, 25000, 15000, 18000, 25000],
    "Marks": [80, 90, 75, 85, 95]
}

df = pd.DataFrame(data)
print(df)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Output:    Name           Course   Fees  Marks
# 0   Amit           Python  15000     80
# 1  Priya   Data Analytics  25000     90
# 2  Rahul           Python  15000     75
# 3   Neha  Web Development  18000     85
# 4  Vikas   Data Analytics  25000     95

# In this DataFrame:
# Rows: 5
# Columns: 4
# Index: 0 to 42. 

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selecting a ColumnSelecting Only the Name Column
print(df["Name"])
# This returns a Pandas Series.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Selecting Only the Fees Column
print(df["Fees"])
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Selecting Multiple Columns
print(df[["Name", "Fees"]])
# This returns a Pandas DataFrame.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Remember:
# df["Name"] — returns a Series.
# df[["Name", "Fees"]] — returns a DataFrame.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. What is loc[]?: loc[] is used to select data based on index labels and column labels.
# Syntax:df.loc[row_label, column_label]
# Example 1: Full Row of a Single Student

print(df.loc[1])
# This displays Priya's complete record.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Example 2: Single Column of a Specific Row
print(df.loc[1, "Name"])
# Output:Priya

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Example 3: Course and Fees of a Specific Student
print(df.loc[1, ["Course", "Fees"]])
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Example 4: Multiple Rows
print(df.loc[0:2])
# This includes the rows at index labels 0, 1, and 2.
# Important: In label-based slicing (loc[]), the ending label is inclusive (included in the result).

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 4. What is iloc[]?: iloc[] is used to select data based on integer positions.
# Syntax: df.iloc[row_position, column_position]
# In our DataFrame:
# Column position 0 = Name
# Column position 1 = Course
# Column position 2 = Fees
# Column position 3 = Marks

# Example 1: First Row
print(df.iloc[0])
# This displays Amit's complete record.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Example 2: First Column of the First Row
print(df.iloc[0, 0])
# Output:Amit
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Example 3: First Three Rows
print(df.iloc[0:3])
# This includes positions 0, 1, and 2.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Example 4: First Two Columns Across All Rows
print(df.iloc[:, 0:2])
# Explanation:: 
# — selects all rows.0:2 
# — selects column positions 0 and 1.

# Important: 
# In position-based slicing (iloc[]), the ending position is exclusive (not included in the result).

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Difference Between loc[] and iloc[]
 
# Feature               |    loc[]                                       |  iloc[]
#                       |                                                |
# Basis                 | Index and column labels                        | Integer positions
# Example               | df.loc[1]                                      | df.iloc[1]
# Column Selection      | df.loc[:, "Name"]                              | df.iloc[:, 0]
# Slicing Endpoint      | Inclusive (included in label-based slice)      | Exclusive (not included in position-based slice)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# If a DataFrame has index labels 10, 20, and 30, then 
# df.loc[20] returns the row with label 20, 
# whereas df.iloc[1] returns the second row (at integer position 1).

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Filtering Data Using Conditions
# Fees Greater Than ₹20,000
print(df[df["Fees"] > 20000])
# This returns Priya and Vikas.
# 
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Marks Greater Than 80
print(df[df["Marks"] > 80])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fees Equal to ₹15,000
print(df[df["Fees"] == 15000])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Students in the Python Course
print(df[df["Course"] == "Python"])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Students in the Data Analytics Course
print(df[df["Course"] == "Data Analytics"])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Comparison Operators
# == — Equal to
# != — Not equal to
# >  — Greater than
# <  — Less than
# >= — Greater than or equal to
# <= — Less than or equal to


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 7. Multiple Conditions
# AND (&)
# Filter students whose fees are greater than ₹20,000 and whose marks are 90 or above:

result = df[
    (df["Fees"] > 20000) &
    (df["Marks"] >= 90)
]

print(result)

# This returns Priya and Vikas.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# OR (|)
# Filter students who are in the Python course or whose marks are 90 or above:
result = df[
    (df["Course"] == "Python") |
    (df["Marks"] >= 90)
]

print(result)
# This returns Amit, Priya, Rahul, and Vikas.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# NOT (~)
# Filter students who are not in the Python course:
result = df[
    ~(df["Course"] == "Python")
]

print(result)
# This returns Priya, Neha, and Vikas.

# Note: When combining multiple conditions, always enclose each condition in parentheses ().

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8. Using isin()
# If you want to select students enrolled in either the Python or Data Analytics courses:

result = df[
    df["Course"].isin(["Python", "Data Analytics"])
]

print(result)

# isin() is a convenient way to filter for multiple possible values at once.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 9. Sorting Data with sort_values()
# Marks in Ascending Order
print(df.sort_values("Marks"))

# The lowest marks appear first.
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Marks in Descending Order
print(df.sort_values("Marks", ascending=False))
# The highest marks appear first.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fees in Descending Order
print(df.sort_values("Fees", ascending=False))

# ascending=False sorts the data from highest to lowest (descending order).
