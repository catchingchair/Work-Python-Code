# open a file for writing and create it if it does not exist
# sample_file = open("textfile.txt", "w+")
# sample_file.write("This is somesample text in our sample file.\nWhat else should we have here?")
# sample_file.close()

# append some more text to the file 
# sample_file = open("textfile.txt","a+")
# sample_file.write("Lets add some more text at the bottom...")
# sample_file.close()

# open the file and read the contents
sample_file = open("textfile.txt","r")

if sample_file.mode == 'r':
    # use the read() function to read the entire file
    contents = sample_file.read()
    print(contents)

    # same result, just reads line by line and printing it. 
    # .readlines() returns a list of lines from the stream
    file_lines = sample_file.readlines()
    for line in file_lines:
        print(line)