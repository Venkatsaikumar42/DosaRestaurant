import json
filename='example_orders.json'
with open(filename,'r') as f:
    orderdata=json.load(f)     
customers=[{order["phone"]:order["name"]} for order in orderdata]
items_info = {}
for order in orderdata:
    for item in order["items"]:
        item_name = item["name"]
        items_info.setdefault(item_name, {"price": item["price"], "orders": 0})
        items_info[item_name]["orders"] +=1

print(customers)
print("-----------\n")
print(items_info)

customer_output_file='customers.json'
items_output_file='items.json'
with open(customer_output_file, 'w') as file:
    json.dump(customers,file,indent=4)
with open(items_output_file, 'w') as file:
    json.dump(items_info,file,indent=4)