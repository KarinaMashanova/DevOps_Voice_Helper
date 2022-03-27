from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "dick"


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    return render_template("index.html")


headings = ("ПП", "ФИО", "Пол", "Дата рождения", "Дата осмотра", "Длина тела, см", "Масса тела, кг",
            "Окружность грудной клетки, см", "Окружность талии, см", "Окружность правого плеча, см",
            "Окружность левого плеча, см", "Окружность бедер, см", "Окружность шеи, см", "Окружность запястья, см",
            "Жизненная емкость легких, л", "Динамометрия правой кисти, кг", "Динамометрия левой кисти, кг",
            "Сист.артериальное давление, мм рт.ст.", "Диаст.артериальное давление, мм рт.ст.",
            "Частота сердечных сокращений", "Толщина жировой складки (живот), см",
            "Толщина жировой складки (плечо), см", 'Толщина жировой складки (спина), см', "Тип телосложения")


@app.route('/data', methods=['POST', 'GET'])
def data():
    return render_template('data.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result, headings=headings)


if __name__ == '__main__':
    app.run(debug=True)
