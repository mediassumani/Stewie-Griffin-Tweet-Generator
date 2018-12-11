import re
import os


def clean(text_body):

    expression = re.compile(r'\w')
    return expression.findall(text_body)
