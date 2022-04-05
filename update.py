# Author: Nils van der Deen

from flask import Flask, render_template, request, redirect

from database import do_database

app = Flask(__name__)

@app.route('/update')
def update():
    # Get the actor data from the database
    actor = do_database("SELECT * FROM actors WHERE ID = 1")
    # render the template with the data
    return render_template('update.html', actor=actor)

@app.route('/app/update', methods=['POST'])
def update_user():
    # Get the form data
    actor_id = request.form['actor_id']
    name = request.form['name']
    age = request.form['age']

    # Update the actor in the database
    do_database(f"UPDATE actors SET name = '{name}', age = {age} WHERE id = {actor_id}")

    # Redirect to the home page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)