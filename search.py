# Author: Nils van der Deen


from flask import Flask, render_template, request

from database import do_database

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    # If there is are no search, redirect to the search page
    if 'search' not in request.args:
        return render_template('search.html')
    # Get the search term from the URL
    search_term = request.args.get('search')
    # Get the search results from the database
    search_results = do_database(f"SELECT * FROM user WHERE title LIKE '%{search_term}%'")
    # Render the search results page
    return render_template('search_results.html', search_results=search_results)

if __name__ == '__main__':
    app.run()

