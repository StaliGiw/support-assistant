"""Тесты правил заказов будем писать вместе после первой функции."""
from app.services.orders import can_cancel_order, get_order_status


def test_get_order_status_returns_value_or_unknown():
    assert get_order_status({"status": "new"}) == "new"
    assert get_order_status({"id": 102}) == "unknown"


def test_only_new_order_can_be_cancelled():
    assert can_cancel_order({"status": "new"}) is True
    assert can_cancel_order({"status": "cancelled"}) is False
    assert can_cancel_order({"id": 102}) is False
