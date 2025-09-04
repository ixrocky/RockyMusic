from ROCKY_MUSIC.core.bot import ROCKY
from ROCKY_MUSIC.core.dir import dirr
from ROCKY_MUSIC.core.git import git
from ROCKY_MUSIC.core.userbot import Userbot
from ROCKY_MUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ROCKY()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
