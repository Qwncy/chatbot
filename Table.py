from prettytable import PrettyTable
 
# Specify the Column Names while initializing the Table
myTable = PrettyTable([" ", "List" , "Array" , "Tuple"])

# Add rows
myTable.add_row(["is it mutable?" , "yes" , "Yes" , "no"])
myTable.add_row(["Can we change the size after creation?" , "Yes" , "No" , "No"])
myTable.add_row(["Can items in the list be changed?" , "Yes" , "Yes" , "No"])
myTable.add_row(["How many different data types can be stored?" , "4" , "similar data types" , "multiple data types"])

print(myTable)
