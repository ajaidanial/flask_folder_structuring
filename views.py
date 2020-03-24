"""Define the views and view based operations here"""

from flask.views import MethodView
from flask import render_template, request, flash, redirect
from forms import UserForm
from models import *
from app import db


class TestRoute(MethodView):
    """Dummy route and dummy documentation"""

    def get(self):
        # when method is GET
        form = UserForm()
        return self.render_page(form)

    def post(self):
        # when method is POST
        form = UserForm(request.form)
        if form.validate():
            # form valid | create user
            user = User(**form.data)
            db.session.add(user)
            db.session.commit()
            flash("Successfully added")
            return redirect("/")
        return self.render_page(form)

    def render_page(self, form):
        # return the html page with other context
        return render_template("index.html", form=form)
