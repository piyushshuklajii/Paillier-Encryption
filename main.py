import Paillier
from PIL import Image
import ImageCryptography
import time
import numpy as np

(publicKey,privateKey) = Paillier.generate_keys(128)

plainimg=Image.open("---Image path---")
start_time1 = time.time()
encimg=ImageCryptography.ImgEncrypt(publicKey,plainimg)
end_time1=time.time()

img = Image.fromarray(encimg,'RGB')
img.save('encrypted_img.png')

start_time2=time.time()
bright=ImageCryptography.homomorphicBrightness(publicKey,encimg,100)
end_time2=time.time()

decimg=ImageCryptography.ImgDecrypt(publicKey,privateKey,encimg)

start_time3=time.time()
decbright=ImageCryptography.ImgDecrypt(publicKey,privateKey,bright)
end_time3=time.time()

decbright.save('img_cdt.png')
decimg.save('img_decrypted.png')
img.show()

print("encrypt time=",end_time1-start_time1)
print("apply time=",end_time2-start_time2)
print("decrypt time=",end_time3-start_time3)

