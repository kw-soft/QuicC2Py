from src.commands import CommandHandler

def test_whoami():
    handler = CommandHandler()
    result = handler.execute("whoami")
    assert result  # Sollte nicht leer sein