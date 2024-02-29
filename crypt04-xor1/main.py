def xor_bytes(a, b):
    return bytes([x^y for x,y in zip(a,b)])

def hex_to_bytes(hex):
    return bytes.fromhex(hex)

input1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
input2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"
result = xor_bytes(hex_to_bytes(input1),hex_to_bytes(input2))
print(result)