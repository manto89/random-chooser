
import asyncio
from asyncore import loop
import random
from re import A
from flask import Flask

from db import Db

app = Flask(__name__)
db = Db()
db.init_pool()


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
async def index():
	# choices = read_file()
	choices = await db.get_random_items()
	ret = ""
	for a in range(10):
		print(choices)
		random.shuffle(choices)
		ret += get_block(get_span(choices[-1]['text']) + get_span(choices[-2]['text']) + get_span(choices[-3]['text']))
	return ret


if __name__ == "__main__":
	app.run(host="127.0.0.1", port=8080, debug=True)
