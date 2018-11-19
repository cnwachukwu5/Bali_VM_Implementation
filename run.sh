alias antlr4='java -jar /usr/local/lib/antlr-4.7-complete.jar'
antlr4 -no-listener -visitor -Dlanguage=Python3 Bali.g4
python Program.py examples/ex1.bali
python Program.py examples/ex2.bali
python Program.py examples/ex3.bali
python Program.py examples/ex4.bali