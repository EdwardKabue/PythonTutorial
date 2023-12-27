import csv

# with open("names.csv", "r") as csv_file:
#     csv_reader = csv.reader(csv_file) #get csv reader object

#     #next(csv_reader) #skip the first item in the iterator
#     with open("new_names.csv", "w") as new_csv_file:
#         csv_writer = csv.writer(new_csv_file, delimiter="\t")

#         #loop through the csv reader object
#         for line in csv_reader:
#             #print(line[2]) #line is a list of row field values
#             csv_writer.writerow(line) #write to new file using line from original file.

#use dictionary reader and writer
with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file) #get csv dictionary reader object

    with open("new_names.csv", "w") as new_csv_file:
        #field_names = ["first_name","last_name","email"] #specify the field names for the writer
        field_names = ["first_name","last_name"] #specify the field names for the writer
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=field_names, delimiter="\t")
        csv_writer.writeheader() #ensure the header is written based on the field names provided.

        for line in csv_reader:
            #print(line["email"]) #line is a dictionary
            del line["email"] #remove the email values
            csv_writer.writerow(line) #write to new file using line from original file.