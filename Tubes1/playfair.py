# Playfair Cipher - Enkripsi & Dekripsi
# Buatan untuk tugas kriptografi

def generate_table(key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Tanpa J
    table = ''
    for c in key.upper() + alphabet:
        if c not in table:
            table += c
    return [table[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c

def playfair_encrypt(plaintext, matrix):
    plaintext = plaintext.upper().replace("J", "I")
    plaintext = ''.join([c for c in plaintext if c.isalpha()])

    i = 0
    pairs = []
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    ciphertext = ""
    for pair in pairs:
        a, b = pair[0], pair[1]
        ra, ca = find_position(matrix, a)
        rb, cb = find_position(matrix, b)

        if ra == rb:  # baris sama
            ciphertext += matrix[ra][(ca + 1) % 5]
            ciphertext += matrix[rb][(cb + 1) % 5]
        elif ca == cb:  # kolom sama
            ciphertext += matrix[(ra + 1) % 5][ca]
            ciphertext += matrix[(rb + 1) % 5][cb]
        else:  # persegi
            ciphertext += matrix[ra][cb]
            ciphertext += matrix[rb][ca]
    return ciphertext

def playfair_decrypt(ciphertext, matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        ra, ca = find_position(matrix, a)
        rb, cb = find_position(matrix, b)

        if ra == rb:  # baris sama
            plaintext += matrix[ra][(ca - 1) % 5]
            plaintext += matrix[rb][(cb - 1) % 5]
        elif ca == cb:  # kolom sama
            plaintext += matrix[(ra - 1) % 5][ca]
            plaintext += matrix[(rb - 1) % 5][cb]
        else:  # persegi
            plaintext += matrix[ra][cb]
            plaintext += matrix[rb][ca]
    return plaintext

# ===== Main Program =====
key = input("Masukkan kunci Playfair: ")
plain = input("Masukkan teks asli: ")

matrix = generate_table(key)
print("\nTabel Playfair:")
for row in matrix:
    print(row)

cipher = playfair_encrypt(plain, matrix)
print("\nCiphertext:", cipher)

decrypted = playfair_decrypt(cipher, matrix)
print("Hasil Dekripsi:", decrypted)
