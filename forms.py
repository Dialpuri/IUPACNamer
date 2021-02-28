from wtforms import Form, StringField, SelectField

class IUPACChecker(Form):
    guess = StringField("Enter your guess")