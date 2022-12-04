from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm	import sessionmaker 
# no need to import Table as will be making Python classes instead

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")

base = declarative_base()

# create a class-based model for the "Programmer table"
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# creating records on our programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

grainne_donegan = Programmer(
    first_name="Grainne",
    last_name="Donegan",
    gender="F",
    nationality="Irish",
    famous_for="Learning How to Code"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(grainne_donegan)

# updating a single record
# programmer = session.query(Programmer).filter_by(id=9).first()
# programmer.famous_for = "World President"
# commit every change after the code every time

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print(f'Programmer found: {programmer.first_name} {programmer.last_name}')
#     confirmation = input("Are you sure you want to delete this record: ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# commit out session to the db
# session.commit()

# query the database to find all programmers
programmers = session.query(Programmer)

for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
