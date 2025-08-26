import openai
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set your OpenAI API key
openai.api_key = "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"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def generate_code():
    try:
        data = request.get_json()
        question = data.get("question", "")
        language = data.get("language", "")

        if not question or not language:
            return jsonify({"result": "⚠️ Please provide both question and language."})

        # Call OpenAI ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert code generator."},
                {"role": "user", "content": f"Write code in {language} for: {question}"}
            ],
            temperature=0.5,
            max_tokens=500
        )

        generated_code = response["choices"][0]["message"]["content"].strip()

        return jsonify({"result": generated_code})

    except Exception as e:
        return jsonify({"result": f"⚠️ Error: {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)
