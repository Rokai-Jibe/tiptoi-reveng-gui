# Tiptoi Reveng GUI

A cross-platform graphical interface for [tttool](https://github.com/entropia/tip-toi-reveng) - the Swiss Army knife for Tiptoi hackers.

[![GitHub Release](https://img.shields.io/github/v/release/Rokai-Jibe/tiptoi-reveng-gui)](https://github.com/Rokai-Jibe/tiptoi-reveng-gui/releases)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![macOS](https://img.shields.io/badge/macOS-10.13+-success)](https://www.apple.com/macos/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)

## Features

✨ **User-friendly GUI** for tttool commands
- Upload and modify Tiptoi binary files (.tiptoi)
- Extract audio and images from books
- Generate OID codes
- Full support for all tttool operations

🎯 **Cross-platform** (macOS with standalone app bundle)

⚙️ **Flexible configuration** with external config files

## Installation

### macOS (Recommended)

1. Download the latest release from [Releases](https://github.com/Rokai-Jibe/tiptoi-reveng-gui/releases)
2. Extract `TiptoiRevengGUI-macOS-v1.0.0.zip`
3. Move `TiptoiRevengGUI.app` to your **Applications** folder
4. Launch the app!

### Manual Installation (All Platforms)

**Requirements:**
- Python 3.10+
- tttool compiled binary
```bash
git clone https://github.com/Rokai-Jibe/tiptoi-reveng-gui.git
cd tiptoi-reveng-gui
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/tttool_gui.py
```
### Usage

1. Launch the application
2. Select a Tiptoi file to modify
3. Choose your operation from available tttool commands
4. Configure options as needed
5. Apply changes and save the modified file

### Building from Source
See [BUILDING.md](https://github.com/Rokai-Jibe/tiptoi-reveng-gui/blob/main/BUILDING.md) for detailed instructions on building the macOS app bundle.

### Project Structure
```bash
tiptoi-reveng-gui/
├── src/
│   ├── tttool_gui.py          # Main GUI application
│   ├── tttool                 # Compiled tttool binary
│   └── config.json            # Configuration file
├── requirements.txt           # Python dependencies
├── BUILDING.md               # Build instructions
└── README.md                 # This file
```
### Configuration
Edit src/config.json to customize:

Default paths
Tttool binary location
UI preferences
```bash
{
  "tttool_path": "~/tiptoi-reveng-gui/src/tttool",
  "default_output_dir": "~/Downloads",
  "theme": "light"
}
```
### Dependencies

tkinter : GUI framework
Python 3.10+ : Runtime

For development/building:

PyInstaller : Create macOS app bundle
cabal : Build tttool from source

### Credits

[tttool](https://github.com/entropia/tip-toi-reveng) - The original command-line tool
[tip-toi-reveng](https://github.com/entropia/tip-toi-reveng) - Reverse engineering project

### License
MIT License - see LICENSE file
Author
Rokai-Jibe - [GitHub Profile](https://github.com/Rokai-Jibe) - with the full help of Claude Sonnet 5
