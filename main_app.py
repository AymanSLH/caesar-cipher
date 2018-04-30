def encrypt(letter, key):
    # must be single alphabetic character
    if not letter.isalpha() or len(letter) != 1:
        return letter
    # convert to lowercase
    letter = letter.lower()
    # convert to numerical value 0 - 25
    value = ord(letter) - 97
    value = (value + key) % 26
    # return encrypted letter
    return chr(value + 97)

def decrypt(letter, key):
    if not letter.isalpha() or len(letter) != 1:
        return letter
    letter = letter.lower()
    value = ord(letter) - 97
    value = (value - key) % 26
    # return encrypted letter
    return chr(value + 97)

# number of characters to shift
key = int(input('Enter the secret key: '))

print ('cipher ( {} )\n'.format(key))
for letter in map(chr, range(97, 123)):
    print ('{} -> {}'.format(letter, encrypt(letter, key)))
print ('')

plaintext = input('Enter the plaintext message: ')
print ('plaintext: {}\n'.format(plaintext))

ciphertext = ''
for letter in plaintext:
    ciphertext += encrypt(letter, key)
print ('ciphertext: {}\n'.format(ciphertext))

# decipher
plaintext2 = ''
for letter in ciphertext:
    plaintext2 += decrypt(letter, key)
print ('plaintext2: {}'.format(plaintext2))