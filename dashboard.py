
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from pathlib import Path

from firewall_engine import evaluate_packet
from packet_logger import log_event


# Project log file
BASE_DIR = Path(__file__).parent
LOG_FILE = BASE_DIR / "logs" / "firewall.log"


# Refresh activity logs
def refresh_logs():

    log_display.config(state="normal")
    log_display.delete("1.0", tk.END)

    if LOG_FILE.exists():
        content = LOG_FILE.read_text()

        log_display.insert(tk.END, content)

    log_display.see(tk.END)
    log_display.config(state="disabled")


# Check simulated traffic
def check_traffic():

    protocol = protocol_var.get().upper()

    try:
        port = int(port_entry.get())

        if not 1 <= port <= 65535:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Port",
            "Enter a valid port between 1 and 65535."
        )
        return

    # Evaluate firewall rules
    action = evaluate_packet(protocol, port)

    # Save activity
    log_event(protocol, port, action)

    # Display decision
    if action == "ALLOW":
        result_label.config(
            text="TRAFFIC ALLOWED",
            foreground="#16A34A"
        )
    else:
        result_label.config(
            text="TRAFFIC BLOCKED",
            foreground="#DC2626"
        )

    # Refresh logs
    refresh_logs()


# Main application window
root = tk.Tk()

root.title("Personal Firewall Dashboard")
root.geometry("760x600")
root.configure(bg="#172033")
root.resizable(True, True)


# Heading
title = tk.Label(
    root,
    text="PERSONAL FIREWALL",
    font=("Arial", 23, "bold"),
    bg="#172033",
    fg="white"
)
title.pack(pady=15)


subtitle = tk.Label(
    root,
    text="Python-Based Firewall Monitoring System",
    font=("Arial", 11),
    bg="#172033",
    fg="#9CA3AF"
)
subtitle.pack()


# Input section
input_frame = tk.Frame(
    root,
    bg="#243047",
    padx=20,
    pady=20
)
input_frame.pack(pady=20, padx=30, fill="x")


tk.Label(
    input_frame,
    text="Select Protocol:",
    bg="#243047",
    fg="white",
    font=("Arial", 11)
).grid(row=0, column=0, padx=10, pady=10)


protocol_var = tk.StringVar(value="TCP")

protocol_box = ttk.Combobox(
    input_frame,
    textvariable=protocol_var,
    values=["TCP", "UDP"],
    state="readonly",
    width=15
)
protocol_box.grid(row=0, column=1, padx=10)


tk.Label(
    input_frame,
    text="Destination Port:",
    bg="#243047",
    fg="white",
    font=("Arial", 11)
).grid(row=1, column=0, padx=10, pady=10)


port_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=18
)
port_entry.grid(row=1, column=1, padx=10)


# Check traffic button
check_button = tk.Button(
    input_frame,
    text="CHECK TRAFFIC",
    command=check_traffic,
    bg="#2563EB",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=15,
    pady=8
)
check_button.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=15
)


# Result display
result_label = tk.Label(
    root,
    text="WAITING FOR TRAFFIC...",
    font=("Arial", 16, "bold"),
    bg="#172033",
    fg="white"
)
result_label.pack(pady=10)


# Log section
log_title = tk.Label(
    root,
    text="FIREWALL ACTIVITY LOGS",
    font=("Arial", 13, "bold"),
    bg="#172033",
    fg="white"
)
log_title.pack(pady=10)


log_display = ScrolledText(
    root,
    width=85,
    height=12,
    bg="#0F172A",
    fg="#22C55E",
    font=("Courier", 9),
    state="disabled"
)
log_display.pack(padx=25, pady=10, fill="both", expand=True)


# Refresh button
refresh_button = tk.Button(
    root,
    text="REFRESH LOGS",
    command=refresh_logs,
    bg="#475569",
    fg="white",
    font=("Arial", 10, "bold")
)
refresh_button.pack(pady=10)


# Footer
footer = tk.Label(
    root,
    text="Educational Firewall Simulation | Python + Tkinter",
    bg="#172033",
    fg="#9CA3AF",
    font=("Arial", 9)
)
footer.pack(pady=8)


# Load existing logs
refresh_logs()

# Start application
root.mainloop()

