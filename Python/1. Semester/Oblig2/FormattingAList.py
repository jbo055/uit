# When writing out a list of items in English, one normally separates the items with commas.
# In addition, the word “and” is normally included before the last item, unless the list only contains one item.
# Consider the following four strings:
# apples
# apples and oranges
# apples, oranges and bananas
# apples, oranges, bananas and lemons

# Write a function that takes a list of strings as its only parameter. Your function should return a string that contains all of the items in the list, formatted in the manner described previously, as its only result.
# While the examples shown previously only include lists containing four elements or less, your function should behave correctly for lists of any length.

items = []
def add_items(items):
    items.append(input("Enter the name of the item: "))
    return items
def format_list(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    else:
        return ", ".join(items[:-1]) + " and " + items[-1]
    
while True:
    items = add_items(items)
    if items[-1] == "":
        items.pop()
        break
    
print(format_list(items))