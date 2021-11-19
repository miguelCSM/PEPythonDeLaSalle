# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 07:30:42 2021

@author: migue
"""

MiLista = ["Miguel", "Krauus", "Maribel", "Krauus", "Miguel", "Krauus"]

contar = {i:MiLista.count(i) for i in MiLista}

print(contar)