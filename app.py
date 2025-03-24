from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from claytonbraden in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_claytonbraden_db_user:oCclnkfeDRkdEGjWij43wCIVuQ5g0GvD@dpg-cvg95flrie7s73bnf35g-a.oregon-postgres.render.com/lab_10_claytonbraden_db")
    conn.close()
    return 'Database Connection sucessful'

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

    
