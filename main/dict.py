

fridge = {'water_bottle': 2, 'yoghurt': 3}

#METHOD .get
#Method get prevent error message if key doesn't exist. Instead of error the result we get default value set by us, in this example it's 0.

print('Inside fridge there is ' + str(fridge.get('water_bottle',0)))


print('Inside fridge there is ' + str(fridge.get('milk',0)))

#Without get gives error - uncomment to check
# print('Inside fridge there is ' + str(fridge['milk']))

#METHOD .setdefault
# Check if item exist in warehouse, if it's exist add value of items from delivery, if it's not
market_warehouse = {'tables':5,'garden_rocker':2, 'sunflower':10}

item_name = input('Please input your item name: ')

if item_name in market_warehouse:
    print(f"There is {market_warehouse[item_name]} {item_name} in warehouse")
    new_item_value = int(input('Number of pieces in delivery? '))
    market_warehouse[item_name] += new_item_value
else:
    market_warehouse.setdefault(item_name, 0)
    new_item_value = int(input('Number of pieces in delivery? '))
    market_warehouse[item_name] = new_item_value

print(market_warehouse)

for k in market_warehouse.values():
    print(v)