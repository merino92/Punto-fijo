#!/usr/bin/env python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- 
#
# main.py
# Copyright (C) 2017 merinocampos <curtidoilmb@gmail.com>
# 
# puntofijo is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# puntofijo is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


def fx(x):
	return ((-3*pow(x,2))-7)/pow(x,2) 
#retorna la funcion resuelta
p1=float(input("ingrese p1:"))
n=int(input("ingrese las iteraciones:"))
t=float(input("ingrese la tolerancia:"))
bandera=0
#le asigno un numero a la variables
for i in range(1,n):
	p=fx(p1)
	if abs(p1-p)<t:
		print "f(x)="+ str(p1)
		print "se econtro en la iteracion N:"+str(i)
		bandera=1
		break
		#rompe el ciclo for 
	else:
		p1=p
if bandera==0:
	print "error"
#si bandera no cambia imprime el error


