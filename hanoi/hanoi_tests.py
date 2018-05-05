from hanoi import hanoi

steps="""1. Move disk from starting pole to ending pole.
2. Move disk from starting pole to middle pole.
3. Move disk from ending pole to middle pole.
4. Move disk from starting pole to ending pole.
5. Move disk from middle pole to starting pole.
6. Move disk from middle pole to ending pole.
7. Move disk from starting pole to ending pole."""

assert hanoi(3) == steps
assert hanoi(3) == steps # check that numbers are reset properly (had a bug here)