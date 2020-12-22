"""find all categories from original_data dir, save to catogory_count"""

import json
import os

file_arr = os.listdir("./original_data")

categories_dict = {}
category_set = set()
for one_file in file_arr:
    # print(one_file[:4])
    if one_file[:4] == 'part':
        print("processing " + one_file)
        f = open("./original_data/" + one_file, 'r', encoding='UTF-8')
        json_list = f.readlines()
        for json_string in json_list:
            dictionary = json.loads(json_string)
            category = dictionary['category']
            categories_dict[category] = 1 if categories_dict.get(category) is None else categories_dict[category] + 1
    f.close()
    
output_file = open("./catogory_count", 'w', encoding='UTF-8')
print(categories_dict)
for (key, value) in categories_dict.items():
    output_string = json.dumps({"category": key, "book_count": value}, ensure_ascii=False) + "\n"
    output_file.write(output_string)
output_file.close()
      

