#!/usr/bin/env python3
#server/seed.py

from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():

    # CReate and Initialize faker generator
    fake = Faker()


    # Delete all rows in the 'pets' table 
    Pet.query.delete()

    # Create an empty list
    pets = []
    
    #Species 
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add 10 Pet instances using Faker
    for n in range(10):
        pet = Pet(name=fake.first_name(), species=rc(species))
        pets.append(pet)

    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()