#!/bin/bash

# Step 1: Path to the log file
read -p "Enter the path to the log file: " log_file

# Step 2: Path to the output file
read -p "Enter the path to the output file: " output_file

# Step 3: Pattern to search for in the log file
search_pattern="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"  #search pattern for ip address

# Step 4: Parse the log file and forward the result to the output file
grep -oP "$search_pattern" "$log_file" > "$output_file"

echo "Search results have been saved to '$output_file'."