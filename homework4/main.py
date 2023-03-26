def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('На 0 делить нельзя')
        return 0
    except TypeError:
        print('Что-то пошло не так')
        return 0
    except ValueError:
        print('Что-то пошло не так')
        return 0

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

result = []

for key in data:
    res = divider(key, data[key])
    result.append(res)


print(result)