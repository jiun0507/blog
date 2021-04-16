import configparser as cfg

config = ".config.cfg"


class Keys:
    def __init__(self):
        self.alpaca_api_id = self.read_key_from_config_file(config, "alpaca_api_id")
        self.alpaca_key = self.read_key_from_config_file(config, "alpaca_key")

    def read_key_from_config_file(self, config, key):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get("creds", key)
