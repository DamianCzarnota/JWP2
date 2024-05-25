from sqlalchemy import create_engine, MetaData
from sqlalchemy import inspect

from sqlalchemy import (
    Table,
    Column,
    String,
    Integer,
    Float,
    Boolean,
    select,
    text,
    func
)

import sqlalchemy as db
engine = create_engine('sqlite:///census.sqlite')
inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)
connection = engine.connect()
print(connection)
metadata = MetaData()
census = Table('census', metadata, autoload_with=engine)
print(repr(census))
stmt = text('SELECT state, sex FROM census')
result_proxy = connection.execute(stmt)
results = result_proxy.fetchall()
print(results[:5])
query = select(census.c.state, census.c.sex)
output = connection.execute(query)
results = output.fetchall()
print(results[:5])
print(query)
stmt = select(
    func.sum(census.c.pop2008)
)
results = connection.execute(stmt).fetchall()
print(results)
stmt = select(
    func.sum(census.c.pop2008)
).where(census.c.sex == 'F')
results = connection.execute(stmt).fetchall()
print(results)
stmt = select(
    func.sum(census.c.pop2008)
).where((census.c.sex == 'F') & (census.c.state == "Alaska"))
results = connection.execute(stmt).fetchall()
print(results)