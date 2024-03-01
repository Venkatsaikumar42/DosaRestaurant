import json 
import os

file_path='example_orders.json'


with open(file_path, 'r') as file:
    orders = json.load(file)
print(orders)
# for order in orders[:1]:
#     name = order['name']
#     phone = order['phone']
#     print(name)
#     print(phone)
#     print(order['items'])
# #     print(f"Name extracted from order: {name}")
# #     print(f"phone Number extracted from order: {phone}")
# #     # checkphone=is_valid_phone_number(phone)
# #     # print(checkphone)
# #     add_customer(phone,name)
#     items = order['items']
#     for item in items:
#         print(item)    
#         itemname=item['name'] if 'name' in item else ''
#         itemprice=item['price'] if 'name' in item else ''
#         print(f"ItemName extracted from order: {itemname}")
#         print(f"ItemPrice extracted from order: {itemprice}")
# #         add_items(itemname,itemprice)