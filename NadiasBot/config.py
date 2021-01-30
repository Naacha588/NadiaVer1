from NadiasBot.sample_config import Config

class Development(Config):
    OWNER_ID = 1404831944  # your telegram ID
    OWNER_USERNAME = "abyssmail"  # your telegram username
    API_KEY = "1408988315:AAH9c0bDPdSN0qKEMWuoPEbE8yd33UqblMw"  # your api key, as provided by the @botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    JOIN_LOGGER = '-1001482674302' # some group chat that your bot is a member of
    USE_JOIN_LOGGER = True
    DRAGONS = [1006428724, 1266129474]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']