import hc128
import codecs
import binascii
import time
start = time.time()
key = "0F62B5085BAE0154A7FA4DA0F34699DC322AEF"
IV  = "288FF65DC42B92F960C72E95FC63CA3116D2FC"

print ("Initializing HC-128 cipher state")
print ("Key = ",key)
print ("IV = ",IV)

hc128.init(key, IV)

print ("\nHC-128 Cipher state initialized")

'''file_name = input("\nEnter file to encrypt: ")'''
file_name = "lmao.jpg"
print ("\nGenerating keystream, 4 bytes at a time")
k = hc128.keygen()
print ("Keystream generated: ", k)
with open (file_name, 'rb') as f:
  plain_text = f.read()
k = k.encode()
print(k)
cipher_text = b""
for i in range(0,len(plain_text)):
  cipher_text += bytes([plain_text[i] ^ k[i % 8]])

with open ("result.txt", "wb") as f:
  f.write(cipher_text)
print ("Finished Encoded!")
end = time.time()
print("Excecution time: ", (end - start)* 10**3,"ms")
