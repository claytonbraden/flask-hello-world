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
    
    # Drop table if it exists
    cur.execute('''
    DROP TABLE IF EXISTS Basketball;
    ''')
    
    #Create table
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
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2) AS new_data(First, Last, City, Name, Number)
    WHERE NOT EXISTS (
        SELECT 1 FROM Basketball WHERE First = new_data.First AND Last = new_data.Last AND Name = new_data.Name
    );
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
    #get column names
    columns = [desc[0] for desc in cur.description]
    conn.commit()
    conn.close()
    
    #Create html table with format
    htmlTable = '<table border="1"><tr>'
    
    #Add column names with header cells
    for column in columns:
        htmlTable += f'<th>{column}</th>'
    
    #Add rows to html table
    html_table += '</tr>'
 
    for row in records:
        html_table += '<tr>'    #starts a new row
        for cell in row:
            html_table += f'<td>{cell}</td>' #creates new cell to 
        html_table += '</tr>'  #ends row
    
    html_table += '</table>' #ends the table
    

    
    return html_table

