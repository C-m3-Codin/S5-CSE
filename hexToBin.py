bin={}
for i in range(10):
    binn=''
    while(i>0):
        if(i%2==0):
            binn='0'+ binn
        else:
            binn='1' + binn
        # print(i)
        i=int(i/2)
    print(binn)
    binn=((4-len(binn))*('0')) + binn 
    print(binn)
    
        