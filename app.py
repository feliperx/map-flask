from flask import Flask, render_template 

app = Flask(__name__)



# function -> homepage 
@app.route('/') #decorator route to fucntion homepage
def homepage():
    return render_template('homepage.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/users/<username>')
def users(username):
    return render_template('users.html', username = username)



# start website 
if __name__ == '__main__':
    app.run(debug=True)