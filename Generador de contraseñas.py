#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string
import random

# Variable longitud de contraseña 

longitud = int(input("Ingrese la longitud de la contraseña: "))

# Caracteres incluyendo letras, dígitos y puntuación

caracteres = string.ascii_letters + string.digits + string.punctuation

# Imprimir caracteres

print(caracteres)

# Contraseña resultante

contrasena = "".join(random.choice(caracteres) for i in range(longitud))

# Imprimir contraseña

print("La contraseña generada es: " + contrasena)


# In[ ]:




