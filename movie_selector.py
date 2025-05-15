from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route("/select", methods=['GET', 'POST'])
def movie_selector():
    candidates = request.json['candidates']

    if not all(isinstance(movie, str) for movie in candidates):
        return jsonify({'error': 'Candidates must be a non-empty array of strings.'})

    movie = candidates[random.randint(0, len(candidates)-1)]
    selection = {'selection': movie}

    return jsonify(selection)



