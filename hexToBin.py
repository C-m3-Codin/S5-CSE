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
        print("entered hex")
        bin_dict[hex(15)[2:]]=binn
print(bin_dict)
    
        