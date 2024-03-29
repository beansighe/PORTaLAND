"""
All paths used to access game assets
"""

import pathlib

ASSETS_PATH = pathlib.Path(__file__).resolve().parent.parent / "assets"

GAMEOVER_IMAGE_PATH = ASSETS_PATH/"images"/"gameover_image.png"

INSTRUCTIONS_PATH = ASSETS_PATH/"images"/"instructions.png"

LYING_CAKE_PATH = ASSETS_PATH/"images"/"theCakeIsALie.png"

TITLE_PATH = ASSETS_PATH/"images"/"portaland.png"

PLAYER_PATH = ASSETS_PATH/"images"/"SPRITES"/"player"

PORTAL_PATH = ASSETS_PATH/"images"/"SPRITES"/"portal"

IDLE_PATH = PLAYER_PATH/"idle"

RUN_SHOOT_PATH = PLAYER_PATH/"run-shoot"

JUMP_PATH = PLAYER_PATH/"jump"

CLIMB_PATH = PLAYER_PATH/"climb"

GAMEVIEW_MUSIC_PATH = ASSETS_PATH/"music"/"TwilightForest.wav"

NEW_SCREENS_MUSIC_PATH = ASSETS_PATH/"music"/"TheTunnel.wav"

GAMEVIEW_MUSIC_PATH = ASSETS_PATH/"music"/"TwilightForest.wav"

NEW_SCREENS_MUSIC_PATH = ASSETS_PATH/"music"/"TheTunnel.wav"
