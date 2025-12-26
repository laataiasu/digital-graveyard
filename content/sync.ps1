# --- Define Variables ---
# Use the backslash for path separation in Windows
$PYTHON_BIN = "C:\Users\al\Projects\sandbox-hub\.venv\Scripts\python.exe"
$PROJECT_DIR = "C:\Users\al\Projects\digital-graveyard\content"
$SYNC_SCRIPT = "$PROJECT_DIR\sync_content.py"
$BLOG_DIR = "C:\Users\al\Projects\digital-garden"

# --- Execute Python Script ---
# Use the call operator (&) to execute the Python executable with the script path
& $PYTHON_BIN $SYNC_SCRIPT

# --- Change Directory ---
# 'cd' is an alias for 'Set-Location' and works in PowerShell
cd $BLOG_DIR

# --- Execute npx command ---
# 'npx' is a standard executable and runs directly
npx quartz build --serve