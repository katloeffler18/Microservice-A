import requests

# Declare URL
url = ' http://127.0.0.1:5000/select'

# Define JSON array
candidates = {"candidates": ['Inception', 'Anora', 'The Devil Wears Prada']}

# Make POST request
movie = requests.post(url, json=candidates)

print(movie.json())
