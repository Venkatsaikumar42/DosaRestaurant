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