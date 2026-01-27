# Your task is to dynamically update the quantity of a supply item after a sale.

# Request as much information from the user in order to know what product is to be sold.

# Print out your inventory after each sale.

# Task 2
# Create a shopping list of supplies that are low in stock (fewer than 10)

# Task 3
# Find which animal type has the most variety. Variety in this case means the animal with the
# most headcount and number of breeds.



petShop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3},
        "birds": {"Parakeet": 4, "Canary": 3, "Cockatiel": 7}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}

# Task 1
purchase = input("what you wanna buy, animal or supplies, input 1 for and 2? ")
if purchase == '1':
    inner_purchase = input('what animal are you buying? ')
    if inner_purchase not in ['dogs', 'cats', 'fish', 'birds']:
        print('oga bye bye')
    else:
        main_purchase = input('what breed? ')
        purchase_count = input(f'how many {main_purchase}? ')
        for key, value in petShop.items():
            for item, detail in value.items():
                for inner, inner_value in detail.items():
                    if key == "animals":
                        if inner == main_purchase:
                            if inner_value >= int(purchase_count):
                                print('sold')
                                detail[inner] -= int(purchase_count)
                                print(petShop)
                            elif inner_value == 0:
                                print('out of stock')
                            else:
                                print(f'we dont have up to that amount we only have {inner_value} amount')
elif purchase == '2':
    inner_purchase = input('what suplies are you buying? ')
    if inner_purchase not in ['food', 'toys', 'habitats']:
        print('oga bye bye')
    else:
        main_purchase = input('what item? ')
        purchase_count = input(f'how many {main_purchase}? ')
        for key, value in petShop.items():
            for item, detail in value.items():
                for inner, inner_value in detail.items():
                    if key == "supplies":
                        if inner == main_purchase:
                            if inner_value >= int(purchase_count):
                                print('sold')
                                detail[inner] -= int(purchase_count)
                                print(petShop)
                            elif inner_value == 0:
                                print('out of stock')
                            else:
                                print(f'we dont have up to that amount we only have {inner_value} amount')





low_stock = {}

for key, value in petShop.items():
    for item, detail in value.items():
        for inner, inner_value in detail.items():
            if key == "supplies":
                if inner_value <= 10:
                    low_stock[inner] = inner_value


print(low_stock)


count = 0

for key, value in petShop.items():
        if key == "animals":
            for item, detail in value.items():
                if len(detail) > count:
                     count = len(detail)
                     answer = item

print(answer)