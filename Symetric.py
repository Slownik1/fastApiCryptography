from cryptography.fernet import Fernet

key = Fernet.generate_key()
def getSymrtricKey():
    return key;