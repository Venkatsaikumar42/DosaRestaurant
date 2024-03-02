import json
import argparse
parser = argparse.ArgumentParser(description='Provide the Json File name')
parser.add_argument('filename', type=str, help='Provide the filename containing json objects')
args = parser.parse_args()
filename=args.filename
with open(filename,'r') as f:
    orderdata=json.load(f)     
items_info = {}
customerdata={}
for order in orderdata:
    customerdata[order['phone']]=order['name']
    for item in order["items"]:
        item_name = item["name"]
        items_info.setdefault(item_name, {"price": item["price"], "orders": 0})
        items_info[item_name]["orders"] +=1

print("-----------\n")
print(items_info)

customer_output_file='customers.json'
items_output_file='items.json'
with open(customer_output_file, 'w') as file:
    json.dump(customerdata,file,indent=4)
with open(items_output_file, 'w') as file:
    json.dump(items_info,file,indent=4)