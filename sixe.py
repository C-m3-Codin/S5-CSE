import binascii



bin_dict={}
for i in range(16):
    # if(i<10):
    binn=''
    key=i
    while(i>0):
        if(i%2==0):
            binn='0'+ binn
        else:
            binn='1' + binn
        # print(i)
        i=int(i/2)
    # print(binn)
    binn=((4-len(binn)  )*('0')) + binn 
    # print(binn)
    if(key<10):
        bin_dict[str(key)]=binn
    else:
        # print("entered hex")
        bin_dict[hex(key)[2:]]=binn
# print(bin_dict)
# def c

def FindAddress(flgs):
    print("flags ",flgs)
    if(flgs[3]=='1' and flgs[4]=='1'):
        return "Base "
    elif(flgs[3]=='0' and flgs[4]=='1'):
        # print("Program Conter Relative")
        return "Program Conter Relative "
    elif(flgs[2]=='1' and flgs[3]=='0' and flgs[4]=='1' ):
        return "Base relative with indexing "
    elif(flgs[2]=='0' and flgs[3]=='0' and flgs[4]=='1'):
        return "Program conter relative addressing"
    elif(flgs[2]=='0' and flgs[3]=='0' and flgs[4]=='0'):
        return "Direct "
    elif(flgs[0]=='0' and flags[1]=='1'):
        return "Immediate addressing "
    elif(flgs[0]=='1' and flgs[1]=='0'):
        return "Indirect "
    else:
        print(flgs[3],flgs[4])
        return "not learned"

def conToHEx(hexNum):
    bin_str=""
    for i in hexNum:
        # print("\t ",i, " is ",bin_dict[i])
        bin_str=bin_str+bin_dict[i]
    return bin_str



inp=input()
# hex_string = 0xhex_string
# hex=int(inp,16)
# print(hex)
# if
inp=inp.lower()
# print(":value to :",inp)
binary=conToHEx(inp)
# print("finally \t ",binary)
# print(binary)

# print(type(binary))
l=len(binary)
# print(l)
l/=8
# print(l)
form=["Format 1","Format 2","Format 3","Format 4"]
print("\t type is ",form[int(l - 1)])
# print("l is ",l)
if(l==1):
    op=binary[0:len(binary)]
    print("\t op :",op)
elif(l==2):
    op=binary[0:7]
    reg1=binary[7:7+4]
    reg2=binary[7+4:7+4+4]
    print("\t op:\t",op,"\n\t reg 1 :\t",reg1,"\n\t reg 2 :\t",reg2)
    # print("addressing mo")
elif(l==3):
    op=binary[0:6]
    flags=binary[6:6+6]
    disp=binary[6+6:len(binary)]
    addressing=FindAddress(flags)
    print("\t op :\t\t",op,"\n\t flags :\t",flags,"\n\t displacement :\t",disp,"\n\t addressing Mode :\t",addressing)
elif(l==4):
    op=binary[0:7]
    flags=binary[7:6+7]
    disp=binary[6+7:len(binary)]
    addressing=FindAddress(flags)
    print("\t op: \t",op,"\n\t flags:\t",flags,"\n\t address :\t",disp,"\n\t addressing Mode :\t",addressing)
