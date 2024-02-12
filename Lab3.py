def write_text_file_with_name(your_name):
file_name = "my_name.txt"
# Open the file in write mode
with open(file_name, 'w') as file:
    # Write your name to the file
    file.write("My name is: " + your_name)

# Call the function with your name
your_name = "Your Name"  
write_text_file_with_name(your_name)
