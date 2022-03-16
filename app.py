from flask import Flask, render_template, request
from azure.servicebus import ServiceBusClient, ServiceBusMessage

app = Flask(__name__)
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/submit/', methods=['POST','GET'])
def submit():

    from urllib.parse import urlencode
    from urllib.request import urlopen
    import json

    URIReCaptcha = 'https://www.google.com/recaptcha/api/siteverify'
    recaptchaResponse = request.form.get("g-recaptcha-response")
    private_recaptcha = '6LcG9WweAAAAAOwg2iS5c_aPvD85tFZbidlwPDfr'
    remoteip = request.remote_addr
    params = urlencode({
        'secret': private_recaptcha,
        'response': recaptchaResponse,
        'remoteip': remoteip,
    })

     # print params
    data = urlopen(URIReCaptcha, params.encode('utf-8')).read()
    result = json.loads(data)
    success = result.get('success')
    challenge_ts = result.get('challenge_ts')
    hostname = result.get('hostname')

    return render_template('submit.html',success=success,challenge_ts=challenge_ts,hostname=hostname)

