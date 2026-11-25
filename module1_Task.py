# Today's Practical Task
# Create a dataset of 5 students for CodeDesk. Include these columns:
# Student_ID
# Name
# Course
# Fees
# Marks

import pandas as pd
dataset = {
    
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110 ],
    "Name" : ["Aarav Sharma", "Ananya Verma", "Rohan Patel", "Diya Nair", "Kabir Gupta",
    "Ishita Joshi", "Aditya Iyer", "Meera Reddy", "Vikram Singh", "Sneha Chatterjee"],
    "Course": ["Python", "Data Analytics", "Web Development", "Graphic Design", "Machine Learning",
        "Python", "Data Analytics", "UI/UX Design", "Web Development", "Cyber Security"],
    "Fees": [15000, 25000, 18000, 20000, 30000, 15000, 25000, 22000, 18000, 28000],
    "Marks": [88, 92, 79, 95, 84, 76, 89, 91, 73, 86]
}

# Create the DataFrame.
data = pd.DataFrame(dataset)

# Display the entire DataFrame.
print(data)

# Show the first 3 rows.
print(data.head(3))

# Check the shape, columns, and dtypes.
print(data.shape)
print(data.columns)
print(data.dtypes)

# Select only the Name and Fees columns.
print(data[["Name" , "Fees"]])

# View the summary of the numerical columns using describe().
print(data.describe())

