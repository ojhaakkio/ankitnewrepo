import os

API_ID = API_ID = 20346550

API_HASH = os.environ.get("API_HASH", "bc79c3bea7a626887bdc0871eecf0327")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6570733797:AAFOU0CM_CE4gLBNi8jwnuRkoWWMAXePo6U")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(is.environ.get("OWNER" ,"6938920339"))
LOG = -1002011373978

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5665231556").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


