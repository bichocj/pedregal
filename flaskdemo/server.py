import json
import datetime
from flask import request, render_template, redirect, url_for

from app import app;
from db import db;
from models import Person


@app.route('/')
def home():
  people = Person.query.all()  
  return render_template('home.html', people=people)

    
@app.route('/create', methods=['GET', 'POST'])
def create_person():
  if request.form:
    name = request.form['name']
    last_name = request.form['last_name']
    mother_last_name = request.form['mother_last_name']
    date_of_birth = request.form['date_of_birth']
    date_of_birth = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')    

    person = Person(
        name=name, 
        last_name=last_name, 
        mother_last_name=mother_last_name,
        date_of_birth=date_of_birth.date()
      )

    db.session.add(person)
    db.session.commit()

    return redirect(url_for('home'))
  return render_template('form.html', 
    title='Crear Persona', 
    action='/create', 
    person=None
  )


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_person(id):
  person = Person.query.filter_by(id=id).first()
  action = f'/edit/{person.id}'

  if request.form:
    name = request.form['name']
    last_name = request.form['last_name']
    mother_last_name = request.form['mother_last_name']
    date_of_birth = request.form['date_of_birth']
    date_of_birth = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')    

    person.name=name
    person.last_name=last_name
    person.mother_last_name=mother_last_name
    person.date_of_birth=date_of_birth.date()
    db.session.commit()

    return redirect(url_for('home'))
  return render_template('form.html', 
    title='Editar Persona',
    action=action,
    person=person
  )


@app.route('/delete/<id>', methods=['GET'])
def delete_person(id):
  person = Person.query.filter_by(id=id).first()
  db.session.delete(person)
  db.session.commit()
  return redirect(url_for('home'))
