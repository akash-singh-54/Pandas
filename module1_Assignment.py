import pandas as pd



# #-------------------------------------------------------------------------------------------------------------------------------------
# # Create a Python list of 5 fruits.

fruits = ["Apple", "Banana", "Peach", "Berry",  "Mango" ]
print(fruits)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Convert that list into a Pandas Series.

f = pd.Series(fruits)
print(f)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Create a Series of marks for 5 students.

marks = pd.Series([88,29,39,47,77])
print(marks)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Create a Series using "Amit", "Priya", and "Rahul" as the index.

marks = [88,29,39]
s1= pd.Series(
    marks,
    index=["Amit", "Priya", "Rahul"]
)
print(s1)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Extract Priya's marks from the Series.

print("Priya's marks =",s1["Priya"])
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Create a DataFrame containing the Name and Marks of three students.

data = {
    "Name" : ["Akash", "Alok", "Aman"],
    "Marks": [89,88,80]
    
}
d = pd.DataFrame(
    data,
    index= [1,2,3]
    )
print(d)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Create a DataFrame for five students with Name, Course, and Fees.

data = {
    "Name" : ["Aman" , "Brain" , "Calvin", "Dango D. Fanc", "Elva"],
    "Course" : ["App Dev" , "Python" , "Web Dev", "Data Analytics", "Java"],
    "Fees" : [15000, 10000, 20000, 30000, 25000]
}
d = pd.DataFrame(
    data,
    index= [1,2,3,4,5]
)
print(d)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Display the first 2 rows of the DataFrame.

print(d.head(2))
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Display the last 3 rows of the DataFrame.

print(d.tail(3))
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Find the shape of the DataFrame.

print(d.shape)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Display all column names.

print(d.columns)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # View the data types of all columns.

print(d.dtypes)
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Extract the DataFrame's information using info().

print(d.info())
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Generate the numerical summary using describe().

print(d.describe())
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Select only the Name column from the DataFrame.

print(d["Name"])
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Select only the Fees column from the DataFrame.

print(d["Fees"])
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Select both the Name and Course columns from the DataFrame.

print(d[["Name", "Fees"]])
print("\n")

# #-------------------------------------------------------------------------------------------------------------------------------------
# # Create a DataFrame of 5 products of your choice with Product Name, Price, and Quantity.

data = {
    "Product Name" : ["iPhone", "Dell G15", "TUF", "Nokia", "IQOO"],
    "Price" : [70999, 80000, 120000, 30000, 55000]
    ,"Quantity" : [1, 1, 2, 3, 2] 
}
d = pd.DataFrame(data)
print (d)