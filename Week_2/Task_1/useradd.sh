#!/bin/bash

echo "This is a simple script to help you create users with password."


read -p "what is your name?: " name
echo ""

echo "Welcome $name, I will guide you through, all you need to do is follow my instructions.
"
echo "## Provide credentials of	user account to	be created ##"


sudo useradd -m $USER -p $PASS
# Step 1: Adding the desired username
read -p "Enter username: " username

# Step 2: Checking if the user exists
if id "$username" &>/dev/null; 
then
    echo "User '$username' already exists."
else

# Step 3: Adding the user if it doesn't exist
    sudo adduser "$username"
    
# Step 4: Showing User ID, Group ID, and Group
    user_id=$(id -u "$username")
    group_id=$(id -g "$username")
    group=$(id -gn "$username")
    
    echo "User ID: $user_id"
    echo "Group ID: $group_id"
    echo "Group: $group"
fi
