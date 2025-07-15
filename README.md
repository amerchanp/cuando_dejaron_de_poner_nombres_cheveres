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


