# corrections_data.py
# Contains the manual mapping dictionary for animal name variations.

manual_corrections = {
    'kangeroo': 'Kangaroo',
    'ants': 'Ant',
    'bees': 'Bee',
    'dogs': 'Dog',
    'cats': 'Cat',
    'monkeys': 'Monkey',
    'walruses': 'Walrus',
    'whales': 'Whale',
    'sharks': 'Shark',
    'fishes': 'Fish', # map to singular 'Fish'
    'alligators': 'Alligator',
    'zebras': 'Zebra',
    'lions': 'Lion',
    'giraffes': 'Giraffe',
    'wolfs': 'Wolf', # specific misspelling of plural
    'wolves': 'Wolf',
    'orangutan': 'Orangutan',
    'rabbits': 'Rabbit',
    'hamsters': 'Hamster',
    'tigers': 'Tiger',
    'snakes': 'Snake',
    'birds': 'Bird',
    'leopards': 'Leopard',
    'bears': 'Bear',
    'pandas': 'Panda',
    'dinosaurs': 'Dinosaur',
    'golden retrievers': 'Golden Retriever', # Standardize capitalization
    'cockroaches': 'Cockroach',
    'worms': 'Worm',
    'centipedes': 'Centipede',
    'millipedes': 'Millipede',
    'beetles': 'Beetle',
    'butterflies': 'Butterfly',
    'moths': 'Moth',
    'kangaroos': 'Kangaroo',
    'hawks': 'Hawk',
    'robins': 'Robin',
    'koala': 'Koala',
    'polar bears': 'Polar Bear',
    'chimpanzees': 'Chimpanzee',
    'pigs': 'Pig',
    'cows': 'Cow',
    'eagles': 'Eagle',
    'seals': 'Seal',
    'parrots': 'Parrot',
    'rats': 'Rat',
    'racoon': 'Raccoon', # spelling
    'racoons': 'Raccoon', # spelling + plural
    'insects': 'Insect',
    'budgie': 'Budgerigar', # map to more formal name
    'otters': 'Otter',
    'wild boar': 'Wild Boar',
    'hornets': 'Hornet',
    'fireflies': 'Firefly',
    'snails': 'Snail',
    'camels': 'Camel',
    'humans': 'Human',
    'kangeroos': 'Kangaroo', # spelling
    'sea lion': 'Sea Lion',
    'sea lions': 'Sea Lion',
    'penguins': 'Penguin',
    'horses': 'Horse',
    'hippo': 'Hippopotamus', # map abbreviation
    'hippos': 'Hippopotamus',
    'lizards': 'Lizard',
    'flying squirrels': 'Flying Squirrel',
    'giant turtles': 'Giant Turtle',
    'crocodiles': 'Crocodile',
    'bats': 'Bat',
    'slugs': 'Slug',
    'clams': 'Clam',
    'koi': 'Koi Fish', # be more specific
    'prawn': 'Prawn',
    'prawns': 'Prawn',
    'lobster': 'Lobster',
    'lobsters': 'Lobster',
    'guppy fish': 'Guppy', # simplify
    'donkeys': 'Donkey',
    'wasps': 'Wasp',
    'termites': 'Termite',
    'beavers': 'Beaver',
    'pigeons': 'Pigeon',
    'goats': 'Goat',
    'pirana': 'Piranha', # spelling
    'dolphins': 'Dolphin',
    'elephants': 'Elephant',
    'beagles': 'Beagle',
    'anteaters': 'Anteater',
    'dugongs': 'Dugong',
    'guinea pigs': 'Guinea Pig',
    'ploar bear': 'Polar Bear', # spelling
    'blue whale': 'Blue Whale',
    'giant river otters': 'Giant River Otter',
    'small otter': 'Otter', # map to general otter unless specific needed
    'tasmanian devil': 'Tasmanian Devil',
    'snow leopard': 'Snow Leopard',
    'snow leopards': 'Snow Leopard',
    'narwhals': 'Narwhal',
    'belugas': 'Beluga Whale', # be more specific
    'beluga': 'Beluga Whale',
    'humpback whales': 'Humpback Whale',
    'sperm whale': 'Sperm Whale',
    'giant squid': 'Giant Squid',
    'blue-ringed octopus': 'Blue-Ringed Octopus',
    'box jellyfish': 'Box Jellyfish',
    'sea slug': 'Sea Slug',
    'flatworm': 'Flatworm',
    'sea cucumbers': 'Sea Cucumber',
    'crabs': 'Crab',
    'mussels': 'Mussel',
    'mice': 'Mouse',
    'geese': 'Goose',
    'moles': 'Mole',
    'hippotamus': 'Hippopotamus', # spelling
    'dophin': 'Dolphin', # spelling
    'crows': 'Crow',
    'blue jays': 'Blue Jay',
    'macaws': 'Macaw',
    'sunbear': 'Sun Bear', # spacing
    'hammerhead shark': 'Hammerhead Shark',
    'dragon fish': 'Dragonfish', # combine? Or keep separate? Let's keep separate: 'Dragon Fish'
    'red panda': 'Red Panda',
    'red pandas': 'Red Panda',
    'terrapins': 'Terrapin',
    'spiders': 'Spider',
    'mosquitoes': 'Mosquito',
    'fruit flies': 'Fruit Fly',
    'tortoises': 'Tortoise',
    'ducks': 'Duck',
    'scallops': 'Scallop',
    'rhinoceres': 'Rhinoceros', # spelling
    'gorillas': 'Gorilla',
    'baboons': 'Baboon',
    'komodo dragon': 'Komodo Dragon',
    'komodo dragons': 'Komodo Dragon',
    'deers': 'Deer', # irregular plural
    'white tiger': 'White Tiger',
    'liger': 'Liger',
    'ligers': 'Liger',
    'squirrels': 'Squirrel',
    'turtles': 'Turtle',
    'bluewhale': 'Blue Whale', # spacing
    'beluga whale': 'Beluga Whale',
    'apes': 'Ape',
    'gineau pigs': 'Guinea Pig', # spelling
    'orangutans': 'Orangutan',
    'chickens': 'Chicken',
    'caterpilla': 'Caterpillar', # spelling
    'rhinocerous': 'Rhinoceros', # spelling
    'human': 'Human',
    'chinchillas': 'Chinchilla',
    'sloths': 'Sloth',
    'flamingos': 'Flamingo',
    'roach': 'Cockroach', # map abbreviation
    'stick insect': 'Stick Insect',
    'cobra': 'Cobra',
    'cobras': 'Cobra',
    'chicks': 'Chick', # map plural
    'cheetahs': 'Cheetah',
    'porpupines': 'Porcupine', # spelling
    'porcupines': 'Porcupine',
    'quokkas': 'Quokka',
    'guppy': 'Guppy',
    'trinoceros': 'Rhinoceros', # spelling
    't-rex': 'T-Rex', # Capitalization
    'hippotomas': 'Hippopotamus', # spelling
    'sparrows': 'Sparrow',
    'angler fish': 'Anglerfish', # Combine
    'mynah birds': 'Mynah', # simplify
    'clown fish': 'Clownfish', # Combine
    'boars': 'Boar',
    'panthers': 'Panther',
    'hippoptamus': 'Hippopotamus', # spelling
    'sheeps': 'Sheep', # irregular plural
    'wildboar': 'Wild Boar', # spacing
    'goost': 'Goose', # spelling
    'koi fish': 'Koi Fish',
    'stonefish': 'Stonefish',
    'frogfish': 'Frogfish',
    'prairie dog': 'Prairie Dog',
    'hump back whale': 'Humpback Whale', # spacing
    'whale shark': 'Whale Shark',
    'seagulls': 'Seagull',
    'croc': 'Crocodile', # abbreviation
    'anteter': 'Anteater', # spelling
    'crcodile': 'Crocodile', # spelling
    'crcocodiles': 'Crocodile', # spelling + plural
    'rabits': 'Rabbit', # spelling
    'guniea pigs': 'Guinea Pig', # spelling
    'oysters': 'Oyster',
    'bulls': 'Bull',
    'meerkats': 'Meerkat',
    'honey badgers': 'Honey Badger',
    'codfish': 'Cod', # simplify
    'sea cucumber': 'Sea Cucumber',
    'seasnail': 'Sea Snail', # spacing
    'eels': 'Eel',
    'swans': 'Swan',
    'hummingbirds': 'Hummingbird',
    'myna': 'Mynah', # standard spelling
    'mynas': 'Mynah',
    'cuckoobirds': 'Cuckoo', # simplify
    'frogs': 'Frog',
    'rhinos': 'Rhinoceros', # map abbreviation + plural
    'rhino': 'Rhinoceros', # map abbreviation
    'wild dog': 'Wild Dog', # or African Wild Dog? Keep simple for now.
    'gorrilla': 'Gorilla', # spelling
    'chipannzee': 'Chimpanzee', # spelling
    'chinpanzee': 'Chimpanzee', # spelling
    'rhinosaurus': 'Rhinoceros', # spelling
    'aligator': 'Alligator', # spelling
    'tortise': 'Tortoise', # spelling
    'drop bear': 'Drop Bear', # Assuming this is intentional :)
    'hares': 'Hare',
    'lady bugs': 'Ladybug', # combine
    'hippopotamu': 'Hippopotamus', # spelling
    'polar': 'Polar Bear', # Assuming context implies Polar Bear
    'hyenna': 'Hyena', # spelling
    'giraff': 'Giraffe', # spelling
    'bull whale': 'Whale', # Simplify - could be ambiguous, map to general Whale
    'naked mole rat': 'Naked Mole Rat',
    'chincilla': 'Chinchilla', # spelling
    'kaola': 'Koala', # spelling
    'sea anemone': 'Sea Anemone',
    'white pomfret': 'White Pomfret',
    'sardines': 'Sardine',
    'jaguars': 'Jaguar',
    'sealion': 'Sea Lion', # spacing
    'rrocodile': 'Crocodile', # spelling
    'flies': 'Fly',
    'vulcan': 'Vulcan', # Fictional? Keep as is unless context differs.
    'stringray': 'Stingray', # spelling
    'stingrays': 'Stingray',
    'komono dragon': 'Komodo Dragon', # spelling
    'lama': 'Llama', # spelling
    'mountain goat': 'Mountain Goat',
    'minks': 'Mink',
    'doves': 'Dove',
    'golden retreiver': 'Golden Retriever', # spelling
    'vultures': 'Vulture',
    'tarantulas': 'Tarantula',
    'kiwis': 'Kiwi',
    'koalas': 'Koala',
    'toads': 'Toad',
    'seahorses': 'Seahorse',
    'crocs': 'Crocodile', # abbreviation
    'wombats': 'Wombat',
    'coyotes': 'Coyote',
    'armadillos': 'Armadillo',
    'hedgehogs': 'Hedgehog',
    'orang utan': 'Orangutan', # spacing
    'snowleopard': 'Snow Leopard', # spacing
    'anteears': 'Anteater', # spelling
    'jackals': 'Jackal',
    'arctic fox': 'Arctic Fox',
    'mole rat': 'Mole Rat',
    'playtpus': 'Platypus', # spelling
    'golden retriever': 'Golden Retriever',
    'japanese spitz': 'Japanese Spitz',
    'persian cat': 'Persian Cat',
    'ginger tabby cat': 'Ginger Tabby Cat',
    'cocker spaniel': 'Cocker Spaniel',
    'hound dog': 'Hound', # simplify? Or keep 'Hound Dog'? Keep for now.
    'chow chow': 'Chow Chow',
    'monitor lizards': 'Monitor Lizard',
    'pengins': 'Penguin', # spelling
    'wilderbeast': 'Wildebeest', # spelling
    'bettle': 'Beetle', # spelling
    'chincillas': 'Chinchilla', # spelling + plural
    'hens': 'Hen',
    'zebra fish': 'Zebrafish', # combine
    'mosquitos': 'Mosquito', # spelling
    'houseflies': 'Housefly',
    'cheetas': 'Cheetah', # spelling
    'gorrillas': 'Gorilla', # spelling + plural
    'piranha': 'Piranha',
    'milipede': 'Millipede', # spelling
    'mynah': 'Mynah',
    'golden retriver': 'Golden Retriever', # spelling
    'sardine': 'Sardine',
    'ostritch': 'Ostrich', # spelling
    'flammingo': 'Flamingo', # spelling
    'baracuda': 'Barracuda', # spelling
    'sea anemane': 'Sea Anemone', # spelling
    'hermit crab': 'Hermit Crab',
    'horseshoe crab': 'Horseshoe Crab',
    'parrot fish': 'Parrot Fish',
    'needle fish': 'Needlefish', # combine
    'crocodile fish': 'Crocodilefish', # combine
    'sea star': 'Starfish', # Common name preference
    'ponies': 'Pony',
    'meercat': 'Meerkat', # spelling
    'russion blue cat': 'Russian Blue Cat', # spelling + capitalization
    'catepillars': 'Caterpillar', # spelling + plural
    'cannary': 'Canary', # spelling
    'aarddvark': 'Aardvark', # spelling
    'tarantula': 'Tarantula',
    'sabertooth tiger': 'Saber-Toothed Tiger', # Hyphenation & Capitalization
    'sabertooth': 'Saber-Toothed Tiger', # Map incomplete name
    'mammals': 'Mammal', # Generic category, map to singular
    'angelfish': 'Angelfish',
    'boxfish': 'Boxfish',
    'reptile': 'Reptile', # Generic category
    'great white shark': 'Great White Shark',
    'killer whale': 'Orca', # Common name preference
    'clownfish': 'Clownfish',
    'pufferfish': 'Pufferfish',
    'guinea pig': 'Guinea Pig',
    'honey badger': 'Honey Badger',
    'grizzly bear': 'Grizzly Bear',
    'ladybird': 'Ladybug', # Synonym preference
    'sun bear': 'Sun Bear',
    'moon bear': 'Moon Bear',
    'catfish': 'Catfish',
    'blue jay': 'Blue Jay',
    'tiger shark': 'Tiger Shark',
}