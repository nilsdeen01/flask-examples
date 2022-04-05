# Author: Nils van der Deen

from flask import Flask, render_template, redirect, request

from database import do_database

app = Flask(__name__)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/app/create', methods=['POST'])
def create_actor():

    # get the form data
    name = request.form.get('name')
    age = request.form.get('age')

    # check if actor exists
    actor_id = do_database(f"SELECT COUNT(id) FROM actors WHERE name = '{name}'")
    if actor_id[0][0] != 0:
        return render_template('create.html', message="Actor already exists")

    # add actor to database
    do_database(f"INSERT INTO actors (name, age) VALUES ('{name}', '{age}')")

    # redirect to create page
    return redirect('/create')


if __name__ == '__main__':
    app.run()