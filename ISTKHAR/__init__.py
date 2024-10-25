from ISTKHAR.core.bot import PURVI 
from ISTKHAR.core.dir import dirr
from ISTKHAR.core.git import git
from ISTKHAR.core.userbot import Userbot
from ISTKHAR.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PURVI ()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
