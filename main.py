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
  public, private = rsa.generate_keypair(p, q, int(size))
  return f"$('#pubkey').val(`{public[0]}, {public[1]}`); $('#privkey').val(`{private[0]}, {private[1]}`);"

@app.route('/encrypt/<msg>/<key>/<n>')
def encrypt(msg, key, n):
  return f"{rsa.encrypt(msg, key, n)}"

@app.route('/decrypt/<crypted>/<key>/<n>')
def decrypt(crypted, key, n):
  return f"{rsa.decrypt(crypted, key, n)}"


app.run(host='0.0.0.0', port=81)
