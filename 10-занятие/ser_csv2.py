import csv

filename = "20_02_23_b_data.csv"
# список покупок: вес и стоимость (грам / копейка)
shoplist = {"яблоко": [1000, 350], "банан": [2500, 150], "гранат": [5000, 500]}

# Запись в файл
with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
    writer.writeheader()  # Записывает заголовки в файл
    for name, values in sorted(shoplist.items()):
        writer.writerow(dict(name=name, weight=values[0], price=values[1]))

# формите чтение из файла
with open(filename, 'r', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for item in reader:
        print(item)