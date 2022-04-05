# Author: Nils van der Deen

from flask import Flask, render_template, request, redirect

from database import do_database

app = Flask(__name__)

@app.route('/actor/', defaults={'actor_id': 1})
@app.route('/actor/<int:actor_id>')
def actor(actor_id):
    # Get the actor data from the database
    actor = do_database(f"SELECT * FROM actors WHERE ID = {actor_id}")
    # render the template with the data
    return render_template('actor.html', actor=actor)

if __name__ == '__main__':
    app.run()