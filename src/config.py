import json
import os

class Config:
    def __init__(self, config_file="config.json"):
        with open(config_file, "r") as f:
            config = json.load(f)
        self.server_host = config["server"]["host"]
        self.server_port = config["server"]["port"]
        self.client_host = config["client"]["host"]
        self.client_port = config["client"]["port"]
        self.aes_key = bytes.fromhex(config["crypto"]["aes_key"])
        self.aes_iv = bytes.fromhex(config["crypto"]["aes_iv"])
        self.log_path = config["logging"]["path"]
        self.log_level = config["logging"]["level"]

    def __str__(self):
        return f"Config(server={self.server_host}:{self.server_port}, client={self.client_host}:{self.client_port})"