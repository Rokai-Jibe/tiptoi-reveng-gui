# Tiptoi Reveng GUI

A cross-platform graphical interface for **tttool** – the Swiss Army knife for Tiptoi hackers.

This project provides an easy-to-use GUI wrapper around [tttool](https://github.com/entropia/tip-toi-reveng), making it simple to:

- Extract audio from Tiptoi books
- Export books to YAML format
- Modify book metadata (language, product ID)
- Reassemble modified books
- Analyze and validate Tiptoi files

## Features

✅ User-friendly graphical interface  
✅ Auto-detection of tttool executable  
✅ Support for all major tttool commands  
✅ Real-time command output logging  
✅ Cross-platform (Windows, macOS, Linux)  
✅ Portable executable bundles  
✅ No external dependencies (tkinter included with Python)  

## Requirements

- **Python 3.8** or later
- **tkinter** (included with Python on most systems)
- **tttool** compiled binary (included in this project)

## Installation

### macOS (Recommended)

1. Download the latest `TiptoiRevengGUI.app` from [Releases](https://github.com/Rokai-Jibe/tiptoi-reveng-gui/releases)
2. Move it to `/Applications`
3. Double-click to launch (you may need to allow it in System Preferences > Security & Privacy on first run)

### Windows

1. Download the latest `TiptoiRevengGUI.exe` from [Releases](https://github.com/Rokai-Jibe/tiptoi-reveng-gui/releases)
2. Run the executable (no installation required)

### Linux

1. Clone the repository:
   ```bash
   git clone https://github.com/Rokai-Jibe/tiptoi-reveng-gui.git
   cd tiptoi-reveng-gui

Install Python and tkinter:
# Ubuntu/Debian
sudo apt-get install python3 python3-tk

# Fedora
sudo dnf install python3 python3-tkinter

Run the GUI:
python3 src/tttool_gui.py


From Source (All Platforms)

Clone the repository:
git clone https://github.com/Rokai-Jibe/tiptoi-reveng-gui.git
cd tiptoi-reveng-gui

Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run the GUI:
python3 src/tttool_gui.py


Usage

Launch the application
Select a Tiptoi file (.gme or .tiptoi)
Choose a command:
extract – Extract audio and scripts
export – Export to YAML format
convert – Convert between formats
info – Display file information
language – Change language setting
play – Play Tiptoi product information


Configure options (if applicable)
Run and wait for completion
Access output from the results display

Common Operations

Extract audio files: Use the extract command
Modify metadata: Use the language or product commands
Create custom Tiptoi files: Export to YAML, edit, then rebuild

Troubleshooting
"tttool not found"

The application will prompt you to locate the tttool binary
Select it from your system or download it from tip-toi-reveng

"Permission denied" (macOS)

The app bundle may need to be authorized in System Preferences
Go to System Preferences > Security & Privacy > General
Click "Open Anyway" next to the app

"Python not found" (Windows/Linux)

Ensure Python 3.8+ is installed and added to PATH
Verify: python3 --version

Output text is hard to read

The output window uses a system font that should be readable
On Windows/Linux, you can modify the font size in the code if needed

Building from Source
See BUILDING.md for detailed instructions on:

Building macOS .app bundles
Building Windows .exe executables
Creating distribution packages (DMG, MSI, etc.)

Contributing
Contributions are welcome! Please:

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

Areas for Contribution

UI/UX improvements
Windows and Linux builds/testing
Documentation
Bug fixes
Feature requests

License
This project is licensed under the MIT License – see LICENSE file for details.
Acknowledgments

tttool by the Entropia community – the incredible reverse-engineering tool behind this GUI
Tiptoi by Ravensburger – the original interactive book system
Python community for tkinter and PyInstaller

Disclaimer
This project is for educational and personal use only. Tiptoi is a trademark of Ravensburger. This tool is not affiliated with, endorsed by, or connected to Ravensburger. Use at your own risk and respect copyright laws.
Support

📖 Tiptoi Reveng Documentation
🐛 Report issues
💬 Discussions


Made with ❤ ️ by Rokai-Jib, using Claude AI Sonnet 5
