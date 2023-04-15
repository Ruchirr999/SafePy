import os
from Crypto.Cipher import AES


folder_path = "C:\\Users\\username\\foldername"
def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        iv = infile.read(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(cipher.decrypt(chunk))

        try:
            with open(out_filename, 'rb') as f:
                decrypted_data = f.read()

            # Check that the decrypted data is correct
            original_file_path = os.path.splitext(in_filename)[0]
            with open(original_file_path, 'rb') as f:
                original_data = f.read()

            if decrypted_data != original_data:
                raise ValueError('Decrypted data does not match the original data.')
                
        except Exception as e:
            print(f'Error: {e}')
            os.remove(out_filename)
        else:
            print(f'Decrypted file: {out_filename}')
    

if __name__ == '__main__':
    key_file_path = os.path.join(os.path.dirname(folder_path), 'key.txt')
    with open(key_file_path, 'rb') as key_file:
        key = key_file.read()

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            decrypt_file(key, file_path)
