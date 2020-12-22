"""process data in ./original_data dir, save to ./output"""

import json
import os
file_arr = os.listdir("./original_data")

def strip_string(string):
    return string.strip('\n')

book_list_file = open("./all_books", 'r', encoding='UTF-8')
book_list = book_list_file.readlines()

book_list = map(lambda x: x.strip("\n"), book_list)
book_list = set(x.strip("\n") for x in book_list)



# clean
for one_file in file_arr:
    if one_file[:4] == 'part':
        print("processing " + one_file)
        f = open("./original_data/" + one_file, 'r', encoding='UTF-8')
        output_strings = []
        json_list = f.readlines()
        for json_string in json_list:
            dictionary = json.loads(json_string)
            try:
                dictionary['price'] = -1 if dictionary['price'] == '' or dictionary['price'] == '[]' else float(dictionary['price'])
            except Exception as e:
                dictionary['price'] = -1
                print(e)
                print("================ranking error==================")

            try:
                dictionary['rank'] = -1 if dictionary['rank'] == '' or dictionary['rank'] == '[]' else int(dictionary['rank'])
            except:
                dictionary['rank'] = -1   
                print("================ranking error==================") 
            
            try:
                related_list = [] if dictionary['related'] == "" or dictionary['related'] == "[]" else dictionary['related'].strip("[]").split(',')
                dictionary['related'] = [x for x in related_list if x in book_list ]
            except:
                dictionary['related'] = []
                print("=================related error=============== ") 

                print(dictionary['related'])
            output_strings.append(json.dumps(dictionary, ensure_ascii=False)+"\n")
        output_file = open("./output/" + one_file, 'w', encoding='UTF-8')
        output_file.writelines(output_strings)
        output_file.close()
        f.close()



