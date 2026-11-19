# Personal Firewall Using Python

## Project Overview

Personal Firewall Using Python is a beginner-friendly cybersecurity project developed to demonstrate basic firewall concepts, traffic evaluation, rule-based filtering and activity logging.

The application evaluates simulated network traffic against predefined firewall rules and displays an ALLOW or BLOCK decision through a graphical dashboard.

## Objectives

- Understand basic firewall concepts.
- Implement rule-based traffic evaluation.
- Work with TCP and UDP protocols.
- Record firewall activity with timestamps.
- Develop a graphical dashboard using Tkinter.
- Practice Python programming and cybersecurity fundamentals.

## Technologies Used

- Python 3
- Scapy
- Tkinter
- JSON
- Kali Linux
- Git and GitHub

## Project Structure

```text
Personal-Firewall/
├── firewall.py
├── firewall_engine.py
├── packet_logger.py
├── dashboard.py
├── rules.json
├── README.md
├── .gitignore
└── logs/
    └── firewall.log
```

## Features

1. Rule-based traffic evaluation.
2. TCP and UDP protocol selection.
3. Destination port validation.
4. ALLOW and BLOCK decisions.
5. Automatic activity logging.
6. Interactive graphical dashboard.
7. Log viewing and refreshing.

## Firewall Rules

| Protocol | Port | Action |
|---|---:|---|
| TCP | 80 | ALLOW |
| TCP | 443 | ALLOW |
| UDP | 53 | ALLOW |
| Other unmatched traffic | Any | BLOCK |

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Enter the project folder:

```bash
cd Personal-Firewall
```

Create a virtual environment:

```bash
python3 -m venv --system-site-packages venv-scapy
```

Activate it:

```bash
source venv-scapy/bin/activate
```

Install Scapy:

```bash
pip install scapy
```

Install Tkinter if necessary:

```bash
sudo apt install python3-tk
```

## Running the Project

Run the firewall engine:

```bash
python firewall_engine.py
```

Run the main application:

```bash
python firewall.py
```

Launch the graphical dashboard:

```bash
python dashboard.py
```

## Testing

The project uses simulated traffic inputs to test firewall decisions.

| Test Case | Expected Result |
|---|---|
| TCP port 80 | ALLOW |
| TCP port 443 | ALLOW |
| UDP port 53 | ALLOW |
| TCP port 9999 | BLOCK |

## Activity Logging

Firewall decisions are stored in:

```text
logs/firewall.log
```

Logs include timestamps, protocols, destination ports and firewall decisions.

## Learning Outcomes

- Python programming fundamentals.
- Basic network security concepts.
- Firewall rule management.
- JSON configuration handling.
- Activity logging.
- Tkinter GUI development.
- GitHub project management.

## Project Limitations

This version is an educational firewall simulator. It evaluates manually entered protocol and port combinations. It does not currently intercept, inspect or block actual network traffic.

Scapy is included as a networking library for future development.

## Future Improvements

- Real-time packet monitoring.
- Advanced firewall rules.
- Source and destination IP filtering.
- Traffic statistics.
- Improved dashboard visualizations.
- Integration with system-level firewall controls.

## Disclaimer

This project is developed for educational purposes and authorized cybersecurity learning.

## Author

**Aritra Pal**

Cybersecurity Student | Cyber crime investigator and fraud analyst

Personal Firewall Using Python
