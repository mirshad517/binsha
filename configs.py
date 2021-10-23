# (c) @MRK_YT

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("MT_BOT_TOKEN")
	BOT_USERNAME = os.environ.get("MT_BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("MT_BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("MT_UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("MT_LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("MO_TECH_YT", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍ **Developer:** @dev_mirshad

👨‍💻 **Users:** movies privet group

📺 **Support:** [Instagram](https://instagram.com/mirshad_kvr?utm_medium=copy_link)

🗣️ **Any Doubt:** @dev_mirshad

📢 **ഞാൻ 😁:** [ഞാൻ😁] (എന്നെ ഡെവലപ്പ് ചെയ്തത് @dev_mirshad ആണ് അത് കൊണ്ട് ചിലപ്പോൾ എന്തങ്കിലും പ്രേശ്നങ്ങൾ ഉണ്ടങ്കിൽ അറിയിക്കുക NB:എന്നെ എന്റെ chunks ഉള്ള മൂവീസ് എന്നാ പ്രൈവറ്റ് ഗ്രൂപ്പിൽ മാത്രേ യൂസ് ചെയ്യാൻ പറ്റു 
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍ **Developer:** @dev_mirshad

💻 **Developer Details:** [Clcik Here](https://instagram.com/mirshad_kvr?utm_medium=copy_link)

👨‍💻 **Users:** Movies Privet Group

🗣️ **Any Doubt:** @dev_mirshad

📺 **Support :** [Instagram](https://instagram.com/mirshad_kvr?utm_medium=copy_link)

📢  **ഞാൻ 😁:** [ഞാൻ😁] (എന്നെ ഡെവലപ്പ് ചെയ്തത് @dev_mirshad ആണ് അത് കൊണ്ട് ചിലപ്പോൾ എന്തങ്കിലും പ്രേശ്നങ്ങൾ ഉണ്ടങ്കിൽ അറിയിക്കുക NB:എന്നെ എന്റെ chunks ഉള്ള മൂവീസ് എന്നാ പ്രൈവറ്റ് ഗ്രൂപ്പിൽ മാത്രേ യൂസ് ചെയ്യാൻ പറ്റു 
"""

Donate Now (coming soon)
"""
	HOME_TEXT = """
**👋Hi. എന്നെ ഉണ്ടാക്കിയത് @dev_mirshad ആണ് അത് കൊണ്ട് ചിലപ്പോൾ errors ഒക്കെ ഉണ്ടാകും 🤣 എന്നെ
ഞാൻ വർക്ക്‌ ചെയ്യുന്നത് phython എന്നാ ഭാഷയിലാണ് എന്നെ എല്ലാ ഗ്രൂപ്പിലും യൂസ് ചെയ്യാൻ പറ്റില്ല എല്ലാ ഗ്രൂപ്പിലും വാരി വലിച്ചു ഇടരുത് ഞാൻ ഒരു പാവം ആണ്
(**, [{}](tg://user?id={})\n\n**This is Permanent** **Bot**.

**Send me any file I will give you a permanent Sharable Link.**.
"""

