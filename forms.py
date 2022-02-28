from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class DataForm(FlaskForm):
    pp = IntegerField('№пп', validators=[DataRequired()])
    fio = StringField('ФИО', validators=[DataRequired(), Length(min=4, max=100)])
    dlinaTela = IntegerField("Длина тела (см) ", validators=[DataRequired()])
    massaTela = IntegerField("Масса тела (кг) ", validators=[DataRequired()])
    ogk = IntegerField("Окружность грудной клетки (см) ", validators=[DataRequired()])
    ot = IntegerField("Окружность талии (см) ", validators=[DataRequired()])
    opp = IntegerField("Окружность правого плеча (см) ", validators=[DataRequired()])
    olp = IntegerField("Окружность левого плеча (см) ", validators=[DataRequired()])
    ob = IntegerField("Окружность бедер (см) ", validators=[DataRequired()])
    osh = IntegerField("Окружность шеи (см) ", validators=[DataRequired()])
    oz = IntegerField("Окружность запястья (см) ", validators=[DataRequired()])
    zhel = IntegerField("Жизненная емкость легких (кг) ", validators=[DataRequired()])
    dpk = IntegerField("Динамометрия правой кисти (кг) ", validators=[DataRequired()])
    dlk = IntegerField("Динамометрия левой кисти (кг) ", validators=[DataRequired()])
    sad = IntegerField("Систолагическое артериальное давление (мм рт.ст", validators=[DataRequired()])
    dad = IntegerField("Диастолагическое артериальное давление (мм рт.ст.", validators=[DataRequired()])
    chss = IntegerField("Частота сердечных сокращений ", validators=[DataRequired()])
    tzs = IntegerField("Толщина жировой складики(живот) (см) ", validators=[DataRequired()])
    tzsp = IntegerField("Толщина жировой складики(плечо) (см) ", validators=[DataRequired()])
    tzss = IntegerField("Толщина жировой складики(спина) (см) ", validators=[DataRequired()])

    submit = SubmitField("Получить оценку ФР")

