# импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(INPUT_FILENAME, delimiter=',', newline='\n') -> str:
 # считать содержимое csv файла
    rows = []
    with open(INPUT_FILENAME, 'r', encoding='utf-8', newline=newline) as file:
        reader = csv.DictReader(file, delimiter=delimiter)

# Сериализовать в файл с отступами равными 4
        for row in reader:
            rows.append(row)

    json_data = json.dumps(rows, indent=4)
    return json_data

if __name__ == '__main__':
    # Нужно для проверки

    json_data = task(INPUT_FILENAME)
    with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as output_f:
        output_f.write(json_data)

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
         for line in output_f:
             print(line, end="")
