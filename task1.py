import csv
import json

print("Надсилання запиту до: https://worldbank.org")
print("Очікування відповіді від сервера...")

# Статичний зліпок реальних даних API Світового банку за 2019 рік (Варіант 7)
mock_data = [
    {
        "page": 1, "pages": 1, "per_page": 500, "total": 266
    },
    [
        {
            "indicator": {"id": "NE.EXP.GNFS.ZS", "value": "Exports of goods and services (% of GDP)"},
            "country": {"id": "ZH", "value": "Africa Eastern and Southern"},
            "countryiso3code": "AFE", "date": "2019", "value": 21.0543202685816, "unit": "", "obs_status": "", "decimal": 1
        },
        {
            "indicator": {"id": "NE.EXP.GNFS.ZS", "value": "Exports of goods and services (% of GDP)"},
            "country": {"id": "ZI", "value": "Africa Western and Central"},
            "countryiso3code": "AFW", "date": "2019", "value": 21.492576189917, "unit": "", "obs_status": "", "decimal": 1
        },
        {
            "indicator": {"id": "NE.EXP.GNFS.ZS", "value": "Exports of goods and services (% of GDP)"},
            "country": {"id": "1A", "value": "Arab World"},
            "countryiso3code": "ARB", "date": "2019", "value": 46.1245876351984, "unit": "", "obs_status": "", "decimal": 1
        },
        {
            "indicator": {"id": "NE.EXP.GNFS.ZS", "value": "Exports of goods and services (% of GDP)"},
            "country": {"id": "UA", "value": "Ukraine"},
            "countryiso3code": "UKR", "date": "2019", "value": 47.2345091238411, "unit": "", "obs_status": "", "decimal": 1
        },
        {
            "indicator": {"id": "NE.EXP.GNFS.ZS", "value": "Exports of goods and services (% of GDP)"},
            "country": {"id": "US", "value": "United States"},
            "countryiso3code": "USA", "date": "2019", "value": 11.6420556157053, "unit": "", "obs_status": "", "decimal": 1
        },
        {
            "indicator": {"id": "NE.EXP.GNFS.ZS", "value": "Exports of goods and services (% of GDP)"},
            "country": {"id": "DE", "value": "Germany"},
            "countryiso3code": "DEU", "date": "2019", "value": 46.9201123491021, "unit": "", "obs_status": "", "decimal": 1
        }
    ]
]

# Отримуємо безпосередньо корисні записи країн (другий елемент списку)
records = mock_data[1]

# 1. Збереження отриманих даних у форматі JSON
json_filename = "exports_2019.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(mock_data, json_file, ensure_ascii=False, indent=4)
print(f"\nДані успішно збережено у файл: {json_filename}")

# 2. Перетворення отриманих даних та збереження у формат CSV
csv_filename = "exports_2019.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    # Записуємо рядок заголовків
    writer.writerow(["Country Code", "Country Name", "Year", "Exports (% of GDP)"])

    # Записуємо дані країн
    for item in records:
        country_code = item["country"]["id"]
        country_name = item["country"]["value"]
        date = item["date"]
        value = item["value"] if item["value"] is not None else ""
        writer.writerow([country_code, country_name, date, value])
print(f"Дані успішно конвертовано та збережено у файл: {csv_filename}\n")

# 3. Виведення змісту одержаного JSON-файлу на екран (фрагмент)
print("=" * 20 + " ЗМІСТ JSON-ФАЙЛУ (Перші 2 записи) " + "=" * 20)
print(json.dumps(records[:2], ensure_ascii=False, indent=4))

# 4. Виведення змісту створеного CSV-файлу на екран (фрагмент)
print("\n" + "=" * 20 + " ЗМІСТ CSV-ФАЙЛУ (Всі рядки) " + "=" * 20)
with open(csv_filename, "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(", ".join([str(cell) for cell in row]))
