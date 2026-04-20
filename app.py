from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from src.soccer_detection import detect_soccer_ball, detect_from_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/output/<filename>')
def send_output(filename):
    return send_from_directory('output', filename)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    # Хэрэв файл оруулсан бол
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "Файл сонгоогүй байна"}), 400
        
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        result = detect_from_file(filepath)
        if result.get("detected"):
            result["image_url"] = "/output/detected.jpg"
        return jsonify(result), 200

    # Хэрэв URL оруулсан бол
    data = request.json
    image_url = data.get("image_url") if data else None
    if image_url:
        try:
            result = detect_soccer_ball(image_url)
            if result.get("detected"):
                result["image_url"] = "/output/detected.jpg"
            return jsonify(result), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
            
    return jsonify({"error": "Зураг эсвэл URL оруулна уу"}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)