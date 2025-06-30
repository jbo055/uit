the_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 1,
    "e": 2,
    "f": 3
}
def reverse_lookup(d, k):
    result = {key for (key, value) in d.items() if value == k}
    print(result)

print(reverse_lookup(the_dict, 1))  # Output: ['a', 'd']
print(reverse_lookup(the_dict, 2))  # Output: ['b', 'e']