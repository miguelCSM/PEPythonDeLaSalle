# -*- coding: utf-8 -*-
# Para poder escribir con caracteres especiales

#%% Ciclo while 

"""Solicitar una contraseña y la confimarción de ella y dar la
bienvenida al usuario cuando esta coincidad (Si importa el orden M y m)
"""

errores = 0
# Solicita contraseñas
password = input("Ingrese la contraseña que desea utilizar\n")
passConfirm = input("Confirme su contraseña\n")

# compara la contraseña, si esta es diferente entra al ciclo
while (password != passConfirm):
    passConfirm = input("La contraseña no coincide, vuelva a ingresarla")
    errores +=1   
    if (errores>=3):
        print("Contacte con el centro de computo para restaurar contraseña")
        break#Rompe cualquier tipo de ciclo
        
if (errores<3):
    print("Se ha dado de alta exitosamente con ", errores,"errores")    