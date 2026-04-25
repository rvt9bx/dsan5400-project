import logging
import os
import platform
import subprocess
import webbrowser
from pathlib import Path

logger = logging.getLogger(__name__)


def open_in_browser(path: Path):
    """Open a local file in the default browser, cross-platform.

    Works on Windows, macOS, Linux, and WSL.

    Args:
        path (Path): Path to the local file to open.

    Returns:
        None
    """
    path = Path(path).resolve()
    url = path.as_uri()

    system = platform.system()
    release = platform.release().lower()

    # Detect WSL
    is_wsl = "microsoft" in release or "wsl" in release

    logger.info("Opening in browser — path: %s, system: %s, WSL: %s", path, system, is_wsl)

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
        logger.info("Successfully opened: %s", url)
    except Exception as e:
        logger.warning("Primary browser open failed (%s), falling back to webbrowser module", e)
        webbrowser.open(url)
