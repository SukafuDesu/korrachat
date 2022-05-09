from urllib import response
from flask import Flask,request
import chatter;

bot, trainer = chatter.turnOnBot()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!!"

@app.route('/request')
def search():
    inp = request.args.get('input')
    response = botResponse(bot,inp);
    return f'{response}'

def botResponse(bot, input):
    return (bot.get_response(input));

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)