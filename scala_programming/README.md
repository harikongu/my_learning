Scala Programming
===================

Installing erlang Compiler
--------------------------
sudo apt-get install erlang-ic

Compile the erlang program
--------------------------
$ erlc hello_world.erl

$ ls
hello_world.beam  hello_world.erl 

Execute the erlang Program
--------------------------
erl -noshell -s hello_world start -s init stop

