import json

# решите задачу
def task(file_input) -> float:
    with open(file_input, 'r') as file:
        data = json.load(file)

    total_sum = sum(item['score'] * item['weight'] for item in data)
    return total_sum


file_input = 'input.json'
print(f"{task(file_input):.3f}")
