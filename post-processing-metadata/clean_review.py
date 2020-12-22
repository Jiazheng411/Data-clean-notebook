"""change review string to numbers from ./combined_output to ./numerical_output"""

import json 
import csv
import os

reviewed_books = {}

file_arr = os.listdir("./combined_output")

for one_file in file_arr:
    # print(one_file[:4])
    if one_file[:4] == 'part':
        print("processing " + one_file)
        f = open("./combined_output/" + one_file, 'r', encoding='UTF-8')
        output_strings = []
        json_list = f.readlines()
        for json_string in json_list:
            dictionary = json.loads(json_string)
            dictionary['review_number'] = int(dictionary['review_number'])
            dictionary['rating_total'] = float(dictionary['rating_total'])
            dictionary['rating_average'] = float(dictionary['rating_average'])

            # print(dictionary['related'])
            output_strings.append(json.dumps(dictionary, ensure_ascii=False)+"\n")
        output_file = open("./numerical_output/" + one_file, 'w', encoding='UTF-8')
        output_file.writelines(output_strings)
        output_file.close()
        f.close()
