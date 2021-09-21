shop = { "vegetables": {"potato": {"price": 25,
                                   "amount": 40},
                        "mushrooms": {"price": 20,
                                      "amount": 60}},
        "fruits": {"melon": {"price": 45,
                            "amount": 30},
                   "watermelon": {"price": 40,
                                    "amount": 35}},
        "bread": {"black bread": {"price": 15,
                                   "amount": 18},
                    "white bread": {"price": 10,
                                      "amount": 20}},
        "meat": {"duck": {"price": 68,
                           "amount": 5},
                 "turkey": {"price": 75,
                            "amount": 6}},
        "alcohol": {"beer": {"price": 38,
                             "amount": 20},
                    "vine": {"price": 95,
                              "amount": 10}}}

# def price_amount():
#     category = input('Choose category')
#     print(shop[category])
#
# price_amount()

# def add_new():
#     p = input("Please input a product: ")
#     v = input("Plesse input a value: ")
#     new_product = {p: v}
#     shop.update(new_product)
#     print(shop)
# add_new()

def sale():
    while True:
        p = input("your product")
        if p == "potato":
            shop["vegetables"]["potato"]["price"] *= 0.8
            print(shop["vegetables"]["potato"]["price"])
        elif p == "mushrooms":
            shop["vegetables"]["mushrooms"]["price"] *= 0.7
            print(shop["vegetables"]["potato"]["price"])
        elif p == "alcohol":
            shop["alcohol"]["beer"]["price"] *= 0.9
            shop["alcohol"]["vine"]["price"] *= 0.9
            print(shop["alcohol"]["beer"]["price"], shop["alcohol"]["vine"]["price"])
            break
sale()