"""Contains the forms | similar to the db models"""

from wtforms import Form, StringField, validators


class UserForm(Form):
    """User form"""

    username = StringField("Username", [validators.InputRequired()])
    email = StringField("Email Address", [validators.InputRequired()])
