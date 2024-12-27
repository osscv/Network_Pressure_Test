# Network Bandwidth Pressure Tester

A Python-based tool for testing network bandwidth capacity through multi-threaded downloads from various speed test servers worldwide.

## Features

- **Automatic Node Selection**: Automatically tests and selects the fastest server based on latency
- **Multiple Test Servers**: Includes a curated list of speed test servers across different global locations
- **Configurable Threading**: Customizable number of concurrent download threads
- **Real-time Statistics**: Live monitoring of download progress and error counts
- **Custom URL Support**: Ability to test against user-provided URLs
- **Error Handling**: Robust error handling for failed connections and downloads

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/network-pressure-tester.git
cd network-pressure-tester
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

Run the script:
```bash
python pressure_test.py
```

You'll be presented with three options:

1. **Auto-select fastest node**: The script will test all available nodes and choose the one with lowest latency
2. **Choose a specific node**: Select from a predefined list of speed test servers
3. **Enter your own custom node URL**: Test against your own server/URL

### Configuration

- Default number of threads: 32 (configurable during runtime)
- Download chunk size: 1MB
- Connection timeout: 5 seconds

## How It Works

1. The tool first measures latency to all available test servers (if using auto-select)
2. Creates multiple threads to simultaneously download from the selected server
3. Monitors and displays real-time statistics including:
   - Total elapsed time
   - Total data downloaded
   - Number of errors encountered
4. Test continues until interrupted (Ctrl+C)

## Test Servers

Includes speed test servers from:
- Hetzner (Multiple locations)
- NForce
- TransIP
- OneAsiaHost
- And more...

## Warning

⚠️ This tool is designed for network testing purposes only. Please be mindful of:
- Your internet service provider's data caps
- Server bandwidth costs
- Potential impact on other network users

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

Under this license, if you use, modify, or distribute this software, you must:
- Include the original source code
- State changes you made
- Maintain the same license terms
- Include copyright and license notices
- Link to the original repository

Original work by www.dkly.top | 2024
Repository: https://github.com/osscv/Network_Pressure_Test
