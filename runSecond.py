
#run this second
#reads the keywords and filenames and does a fuzzzy search (self made algo)  on the keywords to find the matching imag 
a=[]
f=open("your_file.txt","r")
a=f.read().split("\n\n\n\n===================================\n\n")
# print(len(a))
a.pop()
print(a)

slides=[]
sl=open("a.txt","r")
slides=sl.read().split("\n")
slides.pop()
print(slides)

lis=a
lisMatch=[]
serch = input("enter the string \n")

# serch.lower()
if(serch in lis):
    print(lis.index(serch))
else:
    # print("fussy on the way")
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
imgto=[]
kk=0
img=[]
import cv2
for i in range(len(lisMatch)):
    print(i)
    if (lisMatch[i]>90):
        img.append(cv2.imread(slides[(int)(i)]))
        kk=kk+1
        print("match")
        name=" " + str(kk) +" "+ slides[(int)(i)]
        cv2.imshow(name, img[kk-1])
# imgToShow=lisMatch.index(max(lisMatch))
# print(imgToShow)

# img = cv2.imread(slides[fimgToShow])
# cv2.imshow("answer",img)
cv2.waitKey()
