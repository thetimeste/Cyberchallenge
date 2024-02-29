from base64 import b64decode

def base64toint(s:str):
    return (b64decode(s))

def base10tobytes(i:int):
    #get minimum number of bytes to represent the input
    n = (i.bit_length() + 7)
    endianness='big'
    return (i).to_bytes(n, endianness)

input1="ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
input2=664813035583918006462745898431981286737635929725
result = str(base64toint(input1))+str(base10tobytes(input2))
print(result)