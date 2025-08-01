#!/usr/bin/env python3
"""
Simple script to start the PaperMiner FastAPI backend.
"""

import sys
import os
from pathlib import Path

# Add the Python directory to the path
python_dir = Path(__file__).parent / "Python"
sys.path.insert(0, str(python_dir))

# Change to Python directory
os.chdir(python_dir)

if __name__ == "__main__":
    print("🚀 Starting PaperMiner Backend...")
    print("📍 Backend will be available at: http://localhost:8000")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        from backend import app
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("Please install dependencies: pip install -r requirements.txt")
    except KeyboardInterrupt:
        print("\n✅ Backend stopped.") 