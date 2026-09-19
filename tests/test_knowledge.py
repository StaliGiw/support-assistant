from app.services.knowledge import contains_query


def test_contains_query_ignores_letter_case():
    assert contains_query("Доставка занимает три дня", "доставка") is True
    assert contains_query("Оплата доступна картой", "ДОСТАВКА") is False
