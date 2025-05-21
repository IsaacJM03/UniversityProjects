# for i in range(10):
#     print(i)
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)

# list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_dict = {num: num ** 2 for num in numbers}
print(square_dict)

even_square = [num ** 2 for num in numbers if num % 2 == 0]
print(even_square)