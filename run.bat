Set GRUN=java -cp .;C:\Bin\Java\antlr-4.7.1-complete.jar org.antlr.v4.gui.TestRig %*
Set ANTLR=java -jar C:\Bin\Java\antlr-4.7.1-complete.jar
%ANTLR% -no-listener -visitor -Dlanguage=Python3 Bali.g4
python Program.py examples/Arrays.bali
