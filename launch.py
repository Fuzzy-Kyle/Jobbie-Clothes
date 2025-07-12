#!/usr/bin/env python3
"""
Alternative launcher for Jobbie-Clothes Resume Enhancer
This script ensures proper startup and provides troubleshooting info
"""

import subprocess
import sys
import time
import webbrowser
import socket

def check_port(port):
    """Check if port is available"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        return result == 0
    except:
        return False

def main():
    print("🚀 Launching Jobbie-Clothes Resume Enhancer...")
    print("💅 👔 👠 👞 🦺 Welcome to your Job Boutique! 🦺 👞 👠 👔 💅\n")
    
    # Check if port 8501 is available
    if check_port(8501):
        print("⚠️  Port 8501 is already in use!")
        print("🔄 Trying alternative port 8502...")
        port = 8502
    else:
        port = 8501
    
    try:
        print(f"🌐 Starting application on port {port}...")
        print(f"📝 Application will be available at: http://127.0.0.1:{port}")
        print("🔒 Running locally only - completely secure and private")
        print("\n" + "="*60)
        print("INSTRUCTIONS:")
        print("1. Wait for 'You can now view your Streamlit app' message")
        print("2. Open your browser and go to the URL shown")
        print("3. Click 'Download Language Data' in sidebar (first time)")
        print("4. Upload your resume and paste job description")
        print("5. Generate enhanced documents!")
        print("="*60 + "\n")
        
        # Start Streamlit
        cmd = [
            sys.executable, "-m", "streamlit", "run", "main.py",
            "--server.port", str(port),
            "--server.address", "127.0.0.1",
            "--browser.gatherUsageStats", "false"
        ]
        
        subprocess.run(cmd)
        
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user.")
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure you're in the project directory")
        print("2. Activate virtual environment: source jobbie-env/bin/activate")
        print("3. Install dependencies: pip install -r requirements.txt")
        print("4. Try: python main.py")

if __name__ == "__main__":
    main()