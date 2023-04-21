"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

import csv

customer = []
with open('north_data/customers_data.csv', 'r', encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")
    for i in file_reader:
        customer.append(tuple(i))

with psycopg2.connect(host="localhost", database="north", user="postgres", password="vadim$1983") as conn:
    with conn.cursor() as cur:
        cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', customer)
        cur.execute('SELECT * FROM customers')
        rows = cur.fetchall()
        for row in rows:
            print(row)

conn.close()







# orders = []
# with open('north_data/orders_data.csv', 'r',encoding='utf-8') as file:
#     file_reader = csv.reader(file, delimiter=",")
#     for i in file_reader:
#         customers.append(tuple(i))
#
# print(customers[1:])
