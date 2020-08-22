#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicio de practica 
Crear las funciones para luego crear una base de datos
usando los datos de una libreria csv
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3
import csv

def create_schema():
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute("""
                DROP TABLE IF EXISTS libros;
            """)
    c.execute("""
        CREATE TABLE libros(
            [id] INTEGER PRIMARY KEY AUTOINCREMENT,
            [titulo] TEXTO NOT NULL,
            [cantidad_paginas] INTEGER,
            [autor] TEXTO NOT NULL   
        );
        """)
    conn.commit()
    conn.close()
group = []
def archivo_csv():
    with open('libreria.csv', 'r') as prop:
        data = list(csv.DictReader(prop))
    dato = []
    for i in range(len(data)):
        row = data[i]
        dato_1 = row.get('titulo')
        dato_2 = int(row.pop('cantidad_paginas', None))
        dato_3 = row.get('autor')
        group.append((dato_1, dato_2, dato_3))
    return   

def fill(group):
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.executemany("""INSERT INTO libros (titulo, cantidad_paginas, autor)
    VALUES (?, ?, ?);""", group)
    conn.commit()
    conn.close()

def fetch(id): 
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute("SELECT * FROM libros")
    data = c.fetchall()
    if id == 0:
        for row in data:
            print(row)
    else:
        for row in data:
            if row[0] == id:
                print(row)
                break
            if id > len(data):
                print('ERROR  No existe dicho "id"')
                break
    print('')

def search_author(book_title):
    conn = sqlite3.connect('libreria.db')
    c = conn.cursor()
    c.execute("SELECT * FROM libros")
    data = c.fetchall()
    for row in data:
        if row[1] == book_title:
            print(row[3])


if __name__ == '__main__':
    create_schema()
    archivo_csv()
    fill(group)
    fetch(int(input('Ingrese el valor de "id": ')))
    search_author('Relato de un naufrago')
