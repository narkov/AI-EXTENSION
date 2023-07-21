import openai
import requests
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def main():
    return "AI Image Generator"

@app.route('/getimage', methods=['POST'])
@cross_origin()
def process_data():
    #PROMPT = request.form['prompt']
    PROMPT = "darth vader"
    openai.api_key = "YOUR API KEY"
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
        headers={'api-key': 'YOUR WAIFU2X KEY'}
    )
    
    if r.status_code == 200:
        data = r.json()
        url = data["output_url"]
        print(url)
    else:
        print("API request failed")

    return jsonify({'result': url})

if __name__ == '__main__':
    app.run()
