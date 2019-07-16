import webbrowser, threading
from flask import Flask, request, jsonify, render_template
from bert import Ner

model = Ner("out/")
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


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
            summary.append({'key': key, 'tag': value['tag'], 'confidence': value['confidence']})
        response['summary'] = summary

    if response['success'] is True:
        num_of_results = len([x for x in response['summary'] if x['tag'] != 'O'])
        return render_template('index.html', result=response, num_of_results=num_of_results, text=text)

    return jsonify(response)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8081

    url = '%s:%s' % (host, port)
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()

    app.run(host=host, debug=False, port=port)


