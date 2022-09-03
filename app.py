import random
from flask import Flask

app = Flask(__name__)

def read_file():
	f = open("input.txt","r")
	lines = f.readlines()
	ret = []
	for line in lines:
		ret.append(line.replace("\n", ""))
	return ret

def get_block(inner_text):
  return "<h1>" + inner_text + "</h1>"

def get_span(inner_text):
  return inner_text + " "

@app.route("/")
def index():
	choices = read_file()
	ret = ""
	for a in range(10):
		random.shuffle(choices)
		ret += get_block(get_span(choices[-1]) + get_span(choices[-2]) + get_span(choices[-3]))
	return ret

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

