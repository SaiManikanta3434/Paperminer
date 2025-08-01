#!/usr/bin/env python3
"""
Startup script for PaperMiner application.
Starts both the FastAPI backend and provides instructions for the frontend.
"""

import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import fastapi
        import uvicorn
        print("✅ Backend dependencies are installed")
    except ImportError as e:
        print(f"❌ Missing backend dependency: {e}")
        print("Please install backend dependencies:")
        print("cd Python && pip install -r requirements.txt")
        return False
    return True

def start_backend():
    """Start the FastAPI backend server."""
    print("🚀 Starting PaperMiner Backend...")
    
    # Change to Python directory
    python_dir = Path("Python")
    if not python_dir.exists():
        print("❌ Python directory not found!")
        return None
    
    try:
        # Start the backend server
        process = subprocess.Popen(
            [sys.executable, "backend.py"],
            cwd=python_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait a moment for the server to start
        time.sleep(3)
        
        if process.poll() is None:
            print("✅ Backend server started successfully!")
            print("📍 Backend URL: http://localhost:8000")
            print("📚 API Documentation: http://localhost:8000/docs")
            return process
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Backend failed to start:")
            print(f"STDOUT: {stdout}")
            print(f"STDERR: {stderr}")
            return None
            
    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        return None

def start_frontend():
    """Provide instructions for starting the frontend."""
    print("\n🎨 Frontend Setup:")
    print("1. Open a new terminal window")
    print("2. Navigate to the frontend directory:")
    print("   cd paperminer-frontend")
    print("3. Install dependencies (if not already done):")
    print("   npm install")
    print("4. Start the development server:")
    print("   npm run dev")
    print("5. Open http://localhost:5173 in your browser")
    
    # Try to open the frontend URL after a delay
    def open_frontend():
        time.sleep(5)
        try:
            webbrowser.open("http://localhost:5173")
        except:
            pass
    
    import threading
    thread = threading.Thread(target=open_frontend)
    thread.daemon = True
    thread.start()

def main():
    """Main startup function."""
    print("=" * 50)
    print("🔬 PaperMiner Application Startup")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Start backend
    backend_process = start_backend()
    if not backend_process:
        print("❌ Failed to start backend. Exiting.")
        return
    
    # Provide frontend instructions
    start_frontend()
    
    print("\n" + "=" * 50)
    print("🎉 Application is starting up!")
    print("=" * 50)
    print("\n📋 Next steps:")
    print("1. Wait for the frontend to start (npm run dev)")
    print("2. Open http://localhost:5173 in your browser")
    print("3. Start searching for papers!")
    print("\n🛑 To stop the application, press Ctrl+C")
    
    try:
        # Keep the backend running
        backend_process.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        backend_process.terminate()
        print("✅ Application stopped.")

if __name__ == "__main__":
    main() 