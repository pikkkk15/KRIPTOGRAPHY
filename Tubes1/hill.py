import numpy as np

def hill_encrypt(plaintext, matrix):
    plaintext = plaintext.upper().replace(" ", "")
    while len(plaintext) % 2 != 0:
        plaintext += "X"
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        pair = [ord(plaintext[i]) - 65, ord(plaintext[i+1]) - 65]
        result = np.dot(matrix, pair) % 26
        ciphertext += chr(result[0] + 65) + chr(result[1] + 65)
    return ciphertext

matrix = np.array([[3, 3],
                   [2, 5]])   # ✅ sama seperti di CrypTool
text = input("Masukkan teks: ")
print("Ciphertext:", hill_encrypt(text, matrix))
