from services.database import get_config


def test_config_database_padrao():
    config = get_config()
    assert config["database"]
    assert isinstance(config["port"], int)
