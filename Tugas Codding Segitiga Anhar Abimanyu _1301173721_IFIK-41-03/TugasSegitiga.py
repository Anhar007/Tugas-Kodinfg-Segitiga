import math 

a = float(input(" Masukan angka untuk sisi a =  "))
b = float(input(" Masukan angka untuk sisi b =  "))
c = float(input(" Masukan angka untuk sisi c =  "))

X = max([a,b,c])

if((a == b) or (b == c) ):
	print("Segitiga Sama Sisi")
elif((a == b) or (b == c) or (a == c)):
	print("Segitiga Sama Kaki")
elif((X**2 == (a**2)+(b**2)) or (X**2 == (b**2)+(c**2)) or (X**2 == (a**2)+(c**2))):
	print("Segitiga Siku siku")
elif((X < (a**2)+(b**2)) or (X < (b**2)+(c**2)) or (X < (a**2)+(c**2))):
	print("Segitiga Sembarang")
elif((a <= 0 ) or (b <= 0) or (c <= 0)):
	print("Angka inputan tidak valid")
elif((X >= (a**2)+(b**2)) or (X >= (b**2)+(c**2)) or (X >= (a**2)+(c**2))):
	print("Angka inputan tidak valid")