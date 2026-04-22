from bot import place_order
from utils import validate_order

def main():
    print("=== Trading Bot ===")

    symbol = input("Enter symbol (e.g. BTCUSDT): ")
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter type (MARKET/LIMIT): ").upper()
    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter price: "))

    valid, msg = validate_order(side, order_type)

    if not valid:
        print("Error:", msg)
        return

    result = place_order(symbol, side, order_type, quantity, price)

    print("\nResult:")
    print(result)


if __name__ == "__main__":
    main()