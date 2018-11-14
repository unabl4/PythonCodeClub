from hex_to_rgb import hex_to_rgb

assert hex_to_rgb('ff9900') == [255, 153, 0]
assert hex_to_rgb('FF9900') == [255, 153, 0] # case-insensitivity
assert hex_to_rgb(1) == []
assert hex_to_rgb([]) == []
