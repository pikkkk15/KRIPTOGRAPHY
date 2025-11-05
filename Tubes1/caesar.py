# Caesar Cipher - Enkripsi & Dekripsi Otomatis

def caesar_encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            result += char
    return result

plain = input("Masukkan teks asli: ")
shift = int(input("Masukkan jumlah pergeseran (0-25): "))

cipher = caesar_encrypt(plain, shift)
decrypted = caesar_decrypt(cipher, shift)

print("\nCiphertext:", cipher)
print("Hasil Dekripsi:", decrypted)

with open("hasil_caesar.txt", "w") as f:
    f.write(f"Teks Asli: {plain}\n")
    f.write(f"Pergeseran: {shift}\n")
    f.write(f"Ciphertext: {cipher}\n")
    f.write(f"Dekripsi: {decrypted}\n")

print("\n✅ Hasil disimpan di file 'hasil_caesar.txt'")
