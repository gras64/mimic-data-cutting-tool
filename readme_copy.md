# This is a data-cutting-tool

the is an simple tool, to get a train.text to import in mimic2 https://github.com/MycroftAI/mimic2 (tacotron).


### Prozess Files

For now, `train.text` made available which
can be found in this folder. To use your own corpus follow these steps.

1. you can use it to sort out all sentences with a certain number of characters

### use the cutting tool

that cuts out all sentences over 499 characters. further things could be added you can use the tool with
* 'python3 data-cutting-tool.py'

if you want to use a different file.
* python3 corpus_file_gen.py --file train.text.csv
if you want to allow more characters
* python3 corpus_file_gen.py --max_char 500
or --help for help.

requests for expansion are welcome

# Contributions
by gras64
