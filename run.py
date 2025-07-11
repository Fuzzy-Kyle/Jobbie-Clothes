#!/usr/bin/env python3
"""
Quick launcher for Jobbie-Clothes Resume Enhancer
Run this file to start the Streamlit application
"""

import subprocess
import sys
import os

def main():
    """Launch the Streamlit application"""
    try:
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        main_py_path = os.path.join(script_dir, "main.py")
        
        # Run streamlit with the main.py file
        subprocess.run([sys.executable, "-m", "streamlit", "run", main_py_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running the application: {e}")
        print("Make sure you have installed the requirements:")
        print("pip install -r requirements.txt")
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")

if __name__ == "__main__":
    main()