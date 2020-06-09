from flask import Flask , request, render_template, redirect, url_for
import game
import json
import dbdb

app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

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

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html', data=character)

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character['item'])
    return "{}아이템을 사용했습니다. ".format(character["item"])

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        with open("static/save.txt", "r", encoding='utf-8') as f:
            data = f.read()
            character = json.loads(data)
            print(character['name'])
        return "{}은 건물을 수색하기로 했습니다... ".format(character["name"])
    elif num == 2:
        return "당신은 건물을 그냥 지나치기로 하였습니다. "
    else:
        return "어떻게 할지 선택하세요."

@app.route('/move/naver')
def naver():
    return render_template("naver.html")

@app.route('/move/daum')
def daum():
    return redirect("https://www.daum.net")

@app.route('/urltest')
def url_test():
    return redirect(url_for('daum'))


@app.route('/img')
def img():
    return render_template("image.html")


if __name__ =='__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)
