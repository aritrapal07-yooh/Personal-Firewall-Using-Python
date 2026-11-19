
from firewall_engine import evaluate_packet
from packet_logger import log_event


def start_firewall():

    print("=" * 40)
    print("       PERSONAL FIREWALL")
    print("=" * 40)

    print("Firewall simulation started!")
    print("Enter 'exit' to stop.")

    while True:

        protocol = input(
            "\nEnter protocol (TCP/UDP): "
        ).strip().upper()

        if protocol == "EXIT":
            print("Firewall stopped.")
            break

        if protocol not in ["TCP", "UDP"]:
            print("Invalid protocol. Try TCP or UDP.")
            continue

        try:
            port = int(input("Enter destination port: "))

            if not 1 <= port <= 65535:
                print("Port must be between 1 and 65535.")
                continue

        except ValueError:
            print("Please enter a valid port number.")
            continue

        action = evaluate_packet(protocol, port)

        log_event(protocol, port, action)

        print("-" * 40)
        print("Firewall Decision:", action)
        print("-" * 40)


if __name__ == "__main__":
    start_firewall()
