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
        
