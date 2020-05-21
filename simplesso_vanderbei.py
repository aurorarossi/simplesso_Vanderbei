#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division
from fractions import Fraction
from numpy import *

class Tableau:
    #inizializzazione
    def __init__(self, obj, prob_type):
        self.rows = []
        self.cons = []
        self.nonbasis = []
        self.basis=[]
        if prob_type == 'max':
            self.obj =[Fraction(x) for x in obj]
        elif prob_type == 'min':
            self.obj =[-Fraction(x) for x in obj]
     #vincoli
    def aggiungi_vincolo(self, expression, value):
        self.cons.append(Fraction(value))
        self.rows.append([-Fraction(x) for x in expression])
    #print del tablau
    def mostra_tableau(self):
        s = ' '
        #prima riga di etichette
        s += '\t-'
        for i in range(len(self.obj)-1):
            s += '\t'+str(self.nonbasis[i])
        #colonna di etichette
        s += '\nz'
        for i in range(0,len(self.obj)):
            s += '\t' + str(self.obj[i])
        
        for i in range(len(self.rows)):
            s += '\n'+str(self.basis[i])
            for j in range(0,len(self.rows[i])):
                s += '\t' + str(self.rows[i][j])
        
        print(s)

    def crea_primo_tableau(self):
        for i in range(len(self.cons)):
            self.rows[i].insert(0,self.cons[i])
        self.obj = array([Fraction(0)]+self.obj)
        
        dim = len(self.rows)
        dim2=len(self.obj)
        for i in range(dim):
            self.basis += ["s"+str(1+i)]
            
        for i in range(1,dim2):
            self.nonbasis += ["x"+str(i)]

    def pivot(self,row,col):
        r=0
        c=0
        #individuo riga e colonna associato a etichette
        while self.basis[r]!=str(row):
            r+=1
        while self.nonbasis[c]!=str(col):
            c+=1
        c=c+1
        e = self.rows[r][c]
        self.basis[r]=str(col)
        self.nonbasis[c-1]=str(row)
        assert e != 0
        #cambio coefficienti tabella tranne riga e solonna pivot
        for i in range(len(self.rows)):
            for j in range(len(self.obj)):
                if i!=r and j!=c:
                    self.rows[i][j]=self.rows[i][j]-(self.rows[r][j]*self.rows[i][c])/e
        for j in range(len(self.obj)):
                if j!=c:
                    self.obj[j]=self.obj[j]-(self.rows[r][j]*self.obj[c])/e
        #cambio pivot
        self.rows[r][c]=1/self.rows[r][c]
        #cambio colonna pivot
        self.obj[c]=self.obj[c]/e
        for i in range(len(self.rows)):
            if i!=r:
                self.rows[i][c]=self.rows[i][c]/e
        #cambio riga pivot
        for i in range(len(self.obj)):
            if i!=c:
                self.rows[r][i]=-self.rows[r][i]/e
                
                

    
