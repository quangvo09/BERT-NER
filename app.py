import webbrowser, threading
from flask import Flask, request, jsonify, render_template
from bert import Ner

model = Ner("out/")
app = Flask(__name__)


@app.route('/')
def home():
    return 'Server is running...'


@app.route('/predict', methods=['GET'])
def predict():
    return render_template('predict.html', title="Predict")


@app.route('/predict', methods=['POST'])
def do_predict():
    response = {'success': False}

    payload = request.form
    if payload is None or 'text' not in payload:
        text = request.args.get('text')
    else:
        text = payload['text']

    if text is not None:
        result = model.predict(text)
        response['text'] = text
        response['predict'] = result
        response['success'] = True

        summary = []
        for word in result:
            key, value = list(word.items())[0]
            summary.append({'key': key, 'tag': value['tag']})
        response['summary'] = summary

    if response['success'] is True:
        return render_template('predict_result.html', result=response)

    return jsonify(response)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8080

    url = '%s:%s/predict' % (host, port)
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()

    app.run(host=host, debug=False, port=port)


