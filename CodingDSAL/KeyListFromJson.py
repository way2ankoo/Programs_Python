import json


def extract_keys_and_values(json_obj, keys_list=None, values_list=None):
    if keys_list is None:
        keys_list = []
    if values_list is None:
        values_list = []

    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            keys_list.append(key)
            extract_keys_and_values(value, keys_list, values_list)
    elif isinstance(json_obj, list):
        for item in json_obj:
            extract_keys_and_values(item, keys_list, values_list)
    else:
        # For primitive types
        values_list.append(json_obj)

    return keys_list, values_list


# Example usage
json_string = '''
{
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
'''

# Convert JSON string to Python dictionary
json_obj = json.loads(json_string)

# Extract keys and values
keys, values = extract_keys_and_values(json_obj)

# Print results
print("Keys:", keys)
print("Values:", values)
