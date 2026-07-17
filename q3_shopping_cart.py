# Part A - Spotting the bug

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']

# Explanation:-
# The default list is created only once and shared across function calls.
# Passing a new list (["bread"]) creates an independent cart.


# Part B – Fixing the bug

def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart


# Part C – Build the Cart

def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


def update_price(price_tuple, new_price):
    # Tuples are immutable, so modifying an element raises TypeError.
    price_tuple[0] = new_price


def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]

    total = total - (total * cart["discount"] / 100)
    return total


cart1 = create_cart("Alice", 10)
cart2 = create_cart("Bob", 5)

add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)

add_to_cart(cart2, "Keyboard", 2000, 1)
add_to_cart(cart2, "Monitor", 15000, 1)

print(cart1)
print("Total:", calculate_total(cart1))

print(cart2)
print("Total:", calculate_total(cart2))

price = (50000,)

try:
    update_price(price, 45000)
except TypeError as e:
    print("Error:", e)


# Why is discount=0 safe but cart=[] dangerous?
# discount=0 is immutable, so it is not shared in a harmful way.
# cart=[] is mutable, so the same list is shared across function calls.

# What is the difference between rebinding and mutating?
# Rebinding assigns a variable to a new object.
# Mutating changes the existing object.

# Which of these are mutable? – list, tuple, dict, set, str, int
# Mutable: list, dict, set
# Immutable: tuple, str, int

# When you pass a list into a function and modify it, do changes reflect outside? Why?
# Yes. Lists are mutable and functions receive a reference to the same object.