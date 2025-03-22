#
# class BuildingError(Exception):
#     def __str__(self):
#         return f"недостатньо матеріалів"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "Dostatno materialiv"
#     else:
#         raise BuildingError(amount_of_material)
#
# material = 123
# check_material(material, 300)

# try:
#     numerator = int(input("Введіть чисельник:"))
#     denominator = int(input("Введіть знаменик:"))
#     print(numerator / denominator)
# except ZeroDivisionError:
#     print("Помилка: Ділення на 0 не можливо")
# except ValueError:
#     print("Помилка: Введені дані не є числом")

import warnings
warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("No code here", SyntaxWarning)
try:
    warnings.warn("Warning, module is not imported", ImportWarning)
except():
    print('Warning')
