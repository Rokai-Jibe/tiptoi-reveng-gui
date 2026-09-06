# Building Tiptoi Reveng GUI

## Prerequisites

- Python 3.8 or later
- pip
- PyInstaller

## macOS Build

### 1. Clone and setup
git clone https://github.com/your-username/tiptoi-reveng-gui.git
cd tiptoi-reveng-gui

###2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

###3. Build the app bundle
cd src
pyinstaller TiptoiRevengGUI.spec --clean
The macOS .app bundle will be in dist/TiptoiRevengGUI.app

###4. Test the app
open dist/TiptoiRevengGUI.app

###5. Create a DMG for distribution (optional)
# Install create-dmg if not already installed
brew install create-dmg

# Create DMG
create-dmg --volname "Tiptoi Reveng GUI" --window-pos 200 120 --window-size 800 400 \
  dist/TiptoiRevengGUI.dmg dist/TiptoiRevengGUI.app

Windows Build
Follow the same steps, but replace:

Virtual env activation: venv\Scripts\activate (or venv\Scripts\activate.bat)
Final output will be dist/TiptoiRevengGUI.exe

Notes

The tttool binary must be in the src/ directory when building
PyInstaller bundles will be self-contained and portable
On first run, users will be prompted to select tttool if not found automatically
