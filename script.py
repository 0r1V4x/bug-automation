#!/usr/bin/env python3
"""
BountyHunter Pro 5.0 - One-Click Launcher
Just run this file and everything works!
"""

import os
import sys
import subprocess
from pathlib import Path

def check_requirements():
    """Check if Python is installed"""
    try:
        subprocess.run([sys.executable, "--version"], check=True, capture_output=True)
        return True
    except:
        return False

def install_python():
    """Guide user to install Python"""
    print("Python is not installed or not in PATH.")
    print("\nPlease install Python 3.8 or higher:")
    print("1. Windows: Download from python.org")
    print("2. Linux: sudo apt install python3 python3-pip")
    print("3. macOS: brew install python3")
    print("\nAfter installation, run this script again.")
    input("\nPress Enter to exit...")
    sys.exit(1)

def main():
    """One-click launcher"""
    print("🚀 Launching BountyHunter Pro 5.0...")
    
    # Check Python
    if not check_requirements():
        install_python()
    
    # Check if script exists
    script_path = Path(__file__).parent / "bountyhunter.py"
    if not script_path.exists():
        print(f"Error: {script_path} not found!")
        print("Please ensure bountyhunter.py is in the same directory.")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Launch the application
    try:
        subprocess.run([sys.executable, str(script_path)])
    except KeyboardInterrupt:
        print("\n\nGoodbye! 👋")
    except Exception as e:
        print(f"Error launching application: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
