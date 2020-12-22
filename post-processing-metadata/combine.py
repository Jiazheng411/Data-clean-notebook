"""combine review and book metadata information from ./output, save to ./combined_output"""

import json 
import csv
import os

reviewed_books = {}

with open('book_review_stats.csv', newline='') as csvfile:
    csvlines = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in csvlines:
        # print(row)
        # print(row[0].strip("\"") , row[1].strip("\"") , row[2].strip("\""))
        reviewed_books[row[0].strip("\"")] = [row[1].strip("\""), row[2].strip("\""), row[3].strip("\"") ]
# print(reviewed_books)

file_arr = os.listdir("./output")

book_with_review_number = 0

for one_file in file_arr:
    # print(one_file[:4])
    if one_file[:4] == 'part':
        print("processing " + one_file)
        f = open("./output/" + one_file, 'r', encoding='UTF-8')
        output_strings = []
        json_list = f.readlines()
        for json_string in json_list:
            dictionary = json.loads(json_string)
            # print(dictionary['asin'])
            if dictionary['asin'] in reviewed_books:
                book_with_review_number += 1
                dictionary['review_number'] = reviewed_books[dictionary['asin']][0]
                dictionary['rating_average'] = reviewed_books[dictionary['asin']][1]
                dictionary['rating_total'] = reviewed_books[dictionary['asin']][2]
            else:
                dictionary['review_number'] = 0
                dictionary['rating_average'] = 0
                dictionary['rating_total'] = 0

            # print(dictionary['related'])
            output_strings.append(json.dumps(dictionary, ensure_ascii=False)+"\n")
        output_file = open("./combined_output/" + one_file, 'w', encoding='UTF-8')
        output_file.writelines(output_strings)
        output_file.close()
        f.close()

print("with review = " + str(book_with_review_number))
