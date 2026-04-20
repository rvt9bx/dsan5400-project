import os
import platform
import subprocess
import webbrowser
from pathlib import Path

def open_in_browser(path: Path):
    """
    Open a local file in the default browser, cross-platform.
    Works on Windows, macOS, Linux, and WSL.
    """
    path = Path(path).resolve()
    url = path.as_uri()

    system = platform.system()
    release = platform.release().lower()

    # Detect WSL
    is_wsl = "microsoft" in release or "wsl" in release

    try:
        if is_wsl:
            # Use Windows browser via explorer.exe
            win_path = subprocess.check_output(["wslpath", "-w", str(path)]).decode().strip()
            subprocess.run(["explorer.exe", win_path], check=False)
        elif system == "Windows":
            os.startfile(path)  # type: ignore
        elif system == "Darwin":
            subprocess.run(["open", url], check=False)
        else:
            # Linux
            subprocess.run(["xdg-open", url], check=False)
    except Exception:
        # Fallback (last resort)
        webbrowser.open(url)