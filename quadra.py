import math
import sys
import numpy as np
import matplotlib.pyplot as plt

#name2=str(input("please provide the name of the old dump file "))
#name1=str(input("please provide the name of the new dump file "))
##111111111111111111111111111111111111111111111111111111111111111111111111111111########################################################################
c=open("dump.relaxedge10.0","r+")

k=c.readlines()
i=9
array=([])
brray=([])
for i in range(9):

    a=k[i]
    a1=a.split()
    a1.append("\n")
    a1="".join(a1)
    brray.append(a1)           
          
    k[i]=" ".join(a1)
i=9
while True:
    try:
        a=k[i]
        
        a1=a.split(" ")
#        a1.append("\n")

        array.append(a1)           
        
        
        i=i+1
    except IndexError:
            print(i)
           
            break
array.sort(key=lambda x: int(x[0]))

i=0
while True:
    try:
        a=array[i]
        a=" ".join(a)
        array[i]=a
        i=i+1
    except IndexError:
           
            break 
c.close()
d=open("dump.relaxedgeafter.0","w")
d.write("".join((brray)))
d.write("".join((array)))
d.close()

##2222222222222222222222222222222222222222222222222222222222222222222222222222222
c=open("dump.edge.470","r+")
k=c.readlines()
i=9
array=([])
brray=([])
for i in range(9):

    a=k[i]
    a1=a.split()
    a1.append("\n")
    a1="".join(a1)
    brray.append(a1)           
          
    k[i]=" ".join(a1)
i=9
while True:
    try:
        a=k[i]
        
        a1=a.split(" ")
#        a1.append("\n")

        array.append(a1)           
        
        
        i=i+1
    except IndexError:
            print(i)
           
            break
array.sort(key=lambda x: int(x[0]))

i=0
while True:
    try:
        a=array[i]
        a=" ".join(a)
        array[i]=a
        i=i+1
    except IndexError:
           
            break 
c.close()
d=open("dump.edge302after.0","w")
d.write("".join((brray)))
d.write("".join((array)))
d.close()


################################################################################################read dump file

c=open("dump.relaxedgeafter.0","r+")

k=c.readlines()
#################################################################################################the calculation part
i=9



print("")
print("")
print("")
print("")
print("-----------------------------------------------")
print("-----------------------------------------------")



i=9
qarray=([])
while True:
    try:
        a=k[i]
        a1=a.split()
        if a1[4]=="0.737909" and float(a1[2])>29 and float(a1[2])<30 :
#            a1.append("\n")
#            a1=" ".join(a1)
#            qarray.append(a1)
            pass
        elif  a1[4]=="0.737909" and float(a1[2])<-24 and float(a1[2])>-25:
#            a1.append("\n")
#            a1=" ".join(a1)
#            qarray.append(a1)           
            pass 
        else:
            a1[0]="0"   
        


        
        a1.append("\n")
        k[i]=" ".join(a1)
        
        i=i+1
    except IndexError:
            print(i)
 
            break
########################################################################



c22=open("dump.edge302after.0","r+")

T=c22.readlines()
i=9
checkarray=([])
while True:
    try:


        b=T[i]
        a=k[i]
        a1=a.split()
        a2=b.split()

        if a1[0]!="0":
            a2.append("\n")
            a2=" ".join(a2)
            checkarray.append(a2)
            
       
        
        i=i+1
    except IndexError:
            print(i)
           
            break

print("")
print("")
print("")
print("")
print("The simulation is completed.")
c.close()
c22.close()
i=0


for i in range(160):

    W=checkarray[i]
    W=W.split(" ")
    checkarray[i]=W
    i=i+1



#checkarray.sort(key=lambda x: float(x[3]))
i=0
for i in range(160):
    a=checkarray[i]
    a=" ".join(a)
    checkarray[i]=a
    i=i+1
        



    






d=open("dump.allcheckedbeforemini27.0","w")
d.write("".join((checkarray)))
d.close()
i=9
#?????????????????????????????????????????????????????/
def pointp():
    c=open("dispoint.0","r+")

    k=c.readlines()
    i=9
    darray=([])
    while True:
        try:
            a=k[i]
            a1=a.split()
            if a1[4]=="0.737909" or a1[4]=="-0.737909" :
                 darray.append(a1[3])
    
        
            i=i+1
        except IndexError:
                print(i)
                print(darray)
                break
#?????????????????????????????????????????????????????????
#########################################################################
def plotting(a):

    c23=open(a,"r+")

    I=c23.readlines()
    
    i=0
    P=0
    Q=1
    dataY=np.zeros((80,2))
    dataX1=np.zeros((80,1))
    while True:
        try:


            C=I[i]
            
            a3=C.split()
            
            if i%2 == 0:
                dataY[i-P][0]=a3[3]
            
                dataX1[i-P]=a3[3]
                P=P+1
            else:
                dataY[i-Q][1]=a3[3]
                Q=Q+1
       
        
            i=i+1
        except IndexError:
            print(i)
           
            break
    DATA1=(np.diff(dataY))

    return(dataX1,DATA1)
plt.ylim(0,6)
dataX1,DATA1=plotting("dump.allcheckedbeforeminimize8.28.0")
##<<
#r=plt.plot(dataX1,np.tan(DATA1/100)*(180/np.pi),'-', label='15before')  #15before

dataX2,DATA2=plotting("dump.allchecked9.4.0")
 
g=plt.plot(dataX2,np.tan(DATA2/100)*(180/np.pi),'-', label='15 dislocation')  #15


dataX3,DATA3=plotting("dump.allchecked19.0")
#y=plt.plot(dataX3,np.tan(DATA3/100)*(180/np.pi),'--', label='19before')  # 19before
dataX4,DATA4=plotting("dump.allcheckedbeforemini19.0")
b=plt.plot(dataX4,np.tan(DATA4/100)*(180/np.pi),'--', label='19 dislocation')#19

dataX5,DATA5=plotting("dump.allcheckedbeforemini23.0")
#m=plt.plot(dataX5,np.tan(DATA5/100)*(180/np.pi),'-.', label='23before')   # 23before
dataX6,DATA6=plotting("dump.allchecked23.0")
c=plt.plot(dataX6,np.tan(DATA6/100)*(180/np.pi),'-.', label='23 dislocation')# 23

dataX7,DATA7=plotting("dump.allchecked27.0")
#k=plt.plot(dataX7,np.tan(DATA7/100)*(180/np.pi),'^', label='27before')   # 27before

dataX8,DATA8=plotting("dump.allcheckedbeforemini27.0")
w=plt.plot(dataX8,np.tan(DATA8/100)*(180/np.pi),'^', label='27 dislocation')   # 27             


dataX9,DATA9=plotting("dump.allcheckedbeforemini31.0")
#w=plt.plot(dataX9,np.tan(DATA9/100)*(180/np.pi),'b.', label='31before')   # 31 before


dataX10,DATA10=plotting("dump.allchecked31.0")
w=plt.plot(dataX10,np.tan(DATA10/100)*(180/np.pi),'b.', label='31 dislocation')   # 31
plt.legend()
#plt.title("characteristics angles along Y axis under different dislocation number before energy minimization  ")

plt.xlabel("Y coordinate in Angstrom") 
plt.ylabel("inclination angle in degree") 
plt.show()



#i=0
#j=0
#H=0
#dx1=dataX1
#DX1=DATA1
#for i in range(len(dx1)):
#    for j in range(len(darray)):
#        cp1=round(float(darray[j]),-1)
#        cp2=round(float(dataX1[i]),-1)
#        if cp1==cp2:
#            dx1[i][0]=cp1
#            print("a")
#            H=1
#        j=j+1
#    if H==0:
#        dx1[i][0]=0
#        DX1[i][0]=0
#    H=0
#    i=i+1
#plt.ylim(0,10)
