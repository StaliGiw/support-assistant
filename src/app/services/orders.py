def get_order_status(order: dict):
    return order.get("status", "unknown")


def can_cancel_order(order: dict):
    res = get_order_status(order)
    return res == "new"


if __name__ == "__main__":
    order_1 = {"status": "new", "id": 101}
    order_2 = {"id": 102}

    print(can_cancel_order(order_1))
    print(can_cancel_order(order_2))

    if can_cancel_order(order_1):
        order_1["status"] = "cancelled"
    else:
        print("Отмена недоступна")
