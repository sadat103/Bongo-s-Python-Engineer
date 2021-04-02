def print_depth(data, depth=1):
    for key in data:
        print(f"{key} {depth}")
        if isinstance(data[key], dict):
            print_depth(data[key], depth+1)


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}
print_depth(a)
