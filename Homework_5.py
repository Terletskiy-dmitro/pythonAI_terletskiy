result = []
def divider(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if a < b:
            raise ValueError("a is less than b")
        if b > 100:
            raise IndexError("b is greater than 100")
        return a / b
    except (ValueError, IndexError, TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        return None
data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)
print(result)