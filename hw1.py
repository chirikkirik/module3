calls = 0
list_to_search = []

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()

    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()

    if string in list_to_search:
        return True
    else:
        return False

print(string_info("Crocodile"))
print(string_info("Elephant"))
print(is_contains("fox", ["wolf".casefold(), "cat".casefold() , "fOX".casefold()]))
print(is_contains("opel", ["nissan", "Lexus"]))
print(calls)

