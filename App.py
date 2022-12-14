import logging
from codeitsuisse import app
from flask import render_template, request, send_from_directory, jsonify
from codeitsuisse.routes.ticker import to_cumulative, to_cumulative_delayed
from codeitsuisse.routes.cryptocollapz import solve_cryptocollapz
from codeitsuisse.routes.calendar import calendar_part1, calendar_part2
from codeitsuisse.routes.rubiks import RubiksCube
from codeitsuisse.routes.magic_cauldrons import solve_magic_cauldron
from codeitsuisse.routes.dnscache import store_dns, simulate_query
from codeitsuisse.routes.quordleKeyboard import quordleKeynoard_part1, quordleKeynoard_part2

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
    ans = to_cumulative(data.get('stream'))
    logging.info("My result :{}".format(ans))
    return jsonify({"output":ans})

@app.route('/tickerStreamPart2', methods=['POST'])
def part_2():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative_delayed(data.get("stream"), data.get("quantityBlock"))
    logging.info("My result :{}".format(ans))
    return jsonify({"output": ans})

@app.route('/cryptocollapz', methods=['POST'])
def cryptocollapz():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans=solve_cryptocollapz(data)
    logging.info("My result :{}".format(ans))
    return jsonify(ans)

@app.route('/magiccauldrons', methods=['POST'])
def magiccauldrom():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = solve_magic_cauldron(data)
    logging.info("My result :{}".format(ans))
    return jsonify(ans)

@app.route('/travelling-suisse-robot', methods=['POST'])
def tsr():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative_delayed(data.get("stream"), data.get("quantityBlock"))
    logging.info("My result :{}".format(ans))
    return jsonify({"output": ans})

@app.route('/calendarDays', methods=['POST'])
def calender_days():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = calendar_part1(data.get("numbers"))
    ans2 = calendar_part2(ans)
    logging.info("My result :{}".format(ans))
    logging.info("My result :{}".format(ans2))
    return jsonify({"part1": ans, "part2": ans2})

@app.route('/rubiks', methods=['POST'])
def rubiks():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = RubiksCube(data.get("ops"), data.get("state"))
    logging.info("My result :{}".format(ans))
    return jsonify(ans)

@app.route('/reversle', methods=['POST'])
def reversle():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative_delayed(data.get("stream"), data.get("quantityBlock"))
    logging.info("My result :{}".format(ans))
    return jsonify({"output": ans})

@app.route('/stonks', methods=['POST'])
def stonks():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative_delayed(data.get("stream"), data.get("quantityBlock"))
    logging.info("My result :{}".format(ans))
    return jsonify({"output": ans})

@app.route('/payload_stack', methods=['POST'])
def payload_stack():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative_delayed(data.get("stream"), data.get("quantityBlock"))
    logging.info("My result :{}".format(ans))
    return jsonify({"output": ans})

@app.route('/payload_shellcode', methods=['POST'])
def payload_shellcode():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = to_cumulative_delayed(data.get("stream"), data.get("quantityBlock"))
    logging.info("My result :{}".format(ans))
    return jsonify({"output": ans})

@app.route('/instantiateDNSLookup', methods=['POST'])
def dns_cache1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = store_dns(data.get("lookupTable"))
    logging.info("My result :{}".format(ans))
    return jsonify(ans)

@app.route('/simulateQuery', methods=['POST'])
def dns_cache2():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = simulate_query(data.get("cacheSize"), data.get("log"))
    logging.info("My result :{}".format(ans))
    return jsonify(ans)

@app.route('/quordleKeyboard', methods=['POST'])
def quordleKeyboard():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = quordleKeynoard_part1(data.get("answers"),data.get("attempts"))
    ans2 = quordleKeynoard_part2(data.get("answers"),data.get("attempts"),data.get("numbers"))
    logging.info("My result :{}".format(ans))
    logging.info("My result :{}".format(ans2))
    return jsonify({"part1": ans, "part2": ans2})

if __name__ == "__main__":
    logging.info("Starting application ...")
    app.run(port=8000)
