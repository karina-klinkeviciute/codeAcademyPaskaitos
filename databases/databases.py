import sqlite3

conn = sqlite3.connect('zmones.db')
c = conn.cursor()

query = '''
CREATE TABLE IF NOT EXISTS draugai (
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    email VARCHAR(100)
);
'''
c.execute(query)

# query_insert = '''
# INSERT INTO draugai (f_name, l_name, email)
# VALUES ("Jonas", "Viršaitis", "ponasjonas@gmail.com");
# '''

# c.execute(query_insert)


# with conn:
#     c.execute("INSERT INTO draugai VALUES ('Domantas', 'Rutkauskas', 'd.rutkauskas@imone.lt')")
#     c.execute("INSERT INTO draugai VALUES ('Rimas', 'Radzevičius', 'RR@gmail.com')")

with conn:
    c.execute("SELECT * From draugai WHERE l_name LIKE 'R%'")
    irasas = c.fetchone()
    while irasas:
        print(f"Vardas: {irasas[0]} Pavarde: {irasas[1]}, email: {irasas[2]}" )
        irasas = c.fetchone()

# with conn:
#     c.execute("UPDATE draugai SET email='naujas.email@aol.com' WHERE l_name='Radzevičius'")

vardas = "Rimas"

uzklausa = f"SELECT * From draugai WHERE f_name =?"

print(uzklausa)

with conn:
    c.execute(uzklausa, (vardas, ))
    print(c.fetchall())
# with conn:
#     c.execute("DELETE from draugai WHERE l_name='Rutkauskas'")

draugai = [
    ('Jonas', 'Jonaitis', 'jjonaitis@mail.lt'),
    ('Petras', 'Miltelis', 'petras@pastas.lt'),
    ('Inga', 'Guobytė', 'ingag@koksskirtumas.lt')
]

with conn:
    c.executemany("INSERT INTO draugai VALUES(?,?,?)", draugai)


conn.commit()
conn.close()


