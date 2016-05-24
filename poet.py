import random
import grammy
from flask import Flask
app = Flask(__name__)

class Poet:
    def read(self, book):
        grammy.read_file(book)

    def poem(self, l=100):
        return grammy.gen(l)

poet = Poet()

@app.route('/')
def poem():
    return poet.poem(1500).replace('\n', '\n<br>')

if __name__=="__main__":
    grammy.num_chars = 4
    poet.read('paradise.txt')
    poet.read('dickinson.txt')
    app.run()
