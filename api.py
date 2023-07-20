import openai
import requests
from flask import Flask, render_template
import json

app = Flask(__name__)

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"
openai.api_key = "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"
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
    headers={'api-key': '904db71b-6abd-4863-a76b-5056433d917b'}
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