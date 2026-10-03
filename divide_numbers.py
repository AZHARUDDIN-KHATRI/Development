def divide_numbers():
    print("--- Simple Python Divider ---")
    
    # ERROR 1: input() हमेशा string देता है, इसे integer में नहीं बदला गया
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    
    # ERROR 2: अगर user ने num2 को 0 डाला, तो ZeroDivisionError आएगा
    result = num1 / num2 
    print(f"Result: {result}")

divide_numbers()
