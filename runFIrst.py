#Extracts texts from a image file and saves it in a list with its name and the texts extracted
#run this before the next one 


import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image
# 
#  Batch processing with a single file containing the list of multiple image file paths
f=open("a.txt","r")
a=[]
a=f.read().split("\n")
print(a)
texts = []
a.pop()
# print(pytesseract.image_to_string('a.txt'))
for i in a:
    # texts.append(pytesseract.image_to_string(i))
    textIs = (pytesseract.image_to_string(Image.open(i)))
    
    # print(textIs)
    texts.append(textIs.replace("\n"," "))
# print(texts)
print(len(texts))

with open('your_file.txt', 'w') as f:
    for item in texts:
        f.write("%s\n\n\n\n===================================\n\n" % item)


# print()



# lis = input("input keywords in list seperated by space").split(' ')
lis=texts
lisMatch=[]
serch = input("enter the string \n")

# serch.lower()
if(serch in lis):
    print(lis.index(serch))
else:
    print("fussy on the way")
    for k in range(len(lis)):
        lisMatch.append(0)
        i=lis[k]
        point=0
        sub=serch
        # if(sub==i):
            # print("1000")
        for subStrControl in range(len(serch),-1,-1):
            point=subStrControl
            sub=serch[0:subStrControl]
            
            # print("searching  ",sub,"in ",i)
            if(sub in i):
                break
            elif(sub in i.lower() or sub in i.upper()):
                    point=point-.5
                    # print(i,"   not match Case   ", sub)
                    break
        lisMatch[k]=point
    # lisMatch = for i in 
    for i in range(len(lisMatch)):
        lisMatch[i]=(lisMatch[i]/len(serch))*100

    print(lisMatch)
print(max(lisMatch))
imgToShow=lisMatch.index(max(lisMatch))
print(imgToShow)

            
# import cv2
# img = cv2.imread('messi5.jpg',0)
