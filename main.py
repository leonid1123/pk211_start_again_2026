from flask import (Flask,
                   render_template,
                   request)
from db_handler import Db_handler

app = Flask(__name__)
db = Db_handler()
pokupki = {}

@app.route('/', methods=['POST','GET'])
def page1():
    if request.method == 'POST':
        nazvanie = request.form.get('c_name')
        garan = request.form.get('c_war')
        cena = request.form.get('c_price')
        sql = '''INSERT INTO `Кондиционры`(`Название`,
        `Гарантия`,`Цена`) VALUES(%s,%s,%s)  
        '''
        new_info = (nazvanie,garan,cena)
        db.cur.execute(sql,new_info)
        db.conn.commit()

    db.cur.execute('SELECT * FROM `Кондиционеры`')
    ans = db.cur.fetchall()
    return render_template('index.html',
                           par1=ans)

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
