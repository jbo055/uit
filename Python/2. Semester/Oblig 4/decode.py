def decode(bit_pattern:str, tree) -> str:
    answer = ""
    current = tree
    n = len(bit_pattern)
    for i in range(n):
        if bit_pattern[i] == '0':
            current = current.left
        else:
            current = current.right
        
        if current.left is None and current.right is None:
            answer += current.element
            current = tree
    return answer 
