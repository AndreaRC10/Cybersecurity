#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importar librería socket

import socket 

# Pedir al usuario la dirección IP que vamos a usar

ip = input("Ingrese la dirección IP a escanear: ")

# Bucle for para escanear puertos; INET por iPv4 y STREAM por TCP

for puerto in range(1,65535):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.settimeout(5)
    
    result = sock.connect_ex((ip, puerto))
    
    if result == 0:
        print("Puerto abierto: " + str(puerto))
    
    sock.close()
    
else:
        print("Puerto cerrado: " + str(puerto))
        
        
    


# In[ ]:




