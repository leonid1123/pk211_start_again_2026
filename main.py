from flask import (Flask,
                   render_template,
                   request)

app = Flask(__name__)
pokupki = {}

@app.route('/')
def page1():
    ezik = 'Можно (НЕТ) писать гадости o_0'
    return render_template('index.html', par1=ezik)

@app.route('/p2', methods=['POST', 'GET'])
def page2():
    txt = ''
    num = ''
    if request.method == 'POST':
        txt = request.form.get('pole1')
        num = request.form.get('pole2')
        pokupki[txt] = num
    return render_template('page2.html',
                           val_1=pokupki)


app.run(debug=True)
