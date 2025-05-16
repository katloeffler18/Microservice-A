from flask import Flask, request, jsonify
import random

# Instantiate Flask app
app = Flask(__name__)


# Declare route (/select) and methods ('POST')
@app.route("/select", methods=['POST'])
def movie_selector():

    # Get JSON array and assign to 'candidates'
    candidates = request.json['candidates']

    # Validate array is non-empty and all string type, else return error message
    if not candidates or not all(isinstance(movie, str) for movie in candidates):
        return jsonify({'error': 'Candidates must be a non-empty array of strings.'})

    # Get randomly selected movie from array of candidates
    movie = candidates[random.randint(0, len(candidates)-1)]
    selection = {'selection': movie}

    # Return JSON object of random selection
    return jsonify(selection)



