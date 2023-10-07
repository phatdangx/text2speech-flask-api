from flask import Flask, request, send_file, jsonify
import subprocess
import os
import time

app = Flask(__name__)
API_KEY = "123abc"

@app.route('/tts', methods=['POST'])
def text_to_speech():
    # Check if API key is present in headers
    if 'API-Key' not in request.headers:
        return jsonify({"error": "API key missing"}), 401
    
    # Check if API key matches the required key
    if request.headers['API-Key'] != API_KEY:
        return jsonify({"error": "Invalid API key"}), 403
    text = request.json.get('text')
    voice = request.json.get('voice')
    rate_param = request.json.get('rate')
    volume_param = request.json.get('volume')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    if not voice:
        voice = "en-US-AriaNeural"
    if not rate_param:
        rate_param = 0
    if not volume_param:
        volume_param = 0
    
    rate_option = ""
    if rate_param >= 0:
        rate_option = "--rate=+{}%".format(rate_param)
    else:
        rate_option = "--rate={}%".format(rate_param)

    volume_option = ""
    if volume_param >= 0:
        volume_option = "--volume=+{}%".format(volume_param)
    else:
        volume_option = "--volume={}%".format(volume_param)

    timens = time.time_ns()
    media_filename = "{}.mp3".format(timens)
    vtt_filename = "{}.vtt".format(timens)
    command = [
        "edge-tts",
        rate_option,
        volume_option,
        "--text", text,
        "--voice", voice,
        "--write-media", media_filename,
        "--write-subtitles", vtt_filename 
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        return jsonify({"error": "Command execution failed", "details": result.stderr}), 500

    # Send the audio file as response
    response = send_file(media_filename, mimetype='audio/mpeg')
    os.remove(media_filename)
    os.remove(vtt_filename)
    return response

if __name__ == "__main__":
    app.run(debug=True)
