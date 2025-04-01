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
