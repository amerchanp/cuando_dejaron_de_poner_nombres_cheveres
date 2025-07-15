# RETO 11
¿Qué hacen los siguientes métodos de trings?:
### .endswith()
Valida si un string termina con el prefijo que esté dentro de los paréntesis, dará True o False si no.

### .startswith()
Valida si un string comieza con el sufijo que esté dentro de los paréntesis, dará True o False si no.

### .isalpha()
Dará True si todos los caracteres son letras.

### .isalnum()
Dará True si todos los caracteres son letras o números (sin espacios ni símbolos).

### .isdigit()
Devuelve True si todos los caracteres son dígitos numéricos 0-9.

### .isspace()
Devuelve True si todos los caracteres son espacios.

### .istitle()
Dará True si el primer caracter está en mayúscula y el resto en minúscula.

### .islower()
Devuelve True si todos los caracteres alfabéticos están en minúscula.

### .isupper()
Devuelve True si todos los caracteres alfabéticos están en mayúscula.

## Ejemplos
```python
# 1. endswith()
print("endswith:", "hola.py".endswith(".py"))         # True

# 2. startswith()
print("startswith:", "hola.py".startswith("ho"))      # True

# 3. isalpha()
print("isalpha 1:", "Python".isalpha())               # True
print("isalpha 2:", "Python3".isalpha())              # False

# 4. isalnum()
print("isalnum 1:", "Python3".isalnum())              # True
print("isalnum 2:", "Python 3".isalnum())             # False

# 5. isdigit()
print("isdigit 1:", "12345".isdigit())                # True
print("isdigit 2:", "123a".isdigit())                 # False

# 6. isspace()
print("isspace 1:", "   ".isspace())                  # True
print("isspace 2:", " a ".isspace())                  # False

# 7. istitle()
print("istitle 1:", "Hola Mundo".istitle())           # True
print("istitle 2:", "Hola mundo".istitle())           # False

# 8. islower()
print("islower 1:", "hola mundo".islower())           # True
print("islower 2:", "Hola mundo".islower())           # False

# 9. isupper()
print("isupper 1:", "PYTHON".isupper())               # True
print("isupper 2:", "Python".isupper())               # False

```
## Ejercicio
En esta actividad teníamos que leer un archivo de texto con Python y hacer tres cosas: contar cuántas vocales y consonantes había, y mostrar las 50 palabras que más se repiten. Para eso, primero abrí el archivo y pasé todo el texto a minúsculas. Luego conté letra por letra y también fui guardando cuántas veces aparecía cada palabra (quitando signos y cosas raras). Al final, ordené las palabras por frecuencia y mostré los resultados.
```python
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
```

Muchas gracias.
