from flask import Flask 

app = Flask(__name__)



# function -> homepage 
@app.route('/') #decorator route to homepage
def homepage():
    return 'Learning Flask. A webGIS dream.'


# start website 

app.run()