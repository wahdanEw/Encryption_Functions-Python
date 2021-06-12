import hashlib

#--Encrypted_Stamp Function--#
# For Name Encryption And Encrypted signature
def Encrypted_Stamp(encrypt_Name,encrypt_Stamp,ID):
    m = hashlib.md5()
    n = hashlib.md5()
    for s in encrypt_Name:
        for s2 in encrypt_Stamp:
            m.update(s.encode())
            n.update(s2.encode())
    encrypted_Name = m.hexdigest()
    encrypted_Stamp = n.hexdigest()
    print("\nEncrypted Name: ",encrypted_Name)
    Caesar_Cipher(ID)
    print("Encrypted signature: ",encrypted_Stamp)

#--Caesar_Cipher Function--#
# Ecrypted/Encode ID number
def Caesar_Cipher(idNumber):
    alphabet_Num = '0123456789'
    key = 5
    encryptID = ''
    for i in idNumber:
        post = alphabet_Num.find(i)
        newpost = (post + key) % 10  # 10%10=0
        encryptID += alphabet_Num[newpost]
    print("Ecrypted Id Number: ",encryptID)

# --is_String Function--#
# check validation
# check User Name input if its string
def is_String(input):
    if input.replace(" ", "").isalpha():
        return True
    else:
        print("Error - Name value isNot String")
        return exit()

# --isNumber Function--#
# check validation
# check User ID input if its integer
def is_Number(IDinput_check):
    for i in range(len(IDinput_check)):
        if IDinput_check[i].isdigit() != True:
            print("Error - ID Number value is Not integer")
            return exit()
    return True

def main():
    print("Enter Name for Encryption: ")
    name = input()
    is_String(name)
    print("Enter ID Number for Encrypt: ")
    ID= input()
    is_Number(ID)
    print("Enter Stamp for Encryption: ")
    Encrypted_Stamp(input(), name , ID)
    print("\n**************************")
    print("*  Encryption completed  *")
    print("**************************")

if __name__ == main():
    main()