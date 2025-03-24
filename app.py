from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from claytonbraden in 3308'

#route to test our database link from render
@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_claytonbraden_db_user:oCclnkfeDRkdEGjWij43wCIVuQ5g0GvD@dpg-cvg95flrie7s73bnf35g-a.oregon-postgres.render.com/lab_10_claytonbraden_db")
    conn.close()
    return 'Database Connection sucessful'

#route to create a table using render db link
@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://lab_10_claytonbraden_db_user:oCclnkfeDRkdEGjWij43wCIVuQ5g0GvD@dpg-cvg95flrie7s73bnf35g-a.oregon-postgres.render.com/lab_10_claytonbraden_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return 'Basketball Table Succesfully Created'

#route to populate our db table with information
@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect("postgresql://lab_10_claytonbraden_db_user:oCclnkfeDRkdEGjWij43wCIVuQ5g0GvD@dpg-cvg95flrie7s73bnf35g-a.oregon-postgres.render.com/lab_10_claytonbraden_db")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
''')
    conn.commit()
    conn.close()
    return 'Basketball Table Sucesfully populated'

#route to select and show our populated table

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect("postgresql://lab_10_claytonbraden_db_user:oCclnkfeDRkdEGjWij43wCIVuQ5g0GvD@dpg-cvg95flrie7s73bnf35g-a.oregon-postgres.render.com/lab_10_claytonbraden_db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    
    conn.commit()
    conn.close()
    
     # Convert records to HTML format
    record_html = "<br>".join([f"First: {row[0]}, Last: {row[1]}, City: {row[2]}, Name: {row[3]}, Number: {row[4]}" for row in records])
    
    return record_html
