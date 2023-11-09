import random
cnt=0
def op1(cnt):
    while 1:
        x=random.randint(0,100)
        y=random.randint(0,100)
        print("Introduce el resultado de: ",x," x ",y)
        z=int(input())
        while z!=x*y:
            print("Incorrecto, ¿Quieres intentar de nuevo?")
            s=input()
            if s=="no":
               break
            else:
                print("Introduce tu nueva respuesta: ")
                z=int(input())
                
                    
            
        if z==x*y:
            print("Correcto!")
            cnt+=1
        print("¿Quieres resolver otra multiplicacion?")
        p=input()
        if p=="no":
            return cnt
            break
        
        
        
def op2(cnt):
    ar1=open("Estados.txt",'r')
    ar2=open("capitales.txt",'r')
    est=[]
    cap=[]
    for i in ar1:
        i=i.replace('\n','')
        est=est+[i]
   
    for i in ar2:
        i=i.replace('\n','')
        cap=cap+[i]
    while 1:
        ind=random.randint(0,31)

        print("Dime la capital del estado de ",est[ind])
        x=input()

        while x!=cap[ind]:
            print("Incorrecto ¿Quieres intentar de nuevo?")
            s=input()
            if s=="no":
                break
            else:
                print("Introduzca la capital: ")
                x=input()
        if x==cap[ind]:
            print("Correcto!")
            cnt+=1
            return cnt
        print("¿Quieres intentar otro estado?")
        s=input()
        if s=="no":
            return cnt
            break 

def op3(cnt):
    while 1:
        a=random.randint(0,50)
        b=random.randint(0,50)
        c=random.randint(0,50)
        if a<b:
            tmp=b
            b=a
            a=tmp
        x=input("Escoja el modo de juego:1(Fracciones impropias a mixtas),2(Mixtas a impropias)")
        if x=="1":
            print("Convierte",a,"/",b,"a fraccion mixta: ")
            e=int(input("Introduce la parte entera: "))
            d=(input("Introduce la parte decimal: (Ejemplo de respuesta: 1/2) "))
            res=str(a%b)
            c=str(b)
            while e!=a//b or d!=res+"/"+c:
                print("Incorrecto, Quieres volver a intentarlo?")
                s=input()
                if s=='no':
                    break
                else:
                    e=int(input("Introduce la parte entera"))
                    d=(input("Introduce la parte decimal"))
            if e==a//b and d==res+"/"+c:
                print("Correcto!")
                cnt+=1
            print("Quieres hacer otro ejercicio?")
            s=input()
            if s=="no":
                return cnt
                break
        elif x=='2':
            if a>b:
                tempo=a
                a=b
                b=tempo
            print("Convierte",c," ",a,"/",b, " a impropia")
            d=input("Introduce la fraccion: (Ejemplo de respuesta: 1/2)")
            ans=str(c*b+a)
            res=str(b)
            while d!=ans+"/"+res:
                print("Incorrecto,¿Quieres intentar de nuevo?")
                s=input()
                if s=='no':
                    break
                else:
                    print("Introduce de nuevo tu respuesta: ")
                    d=input()
            if d==ans+"/"+res:
                print("Correcto")
                cnt+=1
            print("¿Quieres hacer otro ejercicio?")
            s=input()
            if s=="no":
                return cnt
                break
                
def op4(cnt):
    while 1:
        a=random.randint(-8,8)
        b=random.randint(1,9)
        ans=(b*(10**a))
        ans1=str(b)+" x 10^"+str(a)
        
        z=int(input("Escoja el modo de juego:1(Notacion cientifica a decimal),2(Decimal a notacion cientifica): "))
        
        if z==1:
            print("Convierte a decimal "+ans1)
            e=float(input())
            while e!=ans:
                print("Respuesta incorrecta")
                print("Quieres volver a intentarlo? ")
                m=input()
                if m=="no":
                    break
                else:
                    e=float(input("Introduce de nuevo tu respuesta: "))
            if e==ans:
                print("¡Correcto!")
                cnt+=1
            print("¿Quieres hacer otro ejercicio?")
            v=input()   
            if v=="no":
                return cnt
                break
        
        if z==2:
            print("Convierte a notacion cientifica: (Ejemplo de respuesta: 3 x 10^4)"+str(ans))
            e=(input())
            while e!=ans1:
                print("Respuesta incorrecta")
                print("Quieres volver a intentarlo? ")
                m=input()
                if m=="no":
                    break
                else:
                    e=(input("Introduce de nuevo tu respuesta: "))
            if e==ans1:
                print("Correcto")
                cnt+=1
            print("¿Quieres hacer otro ejercicio?")
            v=input()  
            if v=="no":
                return cnt
                break
            
                    
                    
                    
                
            



while 1:
    print("Bienvenidos a la aplicacion de repaso para ciencias, matematicas y lecturas")
    print()

    print("Introduce que numero de juego quieres jugar: ")
    print("1:Multiplicaciones con numeros de hasta dos digitos")
    print("2:Capitales del pais")
    print("3:Fraciones mixtas a impropias o impropias a mixtas")
    print("4: Notacion cientifica")
    print("\nEl numero de respuestas correctas es: ",cnt)
    n=int(input())

    if n==1:
        cnt=op1(cnt)
    elif n==2:
        cnt=op2(cnt)
    elif n==3:
        cnt=op3(cnt)
    elif n==4:
        cnt=op4(cnt)
    
                
            
            
            

       
            
            
        
        