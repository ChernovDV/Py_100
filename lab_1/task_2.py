# Найдите количество книг, которое можно разместить на дискете

pages = 100
line = 50
symbols = 25
size = 4
disk_size = 1.44 * 1024 * 1024 # размер диска в байтах

one_book_symbols = pages * line * symbols  # количество символов в книге
size_one_book = one_book_symbols * size    # размер книги в байтах
book_count = int(disk_size // size_one_book)  # количество книг на дискете
print("Количество книг, помещающихся на дискету:", book_count)
