# Architecture of QuicC2Py

## Overview
QuicC2Py is structured as a modular client-server application using UDP for communication. It employs AES encryption for data security and supports extensible command handling.

## Components
- **src/config.py**: Loads configuration from `config.json`.
- **src/crypto.py**: Handles AES encryption and decryption.
- **src/commands.py**: Defines and executes client-side commands.
- **src/protocol.py**: Core protocol logic for UDP communication.
- **src/server.py**: Server entry point and command interface.
- **src/client.py**: Client entry point and command execution.

## Data Flow
1. Server starts and listens on UDP port (default: 4433).
2. Client connects and sends an encrypted "Agent ready!" message.
3. Server receives, decrypts, and registers the client.
4. User inputs commands, which are encrypted and sent to clients.
5. Clients decrypt, execute, and return encrypted results.