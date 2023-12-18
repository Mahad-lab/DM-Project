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
  return f"$('#pubkey').val(`{public}`); $('#privkey').val(`{private}`)"

@app.route('/encrypt/<crypted>/<keys>')
def decrypt(crypted, keys):
  return f"$('#encrypted').val(`{rsa.decrypt(crypted, keys)}`);"

@app.route('/decrypt/<crypted>/<keys>')
def decrypt(crypted, keys):
  return f"$('#decrypted').val(`{rsa.decrypt(crypted, keys)}`);"


app.run(host='0.0.0.0', port=81)
