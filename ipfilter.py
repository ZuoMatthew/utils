from functools import wraps    

IP = "192.168.0.1"    

def decorator(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if IP == "192.168.0.1":
            return f(*args, **kwargs)
        else:
            return abort(403)    

    return wrapped

@app.route('/')
@decorator
def hello_world():
    return "Hello"
