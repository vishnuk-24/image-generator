from flask import Flask, request, render_template, jsonify

from app.openai import image_generator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate-image/", methods=["POST"])
def generate_image():
    """Generate images based on the provided prompt."""
    data = request.get_json()
    response = image_generator(data["prompt"], data["size"])
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
