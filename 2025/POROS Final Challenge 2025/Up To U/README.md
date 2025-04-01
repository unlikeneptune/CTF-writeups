## Up To U
> So we've design new encryption algorithm!! can u try to find the flag??

## Penjelasan challenge
Diberikan dua file, `main.py` dan `secret.txt`. main.py akan mengeknkripsi isi dari secret.txt 

## Penyelesaian
Ketika membuka file `secret.txt`, yang muncul hanyalah karakter yang tidak bisa langsung dibaca.
![image](https://github.com/user-attachments/assets/884f3743-9ec6-4934-b054-b53399a53b62)<br>
Ketika menjalankan skrip `main.py`, teks dari `secret.txt` akan dienkripsi, tetapi tetap dalam bentuk karakter yyang belum bisa kita baca.<br>
![image](https://github.com/user-attachments/assets/9163d69e-7173-4d2a-a95b-68fff8f78906)<br>
Oleh karena itu, kita harus memahami bagaimana cara skrip `main.py` bekerja. 
```
def generate_key(seed):
    return seed % 1312

def encrypt(plaintext, seed):
    key = generate_key(seed)
    ciphertext = ""
    for char in plaintext:
        encrypted_char = (ord(char) * key) % 1312
        ciphertext += chr(encrypted_char)
    return ciphertext

def save_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)

plaintext = "LET'S GO LAST INCUBATION"

seed = 1035767061
ciphertext = encrypt(plaintext, seed)
print("Encrypted:", ciphertext)

save_to_file("secret.txt", ciphertext)
```
Skrip ini bekerja dengan cara mengenkripsi teks dengan cara mengubah setiap karakter menjadi nilai ASCII, mengalikannya dengan kunci yang dihasilkan dari seed, dan kemudian mengambil hasil modulus 1312 sebelum mengonversinya kembali menjadi karakter. Hasil enkripsi ini disimpan dalam file `secret.txt`. Namun, karena penggunaan modulus 1312 membatasi rentang karakter yang valid, ada kemungkinan muncul karakter yang tidak dapat direpresentasikan dengan baik, yang dapat mengakibatkan kesalahan atau data yang tidak terbaca.
Dengan demikian, kita bisa membuat skrip 'kebalikan' untuk mendekripsi output dari `main.py` di atas.
```
def calc_key(seed):
    return seed % 1312

def decrypt(msg, seed):
    key = calc_key(seed)
    result = ""

    for char in msg:
        enc_val = ord(char)

        for val in range(32, 127):
            if (val * key) % 1312 == enc_val:
                result += chr(val)
                break
        else:
            result += "?"

    return result

with open("secret.txt", "r", encoding="utf-8") as f:
    msg = f.read()

seed = 1035767061
text = decrypt(msg, seed)
print(text)
```
Jalankan skrip di atas dan kita dapatkan flag-nya.
```
porosCTF{REDACTED_UNTIL_EVENT_FINISHED}
```
