#use context manager to handle file closure and clean up automatically.
with open("test.txt", "r") as f:
    # f_contents = f.readlines() #get all the lines in a list
    # print(type(f_contents))
    # f_contents = f.readline() #get a single line starting with the first line
    # print(f_contents, end='')

    #iterate through each line. Efficient since it reads lines one at a time.
    # for line in f:
    #     print(line, end='')

    #f_contents = f.read() #get all the lines in a string.
    # f_contents = f.read(100) #get first 100 characters in the string.
    # print(f_contents, end='')

    # f_contents = f.read(100) #get the next 100 characters in the string.
    # print(f_contents, end='')

    # size_to_read = 100

    # #loop through the file in chunks.
    # f_contents = f.read(size_to_read)

    # while len(f_contents) > 0:
    #     print(f_contents, end='')
    #     f_contents = f.read(100)

    #use the seek method
    # size_to_read = 20
    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # f.seek(0) #go back to the beginning of the file and read 20 characters
    # f_contents = f.read(size_to_read)
    # print(f_contents)
    pass


#write to file. If file does not exist, it is created. If file exists, it is overwritten.
# with open("test2.txt", "w") as f:
#     f.write("Test")
#     #f.write("Test") #Subsequent calls to write writes from the end of the last written string.
#     f.seek(0) #Make the next write start from the beginning of the file.
#     f.write("R")

#Copy one file to another.
# with open("test.txt", "r") as rf:
#     with open("test_copy.txt", "w") as wf:
#         for line in rf:
#             wf.write(line)

#Copy binary file (e.g. image) to another
# with open("photo-1516117172878-fd2c41f4a759", "rb") as rf:
#     with open("hills_copy.jpg", "wb") as wf:
#         for line in rf:
#             wf.write(line)


#Copy binary file (e.g. image) to another in chunks
with open("photo-1516117172878-fd2c41f4a759", "rb") as rf:
    with open("hills_copy.jpg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)

        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)