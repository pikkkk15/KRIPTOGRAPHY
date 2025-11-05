# Affine Cipher - Enkripsi & Dekripsi Otomatis
# Rumus: E(x) = (a*x + b) mod 26

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            x = ord(char) - 65
            y = (a * x + b) % 26
            ciphertext += chr(y + 65)
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("a tidak memiliki invers modulo 26.")
    for char in ciphertext.upper():
        if char.isalpha():
            y = ord(char) - 65
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + 65)
        else:
            plaintext += char
    return plaintext

plain = input("Masukkan teks asli: ")
a = int(input("Masukkan nilai a (harus relatif prima dengan 26): "))
b = int(input("Masukkan nilai b: "))

cipher = affine_encrypt(plain, a, b)
decrypted = affine_decrypt(cipher, a, b)

print("\nCiphertext:", cipher)
print("Hasil Dekripsi:", decrypted)

with open("hasil_affine.txt", "w") as f:
    f.write(f"Teks Asli: {plain}\n")
    f.write(f"a: {a}, b: {b}\n")
    f.write(f"Ciphertext: {cipher}\n")
    f.write(f"Dekripsi: {decrypted}\n")

print("\n✅ Hasil disimpan di file 'hasil_affine.txt'")
