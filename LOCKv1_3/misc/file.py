import os

def file_exists(filename):
    try:
        with open(filename, 'r'):
            return True
    except OSError:
        return False

def create_file(filename):
    try:

        with open(filename, "w") as f:
            f.write("")
        print("File '{}' created successfully.".format(filename))
        
    except OSError as e:
        
        print("Failed to create file: {}".format(e))

def read_file(file_path):

    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except OSError:
        print(f"Error: Unable to read file '{file_path}'")
        return ""

def write_to_file(filename, content):
    try:

        with open(filename, "a") as f:
            f.write(content)
            
        print("Content written to '{}' successfully.".format(filename))
        
    except OSError as e:
        
        print("Failed to write to file: {}".format(e))

def clear_file(file_name):
    
    with open(file_name, 'w') as file:
        pass