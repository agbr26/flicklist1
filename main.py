from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    todays_movie = get_random_movie()
    tomorrows_movie = get_random_movie()
    # build the response string
    content = "<h1>Movie of the Day:</h1>"
    content += "<ul>"
    content += "<li>" + todays_movie + "</li>"
    content += "</ul>" 

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    
    content += "<h1>Tomorrow's Movie:</h1>"
    content += "<ul>"
    content += "<li>" + tomorrows_movie + "</li>"
    content += "<ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies_list = ["Legally Blonde", "Horrible Bosses", "Shaun of the Dead", "Rat Race", "Clueless"]
    # TODO: randomly choose one of the movies, and return it
    return random.choice(movies_list)
  

app.run()
