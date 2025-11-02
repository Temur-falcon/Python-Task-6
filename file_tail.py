# tail_in_IDE.py
# Program to display the last 10 lines of a text file

# Step 1: Ask user for filename
filename = input("Enter the name of the file: ")

try:
    # Step 2: Open the file
    file = open(filename, "r")

    # Step 3: Read all lines into a list
    lines = file.readlines()

    # Step 4: If file has more than 10 lines, keep only the last 10
    if len(lines) > 10:
        lines = lines[-10:]

    # Step 5: Print each line
    print("\nLast 10 lines of the file:\n")
    for line in lines:
        print(line.strip())

    # Step 6: Close the file
    file.close()

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except Exception as e:
    print("Something went wrong:", e)

#Didn't use command line argument , since in my IDE I wasn't able to run the code using it
