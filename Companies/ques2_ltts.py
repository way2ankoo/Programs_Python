my_dict = {"name": "Ankit", "age": 35, "city": "Noida"}

print(my_dict)
print(my_dict.get("city1", "ankit"))  # if not exists, returns default 2nd argument
print(my_dict.values())
view = my_dict.items()
print(len(view))
