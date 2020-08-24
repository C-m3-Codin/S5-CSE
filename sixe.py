import binascii


# def conToHex(a):



inp=input()
# hex_string = 0xhex_string
# hex=int(inp,16)
# print(hex)
# if
binary=conToHEx(inp)
print(binary)

# print(type(binary))
l=len(binary)
print(l)
l/=4
print(l)
form=["Format 1","Format 2","Format 3","Format 4"]
print("\t type is ",form[int(l - 1)])
print("l is ",l)
if(l==1):
    op=binary[0:len(binary)]
    print("\t op :",op)
elif(l==2):
    op=binary[0,7]
    reg1=binary[7,7+4]
    reg2=binary[7+4:7+4+4]
    print("\t op: ",op,"\n\t reg 1 :",reg1,"\n\t reg 2 :",reg2)
elif(l==3):
    op=binary[0,7]
    flags=binary[7:6+7]
    disp=binary[6+7:len(binary)]
    print("\t op: ",op,"\n\t flags  :",reg1,"\n\t displacement :",reg2)
elif(l==4):
    op=binary[0,7]
    flags=binary[7:6+7]
    disp=binary[6+7:len(binary)]
    print("\t op: ",op,"\n\t flags  :",reg1,"\n\t address :",reg2)
