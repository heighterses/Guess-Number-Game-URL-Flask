from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1 style = "text-align: center"> Hello World! </h2>' \
           '<p style = "text-align: center">Guess The Number from 1 to 9</p>' \
           '<img src = "https://media4.giphy.com/media/k8QFDXU7AFOERD399O/giphy.gif?cid=ecf05e47smvntskzwm28m2sye3wwou8k1fh254e9kxep7phl&ep=v1_gifs_search&rid=giphy.gif&ct=g" width = 200>'


@app.route('/<int:n>')
def number(n):
   if n > random_number:
       return '<h1>Too High</h1>' \
              '<img src ="https://media.giphy.com/media/l2SqeBp51QTM1sy6k/giphy.gif" width = 200>'
   elif n < random_number:
       return '<h1>Too Low</h1>' \
              '<img src ="https://media.giphy.com/media/11qBG0k3hCDRCM/giphy.gif" width = 200>'
   elif n==random_number:
       return '<h1>Correct!!!!!!!</h1>' \
              '<img src ="https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif" width = 200>'




if __name__ == '__main__':
    app.run(debug=True)
