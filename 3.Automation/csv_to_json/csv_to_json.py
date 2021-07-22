'''

- This script is to convert csv format into json format, which is used in API.
- It also supports Myanmar font(Unicode) in CSV file.
- In this script, mmCOVID-Services.csv(from) is used as sample.
- You can use another CSV file.
  
'''


# importing modules
import csv 
import json 


def csv_to_json(csvFilePath, jsonFilePath):
    # initialize json array list
    jsonArray = []
      
    # read csv file
    with open(csvFilePath, encoding='utf8') as csvf: 
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        # convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            row = {'name':row['name'],
                    'name_mm':row['name_mm'],
                    'phone1':row['phone1']
            }
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)
          
csvFilePath = r'mmCOVID-Services.csv'
jsonFilePath = r'mmCOVID-Services.json'
csv_to_json(csvFilePath, jsonFilePath)


    