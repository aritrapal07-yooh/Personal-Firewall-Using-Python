

import json
from pathlib import Path
from packet_logger import log_event

def load_rules():
    """Load firewall rules from rules.json."""

    file_path = Path(__file__).with_name("rules.json")

    with open(file_path, "r") as file:
        data = json.load(file)

    return data


def evaluate_packet(protocol, port):
    """Decide whether simulated traffic is allowed or blocked."""

    data = load_rules()

    protocol = protocol.upper()

    for rule in data["rules"]:

        if (rule["protocol"] == protocol
                and rule["port"] == port):

            return rule["action"]

    return data["default_action"]


if __name__ == "__main__":

    print("PERSONAL FIREWALL ENGINE")
    print("------------------------")

    test_packets = [
        ("TCP", 80),
        ("TCP", 443),
        ("UDP", 53),
        ("TCP", 9999)
    ]

    for protocol, port in test_packets:

        result = evaluate_packet(protocol, port)
        log_event(protocol, port, result)

        print(
            f"Protocol: {protocol} | "
            f"Port: {port} | "
            f"Action: {result}"
        )

