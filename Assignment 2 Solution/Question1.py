def encrypt(text, n, m):
    result = []
    for ch in text:
        if 'a' <= ch <= 'm':
            shift = n * m
            new_ord = (ord(ch) - ord('a') + shift) % 26
            result.append(chr(new_ord + ord('a')))
        elif 'n' <= ch <= 'z':
            shift = n + m
            new_ord = (ord(ch) - ord('a') - shift) % 26
            result.append(chr(new_ord + ord('a')))
        elif 'A' <= ch <= 'M':
            shift = n
            new_ord = (ord(ch) - ord('A') - shift) % 26
            result.append(chr(new_ord + ord('A')))
        elif 'N' <= ch <= 'Z':
            shift = m ** 2
            new_ord = (ord(ch) - ord('A') + shift) % 26
            result.append(chr(new_ord + ord('A')))
        else:
            result.append(ch)
    return ''.join(result)

def decrypt(text, n, m):
    result = []
    for ch in text:
        if 'a' <= ch <= 'm':
            shift = n * m
            new_ord = (ord(ch) - ord('a') - shift) % 26
            result.append(chr(new_ord + ord('a')))
        elif 'n' <= ch <= 'z':
            shift = n + m
            new_ord = (ord(ch) - ord('a') + shift) % 26
            result.append(chr(new_ord + ord('a')))
        elif 'A' <= ch <= 'M':
            shift = n
            new_ord = (ord(ch) - ord('A') + shift) % 26
            result.append(chr(new_ord + ord('A')))
        elif 'N' <= ch <= 'Z':
            shift = m ** 2
            new_ord = (ord(ch) - ord('A') - shift) % 26
            result.append(chr(new_ord + ord('A')))
        else:
            result.append(ch)
    return ''.join(result)

def check_correctness(original, decrypted):
    return original == decrypted

# Robust input handling
try:
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
except ValueError:
    print("Error: n and m must be integers.")
    exit()

try:
    with open("raw_text.txt", "r") as f:
        raw = f.read()
except FileNotFoundError:
    print("Error: raw_text.txt not found.")
    exit()

enc = encrypt(raw, n, m)

try:
    with open("encrypted_text.txt", "w") as f:
        f.write(enc)
except IOError:
    print("Error writing encrypted_text.txt.")
    exit()

dec = decrypt(enc, n, m)
print("Decryption correct:", check_correctness(raw, dec))
