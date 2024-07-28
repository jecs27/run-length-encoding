def encode_count(count, char):
    if count == 1:
        return char
    elif count == 2:
        return char * 2
    elif count < 10:       
        return f'{char}({count})'
    else:
        return f'{char}({chr(87 + count)})'

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


def decompress(compressed):
    result = []
    i = 0
    while i < len(compressed):
        char = compressed[i]
        i += 1
        if i < len(compressed) and compressed[i] == '(':
            count = ''
            i += 1
            while compressed[i] != ')':
                count += compressed[i]
                i += 1
            i += 1
            if count.isalpha():
                count = ord(count) - 87
            else:
                count = int(count)
            result.extend([char] * count)
        else:
            result.append(char)
    return ''.join(result)


# Pruebas
test_cases = [
    "AABBBCCCC",
    "WWWWWWWWWWWWWWWWWWWW",
    "ABCDE",
    "AABBCCDDEE",
    "AAAAABBBBBBBBBBBBBBB",
    "A",
    "AA",
    ""
]

for case in test_cases:
    compressed = compress(case)
    decompressed = decompress(compressed)
    print(f"Original: {case}")
    print(f"Comprimido: {compressed}")
    print(f"Descomprimido: {decompressed}")
    print(f"¿Coinciden?: {case == decompressed}")
    print()