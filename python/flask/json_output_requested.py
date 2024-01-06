from flask import request

def json_output_requested():
    if request.args.get('json') is not None:
        return True
    return False