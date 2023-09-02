import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table_name='StudentRecords'      # declares name of Table

# Step 1: Create a DynamoDB Table

def create_dynamodb_table(table_name):
    table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
       {
            'AttributeName': 'Student_ID',
            'KeyType': 'HASH'  # Partition key
        }  
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Student_ID',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
    )

    print("creating table......")
    table.wait_until_exists()
    print(f"Table '{table_name}' created successfully.")
# calls function that creates table
create_dynamodb_table(table_name)

# Step 2: Add Items to the Table
def add_items_to_table(table_name, items):
    table = dynamodb.Table(table_name)
    for item in items:
        table.put_item(Item=item)
    
    print(f"Added {len(items)} items to the table.")

# records of students to be added to the table
items=[
{'Student_ID': 101, 'Student_Name': "Alice", 'Age': 20, 'Class': "Mathematics"},
{'Student_ID': 102, 'Student_Name': "Bob", 'Age': 22, 'Class': "Physics"},
{'Student_ID': 103, 'Student_Name': "Charlie", 'Age': 19, 'Class': "Biology"},
]

# calls function to add above items to table
add_items_to_table(table_name, items)

# Step 3: Query the Table
def query_table(table_name, student_id):
    table = dynamodb.Table(table_name)
    
    response = table.get_item(
        Key={'Student_ID': student_id}
    )
    
    item = response['Item']

    print(f"Query result for Student ID {student_id}: {item}")

# Queries item with student_id '101'
student_id= 101
query_table(table_name, student_id)

# Step 4: Remove an Item
def remove_item_from_table(table_name, student_id):
    table = dynamodb.Table(table_name)
    
    table.delete_item(
        Key={'Student_ID': student_id}
    )
    
    print(f"Removed item with Student _ID: {student_id} from the table.")

# Deletes item with student_id '103'
student_id= 103
remove_item_from_table(table_name, student_id)

# Step 5: Delete the Table

def delete_dynamodb_table(table_name):
    
    table = dynamodb.Table(table_name)
    table.delete()
    print(f"Table '{table_name}' deleted successfully.")

# calls function to delete table
delete_dynamodb_table(table_name)

