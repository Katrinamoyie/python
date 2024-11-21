# file1 = open("ass.txt", "r")
# print(file1.read())
# File1= open("ass.txt", "a")
# file1.write("\n This assignment was fun")


filename = input("assignment.txt")

try:
    
    with open(filename, "r") as file:
        # Read the contents of the file and print them
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except PermissionError:
    print(f"Permission denied to read the file '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")

# Attempt to append to the file if no exceptions were raised
try:
    with open(filename, "a") as file:
        file.write("\n This assignment was fun")
        print("Content appended successfully.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

