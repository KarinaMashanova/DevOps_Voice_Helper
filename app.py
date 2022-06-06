import pandas as pd
from flask import Flask, render_template, request
import xlwings as xw

app = Flask(__name__)
app.config['SECRET_KEY'] = "dick"


@app.route('/', methods=['POST', 'GET'])
def index():  # put application's code here
    return render_template("index.html")


headings = ("ПП", "ФИО", "Пол", "Дата рождения", "Дата осмотра", "Длина тела, см", "Масса тела, кг", # noqa
            "Окружность грудной клетки, см", "Окружность талии, см", "Окружность правого плеча, см", # noqa
            "Окружность левого плеча, см", "Окружность бедер, см", "Окружность шеи, см", "Окружность запястья, см", # noqa
            "Жизненная емкость легких, л", "Динамометрия правой кисти, кг", "Динамометрия левой кисти, кг", # noqa
            "Сист.артериальное давление, мм рт.ст.", "Диаст.артериальное давление, мм рт.ст.", # noqa
            "Частота сердечных сокращений", "Толщина жировой складки (живот), см", # noqa
            "Толщина жировой складки (плечо), см", 'Толщина жировой складки (спина), см', "Тип телосложения") # noqa


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        df = pd.DataFrame([result.values()])
        wb = xw.Book("vershion2.xlsm")
        wb_list = wb.sheets[1]
        wb_row = wb_list.range('A' + str(wb_list.cells.last_cell.row)).end('up').row # noqa
        wb_list.range(wb_row + 1, 1).options(index=False, header=False).value = df # noqa
        wb.save()
        macro1 = wb.macro("main")
        macro1()
        return render_template("result.html", result=result, headings=headings)


if __name__ == '__main__':
    app.run(debug=True)
