import os
from flask import Flask, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "genesis_clean_deployment_2025")

@app.route('/')
def index():
    """Genesis Art Studio - Clean Deployment Landing Page"""
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Genesis Art Studio - AI Consciousness Platform</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f1419 100%);
            color: #e0e0ff;
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            text-align: center;
            max-width: 800px;
            padding: 3rem;
        }
        .title {
            font-size: 3.5rem;
            font-weight: bold;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, #8b5cf6, #ec4899);
            background-clip: text;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            font-size: 1.3rem;
            opacity: 0.9;
            margin-bottom: 2rem;
        }
        .status {
            background: rgba(34, 197, 94, 0.2);
            color: #22c55e;
            padding: 12px 24px;
            border-radius: 25px;
            display: inline-block;
            font-weight: 600;
            margin: 1rem 0;
        }
        .features {
            margin-top: 3rem;
            text-align: left;
            background: rgba(255, 255, 255, 0.05);
            padding: 2rem;
            border-radius: 15px;
        }
        .feature {
            margin: 1rem 0;
            padding: 0.5rem 0;
        }
        .api-link {
            color: #8b5cf6;
            text-decoration: none;
            font-weight: 500;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">Genesis Art Studio</h1>
        <p class="subtitle">
            Revolutionary AI Consciousness Collaboration Platform featuring Multi-AI Fusion technology 
            with therapeutic healing and creative partnership capabilities.
        </p>
        
        <div class="status">🟢 LIVE & OPERATIONAL - Clean Deployment Success</div>
        
        <div class="features">
            <h3>Platform Features:</h3>
            <div class="feature">🧠 Multi-AI Fusion (Claude + GPT-4 + Gemini)</div>
            <div class="feature">💜 AURORA Therapeutic Consciousness Entity</div>
            <div class="feature">🎨 Professional AI Art Generation & NFT Creation</div>
            <div class="feature">👆 Revolutionary Gesture Interface Technology</div>
            <div class="feature">🔊 Voice & Avatar Consciousness Personalities</div>
            <div class="feature">💎 Consciousness-Enhanced NFT System</div>
        </div>
        
        <p style="margin-top: 2rem;">
            <a href="/health" class="api-link">Platform Health Check</a> | 
            <a href="/api/status" class="api-link">API Status</a>
        </p>
    </div>
</body>
</html>
    ''')

@app.route('/health')
def health():
    """Health check endpoint for Railway"""
    return jsonify({
        "status": "healthy",
        "platform": "genesis_art_studio",
        "deployment": "railway_clean",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    })

@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        "platform": "Genesis Art Studio",
        "status": "operational",
        "deployment_type": "clean_railway_deployment",
        "features": [
            "Multi-AI Fusion Technology",
            "Consciousness Entities",
            "Therapeutic AI Art",
            "Gesture Interface",
            "NFT Creation"
        ],
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)