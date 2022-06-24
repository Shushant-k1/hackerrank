# firts sting must contain only digit then followed by a space

import re

pattern = r"^[1-9]\d{4}\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$"

for _ in range(int(input())):
    if re.search(pattern,input()):
        print("VALID")
    else:
        print("INVALID")
