def contains_query(text, query) -> bool:
	"""ПРоверят вхождение"""
	return query.lower() in text.lower()
knowledge_base = ["Доставка занимает три дня", "Оплата доступна картой"]
found = False
for text in knowledge_base:
	if contains_query(text, "доставка"):
		found = True
		print(text)
if not found:
	print("Ответ не найден")

