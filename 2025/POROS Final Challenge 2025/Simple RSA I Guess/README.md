## Simple RSA I Guess
> so we've made some simple RSA encryption (I Guess) :)??

## Penjelasan challenge
Di sini, kita ada satu file `chall.py` yang akan melakukan enkripsi RSA sederhana.

## Penyelesaian
Seperti yang telah disebutkan, `chall.py` melakukan operasi RSA sederhana. Kita diberikan p = 47 dan q = 73 adalah bilangan prima untuk membentuk kunci dengan e = 1153 sebagai public key, kemudian mengenkripsi teks "ini flag untuk nyata" ke ciphertext berupa string karakter khusus yaitu "ঐڵವڵँಆࠇްӂࡎગॡ_ஙૂ_ްߟЃ_Όૂਠۿࠇ_ஙΗв". 
```
p = 47
q = 73
e = 1153

ciphertext = "ঐڵವڵँಆࠇްӂࡎગॡ_ஙૂ_ްߟЃ_Όૂਠۿࠇ_ஙΗв"

plaintext = "ini flag untuk nyata"

print("plaintext: " + plaintext)
```
Untuk itu, kita bisa menyusun skrip penghitungan RSA sederhana untuk mendekripsi ciphertext-nya, sebut saja `solve.py` seperti di bawah ini.
```
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Invers modular tidak ada')
    else:
        return x % m

def decrypt_rsa(ciphertext, d, n):
    plaintext = ""
    for char in ciphertext:
        m = ord(char)
        c = pow(m, d, n)
        plaintext += chr(c)
    return plaintext

p = 47
q = 73
e = 1153
ciphertext = "ঐڵವڵँಆࠇްӂࡎગॡ_ஙૂ_ްߟЃ_Όૂਠۿࠇ_ஙΗв"

n = p * q

phi = (p - 1) * (q - 1)

d = mod_inverse(e, phi)

plaintext = decrypt_rsa(ciphertext, d, n)
print(plaintext)
```
Kita bisa langsung jalankan skripnya dan kita akan dapatkan flag-nya.
```
porosCTF{REDACTED_UNTIL_EVENT_FINISHED}
```
