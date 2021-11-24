import math
print("Egyenleteket oldok meg.")
print("1-es menüpont: Elsőfokú egyenlet")
print("2-es menüpont: Másodfokú egyenlet")
menüpont=float(input("Kérem a választott menüpont számát: "))
if menüpont==1:
    print("a*x+b=0 alakban kérem az egyenletet átalakítani.")
    a=float(input("Add meg az a értékét: "))
    b=float(input("Add meg a b értékét: "))
    if a==0:
        if b==0:
            print("Minden x megoldás!")
        else:
            print("Nincs megoldás!")
    else:
        x=-b/a
        print("Az ",x," megoldás!")
elif menüpont==2:
    print("a*x*x+b*x+c=0 alakban kérem az egyenletet átalakítani.")
    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))

    if a==0:
        #Ez elsőfokú alakra alakul ekkor!


        if b==0:
            if c==0:
                print("Minden x megoldás!")
            else:
                print("Nincs megoldás!")
        else:
            x=-c/b
            print("Az ",x," megoldás!")

            print("")
    else:
        #Ez a valódi másodfokú eset!

        x1=(b*b)-4*a*c
        if x1<0:
            print("Nem lehet kisebb mint 0, tehát nincs megoldás a valós számok halmazán.")
        elif x1==0:
            megoldás=-b/2*a
            print("Ez a megoldás: ",megoldás)
        elif x1>0:
            gyok=math.sqrt(x1)    
            x2=gyok-b
            x3=-gyok-b
            x4=2*a
            res1=x2/x4
            res2=x3/x4
            print(res1,res2)
