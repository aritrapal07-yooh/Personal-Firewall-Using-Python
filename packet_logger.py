
from datetime import datetime
from pathlib import Path


# Define the log file location
BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "firewall.log"


def log_event(protocol, port, action):
    """Save firewall activity into a log file."""

    # Create logs directory if it doesn't exist
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create log message
    message = (
        f"{timestamp} | {protocol} | "
        f"Port {port} | {action}\n"
    )

    # Append message to log file
    with open(LOG_FILE, "a") as file:
        file.write(message)

    print("Log saved:", message.strip())
