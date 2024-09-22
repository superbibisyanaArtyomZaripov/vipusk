#Импорт
from flask import Flask, render_template,request, redirect
#Подключение библиотеки баз данных


app = Flask(__name__)
#Подключение SQLitese
@app.route("/")
def site():
    return render_template('site.html')


@app.route("/howtodealwith")
def howtodealwith():
    return render_template('howtodealwith.html')

@app.route("/nerd")
def nerd():
    return render_template('nerd.html')

@app.route("/meme")
def meme():
    return render_template('meme.html')

if __name__ == "__main__":
    app.run(debug=True)