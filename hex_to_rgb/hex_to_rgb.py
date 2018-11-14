def hex_to_rgb(s):
    if not isinstance(s, str) or len(s) != 6:
        return []

    try:
        rgb = list(map(lambda o: int(o,16), [s[i:i+2] for i in range(0,len(s),2)]))
    except:
        rgb = []

    return rgb
