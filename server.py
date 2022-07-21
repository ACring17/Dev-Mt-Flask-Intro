"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'amazing', 'fantabulous', 'wowza',
    'Mr.Fantastic', 'brilliant', 'ducky', 'cool', 'incredible',
    'wonderful', 'smashing', 'lovely']

MEANNESS = [
  'slow', 'miserable', 'a ding-dong', 'childish', 'dim', 'naivie', 'incompitent', 'a chungus', 'dopey', 'a clown'
]

@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Click here to start!</a> </html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          What compliment would you like?<br>
          <input type="radio" name="compliment" value="awesome">Awesome<br>
          <input type="radio" name="compliment" value="terrific">Terrific<br>
          <input type="radio" name="compliment" value="fantastic">Fantastic<br>
          <input type="radio" name="compliment" value="amazing">Amazing<br>
          <input type="radio" name="compliment" value="fantabulous">Fantabulous<br>
          <input type="radio" name="compliment" value="wowza">Wowza<br>
          <input type="radio" name="compliment" value="Mr.Fantastic">Mr.Fantastic<br>
          <input type="radio" name="compliment" value="brilliant">Brilliant<br>
          <input type="radio" name="compliment" value="beautiful">Beautiful<br>
          <input type="radio" name="compliment" value="cool">Cool<br>
          <input type="radio" name="compliment" value="incredible">Incredible<br>
          <input type="radio" name="compliment" value="wonderful">Wonderful<br>
          <input type="radio" name="compliment" value="smashing">Smashing<br>
          <input type="radio" name="compliment" value="lovely">Lovely<br>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss" method='GET'>
          What's your name? <input type="text" name="person">
          What diss would you like?<br>
          <input type="radio" name="diss" value="slow">Slow<br>
          <input type="radio" name="diss" value='miserable'>Miserable<br>
          <input type="radio" name="diss" value='a ding-dong',>Ding-Dong<br>
          <input type="radio" name="diss" value='childish'>Childish<br>
          <input type="radio" name="diss" value="dim">Dim<br>
          <input type="radio" name="diss" value='naivie'>Naivie<br>
          <input type="radio" name="diss" value='incompitent'>Incompitent<br>
          <input type="radio" name="diss" value='a chungus'>Chungus<br>
          <input type="radio" name="diss" value='dopey'>Dopey<br>
          <input type="radio" name="diss" value='a clown'>Clown<br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    compliment = choice(AWESOMENESS)


    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    diss = request.args.get("diss")

    diss = choice(MEANNESS)


    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
