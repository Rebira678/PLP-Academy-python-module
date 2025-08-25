"""
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
"""
"""
answer
"""
try:
    # Ask user for input file name
    filename = input("Enter the name of the file to read: ").strip()
    
    # Open and read the file
    with open(filename, "r") as infile:
        content = infile.read()
    
    # Modify content (example: convert to uppercase)
    modified_content = content.upper()
    
    # Ask for new file name
    new_filename = input("Enter the name of the new file to write: ").strip()
    
    # Write modified content to new file
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)
    
    print(f" Success! The modified content has been written to '{new_filename}'.")
    
except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read or write this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
