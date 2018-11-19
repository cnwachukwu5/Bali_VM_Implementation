Set GRUN=java -cp .;C:\Bin\Java\antlr-4.7.1-complete.jar org.antlr.v4.gui.TestRig %*
Set ANTLR=java -jar C:\Bin\Java\antlr-4.7.1-complete.jar
%ANTLR% -no-listener -visitor -Dlanguage=Python3 Bali.g4
python Program.py examples/ex1.bali
python Program.py examples/ex2.bali
python Program.py examples/ex3.bali
python Program.py examples/ex4.bali