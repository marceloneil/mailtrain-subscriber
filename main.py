import requests

from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_json('settings.json')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    if not all(k in request.form for k in ['EMAIL', 'FIRST_NAME', 'LAST_NAME']):
        return jsonify({'error': 'missing field'}), 400
    params = { 'access_token': app.config.get('ACCESS_TOKEN') }
    data = {
        'EMAIL': request.form['EMAIL'],
        'FIRST_NAME': request.form['FIRST_NAME'],
        'LAST_NAME': request.form['LAST_NAME'],
        'FORCE_SUBSCRIBE': app.config.get('FORCE_SUBSCRIBE'),
        'REQUIRE_CONFIRMATION': app.config.get('REQUIRE_CONFIRMATION')
    }
    r = requests.post(app.config.get('URL'), params=params, data=data)
    return jsonify(r.json()), r.status_code

if __name__ == '__main__':
    app.run()
