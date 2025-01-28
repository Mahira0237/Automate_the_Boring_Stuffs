def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k in inventory.keys():
            inventory[k]+=1
        else:
            inventory.setdefault(str(k),1)
    return inventory
   
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total=item_total + inventory.get(k,0)
        print(str(v)  + ' ' + k) 
    print() 
    print("Total number of items: " + str(item_total))

displayInventory(inv)

