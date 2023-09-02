# Using AWS Boto3 library - Create, add item and Delete DynamoDB table
## Task
* step 1; Create a DynamoDB table
* step 2; Add items to the table
* step 3; Query the table 
* step 4; Remove an item
* step 5; Delete the table

## Solution
I created a python function for each step to ensure flexibility and reusability of code. This code can be used to add items to table independently by calling only the add_item function.

1. Create a DynamoDB table
I created DynamoDB table named "StudentRecords" with the following specifications:
Table Name: StudentRecords
Primary Key: student_id (Number)
Provisioned Throughput: Read Capacity Units = 5, Write Capacity Units = 5
```
create_dynamodb_table(table_name)
```
2. Add items to the table
I added the following student records to the "StudentRecords" table:

{'Student_ID': 101, 'Student_Name': "Alice", 'Age': 20, 'Class': "Mathematics"},
{'Student_ID': 102, 'Student_Name': "Bob", 'Age': 22, 'Class': "Physics"},
{'Student_ID': 103, 'Student_Name': "Charlie", 'Age': 19, 'Class': "Biology"},
```
add_items_to_table(table_name, items)
```
3. Query the Table:
I queried the table for an item with Student_ID: 101 by passing the table name and Student_ID into my query function.

```
student_id= 101
query_table(table_name, student_id)
```

4. Remove an item
I removed an item with Student_ID: 103
```
student_id= 103
remove_item_from_table(table_name, student_id)
```

5. Delete the Table:
I deleted the table by calling the delete function 
```
delete_dynamodb_table(table_name)
```
