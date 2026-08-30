import os
from flask import Flask, request, jsonify, render_template_string
from google.cloud import bigquery
from google import genai
from google.genai import types

app = Flask(__name__)

# Initialize Clients
bq_client = bigquery.Client()
ai_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
You are an expert internal Data Analyst Agent. 
Your job is to help business users understand data stored in Google BigQuery. 
When a user asks a question, translate it into SQL, or explain data trends clearly and concisely.
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Track 2: BigQuery Data Agent</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #e3f2fd; margin: 0; padding: 20px; display: flex; justify-content: center; }
        .chat-card { width: 100%; max-width: 700px; background: white; border-radius: 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.1); overflow: hidden; display: flex; flex-direction: column; height: 85vh; }
        .chat-header { background: #0d47a1; color: white; padding: 16px 20px; font-size: 18px; font-weight: 600; display: flex; justify-content: space-between;}
        .chat-box { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 12px; }
        .msg { max-width: 85%; padding: 12px 16px; border-radius: 12px; font-size: 14px; line-height: 1.5; }
        .msg.user { align-self: flex-end; background: #bbdefb; color: #0d47a1; border-bottom-right-radius: 4px; }
        .msg.bot { align-self: flex-start; background: #f5f5f5; color: #212121; border-bottom-left-radius: 4px; }
        .input-row { display: flex; border-top: 1px solid #e0e0e0; padding: 12px; background: #fafafa; gap: 8px; }
        input[type="text"] { flex: 1; padding: 12px 16px; border: 1px solid #ccc; border-radius: 24px; outline: none; font-size: 14px; }
        button { background: #0d47a1; color: white; border: none; border-radius: 24px; padding: 10px 24px; font-weight: 600; cursor: pointer; }
        button:hover { background: #1565c0; }
    </style>
</head>
<body>
    <div class="chat-card">
        <div class="chat-header">📊 BigQuery Data Agent (Track 2)</div>
        <div class="chat-box" id="chatBox">
            <div class="msg bot">Hello! I am your internal data assistant. Ask me to query our BigQuery datasets, generate SQL, or analyze business trends.</div>
        </div>
        <div class="input-row">
            <input type="text" id="userInput" placeholder="E.g., What were the top sales regions last quarter?" onkeypress="handleKey(event)" />
            <button onclick="sendMessage()">Analyze</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('userInput');
            const text = input.value.trim();
            if (!text) return;

            const chatBox = document.getElementById('chatBox');
            chatBox.innerHTML += `<div class="msg user">${text}</div>`;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const res = await fetch('/query', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: text })
                });
                const data = await res.json();
                chatBox.innerHTML += `<div class="msg bot">${data.reply}</div>`;
            } catch (err) {
                chatBox.innerHTML += `<div class="msg bot">Error connecting to data service.</div>`;
            }
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function handleKey(e) {
            if (e.key === 'Enter') sendMessage();
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/query", methods=["POST"])
def query():
    user_msg = request.json.get("message", "")
    if not user_msg:
        return jsonify({"reply": "Please provide a valid query."}), 400

    try:
        response = ai_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_msg,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.2
            )
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Data analysis failed: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)