import csv
import json
data_json = []

with open('sample_export.csv', 'r', encoding='utf-8', newline='')  as csvfile:

    reader = csv.reader(csvfile)
    key = 0
    for row in reader:

        key +=1
        result = row[0].split(";")
        try:
            if len(result) < 18:
                for i in range(18- len(result)):
                   result.append('')
            if result[7] == '':
                result[7] = "/img/no-foto.jpg"
            data = {
                "key": str(key),
                "Category": result[0],
                "Manufacturer": result[1],
                "Model": result[2],
                "Manufacturer_Model":  result[3],
                "Name_without_use":  result[4],
                "Product_name":  result[5],
                "Price":  result[6],
                "Image": result[7],
                "OEM":  result[8],
                "Part_code":  result[9],
                "Note":  result[10],
                "Compatibility":  result[11],
                "Substitutions":  result[12],
                "Title_Images":  result[13],
                "Title_page":  result[14],
                "Year":  result[15],
                "Warehouse":  result[16],
                "guide":  result[17],
                }
            data_json.append(data)
        except:
            print('Error', result[1], len(result))
with open('Output.json',  'w', encoding='utf-8') as file:
    json.dump(data_json, file, ensure_ascii=False, indent=4)