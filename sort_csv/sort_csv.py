# insep = ',', inend = '\n', outsep=':', outend=' -- end\n'

allowed_params = set(['insep','inend','outsep','outend'])

def sort_file(contents, **params):
    # check the incoming keyword params
    for param in params:
        if param not in allowed_params:
            # quit
            raise TypeError('invalid or unsupported function parameters supplied')

    # set the keyword defaults
    insep = params.get('insep', ',')
    inend = params.get('inend', '\n')
    outsep = params.get('outsep', insep) # ?
    outend = params.get('outend', inend)

    # the main logic
    lines = sorted(line.split(insep) for line in contents.split(inend) if len(line) > 0 and '#' not in line) # split and sort
    return outend.join(outsep.join(line) for line in lines)
