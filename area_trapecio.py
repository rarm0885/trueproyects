print("""Ingresa Altura(a), Base menor(b) y la Base mediana(m):
(separa los datos con espacios...)
""")
a, b, m = map(int,input().split())

c = (2*m)-b
area_trapecio = ((c+b)*a)/2

print(area_trapecio)