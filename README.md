# QuicC2Py

## Project Overview
**QuicC2Py** is an advanced, modular proof-of-concept implementation of a Command-and-Control (C2) system built using Python's `asyncio` framework over UDP. Designed primarily for educational purposes and authorized security testing, this project features an extensible client-server architecture secured with AES encryption, ideal for exploring network security, penetration testing, and protocol development.

## Features

- **UDP-based Communication**: Efficient, low-latency, connectionless communication.
- **AES Encryption**: AES-CBC with 256-bit key (hardcoded for demo).
- **Interactive Command Interface**: Real-time server-side interaction.
- **Supported Commands**:
  - `whoami`: Get current username.
  - `dir`: Directory listing (Windows).
  - `ls`: Directory listing placeholder (Linux).
  - `info`: System info.
  - `upload <filename>`: Client uploads file (string-based).
  - `download <filename>`: Server file download (basic implementation).
  - `help`: List available commands.
  - `exit`: Graceful shutdown.
- **Modular Design**: Modules include `config`, `crypto`, `commands`, `protocol`.
- **Logging**: Actions logged to `logs/udp_c2.log`.
- **Configuration File**: Settings in `config.json`.
- **Cross-Platform**: Compatible with Windows/Linux.
- **Unit Tests**: Preliminary tests (`tests/`) included.

## Potential Use Cases

- **Security Research**: Analyze C2 traffic patterns.
- **Traffic Obfuscation**: Experiment with cloud-based obfuscation (Dropbox, AWS).
- **File Transfer Experiments**: Enhance binary transfer capabilities.
- **Protocol Development**: Simulate advanced protocol features (QUIC-like).
- **Penetration Testing Training**: Implement persistence and stealth features.
- **Educational Tool**: Teaching network security and cryptography.

## Prerequisites

- **Python 3.8+**
- **Dependencies**:
  - `cryptography`
  - `pytest` (optional)
- **Network**: UDP port 4433 (configurable in `config.json`).
- **Operating System**: Tested on Windows/Linux; macOS may need adjustments.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/KW-Soft/QuicC2Py.git
   cd QuicC2Py
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   > _If not running tests, `pip install cryptography` is sufficient._

3. **Verify Configuration**:
   - Check `config.json` for host, port, encryption settings.

## Usage

Detailed usage in [`docs/usage.md`](docs/usage.md).

### Quick Start Guide

**Start Server**:
```bash
python src/server.py
```
Server example output:
```
[Server] QuicC2Py is running on 0.0.0.0:4433...
[Server] Enter command (type 'help' for list, 'exit' to quit):
```

**Start Client**:
```bash
python src/client.py
```
Client example output:
```
[Client] Connecting to localhost:4433...
[Client] Sent: Agent ready!
```

**Interact with Clients** (Server-side):
```
[Server] Enter command: whoami
[Server] Command sent to ('127.0.0.1', 54321): whoami
[Server] Received from ('127.0.0.1', 54321): desktop-XXX\xxxx
```

**Run Tests (optional)**:
```bash
pytest tests/
```

## Directory Structure
```
QuicC2Py/
├── src/
│   ├── server.py
│   ├── client.py
│   ├── config.py
│   ├── crypto.py
│   ├── protocol.py
│   └── commands.py
├── tests/
│   ├── test_crypto.py
│   └── test_commands.py
├── docs/
│   ├── architecture.md
│   └── usage.md
├── logs/ (created at runtime)
│   └── udp_c2.log
├── config.json
├── requirements.txt
└── README.md
```

## Security Warning

> **Important**: **QuicC2Py** is intended **only** for educational and authorized security testing within controlled, permissioned environments. **Never** use in unauthorized or production environments.

- AES keys and IV are hardcoded (not secure).
- No authentication or integrity protection.
- Misuse can result in criminal liability.

Always:

- Obtain explicit permission before testing.
- Comply with local laws and ethical guidelines.
- Consider secure enhancements (dynamic keys, DTLS).

## Limitations

- **Encryption**: Hardcoded AES keys.
- **File Transfers**: Basic text-based handling.
- **Scalability**: Single-threaded.
- **Platform Support**: Some commands unimplemented.
- **Error Handling**: Limited robustness.

## Future Enhancements

- **DTLS Integration**: Secure UDP.
- **Binary File Transfers**: Improve file handling.
- **Dynamic Key Exchange**: Diffie-Hellman implementation.
- **Client Authentication**: Identity verification.
- **Multi-threading**: Concurrent client management.
- **Cloud Integration**: Enhanced obfuscation.

## Contributing

Contributions welcome!

1. Fork repository and create a feature branch.
2. Follow PEP 8 guidelines.
3. Update/add tests in `tests/`.
4. Submit pull requests clearly describing changes.

Report bugs or request features by opening a GitHub issue.

## License

MIT License ([LICENSE](LICENSE)).

## Disclaimer

The software is provided "as is," without any warranty. Users assume full responsibility. Unauthorized or malicious use strictly prohibited.

