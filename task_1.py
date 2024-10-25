# Напишите функцию для поиска индекса товара
def fun(items_list_, find_item_):
    for product in items_list_:
        if product == find_item_:
            return items_list_.index(product)



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = fun(items_list, find_item)  # Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
