# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Copyright (c) 2020 - mark-the-dev-01
"""
from app.home import blueprint
from flask import render_template
from jinja2 import TemplateNotFound

current_user = {
    'is_authenticated': True
}


@blueprint.route('/')
def index():
    return render_template('index.html', current_user=current_user)


@blueprint.route('/<template>')
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'

        return render_template(template, current_user=current_user)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500
