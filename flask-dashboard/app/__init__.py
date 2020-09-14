# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Copyright (c) 2020 - mark-the-dev-01
"""
from flask import Flask
from importlib import import_module


def register_blueprints(app):
    for module_name in ['home']:
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def create_app(config=None):
    app = Flask(__name__, static_folder="home/static")
    register_blueprints(app)
    return app
