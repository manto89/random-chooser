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

@app.route("/")
def index():
	choices = read_file()
	ret = []
	for a in range(10):
		random.shuffle(choices)
		ret.append(choices[-1] + " | " + choices[-2] + " | " + choices[-3])
	return ret

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

