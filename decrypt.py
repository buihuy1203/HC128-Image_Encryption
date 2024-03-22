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

'''file_name = input("\nEnter file to decrypt: ")'''
file_name = "result.txt"
print ("\nGenerating keystream, 4 bytes at a time")
k = hc128.keygen()
print ("Keystream generated: ", k)
with open (file_name, 'rb') as f:
  cipher_text = f.read()
k = k.encode()
print(k)
plain_text = b""
for i in range(0,len(cipher_text)):
    plain_text += bytes([cipher_text[i] ^ k[i%8]])
with open ("result_decrypt.jpg", "wb") as f:
  f.write(plain_text)
print ("Finished Decode! ")
end = time.time()
print("Exceution time: ", (end - start)* 10**3,"ms")