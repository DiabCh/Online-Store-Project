SHIPPING_ADDRESS = 1
BILLING_ADDRESS = 2
no_difficulty = 0
new_bg = 1
ACTIVATION_AVAILABILITY = {
    'unit': 'minutes',
    'value': 60,
}
ACTIVATION_AVAILABILITY_DICT = {
    ACTIVATION_AVAILABILITY['unit']: ACTIVATION_AVAILABILITY['value']

} # { 'minutes' : 30 }

ACCESSORY = 'AC'
FAMILY_GAME = 'FG'
DEXTERITY_GAME = 'DG'
PARTY_GAME = 'PG'
ABSTRACT = 'A'
THEMATIC_GAME = 'TG'
EUROGAME = 'EG'
WARGAME = 'WG'
AREA_CONTROL = 'AR'
LEGACY = 'L'
DECKBUILDER = 'DB'
DRAFTING = 'DR'
DUNGEON_CRAWLER = 'DC'
WORKER_PLACEMENT = 'WP'
MINIATURE = 'MI'
STRATEGY = 'ST'
GAME_GENRES = [
    (ACCESSORY, 'Accessory'),
    (FAMILY_GAME, 'Family Game'),
    (DEXTERITY_GAME, 'Dexterity Game'),
    (PARTY_GAME, 'Party Game'),
    (ABSTRACT, 'Abstract Game'),
    (THEMATIC_GAME, 'Thematic Game'),
    (EUROGAME, 'Eurogame'),
    (WARGAME, 'Wargame'),
    (AREA_CONTROL, 'Area Control'),
    (LEGACY, 'Legacy'),
    (DECKBUILDER, 'Deckbuilder'),
    (DRAFTING, 'Drafting'),
    (DUNGEON_CRAWLER, 'Dungeon Crawler'),
    (WORKER_PLACEMENT, 'Worker Placement'),
    (MINIATURE, 'Miniature'),
    (STRATEGY, 'Strategy')
]