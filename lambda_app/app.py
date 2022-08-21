# -*- coding: utf-8 -*-

from chalice import Chalice
from wow_wtf_manager.lbd import hello

app = Chalice(app_name="wow_wtf_manager")


@app.lambda_function(name="hello")
def handler_hello(event, context):
    return hello.high_level_api(event, context)
