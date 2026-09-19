import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel serverless handler
# The app is a WSGI application that Vercel can use directly
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
