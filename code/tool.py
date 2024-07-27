import sys
import time
import pygame


# types
class Type:
    def __init__(self, name):
        self.name = name
        self.weakness = []
        self.resistances = []
        self.immunities = []


Bug_type = Type("Bug")
Dark_type = Type("Dark")
Dragon_type = Type("Dragon")
Electric_type = Type("Electric")
Fairy_type = Type("Fairy")
Fighting_type = Type("Fighting")
Fire_type = Type("Fire")
Flying_type = Type("Flying")
Ghost_type = Type("Ghost")
Grass_type = Type("Grass")
Ground_type = Type("Ground")
Ice_type = Type("Ice")
Normal_type = Type("Normal")
Poison_type = Type("Poison")
Psychic_type = Type("Psychic")
Rock_type = Type("Rock")
Steel_type = Type("Steel")
Unknown_type = Type("Unknown")
Water_type = Type("Water")

Bug_type.resistances = (Fighting_type, Ground_type, Grass_type)
Bug_type.weakness = (Fire_type, Flying_type, Rock_type)

Dark_type.immunities = (Psychic_type,)
Dark_type.resistances = (Ghost_type, Dark_type)
Dark_type.weakness = (Fighting_type, Bug_type, Fairy_type)

Dragon_type.resistances = (Fire_type, Water_type, Grass_type, Electric_type)
Dragon_type.weakness = (Ice_type, Dragon_type, Fairy_type)

Electric_type.resistances = (Electric_type, Flying_type, Steel_type)
Electric_type.weakness = (Ground_type,)

Fairy_type.immunities = (Dragon_type,)
Fairy_type.resistances = (Fighting_type, Bug_type, Dark_type)
Fairy_type.weakness = (Poison_type, Steel_type)

Fighting_type.immunities = (Ghost_type,)
Fighting_type.resistances = (Rock_type, Bug_type, Dark_type)
Fighting_type.weakness = (Flying_type, Psychic_type, Fairy_type)

Fire_type.resistances = (Steel_type, Fairy_type, Bug_type, Ice_type, Grass_type)
Fire_type.weakness = (Water_type, Rock_type, Ground_type)

Flying_type.immunities = (Ground_type,)
Flying_type.resistances = (Fighting_type, Bug_type, Grass_type)
Flying_type.weakness = (Electric_type, Ice_type, Rock_type)

Ghost_type.immunities = (Normal_type,)
Ghost_type.resistances = (Poison_type, Bug_type)
Ghost_type.weakness = (Ghost_type, Dark_type)

Grass_type.resistances = (Ground_type, Water_type, Grass_type, Electric_type)
Grass_type.weakness = (Fire_type, Ice_type, Poison_type, Flying_type, Bug_type)

Ground_type.immunities = (Electric_type,)
Ground_type.resistances = (Poison_type, Rock_type)
Ground_type.weakness = (Water_type, Ice_type, Grass_type)

Ice_type.resistances = (Ice_type,)
Ice_type.weakness = (Fire_type, Fighting_type, Rock_type, Steel_type)

Normal_type.immunities = (Ghost_type,)
Normal_type.weakness = (Fighting_type,)

Poison_type.resistances = (Fighting_type, Poison_type, Bug_type, Fairy_type, Grass_type)
Poison_type.weakness = (Ground_type, Psychic_type)

Psychic_type.resistances = (Fighting_type, Psychic_type)
Psychic_type.weakness = (Bug_type, Ghost_type, Dark_type)

Rock_type.resistances = (Normal_type, Fire_type, Poison_type, Flying_type)
Rock_type.weakness = (Water_type, Grass_type, Fighting_type, Ground_type, Steel_type)

Steel_type.immunities = (Poison_type,)
Steel_type.resistances = (Normal_type, Grass_type, Ice_type, Flying_type, Psychic_type, Bug_type, Rock_type,
                          Dragon_type, Steel_type, Fairy_type)
Steel_type.weakness = (Fire_type, Fighting_type, Ground_type)

Water_type.resistances = (Steel_type, Fire_type, Water_type, Ice_type)
Water_type.weakness = (Electric_type, Grass_type)

# controller
controller = {
    "up": pygame.K_z,
    "down": pygame.K_s,
    "left": pygame.K_q,
    "right": pygame.K_d,
    "run": pygame.K_LSHIFT,
    "bike": pygame.K_b,
    "interact": pygame.K_SPACE
}

# data
ALL_DIALOGS = {
    "Saint-Rémy": {"Flora": ["hello !", "aaa"], "Giovani": ["aaa"]},
    "house_a": {"Flora": ["good bye !"]},
    "maptest": {}
}

ALL_FIGHTERS = {
    "Saint-Rémy": {"Flora": ["pikachu"]},
    "house_a": {"Flora": ["pikachu"]},
    "maptest": {}
}

ENTITIES_DESTINATIONS = {}


# function
def delay_print(string):
    for char in string:
        sys.stdout.write(str(char))
        sys.stdout.flush()
        time.sleep(0.01)
    time.sleep(st)
    print("")


def split_spritesheet(spritesheet):
    all_images = {"down": [],
                  "left": [],
                  "right": [],
                  "up": []
                  }
    width = spritesheet.get_width() // 4
    height = spritesheet.get_height() // 4
    for j, k in enumerate(all_images.keys()):
        for i in range(4):
            all_images[k].append(spritesheet.subsurface(pygame.Rect(i * width, j * height, 24, 32)))
    return all_images


# random variables

st = 0.25
f_boost = [0.25, 0.29, 0.33, 0.4, 0.5, 0.66, 1, 1.5, 2, 2.5, 3, 3.5, 4]

# Sex
male = "Male"
female = "Female"

# Category
special = "Special"
physical = "Physical"
status = "Status"

# States
burn = "Burn"
freeze = "Freeze"
paralysis = "Paralysis"
poisoning = "Poisoning"
badly_poisoned = "Badly poisoned"
sleep = "Sleep"

# Second States
attract = "Attract"
confusion = "Confusion"
flinch = "Flinch"

# Weather
clear = "clear"
sun = "sun"
rain = "rain"

# Tiers
anything_goes = 9
uber = 8
over_used = 7
border_line_ou = 6.5
under_used = 6
border_line_uu = 5.5
rarely_used = 5
border_line_ru = 4.5
never_used = 4
border_line_nu = 3.5
pu = 3
nfe = 2
little_cup = 1

# natures
hardy = [1, 1, 1, 1, 1, 1]
lonely = [1, 1.1, 0.9, 1, 1, 1]
brave = [1, 1.1, 1, 1, 1, 0.9]
adamant = [1, 1.1, 1, 0.9, 1, 1]
naughty = [1, 1.1, 1, 1, 0.9, 1]
bold = [1, 0.9, 1.1, 1, 1, 1]
docile = [1, 1, 1, 1, 1, 1]
relaxed = [1, 1, 1.1, 1, 1, 0.9]
impish = [1, 1, 1.1, 0.9, 1, 1]
lax = [1, 1, 1.1, 0.9, 1, 1]
timid = [1, 0.9, 1, 1, 1, 1.1]
hasty = [1, 1, 0.9, 1, 1, 1.1]
serious = [1, 1, 1, 1, 1, 1]
jolly = [1, 1, 1, 0.9, 1, 1.1]
naive = [1, 1, 1, 1, 0.9, 1.1]
modest = [1, 0.9, 1, 1.1, 1, 1]
mild = [1, 1, 0.9, 1.1, 1, 1]
quiet = [1, 1, 1, 1.1, 1, 0.9]
bashful = [1, 1, 1, 1, 1, 1]
rash = [1, 1, 1, 1.1, 0.9, 1]
calm = [1, 0.9, 1, 1, 1.1, 1]
gentle = [1, 1, 0.9, 1, 1.1, 1]
sassy = [1, 1, 1, 1, 1, 1]
careful = [1, 1, 1, 1, 1.1, 0.9]
quirky = [1, 1, 1, 1, 1, 1]

# additional effects
self_boost = "self boost"
target_boost = "target boost"
self_status = "self status"
target_status = "target status"
recoil = "recoil"

# objects
abomasite = "abomasite"
absolite = "absolite"
absorb_bulb = "absorb bulb"
adamant_orb = "adamant orb"
adamant_crystal = "adamant crystal"
aerodactylite = "aerodactylite"
aggronite = "aggronite"
aguav_berry = "aguav berry"
air_balloon = "air balloon"
alakazite = "alakazite"
aloraichium_z = "aloraichium z"
altarianite = "altarianite"
ampharosite = "ampharosite"
apicot_berry = "apicot berry"
aspear_berry = "aspear berry"
assault_vest = "assault vest"
audinite = "audinite"
babiri_berry = "babiri berry"
banettite = "banettite"
beedrillite = "beedrillite"
belue_berry = "belue berry"
berry_juice = "berry juice"
big_root = "big root"
binding_band = "binding band"
black_belt = "black belt"
black_glasses = "black glasses"
black_sludge = "black sludge"
blank_plate = "blank plate"
blastoisinite = "blastoisinite"
blazikenite = "blazikenite"
blue_orb = "blue orb"
bluk_berry = "bluk berry"
bright_powder = "bright powder"
bug_gem = "bug gem"
buginium_z = "buginium z"
burn_drive = "burn drive"
cameruptite = "cameruptite"
cell_battery = "cell battery"
charcoal = "charcoal"
charizardite_x = "charizardite x"
charizardite_y = "charizardite y"
charti_berry = "charti berry"
cheri_berry = "cheri berry"
chesto_berry = "chesto berry"
chilan_berry = "chilan berry"
chill_drive = "chill drive"
choice_band = "choice band"
choice_scarf = "choice scarf"
choice_specs = "choice specs"
chople_berry = "chople berry"
coba_berry = "coba berry"
colbur_berry = "colbur berry"
cornn_berry = "cornn berry"
custap_berry = "custap berry"
damp_rock = "damp rock"
dark_gem = "dark gem"
darkinium_z = "darkinium z"
decidium_z = "decidium z"
deep_sea_scale = "deep sea scale"
deep_sea_tooth = "deep sea tooth"
destiny_knot = "destiny knot"
diancite = "diancite"
douse_drive = "douse drive"
draco_plate = "draco plate"
dragon_fang = "dragon fang"
dragon_gem = "dragon gem"
dragonium_z = "dragonium z"
dread_plate = "dread plate"
durin_berry = "durin berry"
earth_plate = "earth plate"
eevium_z = "eevium z"
eject_button = "eject button"
eject_pack = "eject pack"
electric_gem = "electric gem"
electrium_z = "electrium z"
enigma_berry = "enigma berry"
eviolite = "eviolite"
expert_belt = "expert belt"
fairium_z = "fairium z"
fairy_gem = "fairy gem"
fighting_gem = "fighting gem"
fightinium_z = "fightinium z"
figy_berry = "figy berry"
fire_gem = "fire gem"
firium_z = "firium z"
fist_plate = "fist plate"
flame_orb = "flame orb"
flame_plate = "flame plate"
float_stone = "float stone"
flying_gem = "flying gem"
flyinium_z = "flyinium z"
focus_band = "focus band"
focus_sash = "focus sash"
full_incense = "full incense"
galladite = "galladite"
ganlon_berry = "ganlon berry"
garchompite = "garchompite"
gardevoirite = "gardevoirite"
gengarite = "gengarite"
ghost_gem = "ghost gem"
ghostium_z = "ghostium z"
glalitite = "glalitite"
grass_gem = "grass gem"
grassium_z = "grassium z"
grepa_berry = "grepa berry"
grip_claw = "grip claw"
griseous_orb = "griseous orb"
ground_gem = "ground gem"
groundium_z = "groundium z"
gyaradosite = "gyaradosite"
haban_berry = "haban berry"
hard_stone = "hard stone"
heat_rock = "heat rock"
heavy_duty_boots = "heavy-duty boots"
heracronite = "heracronite"
hondew_berry = "hondew berry"
houndoominite = "houndoominite"
iapapa_berry = "iapapa berry"
ice_gem = "ice gem"
icicle_plate = "icicle plate"
icium_z = "icium z"
icy_rock = "icy rock"
incinium_z = "incinium z"
insect_plate = "insect plate"
iron_ball = "iron ball"
iron_plate = "iron plate"
jaboca_berry = "jaboca berry"
kangaskhanite = "kangaskhanite"
kasib_berry = "kasib berry"
kebia_berry = "kebia berry"
kee_berry = "kee berry"
kelpsy_berry = "kelpsy berry"
kings_rock = "king's rock"
kommonium_z = "kommonium z"
lagging_tail = "lagging tail"
lansat_berry = "lansat berry"
latiasite = "latiasite"
latiosite = "latiosite"
lax_incense = "lax incense"
leftovers = "leftovers"
leppa_berry = "leppa berry"
liechi_berry = "liechi berry"
life_orb = "life orb"
light_ball = "light ball"
light_clay = "light clay"
lopunnite = "lopunnite"
lucarionite = "lucarionite"
lucky_punch = "lucky punch"
lum_berry = "lum berry"
luminous_moss = "luminous moss"
lunalium_z = "lunalium z"
lustrous_orb = "lustrous orb"
lycanium_z = "lycanium z"
magnet = "magnet"
mago_berry = "mago berry"
magost_berry = "magost berry"
manectite = "manectite"
maranga_berry = "maranga berry"
marshadium_z = "marshadium z"
mawilite = "mawilite"
meadow_plate = "meadow plate"
medichamite = "medichamite"
metagrossite = "metagrossite"
metal_coat = "metal coat"
metal_powder = "metal powder"
metronome = "metronome"
mewnium_z = "mewnium z"
mewtwonite_x = "mewtwonite x"
mewtwonite_y = "mewtwonite y"
micle_berry = "micle berry"
mimikium_z = "mimikium z"
mind_plate = "mind plate"
miracle_seed = "miracle seed"
muscle_band = "muscle band"
mystic_water = "mystic water"
nanab_berry = "nanab berry"
never_melt_ice = "never-melt ice"
nomel_berry = "nomel berry"
normal_gem = "normal gem"
normalium_z = "normalium z"
occa_berry = "occa berry"
odd_incense = "odd incense"
oran_berry = "oran berry"
pamtre_berry = "pamtre berry"
passho_berry = "passho berry"
payapa_berry = "payapa berry"
pecha_berry = "pecha berry"
persim_berry = "persim berry"
petaya_berry = "petaya berry"
pidgeotite = "pidgeotite"
pikanium_z = "pikanium z"
pikashunium = "pikashunium"
pinap_berry = "pinap berry"
pinsirite = "pinsirite"
pixie_plate = "pixie plate"
poison_barb = "poison barb"
poison_gem = "poison gem"
poisonium_z = "poisonium z"
pomeg_berry = "pomeg berry"
power_herb = "power herb"
primarium_z = "primarium z"
psychic_gem = "psychic gem"
psychium_z = "psychium z"
qualot_berry = "qualot berry"
quick_claw = "quick claw"
quick_powder = "quick powder"
rabuta_berry = "rabuta berry"
rawst_berry = "rawst berry"
razor_claw = "razor claw"
razor_fang = "razor fang"
razz_berry = "razz-berry"
red_card = "red card"
red_orb = "red orb"
rindo_berry = "rindo berry"
ring_target = "ring target"
rock_gem = "rock gem"
rock_incense = "rock incense"
rockium_z = "rockium z"
rocky_helmet = "rocky helmet"
rose_incense = "rose incense"
roseli_berry = "roseli berry"
rowap_berry = "rowap berry"
sablenite = "sablenite"
safety_goggles = "safety goggles"
salac_berry = "salac berry"
salamencite = "salamencite"
sceptilite = "sceptilite"
scizorite = "scizorite"
scope_lens = "scope lens"
sea_incense = "sea incense"
sharp_beak = "sharp beak"
sharpedonite = "sharpedonite"
shed_shell = "shed shell"
shell_bell = "shell bell"
shock_drive = "shock drive"
shuca_berry = "shuca berry"
silk_scarf = "silk scarf"
silver_powder = "silver powder"
sitrus_berry = "sitrus berry"
sky_plate = "sky plate"
slowbronite = "slowbronite"
smooth_rock = "smooth rock"
snorlium_z = "snorlium z"
snowball = "snowball"
soft_sand = "soft sand"
solganium_z = "solganium z"
soul_dew = "soul dew"
spell_tag = "spell tag"
spelon_berry = "spelon berry"
splash_plate = "splash plate"
spooky_plate = "spooky plate"
starf_berry = "starf berry"
steel_gem = "steel gem"
steelium_z = "steelium z"
steelixite = "steelixite"
stick = "stick"
sticky_barb = "sticky barb"
stone_plate = "stone plate"
swampertite = "swampertite"
sweet_heart = "sweet heart"
tamato_berry = "tamato berry"
tanga_berry = "tanga berry"
tapunium_z = "tapunium z"
thick_club = "thick club"
throat_spray = "throat spray"
toxic_orb = "toxic orb"
toxic_plate = "toxic plate"
twisted_spoon = "twisted spoon"
tyranitarite = "tyranitarite"
ultranecrozium_z = "ultranecrozium z"
venusaurite = "venusaurite"
wacan_berry = "wacan berry"
water_gem = "water gem"
waterium_z = "waterium z"
watmel_berry = "watmel berry"
wave_incense = "wave incense"
weakness_policy = "weakness policy"
wepear_berry = "wepear berry"
white_herb = "white herb"
wide_lens = "wide lens"
wiki_berry = "wiki berry"
wise_glasses = "wise glasses"
yache_berry = "yache berry"
zap_plate = "zap plate"
zoom_lens = "zoom lens"

# Talents
water_absorb = "water_absorb"
volt_absorb = "volt_absorb"
defiant = "defiant"
adaptability = "adaptability"
hustle = "hustle"
gale_wings = "gale_wings"
air_lock = "air_lock"
snow_warning = "snow_warning"
wandering_spirit = "wandering_spirit"
parental_bond = "parental_bond"
analytic = "analytic"
soul_heart = "soul-heart"
no_guard = "no_guard"
soundproof = "soundproof"
anticipation = "anticipation"
water_bubble = "water_bubble"
magma_armor = "magma_armor"
battle_armor = "battle_armor"
mirror_armor = "mirror_armor"
weak_armor = "weak_armor"
aroma_veil = "aroma_veil"
inner_focus = "inner_focus"
fairy_aura = "fairy_aura"
aura_break = "aura_break"
dark_aura = "dark_aura"
sand_rush = "sand_rush"
cheek_pouch = "cheek_pouch"
schooling = "schooling"
competitive = "competitive"
battery = "battery"
oblivious = "oblivious"
chilling_neigh = "chilling_neigh"
aftermath = "aftermath"
steely_spirit = "steely_spirit"
beast_boost = "beast_boost"
shields_down = "shields_down"
fluffy = "fluffy"
blaze = "blaze"
mold_breaker = "mold_breaker"
screen_cleaner = "screen_cleaner"
trace = "trace"
power_spot = "power_spot"
neuroforce = "neuroforce"
super_luck = "super_luck"
slush_rush = "slush_rush"
honey_gather = "honey_gather"
chlorophyll = "chlorophyll"
cloud_nine = "cloud_nine"
big_pecks = "big_pecks"
justified = "justified"
healer = "healer"
anger_point = "anger_point"
huge_power = "huge_power"
contrary = "contrary"
shell_armor = "shell_armor"
flame_body = "flame_body"
dazzling = "dazzling"
perish_body = "perish_body"
ice_body = "ice_body"
cursed_body = "cursed_body"
clear_body = "clear_body"
corrosion = "corrosion"
drizzle = "drizzle"
guts = "guts"
misty_surge = "misty_surge"
electric_surge = "electric_surge"
grassy_surge = "grassy_surge"
psychic_surge = "psychic_surge"
merciless = "merciless"
rain_dish = "rain_dish"
dancer = "dancer"
slow_start = "slow_start"
hunger_switch = "hunger_switch"
stance_change = "stance_change"
defeatist = "defeatist"
gulp_missile = "gulp_missile"
color_change = "color_change"
unburden = "unburden"
flower_gift = "flower_gift"
berserk = "berserk"
dragons_maw = "dragon's_maw"
marvel_scale = "marvel_scale"
ice_scales = "ice_scales"
limber = "limber"
white_smoke = "white_smoke"
shield_dust = "shield_dust"
cotton_down = "cotton_down"
dauntless_shield = "dauntless_shield"
stamina = "stamina"
overgrow = "overgrow"
gorilla_tactics = "gorilla_tactics"
overcoat = "overcoat"
iron_barbs = "iron_barbs"
wimp_out = "wimp_out"
vital_spirit = "vital_spirit"
swarm = "swarm"
steelworker = "steelworker"
sand_spit = "sand_spit"
innards_out = "innards_out"
disguise = "disguise"
prankster = "prankster"
sturdy = "sturdy"
leaf_guard = "leaf_guard"
stakeout = "stakeout"
filter = "filter"
flower_veil = "flower_veil"
pure_power = "pure_power"
sand_force = "sand_force"
solar_power = "solar_power"
frisk = "frisk"
stall = "stall"
run_away = "run_away"
friend_guard = "friend_guard"
magic_guard = "magic_guard"
wonder_guard = "wonder_guard"
neutralizing_gas = "neutralizing_gas"
swift_swim = "swift_swim"
gluttony = "gluttony"
sweet_veil = "sweet_veil"
sticky_hold = "sticky_hold"
tough_claws = "tough_claws"
heavy_metal = "heavy_metal"
sap_sipper = "sap_sipper"
liquid_voice = "liquid_voice"
hydration = "hydration"
hyper_cutter = "hyper_cutter"
comatose = "comatose"
water_veil = "water_veil"
heatproof = "heatproof"
illusion = "illusion"
steadfast = "steadfast"
imposter = "imposter"
moxie = "moxie"
unaware = "unaware"
infiltrator = "infiltrator"
insomnia = "insomnia"
intimidate = "intimidate"
thick_fat = "thick_fat"
cute_charm = "cute_charm"
intrepid_sword = "intrepid_sword"
storm_drain = "storm_drain"
tinted_lens = "tinted_lens"
levitate = "levitate"
libero = "libero"
light_metal = "light_metal"
long_reach = "long_reach"
illuminate = "illuminate"
moody = "moody"
magician = "magician"
magnet_pull = "magnet_pull"
klutz = "klutz"
shadow_tag = "shadow_tag"
early_bird = "early_bird"
bad_dreams = "bad_dreams"
tangling_hair = "tangling_hair"
natural_cure = "natural_cure"
mega_launcher = "mega_launcher"
primordial_sea = "primordial_sea"
full_metal_body = "full_metal_body"
forecast = "forecast"
mimicry = "mimicry"
minus = "minus"
magic_bounce = "magic_bounce"
zen_mode = "zen_mode"
damp = "damp"
mummy = "mummy"
motor_drive = "motor_drive"
shed_skin = "shed_skin"
skill_link = "skill_link"
multiscale = "multiscale"
multitype = "multitype"
ripen = "ripen"
stalwart = "stalwart"
normalize = "normalize"
compound_eyes = "compound_eyes"
power_of_alchemy = "power_of_alchemy"
lightning_rod = "lightning_rod"
bulletproof = "bulletproof"
aerilate = "aerilate"
rough_skin = "rough_skin"
galvanize = "galvanize"
pixilate = "pixilate"
refrigerate = "refrigerate"
wonder_skin = "wonder_skin"
dry_skin = "dry_skin"
rattled = "rattled"
pickpocket = "pickpocket"
quick_feet = "quick_feet"
tangled_feet = "tangled_feet"
arena_trap = "arena_trap"
plus = "plus"
iron_fist = "iron_fist"
unseen_fist = "unseen_fist"
poison_point = "poison_point"
gooey = "gooey"
effect_spore = "effect_spore"
forewarn = "forewarn"
pressure = "pressure"
queenly_majesty = "queenly_majesty"
triage = "triage"
prism_armor = "prism_armor"
strong_jaw = "strong_jaw"
propeller_tail = "propeller_tail"
protean = "protean"
stench = "stench"
punk_rock = "punk_rock"
scrappy = "scrappy"
flare_boost = "flare_boost"
toxic_boost = "toxic_boost"
pickup = "pickup"
ball_fetch = "ball_fetch"
power_construct = "power_construct"
receiver = "receiver"
harvest = "harvest"
keen_eye = "keen_eye"
regenerator = "regenerator"
emergency_exit = "emergency_exit"
snow_cloak = "snow_cloak"
rivalry = "rivalry"
water_compaction = "water_compaction"
sand_stream = "sand_stream"
sheer_force = "sheer_force"
drought = "drought"
serene_grace = "serene_grace"
simple = "simple"
sniper = "sniper"
poison_heal = "poison_heal"
solid_rock = "solid_rock"
grim_neigh = "grim_neigh"
delta_stream = "delta_stream"
shadow_shield = "shadow_shield"
static = "static"
liquid_ooze = "liquid_ooze"
surge_surfer = "surge_surfer"
symbiosis = "symbiosis"
synchronize = "synchronize"
battle_bond = "battle_bond"
rks_system = "rks_system"
technician = "technician"
download = "download"
telepathy = "telepathy"
reckless = "reckless"
own_tempo = "own_tempo"
unnerve = "unnerve"
teravolt = "teravolt"
desolate_land = "desolate_land"
ice_face = "ice_face"
rock_head = "rock_head"
quick_draw = "quick_draw"
fur_coat = "fur_coat"
grass_pelt = "grass_pelt"
flash_fire = "flash_fire"
torrent = "torrent"
poison_touch = "poison_touch"
transistor = "transistor"
steam_engine = "steam_engine"
speed_boost = "speed_boost"
turboblaze = "turboblaze"
immunity = "immunity"
suction_cups = "suction_cups"
victory_star = "victory_star"
pastel_veil = "pastel_veil"
sand_veil = "sand_veil"

plates = {fist_plate: Fighting_type, dread_plate: Dark_type, flame_plate: Fire_type, draco_plate: Dragon_type,
          stone_plate: Rock_type, zap_plate: Electric_type, iron_plate: Steel_type, meadow_plate: Grass_type,
          splash_plate: Water_type, icicle_plate: Ice_type, toxic_plate: Poison_type, sky_plate: Flying_type,
          blank_plate: Normal_type, insect_plate: Bug_type, earth_plate: Ground_type, spooky_plate: Ghost_type,
          mind_plate: Psychic_type}

type_enhancing_item = {black_belt: Fighting_type, black_glasses: Dark_type, charcoal: Fire_type,
                       dragon_fang: Dragon_type, hard_stone: Rock_type, magnet: Electric_type, metal_coat: Steel_type,
                       miracle_seed: Grass_type, mystic_water: Water_type, never_melt_ice: Ice_type,
                       poison_barb: Poison_type, sharp_beak: Flying_type, silk_scarf: Normal_type,
                       silver_powder: Bug_type, soft_sand: Ground_type, spell_tag: Ghost_type,
                       twisted_spoon: Psychic_type}

type_enhancing_incences = {odd_incense: Psychic_type, rock_incense: Rock_type, rose_incense: Grass_type,
                           sea_incense: Water_type, wave_incense: Water_type}

gems = {bug_gem: Bug_type, dark_gem: Dark_type, dragon_gem: Dragon_type, electric_gem: Electric_type,
        fairy_gem: Fairy_type, fighting_gem: Fighting_type, fire_gem: Fire_type, flying_gem: Flying_type,
        ghost_gem: Ghost_type, grass_gem: Grass_type, ground_gem: Ground_type, ice_gem: Ice_type,
        normal_gem: Normal_type, poison_gem: Poison_type, psychic_gem: Psychic_type, rock_gem: Rock_type,
        steel_gem: Steel_type, water_gem: Water_type}

rbset = {occa_berry: Fire_type, passho_berry: Water_type, wacan_berry: Electric_type, rindo_berry: Grass_type,
         yache_berry: Ice_type, chople_berry: Fighting_type, kebia_berry: Poison_type, shuca_berry: Ground_type,
         coba_berry: Flying_type, iapapa_berry: Psychic_type, tanga_berry: Bug_type, charti_berry: Rock_type,
         kasib_berry: Ghost_type, haban_berry: Dragon_type, colbur_berry: Dark_type, babiri_berry: Steel_type}

punch_moves = ["Dynamic Punch", "Double Iron Bash", "Mach Punch", "Ice Hammer", "Hammer Arm", "Focus Punch",
               "Bullet Punch", "Power-Up Punch", "Comet Punch", "Fire Punch", "Meteor Mash", "Shadow Punch",
               "Thunder Punch", "Ice Punch", "Sky Uppercut", "Mega Punch", "Dizzy Punch", "Drain Punch"]
