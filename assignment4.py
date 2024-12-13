def read_and_modify_file():
    """
    Reads a file specified by the user, modifies its content, and writes the modified
    content to a new file. Handles errors for file reading and writing.
    """
    try:
        input_filename = input("Enter the filename to read: ")
        with open(input_filename, 'r') as infile:
            content = infile.read()
            
        # Modify the content (e.g., convert to uppercase for demonstration)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to {output_filename}")
    except FileNotFoundError:
        print("Error: The specified file does not exist.")
    except IOError:
        print("Error: An error occurred while reading or writing the file.")

# Run the file read & write challenge
read_and_modify_file()