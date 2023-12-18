from flask import Flask, render_template
import rsa
from random import randint as rand

#initial two random numbers p,q
p = rand(1, 1000)
q = rand(1, 1000)

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')



@app.route('/generate/<size>')
def gen(size):
  public, private, n = rsa.generate_keypair(p, q, int(size))
  return f"{public},{private},{n}"

@app.route('/encrypt/<key>/<n>/<msg>')
def encrypt(key, n, msg):
  return f"{rsa.encrypt(msg, key, n)}"

@app.route('/decrypt/<key>/<n>/<crypted>')
def decrypt(key, n, crypted):
  return f"{rsa.decrypt(crypted, key, n)}"


app.run(host='0.0.0.0', port=81)
