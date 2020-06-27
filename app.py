from flask import Flask , request, render_template, redirect, url_for, abort, session
import game

import json
import dbdb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/emty')
def emty(emty):
    return render_template("emty.html")


@app.route('/login')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        if id == 'abc' and pw == '1234':
            session['user'] = id
            return '''
            <script> alert("안녕하세요 {}님");
            location.href="/form"
            </script>
            '''.format(id)
        else:
            return "아이디 또는 패스워드를 확인하세요."

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))

@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')
    return redirect(url_for('login'))


@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method =='GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form["num"]
        name = request.form["name"]
        dbdb.insert_data(num, name)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/getinfo')
def getinfo():
    ret = dbdb.select_all()
    print(ret[3])
    return render_template('getinfo.html', data=ret)


@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/gamestart<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html', data=character)

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['name'])
        return "상대는 가위,{}은 가위를 내서 비겼습니다.".format(character["name"])
    elif num == 2:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['name'])
        return "상대는 가위,{}은 바위를 내 이겼습니다!".format(character["name"])
    elif num == 3:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['name'])
        return "상대는 가위,{}은 보를 내 졌습니다...".format(character["name"])

@app.route('/games/<name>')
def game_route(name):
    character = game.set_charact(name)
    return render_template('game1.html', data=character)

@app.route('/route/<int:num>')
def game1(num1):
    if num1 == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['name'])
        return "{}는 좀비를 물리쳤습니다!".format(character["name"])
    elif num1 == 2:
        return  "당신은 좀비에게서 도망치다 사망했습니다..."
    else:
        return "어떻게 할지 선택하세요."





if __name__ =='__main__':
    app.run(debug=True)

