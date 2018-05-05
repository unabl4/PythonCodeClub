from shortest_way_back import shortest_way_back

assert shortest_way_back('NNN') == 'SSS'
assert shortest_way_back('NNE') in ['WSS', 'SSW'] # both ok
assert shortest_way_back('NNSENWS') == 'S'
# ---
assert shortest_way_back('SSSS') == 'NNNN'
assert shortest_way_back('NESW') == '' # do nothing