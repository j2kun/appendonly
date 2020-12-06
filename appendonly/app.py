import time
from flask import Flask
from flask import Response
from flask import request

from settings import APPENDONLY_FILENAME

app = Flask(__name__)


@app.route('/', methods=['GET'])
def append():
    if request.method == "GET":
        line = request.args.get("data", "")
        line = line.strip()
        if not line:
            return Response("No data GET arg provided", status=400)

        millis = int(round(time.time() * 1000))
        line = '{},{}\n'.format(millis, line)
        try:
            with open(APPENDONLY_FILENAME, 'a') as outfile:
                outfile.write(line)
        except:
            return Request("Could not write to file", status=500)

        return 'Success!'
