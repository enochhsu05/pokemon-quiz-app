import requests
import sys
import random
# from matplotlib import pyplot as plt
# from matplotlib import image as mpimg

BASE_URL = "https://pokeapi.co/api/v2"
types = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']
mons = ['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto', 'pidgeot', 'rattata', 'raticate', 'spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash', 'nidoran-f', 'nidorina', 'nidoqueen', 'nidoran-m', 'nidorino', 'nidoking', 'clefairy', 'clefable', 'vulpix', 'ninetales', 'jigglypuff', 'wigglytuff', 'zubat', 'golbat', 'oddish', 'gloom', 'vileplume', 'paras', 'parasect', 'venonat', 'venomoth', 'diglett', 'dugtrio', 'meowth', 'persian', 'psyduck', 'golduck', 'mankey', 'primeape', 'growlithe', 'arcanine', 'poliwag', 'poliwhirl', 'poliwrath', 'abra', 'kadabra', 'alakazam', 'machop', 'machoke', 'machamp', 'bellsprout', 'weepinbell', 'victreebel', 'tentacool', 'tentacruel', 'geodude', 'graveler', 'golem', 'ponyta', 'rapidash', 'slowpoke', 'slowbro', 'magnemite', 'magneton', 'farfetchd', 'doduo', 'dodrio', 'seel', 'dewgong', 'grimer', 'muk', 'shellder', 'cloyster', 'gastly', 'haunter', 'gengar', 'onix', 'drowzee', 'hypno', 'krabby', 'kingler', 'voltorb', 'electrode', 'exeggcute', 'exeggutor', 'cubone', 'marowak', 'hitmonlee', 'hitmonchan', 'lickitung', 'koffing', 'weezing', 'rhyhorn', 'rhydon', 'chansey', 'tangela', 'kangaskhan', 'horsea', 'seadra', 'goldeen', 'seaking', 'staryu', 'starmie', 'mr-mime', 'scyther', 'jynx', 'electabuzz', 'magmar', 'pinsir', 'tauros', 'magikarp', 'gyarados', 'lapras', 'ditto', 'eevee', 'vaporeon', 'jolteon', 'flareon', 'porygon', 'omanyte', 'omastar', 'kabuto', 'kabutops', 'aerodactyl', 'snorlax', 'articuno', 'zapdos', 'moltres', 'dratini', 'dragonair', 'dragonite', 'mewtwo', 'mew', 'chikorita', 'bayleef', 'meganium', 'cyndaquil', 'quilava', 'typhlosion', 'totodile', 'croconaw', 'feraligatr', 'sentret', 'furret', 'hoothoot', 'noctowl', 'ledyba', 'ledian', 'spinarak', 'ariados', 'crobat', 'chinchou', 'lanturn', 'pichu', 'cleffa', 'igglybuff', 'togepi', 'togetic', 'natu', 'xatu', 'mareep', 'flaaffy', 'ampharos', 'bellossom', 'marill', 'azumarill', 'sudowoodo', 'politoed', 'hoppip', 'skiploom', 'jumpluff', 'aipom', 'sunkern', 'sunflora', 'yanma', 'wooper', 'quagsire', 'espeon', 'umbreon', 'murkrow', 'slowking', 'misdreavus', 'unown', 'wobbuffet', 'girafarig', 'pineco', 'forretress', 'dunsparce', 'gligar', 'steelix', 'snubbull', 'granbull', 'qwilfish', 'scizor', 'shuckle', 'heracross', 'sneasel', 'teddiursa', 'ursaring', 'slugma', 'magcargo', 'swinub', 'piloswine', 'corsola', 'remoraid', 'octillery', 'delibird', 'mantine', 'skarmory', 'houndour', 'houndoom', 'kingdra', 'phanpy', 'donphan', 'porygon2', 'stantler', 'smeargle', 'tyrogue', 'hitmontop', 'smoochum', 'elekid', 'magby', 'miltank', 'blissey', 'raikou', 'entei', 'suicune', 'larvitar', 'pupitar', 'tyranitar', 'lugia', 'ho-oh', 'celebi', 'treecko', 'grovyle', 'sceptile', 'torchic', 'combusken', 'blaziken', 'mudkip', 'marshtomp', 'swampert', 'poochyena', 'mightyena', 'zigzagoon', 'linoone', 'wurmple', 'silcoon', 'beautifly', 'cascoon', 'dustox', 'lotad', 'lombre', 'ludicolo', 'seedot', 'nuzleaf', 'shiftry', 'taillow', 'swellow', 'wingull', 'pelipper', 'ralts', 'kirlia', 'gardevoir', 'surskit', 'masquerain', 'shroomish', 'breloom', 'slakoth', 'vigoroth', 'slaking', 'nincada', 'ninjask', 'shedinja', 'whismur', 'loudred', 'exploud', 'makuhita', 'hariyama', 'azurill', 'nosepass', 'skitty', 'delcatty', 'sableye', 'mawile', 'aron', 'lairon', 'aggron', 'meditite', 'medicham', 'electrike', 'manectric', 'plusle', 'minun', 'volbeat', 'illumise', 'roselia', 'gulpin', 'swalot', 'carvanha', 'sharpedo', 'wailmer', 'wailord', 'numel', 'camerupt', 'torkoal', 'spoink', 'grumpig', 'spinda', 'trapinch', 'vibrava', 'flygon', 'cacnea', 'cacturne', 'swablu', 'altaria', 'zangoose', 'seviper', 'lunatone', 'solrock', 'barboach', 'whiscash', 'corphish', 'crawdaunt', 'baltoy', 'claydol', 'lileep', 'cradily', 'anorith', 'armaldo', 'feebas', 'milotic', 'castform', 'kecleon', 'shuppet', 'banette', 'duskull', 'dusclops', 'tropius', 'chimecho', 'absol', 'wynaut', 'snorunt', 'glalie', 'spheal', 'sealeo', 'walrein', 'clamperl', 'huntail', 'gorebyss', 'relicanth', 'luvdisc', 'bagon', 'shelgon', 'salamence', 'beldum', 'metang', 'metagross', 'regirock', 'regice', 'registeel', 'latias', 'latios', 'kyogre', 'groudon', 'rayquaza', 'jirachi', 'deoxys-normal', 'turtwig', 'grotle', 'torterra', 'chimchar', 'monferno', 'infernape', 'piplup', 'prinplup', 'empoleon', 'starly', 'staravia', 'staraptor', 'bidoof', 'bibarel', 'kricketot', 'kricketune', 'shinx', 'luxio', 'luxray', 'budew', 'roserade', 'cranidos', 'rampardos', 'shieldon', 'bastiodon', 'burmy', 'wormadam-plant', 'mothim', 'combee', 'vespiquen', 'pachirisu', 'buizel', 'floatzel', 'cherubi', 'cherrim', 'shellos', 'gastrodon', 'ambipom', 'drifloon', 'drifblim', 'buneary', 'lopunny', 'mismagius', 'honchkrow', 'glameow', 'purugly', 'chingling', 'stunky', 'skuntank', 'bronzor', 'bronzong', 'bonsly', 'mime-jr', 'happiny', 'chatot', 'spiritomb', 'gible', 'gabite', 'garchomp', 'munchlax', 'riolu', 'lucario', 'hippopotas', 'hippowdon', 'skorupi', 'drapion', 'croagunk', 'toxicroak', 'carnivine', 'finneon', 'lumineon', 'mantyke', 'snover', 'abomasnow', 'weavile', 'magnezone', 'lickilicky', 'rhyperior', 'tangrowth', 'electivire', 'magmortar', 'togekiss', 'yanmega', 'leafeon', 'glaceon', 'gliscor', 'mamoswine', 'porygon-z', 'gallade', 'probopass', 'dusknoir', 'froslass', 'rotom', 'uxie', 'mesprit', 'azelf', 'dialga', 'palkia', 'heatran', 'regigigas', 'giratina-altered', 'cresselia', 'phione', 'manaphy', 'darkrai', 'shaymin-land', 'arceus', 'victini', 'snivy', 'servine', 'serperior', 'tepig', 'pignite', 'emboar', 'oshawott', 'dewott', 'samurott', 'patrat', 'watchog', 'lillipup', 'herdier', 'stoutland', 'purrloin', 'liepard', 'pansage', 'simisage', 'pansear', 'simisear', 'panpour', 'simipour', 'munna', 'musharna', 'pidove', 'tranquill', 'unfezant', 'blitzle', 'zebstrika', 'roggenrola', 'boldore', 'gigalith', 'woobat', 'swoobat', 'drilbur', 'excadrill', 'audino', 'timburr', 'gurdurr', 'conkeldurr', 'tympole', 'palpitoad', 'seismitoad', 'throh', 'sawk', 'sewaddle', 'swadloon', 'leavanny', 'venipede', 'whirlipede', 'scolipede', 'cottonee', 'whimsicott', 'petilil', 'lilligant', 'basculin-red-striped', 'sandile', 'krokorok', 'krookodile', 'darumaka', 'darmanitan-standard', 'maractus', 'dwebble', 'crustle', 'scraggy', 'scrafty', 'sigilyph', 'yamask', 'cofagrigus', 'tirtouga', 'carracosta', 'archen', 'archeops', 'trubbish', 'garbodor', 'zorua', 'zoroark', 'minccino', 'cinccino', 'gothita', 'gothorita', 'gothitelle', 'solosis', 'duosion', 'reuniclus', 'ducklett', 'swanna', 'vanillite', 'vanillish', 'vanilluxe', 'deerling', 'sawsbuck', 'emolga', 'karrablast', 'escavalier', 'foongus', 'amoonguss', 'frillish', 'jellicent', 'alomomola', 'joltik', 'galvantula', 'ferroseed', 'ferrothorn', 'klink', 'klang', 'klinklang', 'tynamo', 'eelektrik', 'eelektross', 'elgyem', 'beheeyem', 'litwick', 'lampent', 'chandelure', 'axew', 'fraxure', 'haxorus', 'cubchoo', 'beartic', 'cryogonal', 'shelmet', 'accelgor', 'stunfisk', 'mienfoo', 'mienshao', 'druddigon', 'golett', 'golurk', 'pawniard', 'bisharp', 'bouffalant', 'rufflet', 'braviary', 'vullaby', 'mandibuzz', 'heatmor', 'durant', 'deino', 'zweilous', 'hydreigon', 'larvesta', 'volcarona', 'cobalion', 'terrakion', 'virizion', 'tornadus-incarnate', 'thundurus-incarnate', 'reshiram', 'zekrom', 'landorus-incarnate', 'kyurem', 'keldeo-ordinary', 'meloetta-aria', 'genesect', 'chespin', 'quilladin', 'chesnaught', 'fennekin', 'braixen', 'delphox', 'froakie', 'frogadier', 'greninja', 'bunnelby', 'diggersby', 'fletchling', 'fletchinder', 'talonflame', 'scatterbug', 'spewpa', 'vivillon', 'litleo', 'pyroar', 'flabebe', 'floette', 'florges', 'skiddo', 'gogoat', 'pancham', 'pangoro', 'furfrou', 'espurr', 'meowstic-male', 'honedge', 'doublade', 'aegislash-shield', 'spritzee', 'aromatisse', 'swirlix', 'slurpuff', 'inkay', 'malamar', 'binacle', 'barbaracle', 'skrelp', 'dragalge', 'clauncher', 'clawitzer', 'helioptile', 'heliolisk', 'tyrunt', 'tyrantrum', 'amaura', 'aurorus', 'sylveon', 'hawlucha', 'dedenne', 'carbink', 'goomy', 'sliggoo', 'goodra', 'klefki', 'phantump', 'trevenant', 'pumpkaboo-average', 'gourgeist-average', 'bergmite', 'avalugg', 'noibat', 'noivern', 'xerneas', 'yveltal', 'zygarde-50', 'diancie', 'hoopa', 'volcanion', 'rowlet', 'dartrix', 'decidueye', 'litten', 'torracat', 'incineroar', 'popplio', 'brionne', 'primarina', 'pikipek', 'trumbeak', 'toucannon', 'yungoos', 'gumshoos', 'grubbin', 'charjabug', 'vikavolt', 'crabrawler', 'crabominable', 'oricorio-baile', 'cutiefly', 'ribombee', 'rockruff', 'lycanroc-midday', 'wishiwashi-solo', 'mareanie', 'toxapex', 'mudbray', 'mudsdale', 'dewpider', 'araquanid', 'fomantis', 'lurantis', 'morelull', 'shiinotic', 'salandit', 'salazzle', 'stufful', 'bewear', 'bounsweet', 'steenee', 'tsareena', 'comfey', 'oranguru', 'passimian', 'wimpod', 'golisopod', 'sandygast', 'palossand', 'pyukumuku', 'type-null', 'silvally', 'minior-red-meteor', 'komala', 'turtonator', 'togedemaru', 'mimikyu-disguised', 'bruxish', 'drampa', 'dhelmise', 'jangmo-o', 'hakamo-o', 'kommo-o', 'tapu-koko', 'tapu-lele', 'tapu-bulu', 'tapu-fini', 'cosmog', 'cosmoem', 'solgaleo', 'lunala', 'nihilego', 'buzzwole', 'pheromosa', 'xurkitree', 'celesteela', 'kartana', 'guzzlord', 'necrozma', 'magearna', 'marshadow', 'poipole', 'naganadel', 'stakataka', 'blacephalon', 'zeraora', 'meltan', 'melmetal', 'grookey', 'thwackey', 'rillaboom', 'scorbunny', 'raboot', 'cinderace', 'sobble', 'drizzile', 'inteleon', 'skwovet', 'greedent', 'rookidee', 'corvisquire', 'corviknight', 'blipbug', 'dottler', 'orbeetle', 'nickit', 'thievul', 'gossifleur', 'eldegoss', 'wooloo', 'dubwool', 'chewtle', 'drednaw', 'yamper', 'boltund', 'rolycoly', 'carkol', 'coalossal', 'applin', 'flapple', 'appletun', 'silicobra', 'sandaconda', 'cramorant', 'arrokuda', 'barraskewda', 'toxel', 'toxtricity-amped', 'sizzlipede', 'centiskorch', 'clobbopus', 'grapploct', 'sinistea', 'polteageist', 'hatenna', 'hattrem', 'hatterene', 'impidimp', 'morgrem', 'grimmsnarl', 'obstagoon', 'perrserker', 'cursola', 'sirfetchd', 'mr-rime', 'runerigus', 'milcery', 'alcremie', 'falinks', 'pincurchin', 'snom', 'frosmoth', 'stonjourner', 'eiscue-ice', 'indeedee-male', 'morpeko-full-belly', 'cufant', 'copperajah', 'dracozolt', 'arctozolt', 'dracovish', 'arctovish', 'duraludon', 'dreepy', 'drakloak', 'dragapult', 'zacian', 'zamazenta', 'eternatus', 'kubfu', 'urshifu-single-strike', 'zarude', 'regieleki', 'regidrago', 'glastrier', 'spectrier', 'calyrex', 'wyrdeer', 'kleavor', 'ursaluna', 'basculegion-male', 'sneasler', 'overqwil', 'enamorus-incarnate', 'sprigatito', 'floragato', 'meowscarada', 'fuecoco', 'crocalor', 'skeledirge', 'quaxly', 'quaxwell', 'quaquaval', 'lechonk', 'oinkologne', 'tarountula', 'spidops', 'nymble', 'lokix', 'pawmi', 'pawmo', 'pawmot', 'tandemaus', 'maushold', 'fidough', 'dachsbun', 'smoliv', 'dolliv', 'arboliva', 'squawkabilly', 'nacli', 'naclstack', 'garganacl', 'charcadet', 'armarouge', 'ceruledge', 'tadbulb', 'bellibolt', 'wattrel', 'kilowattrel', 'maschiff', 'mabosstiff', 'shroodle', 'grafaiai', 'bramblin', 'brambleghast', 'toedscool', 'toedscruel', 'klawf', 'capsakid', 'scovillain', 'rellor', 'rabsca', 'flittle', 'espathra', 'tinkatink', 'tinkatuff', 'tinkaton', 'wiglett', 'wugtrio', 'bombirdier', 'finizen', 'palafin', 'varoom', 'revavroom', 'cyclizar', 'orthworm', 'glimmet', 'glimmora', 'greavard', 'houndstone', 'flamigo', 'cetoddle', 'cetitan', 'veluza', 'dondozo', 'tatsugiri', 'annihilape', 'clodsire', 'farigiraf', 'dudunsparce', 'kingambit', 'great-tusk', 'scream-tail', 'brute-bonnet', 'flutter-mane', 'slither-wing', 'sandy-shocks', 'iron-treads', 'iron-bundle', 'iron-hands', 'iron-jugulis', 'iron-moth', 'iron-thorns', 'frigibax', 'arctibax', 'baxcalibur', 'gimmighoul', 'gholdengo', 'wo-chien', 'chien-pao', 'ting-lu', 'chi-yu', 'roaring-moon', 'iron-valiant', 'koraidon', 'miraidon', 'walking-wake', 'iron-leaves', 'dipplin', 'poltchageist', 'sinistcha', 'okidogi', 'munkidori', 'fezandipiti', 'ogerpon', 'archaludon', 'hydrapple', 'gouging-fire', 'raging-bolt', 'iron-boulder', 'iron-crown', 'terapagos', 'pecharunt']
type_combinations = {('normal', None): 'rattata', ('normal', 'fighting'): 'stufful', ('normal', 'flying'): 'pidgey', ('normal', 'poison'): 'shroodle', ('normal', 'ground'): 'diggersby', ('normal', 'rock'): None, ('normal', 'bug'): None, ('normal', 'ghost'): 'zorua-hisui', ('normal', 'steel'): None, ('normal', 'fire'): 'litleo', ('normal', 'water'): 'bibarel', ('normal', 'grass'): 'deerling', ('normal', 'electric'): 'helioptile', ('normal', 'psychic'): 'girafarig', ('normal', 'ice'): None, ('normal', 'dragon'): 'drampa', ('normal', 'dark'): 'obstagoon', ('normal', 'fairy'): 'jigglypuff', ('fighting', 'normal'): 'stufful', ('fighting', None): 'mankey', ('fighting', 'flying'): 'hawlucha', ('fighting', 'poison'): 'croagunk', ('fighting', 'ground'): 'great-tusk', ('fighting', 'rock'): 'terrakion', ('fighting', 'bug'): 'heracross', ('fighting', 'ghost'): 'marshadow', ('fighting', 'steel'): 'lucario', ('fighting', 'fire'): 'combusken', ('fighting', 'water'): 'poliwrath', ('fighting', 'grass'): 'breloom', ('fighting', 'electric'): 'pawmo', ('fighting', 'psychic'): 'meditite', ('fighting', 'ice'): 'crabominable', ('fighting', 'dragon'): 'hakamo-o', ('fighting', 'dark'): 'scraggy', ('fighting', 'fairy'): 'iron-valiant', ('flying', 'normal'): 'pidgey', ('flying', 'fighting'): 'hawlucha', ('flying', None): 'tornadus-incarnate', ('flying', 'poison'): 'zubat', ('flying', 'ground'): 'gligar', ('flying', 'rock'): 'aerodactyl', ('flying', 'bug'): 'butterfree', ('flying', 'ghost'): 'drifloon', ('flying', 'steel'): 'skarmory', ('flying', 'fire'): 'charizard', ('flying', 'water'): 'gyarados', ('flying', 'grass'): 'hoppip', ('flying', 'electric'): 'zapdos', ('flying', 'psychic'): 'natu', ('flying', 'ice'): 'articuno', ('flying', 'dragon'): 'dragonite', ('flying', 'dark'): 'murkrow', ('flying', 'fairy'): 'togetic', ('poison', 'normal'): 'shroodle', ('poison', 'fighting'): 'croagunk', ('poison', 'flying'): 'zubat', ('poison', None): 'ekans', ('poison', 'ground'): 'nidoqueen', ('poison', 'rock'): 'nihilego', ('poison', 'bug'): 'weedle', ('poison', 'ghost'): 'gastly', ('poison', 'steel'): 'varoom', ('poison', 'fire'): 'salandit', ('poison', 'water'): 'tentacool', ('poison', 'grass'): 'bulbasaur', ('poison', 'electric'): 'toxel', ('poison', 'psychic'): 'munkidori', ('poison', 'ice'): None, ('poison', 'dragon'): 'dragalge', ('poison', 'dark'): 'stunky', ('poison', 'fairy'): 'fezandipiti', ('ground', 'normal'): 'diggersby', ('ground', 'fighting'): 'great-tusk', ('ground', 'flying'): 'gligar', ('ground', 'poison'): 'nidoqueen', ('ground', None): 'sandshrew', ('ground', 'rock'): 'geodude', ('ground', 'bug'): 'nincada', ('ground', 'ghost'): 'golett', ('ground', 'steel'): 'steelix', ('ground', 'fire'): 'numel', ('ground', 'water'): 'wooper', ('ground', 'grass'): 'torterra', ('ground', 'electric'): 'stunfisk', ('ground', 'psychic'): 'baltoy', ('ground', 'ice'): 'swinub', ('ground', 'dragon'): 'vibrava', ('ground', 'dark'): 'sandile', ('ground', 'fairy'): None, ('rock', 'normal'): None, ('rock', 'fighting'): 'terrakion', ('rock', 'flying'): 'aerodactyl', ('rock', 'poison'): 'nihilego', ('rock', 'ground'): 'geodude', ('rock', None): 'sudowoodo', ('rock', 'bug'): 'shuckle', ('rock', 'ghost'): None, ('rock', 'steel'): 'aron', ('rock', 'fire'): 'magcargo', ('rock', 'water'): 'omanyte', ('rock', 'grass'): 'lileep', ('rock', 'electric'): 'iron-thorns', ('rock', 'psychic'): 'lunatone', ('rock', 'ice'): 'amaura', ('rock', 'dragon'): 'tyrunt', ('rock', 'dark'): 'tyranitar', ('rock', 'fairy'): 'carbink', ('bug', 'normal'): None, ('bug', 'fighting'): 'heracross', ('bug', 'flying'): 'butterfree', ('bug', 'poison'): 'weedle', ('bug', 'ground'): 'nincada', ('bug', 'rock'): 'shuckle', ('bug', None): 'caterpie', ('bug', 'ghost'): 'shedinja', ('bug', 'steel'): 'forretress', ('bug', 'fire'): 'larvesta', ('bug', 'water'): 'surskit', ('bug', 'grass'): 'paras', ('bug', 'electric'): 'joltik', ('bug', 'psychic'): 'dottler', ('bug', 'ice'): 'snom', ('bug', 'dragon'): None, ('bug', 'dark'): 'lokix', ('bug', 'fairy'): 'cutiefly', ('ghost', 'normal'): 'zorua-hisui', ('ghost', 'fighting'): 'marshadow', ('ghost', 'flying'): 'drifloon', ('ghost', 'poison'): 'gastly', ('ghost', 'ground'): 'golett', ('ghost', 'rock'): None, ('ghost', 'bug'): 'shedinja', ('ghost', None): 'misdreavus', ('ghost', 'steel'): 'honedge', ('ghost', 'fire'): 'litwick', ('ghost', 'water'): 'frillish', ('ghost', 'grass'): 'phantump', ('ghost', 'electric'): 'rotom', ('ghost', 'psychic'): 'hoopa', ('ghost', 'ice'): 'froslass', ('ghost', 'dragon'): 'giratina-altered', ('ghost', 'dark'): 'sableye', ('ghost', 'fairy'): 'mimikyu-disguised', ('steel', 'normal'): None, ('steel', 'fighting'): 'lucario', ('steel', 'flying'): 'skarmory', ('steel', 'poison'): 'varoom', ('steel', 'ground'): 'steelix', ('steel', 'rock'): 'aron', ('steel', 'bug'): 'forretress', ('steel', 'ghost'): 'honedge', ('steel', None): 'registeel', ('steel', 'fire'): 'heatran', ('steel', 'water'): 'empoleon', ('steel', 'grass'): 'ferroseed', ('steel', 'electric'): 'magnemite', ('steel', 'psychic'): 'beldum', ('steel', 'ice'): 'sandshrew-alola', ('steel', 'dragon'): 'dialga', ('steel', 'dark'): 'pawniard', ('steel', 'fairy'): 'mawile', ('fire', 'normal'): 'litleo', ('fire', 'fighting'): 'combusken', ('fire', 'flying'): 'charizard', ('fire', 'poison'): 'salandit', ('fire', 'ground'): 'numel', ('fire', 'rock'): 'magcargo', ('fire', 'bug'): 'larvesta', ('fire', 'ghost'): 'litwick', ('fire', 'steel'): 'heatran', ('fire', None): 'charmander', ('fire', 'water'): 'volcanion', ('fire', 'grass'): 'scovillain', ('fire', 'electric'): 'rotom-heat', ('fire', 'psychic'): 'victini', ('fire', 'ice'): 'darmanitan-galar-zen', ('fire', 'dragon'): 'reshiram', ('fire', 'dark'): 'houndour', ('fire', 'fairy'): None, ('water', 'normal'): 'bibarel', ('water', 'fighting'): 'poliwrath', ('water', 'flying'): 'gyarados', ('water', 'poison'): 'tentacool', ('water', 'ground'): 'wooper', ('water', 'rock'): 'omanyte', ('water', 'bug'): 'surskit', ('water', 'ghost'): 'frillish', ('water', 'steel'): 'empoleon', ('water', 'fire'): 'volcanion', ('water', None): 'squirtle', ('water', 'grass'): 'lotad', ('water', 'electric'): 'chinchou', ('water', 'psychic'): 'slowpoke', ('water', 'ice'): 'dewgong', ('water', 'dragon'): 'kingdra', ('water', 'dark'): 'carvanha', ('water', 'fairy'): 'marill', ('grass', 'normal'): 'deerling', ('grass', 'fighting'): 'breloom', ('grass', 'flying'): 'hoppip', ('grass', 'poison'): 'bulbasaur', ('grass', 'ground'): 'torterra', ('grass', 'rock'): 'lileep', ('grass', 'bug'): 'paras', ('grass', 'ghost'): 'phantump', ('grass', 'steel'): 'ferroseed', ('grass', 'fire'): 'scovillain', ('grass', 'water'): 'lotad', ('grass', None): 'tangela', ('grass', 'electric'): 'rotom-mow', ('grass', 'psychic'): 'exeggcute', ('grass', 'ice'): 'snover', ('grass', 'dragon'): 'applin', ('grass', 'dark'): 'nuzleaf', ('grass', 'fairy'): 'cottonee', ('electric', 'normal'): 'helioptile', ('electric', 'fighting'): 'pawmo', ('electric', 'flying'): 'zapdos', ('electric', 'poison'): 'toxel', ('electric', 'ground'): 'stunfisk', ('electric', 'rock'): 'iron-thorns', ('electric', 'bug'): 'joltik', ('electric', 'ghost'): 'rotom', ('electric', 'steel'): 'magnemite', ('electric', 'fire'): 'rotom-heat', ('electric', 'water'): 'chinchou', ('electric', 'grass'): 'rotom-mow', ('electric', None): 'pikachu', ('electric', 'psychic'): 'raichu-alola', ('electric', 'ice'): 'arctozolt', ('electric', 'dragon'): 'zekrom', ('electric', 'dark'): 'morpeko-full-belly', ('electric', 'fairy'): 'dedenne', ('psychic', 'normal'): 'girafarig', ('psychic', 'fighting'): 'meditite', ('psychic', 'flying'): 'natu', ('psychic', 'poison'): 'munkidori', ('psychic', 'ground'): 'baltoy', ('psychic', 'rock'): 'lunatone', ('psychic', 'bug'): 'dottler', ('psychic', 'ghost'): 'hoopa', ('psychic', 'steel'): 'beldum', ('psychic', 'fire'): 'victini', ('psychic', 'water'): 'slowpoke', ('psychic', 'grass'): 'exeggcute', ('psychic', 'electric'): 'raichu-alola', ('psychic', None): 'abra', ('psychic', 'ice'): 'jynx', ('psychic', 'dragon'): 'latias', ('psychic', 'dark'): 'inkay', ('psychic', 'fairy'): 'mr-mime', ('ice', 'normal'): None, ('ice', 'fighting'): 'crabominable', ('ice', 'flying'): 'articuno', ('ice', 'poison'): None, ('ice', 'ground'): 'swinub', ('ice', 'rock'): 'amaura', ('ice', 'bug'): 'snom', ('ice', 'ghost'): 'froslass', ('ice', 'steel'): 'sandshrew-alola', ('ice', 'fire'): 'darmanitan-galar-zen', ('ice', 'water'): 'dewgong', ('ice', 'grass'): 'snover', ('ice', 'electric'): 'arctozolt', ('ice', 'psychic'): 'jynx', ('ice', None): 'snorunt', ('ice', 'dragon'): 'kyurem', ('ice', 'dark'): 'sneasel', ('ice', 'fairy'): 'ninetales-alola', ('dragon', 'normal'): 'drampa', ('dragon', 'fighting'): 'hakamo-o', ('dragon', 'flying'): 'dragonite', ('dragon', 'poison'): 'dragalge', ('dragon', 'ground'): 'vibrava', ('dragon', 'rock'): 'tyrunt', ('dragon', 'bug'): None, ('dragon', 'ghost'): 'giratina-altered', ('dragon', 'steel'): 'dialga', ('dragon', 'fire'): 'reshiram', ('dragon', 'water'): 'kingdra', ('dragon', 'grass'): 'applin', ('dragon', 'electric'): 'zekrom', ('dragon', 'psychic'): 'latias', ('dragon', 'ice'): 'kyurem', ('dragon', None): 'dratini', ('dragon', 'dark'): 'deino', ('dragon', 'fairy'): 'altaria-mega', ('dark', 'normal'): 'obstagoon', ('dark', 'fighting'): 'scraggy', ('dark', 'flying'): 'murkrow', ('dark', 'poison'): 'stunky', ('dark', 'ground'): 'sandile', ('dark', 'rock'): 'tyranitar', ('dark', 'bug'): 'lokix', ('dark', 'ghost'): 'sableye', ('dark', 'steel'): 'pawniard', ('dark', 'fire'): 'houndour', ('dark', 'water'): 'carvanha', ('dark', 'grass'): 'nuzleaf', ('dark', 'electric'): 'morpeko-full-belly', ('dark', 'psychic'): 'inkay', ('dark', 'ice'): 'sneasel', ('dark', 'dragon'): 'deino', ('dark', None): 'umbreon', ('dark', 'fairy'): 'impidimp', ('fairy', 'normal'): 'jigglypuff', ('fairy', 'fighting'): 'iron-valiant', ('fairy', 'flying'): 'togetic', ('fairy', 'poison'): 'fezandipiti', ('fairy', 'ground'): None, ('fairy', 'rock'): 'carbink', ('fairy', 'bug'): 'cutiefly', ('fairy', 'ghost'): 'mimikyu-disguised', ('fairy', 'steel'): 'mawile', ('fairy', 'fire'): None, ('fairy', 'water'): 'marill', ('fairy', 'grass'): 'cottonee', ('fairy', 'electric'): 'dedenne', ('fairy', 'psychic'): 'mr-mime', ('fairy', 'ice'): 'ninetales-alola', ('fairy', 'dragon'): 'altaria-mega', ('fairy', 'dark'): 'impidimp', ('fairy', None): 'clefairy'}


def api_call(category, id_or_name):
    url = BASE_URL + "/" + category + "/" + id_or_name
    response = requests.get(url)
    json_response = response.json()
    return json_response


def to_json(object):
    url = object["url"]
    response = requests.get(url)
    json = response.json()
    return json


def get_pokemon_by_name(pokemon_name: str):
    # Make API call to PokeAPI to get information about the Pokemon
    url = f"{BASE_URL}/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception:
        raise Exception("Pokemon not found")


def get_pokemon_by_number(pokedex_number: int):
    url = f"{BASE_URL}/pokemon/{pokedex_number}"
    response = requests.get(url)
    return response.json()


def get_ability(ability_name: str):
    url = f"{BASE_URL}/ability/{ability_name.lower()}"
    response = requests.get(url)
    return response.json()


def has_move_by_number(pokedex_number: int, move_name: str):
    url = f"{BASE_URL}/pokemon/{pokedex_number}"
    response = requests.get(url)
    moves = response.json()["moves"]
    for i in range(len(moves)):
        if moves[i]["move"]["name"] == move_name:
            return True
    return False


def print_has_all_moves(moves: list[str]):
    for n in range(649):
        i = n + 1
        if all(has_move_by_number(i, move) for move in moves):
            print(get_pokemon_name_by_number(i))


def print_ability_with_moves(ability_name: str, moves: list[str]):
    for n in range(649):
        i = n + 1
        for ability in get_pokemon_by_number(i)["abilities"]:
            if ability['ability']['name'] == ability_name:
                for move_name in moves:
                    print(f"{get_pokemon_name_by_number(i)}: {move_name} - {has_move_by_number(i, move_name)}")


def get_pokemon_name_by_number(pokedex_number: int):
    url = f"{BASE_URL}/pokemon/{pokedex_number}"
    response = requests.get(url)
    return response.json()["name"]


def pokemon_to_name(pokemon: list):
    names = []
    for mon in pokemon:
        names.append(mon["name"])
    return names


def get_bst_from_pokemon(pokemon):
    bst = 0
    for stat in pokemon['stats']:
        bst += stat['base_stat']
    return bst


def get_bst_from_species(species):
    bst = get_bst_from_pokemon(get_pokemon_from_species(species))
    return bst


def get_names_from_pokemon(pokemon):
    names = []
    for mon in pokemon:
        names.append(mon['name'])
    return names


def get_pokemon_from_species(species):
    return get_pokemon_by_number(species["pokedex_numbers"][0]["entry_number"])


def get_basic_evo(species):
    while species['evolves_from_species'] is not None:
        species = to_json(species['evolves_from_species'])
    return species


def get_species_line_from_species(species):
    species = get_basic_evo(species)
    species_line = []
    species_line.append(species)
    mon = to_json(species["evolution_chain"])["chain"]
    while len(mon["evolves_to"]) > 0:
        mon = mon["evolves_to"][0]
        species_line.append(to_json(mon["species"]))
    return species_line


def get_random_team(generation: int, fully_evolved: bool = False, amount: int = 6,
                    repeats: bool = False, include_legendaries: bool = False, include_mythicals: bool = False,
                    min_bst: int = 0, max_bst: int = 1000):
    url = f"{BASE_URL}/generation/{generation}"
    response = requests.get(url).json()
    species = response["pokemon_species"]
    mons = []
    checked_numbers = [-1]
    while len(mons) < amount:
        rand = random.randint(0, len(species) - 1)
        if not repeats:
            while rand in checked_numbers:
                rand = random.randint(0, len(species) - 1)
            if fully_evolved:
                line = get_species_line_from_species(to_json(species[rand]))
                for mon in line:
                    checked_numbers.append(mon["pokedex_numbers"][0]["entry_number"])
            else:
                checked_numbers.append(rand)
        mon = to_json(species[rand])
        if fully_evolved:
            mon = to_json(mon["evolution_chain"])["chain"]
            while len(mon["evolves_to"]) > 0:
                mon = mon["evolves_to"][0]
            mon = to_json(mon["species"])
        if (include_legendaries or not mon["is_legendary"]) and \
                (include_mythicals or not mon["is_mythical"] and
                 ((min_bst == 0 and max_bst == 1000) or
                  (min_bst <= get_bst_from_species(mon) <= max_bst))):
            mon = get_pokemon_from_species(mon)
            mons.append(mon)
    return mons


def get_pokemon_with_ability(ability_name: str):
    ability = api_call('ability', ability_name)
    pokemon = [to_json(mon['pokemon']) for mon in ability['pokemon']]
    return pokemon


def display_stats(mon, stats: list[int] = (1, 2, 3, 4, 5, 6)):
    for stat in enumerate(mon['stats']):
        if stat[0] in [num - 1 for num in stats]:
            print(f"{mon['name']} - {api_call('stat', f'{stat[0]+1}')['name']}: {stat[1]['base_stat']}")
    print(f"bst: {get_bst_from_pokemon(mon)}")


def get_front_sprite(mon: str):
    return api_call('pokemon', mon.lower())['sprites']['front_default']


def display_image(image_url: str):
    from PIL import Image, ImageTk
    import tkinter as tk
    import requests

    url = image_url

    root = tk.Tk()

    image = Image.open(requests.get(url, stream=True).raw)
    width, height = image.size
    scale = 5
    image = image.resize((scale * width, scale * height))
    image_tk = ImageTk.PhotoImage(image)

    label = tk.Label(image=image_tk, height=500, width=500)
    label.image = image
    label.pack()

    root.mainloop()


def calculate_max_damage(attacking_mon, defending_mon, move, attacker_level=50, defender_level=50):
    if type(move) == str:
        move = api_call('move', move)
    if type(attacking_mon) is str:
        attacking_mon = get_pokemon_by_name(attacking_mon)
    if type(defending_mon) is str:
        defending_mon = get_pokemon_by_name(defending_mon)
    damage_class = to_json(move['damage_class'])['name']
    if damage_class == 'status':
        return 0
    if damage_class == 'physical':
        attacking_stat = int(0.01 * (2 * (attacking_mon['stats'][1]['base_stat'] + 31 + 0.25*252)) * attacker_level + 5) * 1.1
        defending_stat = int(0.01 * (2 * (defending_mon['stats'][2]['base_stat'] + 31 + 0.25*252)) * defender_level + 5) * 1.1
    else:
        attacking_stat = int(0.01 * (2 * (attacking_mon['stats'][3]['base_stat'] + 31 + 0.25*252)) * attacker_level + 5) * 1.1
        defending_stat = int(0.01 * (2 * (defending_mon['stats'][4]['base_stat'] + 31 + 0.25*252)) * defender_level + 5) * 1.1
    hp = int(0.01 * (2 * defending_mon['stats'][0]['base_stat'] + 31 + int(0.25 * 252)) * defender_level) + defender_level + 10
    effectiveness = type_effectiveness(to_json(move['type']), [to_json(typing['type']) for typing in defending_mon['types']])
    stab = 1.5 if to_json(move['type']) in [to_json(typing['type']) for typing in attacking_mon['types']] else 1
    return ((2 * attacker_level / 5 + 2) * move['power'] * attacking_stat / defending_stat / 50 + 2) * stab * effectiveness / hp * 100


def type_effectiveness(attacking_type, defending_types):
    multiplier = 1
    for type in defending_types:
        relation = type['damage_relations']
        if attacking_type in [to_json(rel) for rel in relation['no_damage_from']]:
            return 0
        elif attacking_type in [to_json(rel) for rel in relation['half_damage_from']]:
            multiplier *= 0.5
        elif attacking_type in [to_json(rel) for rel in relation['double_damage_from']]:
            multiplier *= 2
    return multiplier


def generate_random_typing() -> tuple[str, str or None]:
    types = [type['name'] for type in api_call('type', '')['results']]
    primary_type_value = random.randint(0, 17)
    secondary_type_value = random.randint(0, 17)
    secondary_type = types[secondary_type_value] if secondary_type_value != primary_type_value else None
    primary_type = types[primary_type_value]
    return primary_type, secondary_type


def guess_pokemon_by_type(order=False):
    primary_type, secondary_type = generate_random_typing()
    if secondary_type is not None:
        input_pokemon = input(f'Name a {primary_type}/{secondary_type} type pokemon: ')
        if order:
            return get_type_from_pokemon_name(input_pokemon) == [primary_type, secondary_type]
        return all(type in [primary_type, secondary_type] for type in get_type_from_pokemon_name(input_pokemon))
    else:
        input_pokemon = input(f'Name a {primary_type} type pokemon: ')
        return get_type_from_pokemon_name(input_pokemon) == [primary_type]


def get_type_from_pokemon_name(mon: str):
    mon = get_pokemon_by_name(mon)
    types = [to_json(type['type'])['name'] for type in mon['types']]
    return types


def typing_exists(primary_typing: str, secondary_typing: str, order=False):
    # always true?
    # takes a long time
    if order:
        mons = [to_json(mon['pokemon']) for mon in api_call('type', primary_typing)['pokemon'] if mon['slot'] == 1]
        if secondary_typing in [type['name'] for type in [mon['types'] for mon in mons]]:
            return True
    else:
        mons = [to_json(mon['pokemon']) for mon in api_call('type', primary_typing)['pokemon']]
        if any([[secondary_typing in [to_json(type['type'])['name'] for type in types] for types in [mon['types'] for mon in mons]]]):
            return True
    return False


def how_many_hko(attacking_mon: str, defending_mon: str, move: str, attacker_level=50, defender_level=50):
    return int(100 / calculate_max_damage(attacking_mon, defending_mon, move, attacker_level, defender_level)) + 1


def generate_random_pokemon():
    return get_pokemon_by_number(random.randint(1, 1025))


def generate_random_pokemon_name():
    return mons[random.randint(0, len(mons) - 1)]


def pokemon_generation_quiz():
    mon = generate_random_pokemon()
    return {'name': mon['name'], 'gen': to_json(to_json(mon['species'])['generation'])['id']}


def object_to_name(object):
    return object['name']


def get_pokemon_sprite(pokemon_name):
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(api_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        sprite_url = pokemon_data['sprites']['front_default']
        return sprite_url
    else:
        print(f"Failed to fetch data for {pokemon_name}. Status code: {response.status_code}")
        return None


def get_pokemon_from_typing(typing: tuple[str, str or None]):
    if typing[1] is None:
        for mon in api_call('type', typing[0])['pokemon']:
            mon = to_json(mon['pokemon'])
            if len(mon['types']) == 1:
                return mon['name']
    else:
        for mon in api_call('type', typing[0])['pokemon']:
            mon = to_json(mon['pokemon'])
            types = [to_json(type['type'])['name'] for type in mon['types']]
            if typing[1] in types:
                return mon['name']
    return None


def get_level_up_moveset(mon):  # approxiamately
    moves = []
    for move in mon['moves']:
        if to_json(move['version_group_details'][0]['move_learn_method'])['name'] == 'level-up':
            moves.append(to_json(move['move']))
    return list_to_name(moves)


def list_to_name(arr):
    return [i['name'] for i in arr]


def generate_moveset_question():
    mon = generate_random_pokemon()
    evo = list_to_name(get_species_line_from_species(api_call('pokemon-species', mon['name'])))
    moves = get_level_up_moveset(mon)
    return {'mon': mon['name'], 'line': evo, 'moveset': moves}


def generate_matchup_question():
    offensive_type = api_call('type', str(random.randint(1, 18)))
    rand = random.randint(1, 18)
    damage_relations = offensive_type['damage_relations']
    types_left = types.copy()

    no_damage_to = damage_relations['no_damage_to']
    if rand > len(no_damage_to):
        rand -= len(no_damage_to)
        for typing in no_damage_to:
            types_left.remove(typing['name'])
    else:
        defensive_type = to_json(no_damage_to[rand-1])
        matchup = '0x'
        return {'offensive_type': offensive_type['name'],
                'defensive_type': defensive_type['name'],
                'matchup': matchup}

    half_damage_to = damage_relations['half_damage_to']
    if rand > len(half_damage_to):
        rand -= len(half_damage_to)
        for typing in half_damage_to:
            types_left.remove(typing['name'])
    else:
        defensive_type = to_json(half_damage_to[rand-1])
        matchup = '0.5x'
        return {'offensive_type': offensive_type['name'],
                'defensive_type': defensive_type['name'],
                'matchup': matchup}

    double_damage_to = damage_relations['double_damage_to']
    if rand > len(double_damage_to):
        rand -= len(double_damage_to)
        for typing in double_damage_to:
            types_left.remove(typing['name'])
    else:
        defensive_type = to_json(double_damage_to[rand - 1])
        matchup = '2x'
        return {'offensive_type': offensive_type['name'],
                'defensive_type': defensive_type['name'],
                'matchup': matchup}

    defensive_type = types_left[random.randint(0, len(types_left) - 1)]
    return {'offensive_type': offensive_type['name'],
            'defensive_type': defensive_type,
            'matchup': '1x'}


def generate_damage_question():
    mon_1 = generate_random_pokemon()
    mon_2 = generate_random_pokemon()
    moves = mon_1['moves']
    original_rand = random.randint(0, len(moves) - 1)
    rand = original_rand
    move = to_json(moves[rand]['move'])
    while move['power'] is None and len(moves) > 1:
        if rand == len(moves) - 1:
            rand = 0
        else:
            rand += 1
            if rand == original_rand:
                break
        move = to_json(moves[rand]['move'])
    damage = calculate_max_damage(mon_1, mon_2, move)
    if damage == 0:
        damage = 1
    hits = int(100 / damage) + 1
    if hits >= 5:
        hits = '5+'
    return {'attacking_mon': mon_1['name'], 'defending_mon': mon_2['name'], 'move': move['name'],
            'hits': hits}


# print(pokemon_to_name(get_random_team(5, amount=5, min_bst=450, max_bst=500, fully_evolved=True)))
# for mon in get_pokemon_with_ability('prankster'):
#     display_stats(mon, stats=[6])
# print_ability_with_moves("wonder-guard", ["tackle"])
# print_has_all_moves(['endeavor', 'flail'])
# display_image(get_front_sprite('absol'))
# print(calculate_max_damage('nidorina', 'onix', 'quick-attack'))
# print(guess_pokemon_by_type())
# print(typing_exists('dark', 'fire'))
# print(how_many_hko('charizard', 'leavanny', 'flamethrower'))
