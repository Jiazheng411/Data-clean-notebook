"""get all asins from original_data dir, output to ./all_books"""

import json
import os
file_arr = os.listdir("./original_data")

# get asin
import os
file_arr = os.listdir()
# print(file_arr)

output = open('./all_books', 'w', encoding='UTF-8')

for one_file in file_arr:
    print(one_file[:4])
    if one_file[:4] == 'part':
        print("processing file " + one_file)
        f = open(one_file, 'r', encoding='UTF-8')
        json_list = f.readlines()
        for json_string in json_list:
            asin = json.loads(json_string)['asin']
            # print(asin + "\n")
            output.write(asin + "\n")
