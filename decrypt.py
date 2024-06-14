from base64 import b64decode
from Crypto.Cipher import AES

def decrypt(buff, decryptedDatabyte):
    
    try:      
        aes = AES.new(decryptedDatabyte, AES.MODE_GCM, buff[3:15])
        return aes.decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"

def buildbuff(tok : str):
    res = tok.split('dQw4w9WgXcQ:')[1]
    res = b64decode(res)
    return res

def builddecryptedDatabyte(key : list):
    res = b''
    for i in key:
        res += int(i).to_bytes(2, byteorder='big')[1:]
    return res

key = input("Enter your key: ").split("|")

cleaned = []
result = []

cleaned = input("Enter hash: ").split("|")
try :
    cleaned.remove("")
    key.remove("")
except ValueError:
    pass

print("\nDecrypted Tokens: ")

for token in cleaned:
            try:
                tok = decrypt(buildbuff(token), builddecryptedDatabyte(key))
                if not tok in result : 
                    result.append(tok)
                    print(tok)

            except IndexError == "Error": continue
            