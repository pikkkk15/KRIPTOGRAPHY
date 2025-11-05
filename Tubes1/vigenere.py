# Vigenere Cipher - Enkripsi dan Dekripsi Otomatis
# Buatan untuk tugas kriptografi

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    i = 0
    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            encrypted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
            ciphertext += encrypted_char
            i += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    i = 0
    for char in ciphertext.upper():
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            decrypted_char = chr(((ord(char) - 65 - shift) % 26) + 65)
            plaintext += decrypted_char
            i += 1
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan
plain = input("Masukkan teks asli: ")
key = input("Masukkan kunci: ")

cipher = vigenere_encrypt(plain, key)
print("\nCiphertext:", cipher)

decrypted = vigenere_decrypt(cipher, key)
print("Hasil Dekripsi:", decrypted)

# Simpan hasil ke file
with open("hasil_vigenere.txt", "w") as f:
    f.write(f"Teks Asli: {plain}\n")
    f.write(f"Kunci: {key}\n")
    f.write(f"Ciphertext: {cipher}\n")
    f.write(f"Hasil Dekripsi: {decrypted}\n")

print("\nHasil disimpan di file 'hasil_vigenere.txt'")