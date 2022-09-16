import logging
from codeitsuisse import app
from flask import render_template, request, send_from_directory, jsonify
from codeitsuisse.routes.ticker import to_cumulative, to_cumulative_delayed
import os
import glob

logger = logging.getLogger(__name__)
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)

@app.route('/', methods=['GET'])
def default_route():
    return "Python Template"


@app.route('/tickerStreamPart1', methods=['POST'])
def part_1():
    logging.info("Error")
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative(data)
    logging.info("My result :{}".format(ans))
    return jsonify(ans)

@app.route('/tickerStreamPart2', methods=['POST'])
def part_2():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative_delayed(data["stream"], data["quantityBlock"])
    logging.info("My result :{}".format(ans))
    return jsonify({"output": ans})


if __name__ == "__main__":
    logging.info("Starting application ...")
    app.run(port=8000)
