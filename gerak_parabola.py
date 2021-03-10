# -*- coding: utf-8 -*-
"""Gerak Parabola.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RiihXCTzlhrtjg1bjDqlyTVsp0lpa-Pz
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# variabel awal
y0 = 1
x0 = 0
t = 0
v0 = 100
angle = math.radians(30)
g = -9.8
dt = 0.001

# array untuk menyimpan data
x = x0
y = y0
waktu = [t]
jarak = [x]
ketinggian = [y]

# solusi numerik
vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)

# t = t+dt
# vy = vy + (g*dt)
# x = x + (vx*dt)
# y = y + (vy*dt)

while True:
  t = t+dt
  vy = vy + (g*dt)
  x = x + (vx*dt)
  y = y + (vy*dt)
  waktu.append(t)
  jarak.append(x)
  ketinggian.append(y)
  if y<=0:
    break

# solusi analitikal
xA = x0
yA = y0
jarakA = [xA]
ketinggianA = [yA]

for i in waktu:
  xA = v0*math.cos(angle)*i
  yA = (0.5*g*i**2) + (v0*math.sin(angle)*i)
  jarakA.append(xA) 
  ketinggianA.append(yA)

plt.plot(jarak, ketinggian, c='b', label='numerical')
plt.plot(jarakA, ketinggianA, c='r', label='analitikal')
plt.xlabel('jarak')
plt.ylabel('ketinggian')
plt.xlim(-50, 1000)
plt.ylim(-10, 150)
plt.legend()
plt.show()

tmax = (2*v0*math.sin(angle))/(-g)
xmax = v0*math.cos(angle)*v0
ymax = ((v0**2)*(math.sin(angle)**2))/(-2*g) 
print("waktu numerikal= ", waktu[len(waktu)-1])
print("waktu analitikal= ", tmax)
print("jarak numerikal= ", jarak[len(jarak)-1])
print("jarak analitikal= ", xmax)
print("tinggi maksimum numerikal= ", max(ketinggian))
print("tinggi maksimum analitikal= ", ymax)