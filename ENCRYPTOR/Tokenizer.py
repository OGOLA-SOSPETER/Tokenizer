#A python program to generate token
import re
import rsa

class Tokens:
    def __init__(self):
        self.decMessage = None
        self.email = ''
        self.password = ''
        self.encMessage = ''
        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


    def GetCredentials(self):
        print('\n')
        new_email = input("Enter the email address: ")
        self.email = new_email
        new_password = input("Enter the password: ")
        self.password = new_password



    def Validator(self):

        if re.fullmatch(self.regex, self.email):
            print('Correct Mail Format👍')
            return self.email
        else:
            while not re.fullmatch(self.regex, self.email):
                print('Re-enter mail in the correct format!!!!')
                self.GetCredentials()


    def Encryptor(self):
        # generate public and private keys with rsa.new-keys method,this method accepts key length as its parameter
        # key length should be least 16
        publicKey, privateKey = rsa.newkeys(512)

        # rsa.encrypt method is used to encrypt string with public key string should be
        # encode to byte string before encryption with encode method
        encMessage = rsa.encrypt(self.password.encode(), publicKey)

        print("original Password: ", self.password)
        print("encrypted Password: ", encMessage)

        # the encrypted message can be decrypted
        # with ras.decrypt method and private key
        # decrypt method returns encoded byte string,
        # use decode method to convert it to string
        # public key cannot be used for decryption
        decMessage = rsa.decrypt(encMessage, privateKey).decode()

        print("decrypted Password: ", decMessage)



Token1 = Tokens()
for a in range(5):
    Token1.GetCredentials()
    Token1.Validator()
    Token1.Encryptor()

