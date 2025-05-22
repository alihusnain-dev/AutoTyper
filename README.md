# 📝 Auto Typer VU

**Auto Typer VU** is a lightweight desktop utility that simulates human typing to help **Virtual University (VU)** students automatically enter long text in portals that block paste operations (like LMS assignments, quizzes, etc.).

Instead of pasting, it "types" your content, character-by-character, with configurable speed – bypassing portal restrictions.

---

## 🌟 Features

- ✅ Clean GUI — no coding needed
- ✅ Supports large text input
- ✅ Adjustable typing speed (slider)
- ✅ 5-second delay to place cursor
- ✅ Cross-platform: Windows, macOS, Linux
- ✅ Offline: No internet required after install
- ✅ Free & open source

---

## 📸 Screenshot

> 📷 *(Add your screenshot here)*  
> You can include a screenshot of the app window once it's running.

---

## 📦 How to Install & Run (For Beginners)

### 🔧 Step-by-step Setup (1st time only)

> 🐍 Requires Python 3.7 or newer.  
> [Download Python here if needed](https://www.python.org/downloads/)

```bash
# 1. Clone this repo or download the ZIP
git clone https://github.com/yourusername/auto-typer-vu.git
cd auto-typer-vu

# 2. Create a virtual environment (isolated Python setup)
python -m venv venv

# 3. Activate the virtual environment
# ▶ On PowerShell (Windows)
.\venv\Scripts\Activate.ps1

# ▶ On CMD (Windows)
venv\Scripts\activate.bat

# ▶ On macOS/Linux/Git Bash
source venv/bin/activate

# 4. Install required Python packages
pip install -r requirements.txt

# 5. Run the app
python auto_typer.py
