import openai
import requests
from flask import Flask, render_template
import json

app = Flask(__name__)

PROMPT = "YOUR PROMPT HERE"
openai.api_key = "DALL-E API KEY"
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
)

r = requests.post(
    "https://api.deepai.org/api/waifu2x",
    data={
        'image': response["data"][0]["url"],
    },
    headers={'api-key': 'WAIFU2X API KEY'}
)
#print(r.json())
if r.status_code == 200:
    data = r.json()
    url = data["output_url"]
    print(url)
else:
    print("API request failed")

@app.route('/api/data', methods=['POST'])
def process_data():
    data = request.json
    # Perform backend processing with the received data
    result = url
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
