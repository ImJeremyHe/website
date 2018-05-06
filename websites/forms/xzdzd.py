#!/usr/bin/python
#coding=utf8

from wtforms_tornado import Form
from wtforms import FloatField, validators, IntegerField, RadioField


class XzdzdForm(Form):
    period = FloatField('period', [
        validators.DataRequired(message="基本周期不能为空"),
        validators.NumberRange(max=7, message="基本周期输入有误")
    ])
    type = IntegerField('type', [
        validators.DataRequired(message="场地条件不能为空"),
        validators.AnyOf(values=[1, 2, 3, 4], message="场地类型输入有误")
    ])
    pga = FloatField('pga', [
        validators.Optional(strip_whitespace=True)
    ])
    para = RadioField('para', choices=[('s', '使用弹性谱值查询'), ('t', '使用推荐参数查询')], validators=[
        validators.DataRequired(message="不能为空")
    ])