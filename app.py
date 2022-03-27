from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/result/', methods=['POST','GET'])
def result():

    from urllib.parse import urlencode
    from urllib.request import urlopen
    import json

    uri_recaptcha = 'https://www.google.com/recaptcha/api/siteverify'
    recaptcha_response = request.form.get("g-recaptcha-response")
    secret_key = '6LcG9WweAAAAAOwg2iS5c_aPvD85tFZbidlwPDfr'
    remote_ip = request.remote_addr
    params = urlencode({
        'secret': secret_key,
        'response': recaptcha_response,
        'remoteip': remote_ip,
    })

     # print params
    data = urlopen(uri_recaptcha, params.encode('utf-8')).read()
    result = json.loads(data)
    success = result.get('success')
    challenge_ts = result.get('challenge_ts')
    hostname = result.get('hostname')

    return render_template('result.html',recaptcha_response=recaptcha_response,success=success,challenge_ts=challenge_ts,hostname=hostname)

