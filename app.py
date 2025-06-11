from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/', methods=['POST'])
def virtual_ta():
    data = request.get_json()

    question = data.get("question", "")
    image = data.get("image", None)  # We'll use this later if needed

    # Dummy answer for now
    response = {
        "answer": f"Thanks for your question: '{question}'. This is a dummy answer.",
        "links": [
            {
                "url": "https://example.com/example-post-1",
                "text": "Example link 1"
            },
            {
                "url": "https://example.com/example-post-2",
                "text": "Example link 2"
            }
        ]
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
