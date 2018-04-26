# https://codeclub.thorgate.eu/challenges/111

from capitalizing_this import capitalizing_this

assert capitalizing_this("hello world") == "Hello World"
assert capitalizing_this("hellO worlD") == "Hello World"
assert capitalizing_this("HELLO World") == "Hello World"
# assert capitalizing_this("HellO W0rld") == "Hello World" # ?

# assert capitalizing_this("hello_world") == "Hello_World"
assert capitalizing_this("Don't smoke") == "Don't Smoke"
assert capitalizing_this("Look, Just Because I Don't Be Givin' No Man A Foot") == "Look, Just Because I Don't Be Givin' No Man A Foot"