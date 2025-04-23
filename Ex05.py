#Faça um programa que leia o comprimento do catetp oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa
co = float(input('Comprimento do cateto oposto: ')
ca = float(input('Comprimento do cateto adjacente: ')
hi = (co ** 2 + ca ** 2) ** (1/2)
 print('A hipotenusa vai medir {:.2f}'.format(hi))
# sugunda forma 
import math
co  = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
  print('A hipotenusa vai medir {hi:.2f}')


