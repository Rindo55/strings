import os
from dotenv import load_dotenv

load_dotenv()
API_ID= 10247139 
API_HASH = "96b46175824223a33737657ab943fd6a"
BOT_TOKEN= "5222572158:AAGwMiAMGgj9BmMQdcxn58Cq19stEnoVarI" 

DATABASE_URL = os.getenv("DATABASE_URL", "").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = "neko_bots"

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
