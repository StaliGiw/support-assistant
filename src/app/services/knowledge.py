def contains_query(text, query) -> bool:
    """Проверяет вхождение запроса без учёта регистра."""
    return query.lower() in text.lower()


if __name__ == "__main__":
    knowledge_base = ["Доставка занимает три дня", "Оплата доступна картой"]
    found = False
    for text in knowledge_base:
        if contains_query(text, "доставка"):
            found = True
            print(text)
    if not found:
        print("Ответ не найден")
