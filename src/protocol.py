import logging
from crypto import encrypt_message, decrypt_message

class UDPC2Protocol:
    def __init__(self, config, is_server=False):
        self.transport = None
        self.config = config
        self.is_server = is_server
        self.clients = {} if is_server else None
        logging.basicConfig(filename=config.log_path, level=config.log_level)
        self.logger = logging.getLogger("UDPC2")

    def connection_made(self, transport):
        self.transport = transport
        self.logger.info(f"{'Server' if self.is_server else 'Client'} connected")
        print(f"[{'Server' if self.is_server else 'Client'}] Connected")

    def datagram_received(self, data, addr):
        message = decrypt_message(data, self.config.aes_key, self.config.aes_iv)
        if message:
            self.logger.info(f"Received from {addr}: {message}")
            if self.is_server:
                print(f"[Server] Received from {addr}: {message}")  # Console Print: Server
                if addr not in self.clients:
                    self.clients[addr] = True
                    self.logger.info(f"New client registered: {addr}")
                    print(f"[Server] New client registered: {addr}")
            else:
                print(f"[Client] Received from {addr}: {message}")  # Console Print: Client
            return message
        else:
            self.logger.error(f"Failed to decrypt message from {addr}")
            print(f"[{'Server' if self.is_server else 'Client'}] Failed to decrypt message from {addr}")
            return None

    def error_received(self, exc):
        self.logger.error(f"Error: {exc}")
        print(f"[{'Server' if self.is_server else 'Client'}] Error: {exc}")

    def send_message(self, message, addr=None):
        encrypted = encrypt_message(message, self.config.aes_key, self.config.aes_iv)
        if self.is_server and addr:
            self.transport.sendto(encrypted, addr)
            self.logger.info(f"Sent to {addr}: {message}")
            print(f"[Server] Sent to {addr}: {message}")
        else:
            self.transport.sendto(encrypted)
            self.logger.info(f"Sent: {message}")
            print(f"[Client] Sent: {message}")