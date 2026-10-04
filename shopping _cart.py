def shopping_cart_fixed():
    products = ["Laptop", "Phone", "Headphones"]
    prices = {"Laptop": 50000, "Phone": 15000, "Headphones": 2000}
    
    print("--- Welcome to Fixed Shop ---")
    for i, item in enumerate(products, 1):
        print(f"{i}. {item}")
        
    try:
        choice = int(input("Select product number to buy: "))
        
        # वैलिडेशन: चेक करना कि इनपुट सही रेंज में है या नहीं
        if 1 <= choice <= len(products):
            selected_item = products[choice - 1]
            price = prices.get(selected_item, 0) # safely get price without crash
            print(f"Success! You bought {selected_item} for Rs.{price}")
        else:
            print("Error: Invalid selection! Please choose a number from the list.")
            
    except ValueError:
        print("Error: Please enter a valid number, not text.")
