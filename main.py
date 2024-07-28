def encode_count(count, char):
    if count == 1:
        return char
    elif count == 2:
        return char * 2
    elif count < 10:       
        return f'{char}({count})'
    elif count < 36:
        return f'{char}({chr(87 + count)})'
    else: 
        return f'{char}({count})'

def compress(cadena):
    if not cadena:
        return f' la cadena no puede estar vacía'

    compressed = []
    char = cadena[0]
    count = 1
    
    for i in range(1, len(cadena)):
        if cadena[i] == char:
            count += 1
        else:
            compressed.append(encode_count(count, char))
            count = 1
            char = cadena[i]

    compressed.append(encode_count(count, char))
    compressed_str = ''.join(compressed)
    return compressed_str 

# casos de Pruebas
test_cases = [
    "AABBBCCCC",
    "WWWWWWWWWWWWWWWWWWWW",
    "ABCDE",
    "AABBCCDDEE",
    "AAAAABBBBBBBBBBBBBBB",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWAAA"
    ""
]

for case in test_cases:
    print(f"Original: {case}")
    print(f"Comprimido: {compress(case)}")
    print()