from time import sleep
import os
os.system('cls' if os.name == 'nt' else 'clear')

"""
# Author: Mohammad Saidur Rahman
# Edited by: Brian Cusack
# Python version 3.9
"""
# Function Declarations


def loading():
    for i in range(3):
        sleep(0.5)
        print('.', end=" ")


def getInputs():
    """Get client inputs"""
    y = int(input( "Enter the client value of 'y' (as Integer) or press Enter for default: ") or 44)
    print(f"The value of 'y' is: {y}")
    g = int(input("Enter the client value of 'g' (as Integer) or press Enter for default: ") or 3)
    print(f"The value of 'g' is: {g}")
    p = int(input( "Enter the client value of 'p' (as Integer) or press Enter for default: ") or 139)
    print(f"The value of 'p' is: {p}")
    return y, g, p


def getPrivateKeyValue():
    """Get server private key value"""
    x = int(input( "Enter the servers private key value x 🔑 (as Integer) or press Enter for default:  ") or 12)
    print(f"The value of 'x' is: {x}")
    return x


def serverDecryption( p, C1, C2):
    """Server decryption"""
    print("\nServer decrypts the Cyphertexts and gets the Plaintext.")
    x = getPrivateKeyValue()  # Get server private key value
    k_server = pow(C1, x, p)
    k_Inv = pow(k_server, -1, p) #inverse of k
    M = pow((C2 * k_Inv), 1, p)
    return M


def getMassage(p):
    while True:
        m = int(input('\nEnter the message 💌  (as Integer) to encrypt, m: '))
        if m < p:
            break
        else:
            print(f"\n 😝 The value of 'm' {m} must be less than the value of p' {p}"), sleep(1)
    r = int(input("Enter the random value of 'r' (as Integer): "))
    return m, r

def main():
    print("Welcome to ElGamal Encryption Program 👏  !!!")
    y, g, p = getInputs()  # Get client inputs
    loading()

    m, r = getMassage(p) # Get message and random value
    k = pow(y, r, p)  # Calculate k

    # Client Encryption
    C1 = pow(g, r, p)  # Calculate C1
    C2 = pow((m * k), 1, p)  # Calculate C2

    print(f'Ciphertext "{C1}", "{C2}" is sent to Server.')
    loading()

    M = serverDecryption( p, C1, C2)  # Server Decryption

    print(f"\nServer Extracts Message, M: {M} 😇 ")


if __name__ == "__main__":
    main()
