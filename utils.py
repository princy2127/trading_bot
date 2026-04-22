def validate_order(side, order_type):
    valid_sides = ["BUY", "SELL"]
    valid_types = ["MARKET", "LIMIT"]

    if side not in valid_sides:
        return False, "Invalid side"

    if order_type not in valid_types:
        return False, "Invalid order type"

    return True, "Valid"