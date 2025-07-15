with open("C:/Users/alejo/OneDrive/Escritorio/PC/UNIVERSIDAD/PROGRAMACIÓN DE COMPUTADORES/VSCODE/RETO11/retoonce.txt", "r", encoding="utf-8") as ejercicio:
    texto=ejercicio.read().lower()

vocales='aeiou'
consonantes='qwrtypsdfghjklñzxcvbnm'
contadorpala={}

countv=0
countc=0
for i in texto:
    if i in vocales:
        countv+=1
    elif i in consonantes:
        countc+=1

for palabra in texto.split():
    palabra_limpia=''
    for letra in palabra:
        if letra.isalpha():
            palabra_limpia += letra
    if palabra_limpia!='':
        if palabra_limpia in contadorpala:
            contadorpala[palabra_limpia]+=1
        else:
            contadorpala[palabra_limpia]=1

top50=sorted(contadorpala.items(),key=lambda x: x[1],reverse=True)[:50]

print(f'Cantidad de vocales: {countv}')
print(f'Cantidad de consonantes: {countc}')
print(f'50 palabras más escritas: {top50}')