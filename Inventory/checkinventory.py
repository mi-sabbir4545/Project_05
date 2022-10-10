stuff = {
    'rope': 30,
    'torch': 10,
    'mobile': 20,
    'sim card': 50,
}


# total number of items: 4
# total quantity : 100

# dict1 = {'a': 1, 'b': 2, 'c': 3}


# def count_keys(stuff):
#     count = 0
#     for i in enumerate(stuff):
#         count += 1
#     return count
#
#
# print(count_keys(stuff))

def display_inventory() :
    #     print("Inventory: " )
    #     items = len(stuff)
    #     print("Total number of items " + str (len(stuff)))

    items_total = 0

    for k, v in stuff.items():
        items_total += v

    print("Total quantity: " + str(items_total))


display_inventory()
