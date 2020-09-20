# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Copyright (c) 2020 - mark-the-dev-01
"""

from flask import Flask
from app import create_app

app = create_app(None)

if __name__ == "__main__":
    app.run()
