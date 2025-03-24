from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from claytonbraden in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_claytonbraden_db_user:oCclnkfeDRkdEGjWij43wCIVuQ5g0GvD@dpg-cvg95flrie7s73bnf35g-a/lab_10_claytonbraden_db")
    conn.close()
    return 'Database Connection sucessful;'
