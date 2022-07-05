# Python program that encodes a .pem file into base64
import base64
import sys

def base64_encode(data):
    '''
    Base16 encode data
    '''
    return base64.b64encode(data)


def main():
    '''
    Main function
    '''
    # Read in the file
    with open(sys.argv[1], 'rb') as f:
        data = f.read()
        print(data)
    # Encode the data
    encoded = base64_encode(data)
    # Write the data to a new file
    with open(sys.argv[2], 'wb') as f:
        f.write(encoded)

main()
