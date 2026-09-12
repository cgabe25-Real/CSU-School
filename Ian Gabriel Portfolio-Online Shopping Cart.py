"""online shopping cart application."""


class ItemToPurchase:
    """Represents one purchasable item in a shopping cart."""

    def __init__(
        self,
        item_name="none",
        item_price=0.0,
        item_quantity=0,
        item_description="none",
    ):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        """Print the item's quantity, price, and extended cost."""
        item_total = self.item_price * self.item_quantity
        print(
            f"{self.item_name} {self.item_quantity} @ "
            f"${self.item_price:g} = ${item_total:g}"
        )

    def print_item_description(self):
        """Print the item's name and description."""
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart:
    """Manages items belonging to one customer's shopping cart."""

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Add an ItemToPurchase object to the cart."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Remove an item by name, or report if it cannot be found."""
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        """Update non-default attributes of an existing cart item."""
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_price != 0.0:
                    item.item_price = item_to_modify.item_price

                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity

                if item_to_modify.item_description != "none":
                    item.item_description = item_to_modify.item_description

                return

        print("Item not found in cart. Nothing modified.")

    def get_num_items(self):
        """Return the total quantity of all cart items."""
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        """Return the total cost of all items in the cart."""
        return sum(
            item.item_price * item.item_quantity
            for item in self.cart_items
        )

    def print_total(self):
        """Print the shopping-cart contents and total cost."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items()}")
        print()

        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()

        print()
        print(f"Total: ${self.get_cost_of_cart():g}")

    def print_descriptions(self):
        """Print descriptions for every item in the cart."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")

        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    """Display the cart menu and process options until the user quits."""
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart (totals)\n"
        "q - Quit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option:\n").strip().lower()

        while choice not in {"a", "r", "c", "i", "o", "q"}:
            choice = input("Choose an option:\n").strip().lower()

        if choice == "a":
            print("\nADD ITEM TO CART")
            item_name = input("Enter the item name:\n").strip()
            item_description = input("Enter the item description:\n").strip()
            item_price = float(input("Enter the item price:\n"))
            item_quantity = int(input("Enter the item quantity:\n"))

            new_item = ItemToPurchase(
                item_name,
                item_price,
                item_quantity,
                item_description,
            )
            cart.add_item(new_item)

        elif choice == "r":
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove:\n").strip()
            cart.remove_item(item_name)

        elif choice == "c":
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:\n").strip()
            item_quantity = int(input("Enter the new quantity:\n"))

            updated_item = ItemToPurchase(
                item_name=item_name,
                item_quantity=item_quantity,
            )
            cart.modify_item(updated_item)

        elif choice == "i":
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif choice == "o":
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif choice == "q":
            break


def main():
    """Collect customer information and launch the cart menu."""
    customer_name = input("Enter customer's name:\n").strip()
    current_date = input("Enter today's date:\n").strip()

    cart = ShoppingCart(customer_name, current_date)

    print()
    print(f"Customer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")

    print_menu(cart)


if __name__ == "__main__":
    main()
