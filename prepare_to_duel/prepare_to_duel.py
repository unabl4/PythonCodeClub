def i_draw_my_sword(hilt_len, blade_len, material):
    if hilt_len < 1 or blade_len < 1 or material == '':
        return False

    blade = 'O' + ('=' * hilt_len) + '||' + (str(material) * blade_len) + '>'
    return blade

# ---

assert i_draw_my_sword(2, 8, '<') == 'O==||<<<<<<<<>'
assert i_draw_my_sword(3, 3, '=>o<') == 'O===||=>o<=>o<=>o<>'
assert i_draw_my_sword(3, 0, 'banana') == False
assert i_draw_my_sword(3, 5, '') == False
assert i_draw_my_sword(2, 5, 5) == 'O==||55555>'
