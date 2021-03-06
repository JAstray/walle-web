# -*- coding: utf-8 -*-
"""
    walle-web

    :copyright: © 2015-2017 walle-web.io
    :created time: 2017-03-19 15:50:07
    :author: wushuiyong@walle-web.io
"""
try:
    from flask_wtf import FlaskForm  # Try Flask-WTF v0.13+
except ImportError:
    from flask_wtf import Form as FlaskForm  # Fallback to Flask-WTF v0.12 or older
from flask_wtf import Form

from wtforms import TextField
from wtforms import validators


class TagCreateForm(Form):
    name = TextField('name', [validators.Length(min=1, max=10)])
    label = TextField('label', [validators.Length(min=1, max=30)])
