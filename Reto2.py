
# Esta frase tiene 12 letras y ocupa 14 espacios en la memoria teniendo un total de 15 caracteres
frase = 'Curso de Python'

# Particionar los Strings
frase[9] # Retorna el caracter 'P'
frase[0:5] # Retorna el slice 'Curso'
frase[0:15:2] # Retorna el slice 'Crod yhn'
frase[:5] # Retorna el slice 'Curso'
frase[6:] # Retorna el slice 'de Python'
frase[6::3] # Retorna el slice 'dPh'

# Analizar Strings 
frase.len() # Retorna el tamaño de la cadena de caracteres
frase.count() # Retorna el número de veces que se repite un caracter en la cadena
frase.find # Busca un subString o caracter dentro de la cadena de caracteres
# Ejemplo
len(frase) # Retorna 15
frase.count('o') # Retorna 2
frase.count('o', 0, 8) # Retorna 1 (numero de 'o' desde el cero hasta el 8)
frase.find('rso') # Busca el substring 'rso' retorna 2

# Transformar Strings en Python
frase.upper() # Coloca todo el string en mayúscula
frase.lower() # Coloca todo el string en minúscula
frase.capitalize() # Coloca todo el primer en mayúscula
frase.title() # Coloca todo el primer carcater de cada palabra en mayúscula
#frase.replace(str1,str2) # Reemplaza un substring por otro
frase.strip() # Elimina los espacios innecesarios al inicio y fin del string
frase.rstrip() # Elimina los espacios innecesarios al fin del string
frase.lstrip() # Elimina los espacios innecesarios al inicio del string
# Ejemplo
frase.upper() # CURSO DE PYTHON
frase.lower() # curso de python
frase.capitalize() # Curso de python
frase.title() # Curso De Python
frase.replace('Python','Control') # Curso de Control

# Dividir caracteres
frase.split() # Separa la frase en: "Curso", "de", "Python"
'-'.join(frase) # Une la frase con el caracter especificado, antes del método join, en este caso con un guión. “Curso-de-Python”