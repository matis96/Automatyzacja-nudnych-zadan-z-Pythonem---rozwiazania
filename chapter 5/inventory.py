# inventory.py
stuff = {'lina': 1, 'pochodnia': 6, 'złote monety': 42, 'sztylet': 1, 'strzał': 12}
dragonLoot = ['złote monety', 'sztylet', 'złote monety', 'złote monety', 'rubin']
def displayInventory(inventory):
    print("Inwentarz:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' +k)
        item_total += v
    print("Całkowita liczba pzredmiotów: " +str(item_total))

def addToInventory(inventory, addedItems):
    for items in addedItems:
        inventory.setdefault(items, 0)
        inventory[items] = inventory[items] + 1
    return inventory
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
