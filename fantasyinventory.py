inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(inventory):
    print('Inventory')
    for item in inventory.items():
        print(item[1], item[0])
    print("Total items:", sum(item[1] for item in inventory.items()))


display_inventory(inventory)
print("\n\n\n")


def add_loot(inventory, items):
    loot_dict = {}
    for x in items:
        loot_dict[x] = dragonLoot.count(x)
    new_inventory = {**inventory, **loot_dict}
    for k, v in new_inventory.items():
        if k in inventory and k in loot_dict:
            new_inventory[k] = loot_dict[k] + inventory[k]
    display_inventory(new_inventory)


# loot_dict = {}

# # print(x)

# print(loot_dict)
add_loot(inventory, dragonLoot)
