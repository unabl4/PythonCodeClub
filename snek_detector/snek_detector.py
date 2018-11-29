def is_it_python(code):
    try:
        eval(code) # if not valid it will throw an exception right here
        return True
    except:
        return False
