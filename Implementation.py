from SHA256 import SHA
from DH import DH
from AES import encrypt,decrypt
#Initial Key Exchange
k1,k2 = DH(3,4)
print(k1,k2)

X = "Message by X"
print(X)

while True:
    EncryptedMessageAESX = encrypt(X,k1)
    print(EncryptedMessageAESX)

    #this message is received by Y
    DecryptedMessageOfX = decrypt(EncryptedMessageAESX,k2)

    print(DecryptedMessageOfX)

    k2 = k1 = SHA(DecryptedMessageOfX+k1)
    print("New Key generated from last message by X ",k2)

    EncryptedMessageAESX = encrypt("testt ",k1)
    print(EncryptedMessageAESX)

    #this message is received by Y
    DecryptedMessageOfX = decrypt(EncryptedMessageAESX,k2)

    print(DecryptedMessageOfX)

    k2 = k1 = SHA(DecryptedMessageOfX+k1)
    print("New Key generated from last message by X ",k2)


