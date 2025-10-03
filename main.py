from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Abo's kitchen"
owner_name = "Ado"

# Integer data type
year_since = 2025

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["Pad Thai", "Katsudon", "Crispy Pork Sisig"]
beverages = ["Apple Juice", "Cool Water"]

# Tuple data type
business_hours = ("7:00am", "7:00pm")

# Dictionary data type
menu = {
    "Pad Thai": 200.00,
    "Katsudon": 300.00,
    "Crispy Pork Sisig": 150.00,
    "Apple Juice": 50.00,
    "Cool Water": 10.00
}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Pad Thai']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Katsudon']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Crispy Pork Sisig']:.2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['Apple Juice']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Cool Water']:.2f}", target="price5")

# Display additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")





