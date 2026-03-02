#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importar librería hashlib

import hashlib

# Archivo hash

hash_file = "  "

# Pedir usuario que ingrese directorio en el que se encuentra el diccionario

dic_file = input("Ingrese la dirección del archivo de diccionario: ")

# Leer palabras que están en el diccionario

with open(dic_file, 'r') as file:
    
    diccionario = [line.strip() for line in file] # Leer cada línea del diccionario 
    
    for password in diccionario:
        
        hash_calculado = hashlib.sha256(password.encode()).hexdigest()
        
        if hash_calculado == hash_file:
            
            print("La contraseña original es: " + password)
            break
            
        else:
            print("La contraseña no se encuentra en el diccionario")


# In[ ]:




