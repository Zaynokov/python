with open("text(2).txt", "r", encoding="utf-8") as file:
    rows = file.read().splitlines()

print(f"Всего строк - {len(rows)}")

for i, item in enumerate(rows):
    print(f"В строке № {i + 1} всего слов - {len(item.split())}")
