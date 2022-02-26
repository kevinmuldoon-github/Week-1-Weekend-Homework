# Kevin's Pet Shop :)

# 1. Function to find pet shop name
def get_pet_shop_name(pet_shop): 
    what_pet_shop = pet_shop["name"]
    return what_pet_shop

# 2. Function to determine total cash
def get_total_cash(pet_shop):
    tot_cash = pet_shop["admin"]["total_cash"]
    return tot_cash

# 3. Function to add or remove cash from total cash
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

# 4. Function to find number of pets sold
def get_pets_sold(pet_shop):
    pets_sold = pet_shop["admin"]["pets_sold"]
    return pets_sold

# 5. Function to increase the number of pets sold
def increase_pets_sold(pet_shop, increase):
    pet_shop["admin"]["pets_sold"] += + increase

# 6. Function to retrieve stock count i.e. number of pets
def get_stock_count(pet_shop):
    stock_level = len(pet_shop["pets"])
    return stock_level

# 7. Function to find number of pets by breed
def get_pets_by_breed(pet_shop, breed):
    breed_pets = []
    for animal in pet_shop["pets"]:
        if animal["breed"] == breed:
            breed_pets.append(animal["breed"])
    return breed_pets

# 8. Function to find pet by name -i.e. "Arthur"
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

# 9. Remove pet by name
def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

# 10. Function to add pet to stock
def add_pet_to_stock(pet_shop,new_pet):
        pet_shop["pets"].append(new_pet)
        return pet_shop["pets"]

# 11. Function to get customer cash 
def get_customer_cash(customer):
    return customer["cash"]

#12. Function to remove cash from customer
def remove_customer_cash(customer,money):
    customer["cash"]-= money
    return customer["cash"]
    
#13. Function to check number of pets for customer
def get_customer_pet_count(customer):
    return len(customer["pets"])

#14. Function to add pet to customer
def add_pet_to_customer(customer,new_pet):
    return customer["pets"].append(new_pet)

#15. Function to see if customer can afford pet
def customer_can_afford_pet(customer,new_pet):
    sufficient_funds = False
    if customer["cash"] >= new_pet["price"]:
        sufficient_funds = True
    return sufficient_funds

#16. Function to sell pet to customer
def sell_pet_to_customer(pet_shop,pet,customer):
    if pet is None: # No pet found
        print ("No pet found.")
    elif customer_can_afford_pet(customer,pet) == False: # Insufficient funds
        print ("Insufficent funds.")
    else: 
    # only run if pet exists and sufficent funds are available
        pet_price = pet["price"] # define pet price
        add_pet_to_customer(customer,pet) 
        remove_pet_by_name(pet_shop, pet)
        remove_customer_cash(customer,pet_price)
        increase_pets_sold(pet_shop,1)
        add_or_remove_cash(pet_shop, pet_price)

