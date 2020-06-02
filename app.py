from flask import Flask , request, render_template, redirect, url_for
import save
import json

app = Flask(__name__)

@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello/<name>')
def hellovar(name):
    character = save.set_charact(name)
    return "{0}님 행운을 빕니다. 남은 체력 : {1}".format(character["name"], character["hp"])

@app.route('/game')
def game():
    with open("static/save.txt", "r", encoding='uft-8') as f:
        data = f.read()
        character = json.load(data)
        print(character)
    return "{0}님 행운을 빕니다. 남은 체력 : {1}".format(character["name"], character["hp"])



@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "쑤"
    elif num == 2:
        return "쑤우"
    elif num == 3:
        return "쑤우우"
    else:
        return "없음"

@app.route('/move/naver')
def naver():
    return render_template("naver.html")

@app.route('/move/daum')
def daum():
    return redirect("https://www.daum.net")

@app.route('/urltest')
def url_test():
    return redirect(url_for('daum'))

@app.route('/login', methods=['GET', 'post'])
def method():
    if request.method == 'GET':
        return render_template('login.html')
    
    else:
        id = request.form['id']
        pw = request.form['pw']
        if id == 'abc' and pw == '1234':
            return "반갑습니다.{} ".format(id)
        else:
            return "아이디와 패스워드를 확인해주세요."

@app.route('/img')
def img():
    return render_template("image.html")


if __name__ =='__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)
