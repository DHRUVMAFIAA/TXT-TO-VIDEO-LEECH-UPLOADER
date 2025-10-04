

from os import environ

API_ID = int(environ.get("API_ID", "18741803"))
API_HASH = environ.get("API_HASH", "77d466b3a0637e16f05c161b5d3124e4")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "DHRUVMAFIAA1")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/DHRUVMAFIAA1")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "8462664813"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





