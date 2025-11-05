import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ---------- Caesar Cipher ----------
def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# ---------- Vigenère Cipher ----------
def vigenere_cipher(text, key, mode='encrypt'):
    result = ''
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            k = ord(key[key_index % len(key)]) - ord('A')
            if mode == 'decrypt':
                k = -k
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + k) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# ---------- Fungsi tombol ----------
def browse_input_file():
    filename = filedialog.askopenfilename(title="Pilih file input", filetypes=[("Text files", "*.txt")])
    if filename:
        input_file_var.set(filename)

def browse_output_file():
    filename = filedialog.asksaveasfilename(title="Pilih file output", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        output_file_var.set(filename)

def process_cipher():
    input_file = input_file_var.get()
    output_file = output_file_var.get()
    method = method_var.get()
    mode = mode_var.get()
    shift_or_key = key_input.get().strip()

    if not input_file or not output_file:
        messagebox.showerror("Error", "Pilih file input dan output terlebih dahulu!")
        return

    try:
        with open(input_file, 'r', encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "File input tidak ditemukan!")
        return

    try:
        if method == "Caesar":
            if not shift_or_key.isdigit():
                messagebox.showerror("Error", "Shift harus berupa angka!")
                return
            shift = int(shift_or_key)
            result = caesar_cipher(text, shift, mode)
        else:
            if not shift_or_key.isalpha():
                messagebox.showerror("Error", "Kata kunci Vigenère harus huruf!")
                return
            result = vigenere_cipher(text, shift_or_key, mode)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
        return

    # Simpan hasil ke file
    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(result)

    # Tampilkan hasil di Text widget
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

    messagebox.showinfo("Sukses", f"Hasil {mode} berhasil disimpan di '{output_file}'")

# ---------- GUI ----------
root = tk.Tk()
root.title("Caesar & Vigenère Cipher (File)")
root.geometry("600x400")
root.resizable(False, False)

# Pilihan metode
method_var = tk.StringVar(value="Caesar")
ttk.Label(root, text="Metode Cipher:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
ttk.Radiobutton(root, text="Caesar", variable=method_var, value="Caesar").grid(row=0, column=1)
ttk.Radiobutton(root, text="Vigenère", variable=method_var, value="Vigenère").grid(row=0, column=2)

# Pilihan mode
mode_var = tk.StringVar(value="encrypt")
ttk.Label(root, text="Mode:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
ttk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt").grid(row=1, column=1)
ttk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt").grid(row=1, column=2)

# Input file
input_file_var = tk.StringVar()
ttk.Label(root, text="File Input (.txt):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(root, textvariable=input_file_var, width=40).grid(row=2, column=1)
ttk.Button(root, text="Browse", command=browse_input_file).grid(row=2, column=2)

# Output file
output_file_var = tk.StringVar()
ttk.Label(root, text="File Output (.txt):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
ttk.Entry(root, textvariable=output_file_var, width=40).grid(row=3, column=1)
ttk.Button(root, text="Browse", command=browse_output_file).grid(row=3, column=2)

# Shift / Key
ttk.Label(root, text="Shift / Key:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
key_input = ttk.Entry(root)
key_input.grid(row=4, column=1, columnspan=2, sticky="we", padx=5, pady=5)

# Tombol proses
ttk.Button(root, text="Proses", command=process_cipher).grid(row=5, column=0, columnspan=3, pady=10)

# Output Text
ttk.Label(root, text="Hasil:").grid(row=6, column=0, sticky="nw", padx=5, pady=5)
output_text = tk.Text(root, height=10, width=70)
output_text.grid(row=6, column=1, columnspan=2, pady=5, padx=5)

root.mainloop()
