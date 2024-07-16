#constants.py
import os

VERSION_NR = '0.0.7'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to dirs
DIR_FONTS = os.path.join(os.path.dirname(__file__), 'app_fonts/')
DIR_IMAGES = os.path.join(os.path.dirname(__file__), 'app_pics/')
DIR_POPUPS = os.path.join(os.path.dirname(__file__), 'popups/')
DIR_MAPS = os.path.join(os.path.dirname(__file__), 'app_pics/img_maps/')
DIR_LOGOS = os.path.join(os.path.dirname(__file__), 'app_pics/img_logos/')
DIR_SIGNS = os.path.join(os.path.dirname(__file__), 'app_pics/img_signs/')
DIR_SPLASH_SCR = os.path.join(os.path.dirname(__file__), 'app_pics/img_splashscreens/')
DIR_TRUCKS = os.path.join(os.path.dirname(__file__), 'app_pics/img_trucks/')


# Paths to images
PATH_TO_MAINLOGO = DIR_LOGOS + 'img_logo_fs22-empire.png'
ATH_DIR_IMG_CHO = os.path.join(os.path.dirname(__file__), 'app_pics/img_cho_map/')

# Path splashscreens
SPL_SCREEN_START_APP = DIR_SPLASH_SCR + 'img_spl_giants.jpg'


# Paths datafiles
PATH_DATA_APP = os.path.join(os.path.dirname(__file__), 'files_data/data_app.json')
PATH_DATA_TXT = os.path.join(os.path.dirname(__file__), 'files_data/data_txt.json')
PATH_DATA_GAME = os.path.join(os.path.dirname(__file__), 'files_data/data_game.json')
DF_TRUCKS = os.path.join(os.path.dirname(__file__), 'files_data/data_lkw.json')
PATH_USER_DATA = os.path.join(os.path.dirname(__file__),'files_data/user_data.json')

# Paths .kv-files

PATH_KV_STARTPAGE = os.path.join(os.path.dirname(__file__), 'pages/page_start/startpage.kv')
PATH_KV_SETTINGPAGE = os.path.join(os.path.dirname(__file__), 'pages/page_settings/settingpage.kv')
PATH_KV_PAGE_4 = os.path.join(os.path.dirname(__file__), 'pages/buyitempage/buyitempage.kv')


PATH_KV_COLORS = os.path.join(os.path.dirname(__file__), 'files_kv/colors.kv')
PATH_KV_BOXES = os.path.join(os.path.dirname(__file__), 'files_kv/boxes.kv')
PATH_KV_COMPONENTS = os.path.join(os.path.dirname(__file__), 'files_kv/components.kv')
PATH_KV_WIDGETS = os.path.join(os.path.dirname(__file__), 'files_kv/widgets.kv')


# constants fonts
TITLEFONT = 'Jura-DemiBold.otf'
LABELFONT_M = 'Jura-Medium.otf'

BUT_CLEAR = os.path.join(os.path.dirname(__file__), 'app_pics/img_clear.png')
