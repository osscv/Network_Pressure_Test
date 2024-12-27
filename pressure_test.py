"""
Network Bandwidth Pressure Tester
Copyright (C) 2024 www.dkly.top

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Repository: https://github.com/osscv/Network_Pressure_Test
"""

import requests
import time
import threading
import re

# List of test nodes
nodes = [
    "https://nbg1-speed.hetzner.com/10GB.bin",
    "https://fsn1-speed.hetzner.com/10GB.bin",
    "https://hel1-speed.hetzner.com/10GB.bin",
    "https://ash-speed.hetzner.com/10GB.bin",
    "https://hil1-speed.hetzner.com/10GB.bin",
    "https://sin-speed.hetzner.com/10GB.bin",
    "https://ash-speed.hetzner.com/1GB.bin",
    "https://mirror.sg.gs/10gb.bin",
    "https://mirror.nforce.com/pub/speedtests/10000mb.bin",
    "https://mirror.nforce.com/pub/speedtests/1000mb.bin",
    "https://mirror.nforce.com/pub/speedtests/500mb.bin",
    "https://ping.virtua.cloud/10GB.bin",
    "https://ping.virtua.cloud/100MB.bin",
    "http://speed.transip.nl/1gb.bin",
    "http://speedtest.oneasiahost.com/100mb.bin"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
DEFAULT_THREADS = 32


def measure_latency(url):
    """Measure latency for a given node."""
    try:
        start_time = time.time()
        response = requests.head(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            return time.time() - start_time
    except requests.RequestException:
        pass
    return float('inf')  # Infinite latency for failed requests


def find_fastest_node():
    """Find the fastest node based on latency."""
    print("Testing nodes to find the fastest...")
    latencies = []
    for node in nodes:
        latency = measure_latency(node)
        if latency == float('inf'):
            print(f"Node: {node}, Latency: Failed")
        else:
            print(f"Node: {node}, Latency: {latency:.2f}s")
        latencies.append((latency, node))

    # Filter out nodes with infinite latency
    latencies = [entry for entry in latencies if entry[0] != float('inf')]
    if not latencies:
        print("No reachable nodes. Please check your internet connection.")
        return None

    latencies.sort()  # Sort by latency (ascending)
    fastest = latencies[0][1]
    print(f"Fastest node selected: {fastest}")
    return fastest


def download_file(url, thread_id, stop_event, stats):
    """Download a file to test bandwidth pressure."""
    while not stop_event.is_set():
        try:
            response = requests.get(url, headers=HEADERS, stream=True)
            if response.status_code == 200:
                for chunk in response.iter_content(1024 * 1024):  # 1MB chunks
                    if stop_event.is_set():
                        break
                    stats["total_downloaded"] += len(chunk)
        except requests.RequestException:
            stats["errors"] += 1


def print_realtime_stats(stats, stop_event, start_time):
    """Print real-time statistics while the test is running."""
    while not stop_event.is_set():
        elapsed = time.time() - start_time
        downloaded_mb = stats["total_downloaded"] / (1024 * 1024)
        print(f"\rElapsed: {elapsed:.2f}s | Downloaded: {downloaded_mb:.2f} MB | Errors: {stats['errors']}", end="", flush=True)
        time.sleep(5)  # Update every 5 seconds
    print()  # Add a newline after stopping


def pressure_test(url, threads=DEFAULT_THREADS):
    """Run bandwidth pressure test."""
    print(f"Starting bandwidth pressure test on {url} with {threads} threads...")
    stop_event = threading.Event()
    stats = {"total_downloaded": 0, "errors": 0}
    threads_list = []

    # Initialize start_time to track total elapsed time for the test
    start_time = time.time()

    # Start download threads
    for i in range(threads):
        thread = threading.Thread(target=download_file, args=(url, i, stop_event, stats))
        thread.start()
        threads_list.append(thread)

    # Start real-time stats thread
    stats_thread = threading.Thread(target=print_realtime_stats, args=(stats, stop_event, start_time))
    stats_thread.start()

    try:
        # Wait for user to stop the test with Ctrl+C
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopping test...")
        stop_event.set()
        for thread in threads_list:
            thread.join()
        stats_thread.join()

        elapsed = time.time() - start_time
        downloaded_mb = stats["total_downloaded"] / (1024 * 1024)
        print(
            f"Test completed. Total time: {elapsed:.2f}s, Downloaded: {downloaded_mb:.2f} MB, Errors: {stats['errors']}")


def validate_url(url):
    """Validate if the user-provided URL is valid."""
    url_regex = re.compile(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", re.IGNORECASE)
    return re.match(url_regex, url) is not None


def main():
    print("1. Auto-select fastest node")
    print("2. Choose a specific node")
    print("3. Enter your own custom node URL")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        url = find_fastest_node()
        if url is None:
            return
    elif choice == "2":
        print("Available nodes:")
        for i, node in enumerate(nodes):
            print(f"{i + 1}. {node}")
        selection = int(input("Select a node (number): ").strip()) - 1
        if 0 <= selection < len(nodes):
            url = nodes[selection]
        else:
            print("Invalid selection.")
            return
    elif choice == "3":
        url = input("Enter your custom node URL: ").strip()
        if validate_url(url):
            print(f"Using custom URL: {url}")
        else:
            print("Invalid URL entered. Please try again.")
            return
    else:
        print("Invalid choice.")
        return

    threads = int(input(f"Enter the number of threads (default {DEFAULT_THREADS}): ").strip() or DEFAULT_THREADS)
    pressure_test(url, threads)


if __name__ == "__main__":
    main()
