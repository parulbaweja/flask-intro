"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.<br>
    <a href="/hello">Hello</a></html>"""


@app.route('/hello')
def create_insults(insults):
    """generates insults html"""
    insult_html = []
    for insult in insults:
        insult_str = "<option value={}>{}".format(insult)
        insult_html.append(insult_str)
        print insult_html
    print "\n".join(insult_html)
    return "\n".join(insult_html)


def say_hello():
    """Say hello and prompt for user's name."""

          # Select your compliment:
          #   <select name="compliment">
          #     <option value="awesome">Awesome
          #     <option value="terrific">Terrific
          #     <option value="fantastic">Fantastic
          #     <option value="neato">Neato
          #     <option value="fantabulous">Fantabulous
          #     <option value="wowza">Wowza
          #     <option value="oh-so-not-meh">Oh-so-not-meh
          #     <option value="brilliant">Brilliant
          #     <option value="ducky">Ducky
          #     <option value="coolio">Coolio
          #     <option value="incredible">Incredible
          #     <option value="wonderful">Wonderful
          #     <option value="smashing">Smashing
          #     <option value="studly">Studly
          #   </select>

          # <option value="rude">Rude
          #     <option value="spudly">Spudly
          #     <option value="muggle">Muggle
          #     <option value="average">Average
          #     <option value="insubordinate">Insubordinate
          #     <option value="a_nincompoop">a Nincompoop
          #     <option value="illiterate trashy low class">Illiterate trashy low class

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          <br>
            Select your insult ya filthy animal:
            <select name="insult">
              create_insults(AWESOMENESS)
            </select>
          </form>
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
    """Get user by name & insult."""

    player = request.args.get("person")
    insult = request.args.get("insult")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Ugh, {player}! I think you're <b>{insult}</b>!!
      </body>
    </html>
    """.format(player=player, insult=insult.upper())

@app.route('/greet')
def greet_person():
    """Get user by name & compliment."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
