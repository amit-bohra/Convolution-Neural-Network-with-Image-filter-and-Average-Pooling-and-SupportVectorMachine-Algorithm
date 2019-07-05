import numpy as np
from sklearn import svm
import cv2
from sklearn.neural_network import MLPClassifier as mp
c1=cv2.imread(r'1st type one image') #Provide Path for 1st type 1 image
c2=cv2.imread(r'2n Type one image') #Provide Path for 2nd type 1 image
x1=cv2.imread(r'1st type two image') #Provide Path for 1st type 2 image
x2=cv2.imread(r'2nd type two image') #Provide Path for 2n type 2 image
circle1=cv2.cvtColor(c1,cv2.COLOR_BGR2GRAY)
circle2=cv2.cvtColor(c2,cv2.COLOR_BGR2GRAY)
cross1=cv2.cvtColor(x1,cv2.COLOR_BGR2GRAY)
cross2=cv2.cvtColor(x2,cv2.COLOR_BGR2GRAY)
print(cross1)
print('hello')
count=0
recount=0
population=[circle1,circle2,cross1,cross2]
kernel=[[1,1,1],[1,1,1],[1,1,1]]
kernel=np.array(kernel)
while(count<4):
    while(recount<4):
        img=population[recount]
        lastx=len(img[:,1])-3
        lasty=len(img[:,1])-3
        nlastx=(lastx+3)//3
        nlasty=(lasty+3)//3
        for i in range(0,lastx,3):
            for j in range(0,lasty,3):
                a=i+3
                b=j+3
                kernelx=-1
                listy=[]
                for k in range(i,a):
                    kernelx+=1
                    kernely=-1
                    for l in range(j,b):
                        '''print('i',i)
                        print('j',j)
                        print('k',k)
                        print('a',a)
                        print('l',l)
                        print('b',b)
                        print('stop')
                        print(img[k,l])'''
                        kernely+=1
                        temp=img[k,l]*kernel[kernelx,kernely]
                        listy.append(temp)
                #print(listy)
                #print('happy')
                sumly=(sum(listy))//27
                if(i==0) and (j==0):
                    img[i,j]=sumly
                elif(i==0) and (j!=0):
                    img[i,j-3]=sumly
                elif(j==0) and (i!=0):
                    img[i-3,j]=sumly
        img=np.delete(img,np.s_[nlastx:lastx+3],axis=0)
        img=np.delete(img,np.s_[nlasty:lasty+3],axis=1)
        #print('dfshadjfhjksdhjfhajkshfjkhskjdfhkjfahdksjhjaskdhjjfsajfklsdjfklajdkfjakljfklsdjaklsdjfkljfsdkljkfjsad')
        #print(img)
        population[recount]=img
        recount+=1
        cv2.imshow('a',img)
    count+=1
    recount=0
count=0
final_list=[]
while(count<4):
    a=population[count]
    a=a.reshape(9)
    final_list.append(a)
    count+=1
print(final_list)
final_list=np.array(final_list)
final_list=(final_list)

l=['circle','circle','cross','cross']
a=1
while(True):
    a+=1
    b=a*100
    clf=mp(hidden_layer_sizes=(8,5),max_iter=b,random_state=a)  #c=1 ignore 1 point in each category if kernel is not linear it will be rpf
    trained=clf.fit(final_list,l)
    res=trained.predict(final_list)
    print(res)

    
    

                
                    
                    
            
        
