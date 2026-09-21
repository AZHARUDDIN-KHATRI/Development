RATES = {
    "INR": 1.0,
    "USD": 83.5,
    "EUR": 90.2,
}


def convert_currency(amount, from_currency, to_currency):
    from_code = from_currency.upper()
    to_code = to_currency.upper()


    if from_code not in RATES:
        raise ValueError(f"Unsupported source currency: {from_currency}")
    if to_code not in RATES:
        raise ValueError(f"Unsupported target currency: {to_currency}")

    if from_code == to_code:
        return amount

    amount_in_inr = amount * RATES[from_code] if from_code != "INR" else amount
    converted_amount = amount_in_inr / RATES[to_code] if to_code != "INR" else amount_in_inr
    return round(converted_amount, 2)


if __name__ == "__main__":
    print("Simple Currency Converter")
    print("Supported currencies: INR, USD, EUR")

    try:
        amount = float(input("Enter amount: "))
        source = input("From currency (INR/USD/EUR): ").strip()
        target = input("To currency (INR/USD/EUR): ").strip()

        result = convert_currency(amount, source, target)
        print(f"{amount} {source.upper()} = {result} {target.upper()}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nConversion cancelled.")
