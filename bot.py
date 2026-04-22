import random
from logger import log

def place_order(symbol, side, order_type, quantity, price=None):
    print("Connecting to Binance Testnet...")

    # simulate delay
    print("Placing order...")

    success = random.choice([True, True, False])  # mostly success

    if success:
        order_id = random.randint(10000, 99999)

        result = {
            "status": "SUCCESS",
            "order_id": order_id,
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "price": price
        }

        log(f"Order Success: {result}")
        return result

    else:
        error = "Network Error / Exchange not reachable"
        log(f"Order Failed: {error}")
        return {"status": "FAILED", "error": error}