from os import environ
from flask import Flask, request, redirect

app = Flask(__name__)
REDIRECT_DOMAIN = environ.get('REDIRECT_DOMAIN')

@app.route('/')
def hello():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=", flush=True)
    print(f"Request headers: {request.headers}", flush=True)
    print(f"Redirect to {REDIRECT_DOMAIN}", flush=True)
    return redirect(f"http://{REDIRECT_DOMAIN}", code=302)

@app.route('/p0c')
def p0c():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=", flush=True)
    print(f"Request headers: {request.headers}", flush=True)
    return 'c3ViZG9tYWluIHRha2VvdmVyIC0geF9idWdodW50ZXI='
