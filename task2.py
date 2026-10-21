import csv
import os

def search_country_data(csv_filename):
    # Перевіряємо, чи існує потрібний CSV-файл у папці
    if not os.path.exists(csv_filename):
        print(f"[ПОМИЛКА] Файл '{csv_filename}' не знайдено!")
        print("Будь ласка, спочатку запустіть скрипт із Завдання 1 для створення цього файлу.")
        return

    print("=" * 15 + " СИСТЕМА ПОШУКУ ДАНИХ КРАЇН ЗА 2019 РІК " + "=" * 15)
    search_query = input("Введіть назву країни або її код для пошуку (наприклад: Ukraine або UA): ").strip().lower()

    if not search_query:
        print("[ПОМИЛКА] Запит не може бути порожнім!")
        return

    found_results = []

    # Зчитуємо CSV-файл та шукаємо збіги
    with open(csv_filename, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Пропускаємо рядок заголовків

        for row in reader:
            # Структура рядка: [Country Code, Country Name, Year, Exports (% of GDP)]
            country_code = row[0].lower()
            country_name = row[1].lower()

            # Якщо пошуковий запит є в коді або в назві країни
            if search_query in country_code or search_query in country_name:
                found_results.append(row)

    # Виводимо результати пошуку
    print("\n" + "-" * 25 + " РЕЗУЛЬТАТИ ПОШУКУ " + "-" * 25)
    if found_results:
        # Гарно виводимо заголовок таблиці
        print(f"{'Код':<6} | {'Назва країни / Регіону':<35} | {'Рік':<5} | {'Експорт (% від ВВП)'}")
        print("-" * 75)
        
        for row in found_results:
            # <6 та <35 вирівнюють стовпчики по лівому краю для акуратного вигляду в консолі
            print(f"{row[0]:<6} | {row[1]:<35} | {row[2]:<5} | {row[3]}%")
        print("-" * 75)
        print(f"Знайдено записів: {len(found_results)}")
    else:
        print(f"За запитом '{search_query}' нічого не знайдено.")

if __name__ == "__main__":
    # Назва файлу, який було створено в Завданні 1
    target_csv = "exports_2019.csv"
    search_country_data(target_csv)
