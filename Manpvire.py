#!/user/bin/python3


# Initialize a counter variable to keep track of the number of lines containing "vampire"
counter = 0

# Open the input file in read mode and the output file in write mode
with open("dracula.txt","r") as foo, open("Vapula.txt","w") as fang:

    # Iterate over each line in the input file
    for line in foo:

        # Check if the lowercase version of the line contains the word "vampire"
        if "vampire" in line.lower():

            # Print the line to the console
            print(line)

            # Increment the counter variable by 1
            counter += 1

            # Write the line to the output file
            fang.write(line)

# Print the total number of lines containing "vampire" to the console
print(f"Found {counter} lines containing 'vampire' in the input file.")
