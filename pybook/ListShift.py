  lst = {4, 5, 6, 7, 8, 9}
  temp = lst[0] # Retain the first element

  # Shift elements left
  for i in range(1, len(lst)):
      lst[i - 1] = lst[i]
  
  # Move the first element to fill in the last position
  lst[lst.length - 1] = temp