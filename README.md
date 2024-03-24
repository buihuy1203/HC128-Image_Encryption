# Image Encryption - Decryption HC-128
This is the Image Encryption and Decryption based on HC-128 algorithm, one of the seven eStreams.
# How to use:
## Encryption
To use Encryption, put the Key and IV as Hex text to initialize the algorithm:<br>
```
key = "0F62B5085BAE0154A7FA4DA0F34699DC322AEF"
IV  = "288FF65DC42B92F960C72E95FC63CA3116D2FC"
```
Make sure that the image path and the result path is in the right place:<br>
```
file_name = "E:\Bai Tap\An toan thong tin\python-hc128-master\python-hc128-master\lmao.jpg"
with open ("result.txt", "wb") as f:
  f.write(cipher_text)
```
After that, run the program and the result will be show up in the result.txt file<br>
## Decryption
Same with Encryption, put the Key and IV as Hex text to initialize the algorithm:<br>
```
key = "0F62B5085BAE0154A7FA4DA0F34699DC322AEF"
IV  = "288FF65DC42B92F960C72E95FC63CA3116D2FC"
```
Make sure that the text path and the result path is in the right place:<br>
```
file_name = "result.txt"
with open ("result_decrypt.jpg", "wb") as f:
  f.write(plain_text)
```
After that, run the program and the result will be show up in the result_decrypt.jpg file<br>
#The result:
This is the image we test:
![lmao](https://github.com/buihuy1203/HC128-Image_Encryption/assets/85066488/86521296-1f19-45ea-9aa8-2d93e77d8fdb)
<br>
The result.txt is shown up like this:
![image](https://github.com/buihuy1203/HC128-Image_Encryption/assets/85066488/fcd98d23-68d4-4c6d-b1fa-c7d05ffd29fd)
It can't be converted back to JPG file because the header was corrupted.<br>
But if we put back the text file, put back the Key and IV, it will show again the picture that we encrypt into another picture
![result_decrypt](https://github.com/buihuy1203/HC128-Image_Encryption/assets/85066488/8febc7d5-2d02-4001-bfdc-e9155ba5cc35)
#The time execution
The algorithm takes about 713.19ms to encrypt a 512KB picture, that's such a long time compared to RC4:
![image](https://github.com/buihuy1203/HC128-Image_Encryption/assets/85066488/9794f986-83dd-4227-9b39-04a94c0f1d4e)
