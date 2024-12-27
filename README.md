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


# Disclaimer

## ⚠️ STRICT PROHIBITION OF MALICIOUS USE ⚠️

THIS SOFTWARE IS **STRICTLY PROHIBITED** FOR:
- DDoS (Distributed Denial of Service) attacks
- DoS (Denial of Service) attacks
- Network flooding attacks
- Stress testing without authorization
- CC (Command and Control) attacks
- Any form of network attacks or malicious activities
- Any attempts to overwhelm or disrupt services
- Any form of cyber attacks
- Any illegal network activities
- Targeting individuals or organizations without explicit permission

**VIOLATION OF THESE TERMS MAY RESULT IN LEGAL ACTION**

The developer explicitly condemns and disclaims any use of this software for malicious purposes. This is a testing tool ONLY and should be used responsibly and ethically.

## ⚠️ PERSONAL LIABILITY DISCLAIMER ⚠️

I, THE DEVELOPER OF THIS SOFTWARE, AM NOT RESPONSIBLE FOR:

1. **ANY DAMAGES OR CONSEQUENCES** that may occur from using this tool, including but not limited to:
   - Network outages or disruptions
   - Excessive data charges
   - Bandwidth overages
   - Server costs
   - Hardware damage
   - Loss of service
   - Legal consequences
   - Any financial losses

2. **HOW YOU USE THIS TOOL**
   - I am not responsible for any misuse of this software
   - I am not liable for any illegal activities conducted with this tool
   - I do not endorse any malicious use of this software
   - I take no responsibility for modified versions of this code

3. **THIRD-PARTY ACTIONS**
   - I am not responsible for how third parties may react to your use of this tool
   - I am not liable for any actions taken by network administrators or service providers
   - I take no responsibility for any account suspensions or service terminations

## Important Notice

This Network Bandwidth Pressure Testing Tool ("the Software") is provided for educational and testing purposes only. By using this Software, you acknowledge and agree to the following terms:

## Usage Responsibility

1. **Network Impact**
   - This tool can generate significant network traffic
   - You are solely responsible for any impact on your network or other users
   - Be aware of and respect your network's bandwidth limitations
   - Consider the potential impact on other network users before running tests

2. **Data Usage Warning**
   - The Software downloads large files repeatedly
   - This may result in substantial data consumption
   - Users with data caps should exercise extreme caution
   - Monitor your data usage while using this tool

3. **Server Consideration**
   - Test servers may incur costs from bandwidth usage
   - Excessive use may impact server performance
   - Respect server operators and their resources
   - Do not conduct sustained or abusive testing

## Legal Considerations

1. **Acceptable Use**
   - Only test on networks you own or have explicit permission to test
   - Obtain necessary authorizations before testing
   - Do not use for denial of service attacks or malicious purposes
   - Comply with all applicable laws and regulations

2. **Liability**
   - The Software is provided "AS IS" without warranty of any kind
   - The developers are not responsible for any damages or consequences
   - Users assume all risks associated with using this Software
   - No guarantee of accuracy or reliability is provided

3. **Third-Party Resources**
   - Test nodes listed are third-party services
   - We do not guarantee their availability or performance
   - Users should verify the legitimacy of custom nodes
   - Respect third-party terms of service

## Best Practices

1. **Before Testing**
   - Inform relevant network administrators
   - Check network policies and restrictions
   - Verify available bandwidth capacity
   - Choose appropriate testing parameters

2. **During Testing**
   - Monitor system and network performance
   - Be prepared to stop tests if issues arise
   - Respect fair usage policies
   - Consider off-peak testing times

3. **Security**
   - Verify URLs before testing
   - Do not test unknown or untrusted servers
   - Be cautious with custom node submissions
   - Keep the Software updated

## Indemnification

By using this Software, you agree to indemnify and hold harmless the developer, contributors, and any affiliated parties from any claims, damages, or expenses resulting from your use or misuse of the Software.

## USE AT YOUR OWN RISK

**BY DOWNLOADING, INSTALLING, OR USING THIS SOFTWARE, YOU ACKNOWLEDGE THAT YOU ARE USING IT ENTIRELY AT YOUR OWN RISK. THE DEVELOPER ACCEPTS NO RESPONSIBILITY OR LIABILITY WHATSOEVER.**

## Criminal Liability Notice

The use of this Software for any malicious or illegal purposes may constitute a criminal offense under various local, state, national, and international laws. Users engaging in such activities may be subject to:
- Criminal prosecution
- Civil lawsuits
- Monetary fines
- Imprisonment
- Other legal penalties as applicable

## Updates

This disclaimer may be updated without notice. Continued use of the Software implies acceptance of any changes.

---

Last Updated: December 27, 2024  
For questions or concerns, please open an issue on the GitHub repository.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
