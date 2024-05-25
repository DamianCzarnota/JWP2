import sqlalchemy as db

"""
Korzytając z bazy census (sqlite:///census.sqlite) wykonaj następujące polecenia:
• Nazwy stanów występujące w bazie.
• Policz populacje w stanie Alaska oraz New York w 2000 oraz 2008 roku
• Policz liczbę kobiet oraz mężczyzn w stanie New York w 2008 roku
"""

#Nazwy stanów występujące w bazie.
engine = db.create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload_with=engine)
query = db.select(census.c.state).distinct()
output = connection.execute(query)
print(output.fetchall())

#Policz populacje w stanie Alaska oraz NEW_YORK w 2000 oraz 2008
#Table('census', MetaData(), Column('state', VARCHAR(length=30), table=<census>), Column('sex', VARCHAR(length=1), table=<census>), Column('age', INTEGER(), table=<census>), Column('pop2000', INTEGER(), table=<census>), Column('pop2008', INTEGER(), table=<census>), schema=None)
stmt = db.select(
    census.c.state,
    db.func.sum(census.c.pop2008),
    db.func.sum(census.c.pop2000)
).where((census.c.state == "Alaska") | (census.c.state == "New York")).group_by(census.c.state)
results = connection.execute(stmt).fetchall()
print(results)

#Policz liczbę kobiet oraz mężczyzn w stanie New York w 2008 roku
stmt = (db.select(
    census.c.state,
    census.c.sex,
    db.func.sum(census.c.pop2008)
).where(census.c.state == "New York").group_by(census.c.sex))
results = connection.execute(stmt).fetchall()
print(results)

#zad 2

print("ZADANIE 2")

engine_2 = db.create_engine('sqlite:///college.db')
meta = db.MetaData()

#creating table
students_table = db.Table(
     'students', meta,
    db.Column('id', db.Integer, primary_key = True),
    db.Column('name', db.String),
    db.Column('age', db.Integer),
    db.Column('grade', db.Float),
)
meta.create_all(engine_2,checkfirst=True)
connection_2 = engine_2.connect()
students = db.Table('students', meta, autoload_with=engine_2)

#inserting new students
query = db.insert(students).values(name="Antoni Kowalski",age=19,grade=4.5)
connection_2.execute(query)
query = db.insert(students)
values_list = [{'name': "Stefan Bydgoski",'age':23,'grade':4.1},
              {'name': "Wiktoria Hajdak",'age':20,'grade':4.2}]
connection_2.execute(query,values_list)

#Returning
query = db.text('SELECT * FROM students')
result = connection_2.execute(query).fetchall()
print(result)


#CRUD

def create(name,age,grade):
    engine = db.create_engine('sqlite:///college.db')
    pass
def read(id):
    pass
def update(id,name,age,grade):
    pass
def delete(id):
    pass





