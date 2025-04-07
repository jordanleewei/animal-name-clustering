# tagging_rules.py
# Contains sets defining rule-based tags for different animal categories.

# Basic Types
MAMMALS = {'Aardvark', 'Akbash', 'Alpaca', 'Antelope', 'Ape', 'Armadillo', 'Baboon', 'Badger', 'Bat', 'Bear', 'Beaver', 'Beagle', 'Boar',
           'Bobcat', 'Buffalo', 'Bull', 'Camel', 'Capybara', 'Calf', 'Cat', 'Chihuahua', 'Chimpanzee', 'Chinchilla', 'Chipmunk', 'Civet',
           'Cow', 'Coyote', 'Deer', 'Dingo', 'Dog', 'Dobermann', 'Donkey', 'Dugong', 'Echidna', 'Elephant', 'Elk', 'Ermine', 'Ferret', 'Fox',
           'Gazelle', 'Gerbil', 'Gibbon', 'Giraffe', 'Goat', 'Golden Retriever', 'Gorilla', 'Greyhound', 'Grizzly Bear', 'Guinea Pig', 'Hamster',
           'Hare', 'Hedgehog', 'Hippopotamus', 'Horse', 'Hound', 'Human', 'Hyena', 'Jackal', 'Jaguar', 'Japanese Spitz', 'Kangaroo', 'Koala',
           'Lamb', 'Lemur', 'Leopard', 'Liger', 'Lion', 'Llama', 'Manatee', 'Mandrill', 'Mara', 'Marmot', 'Meerkat', 'Mink', 'Mole', 'Mole Rat',
           'Mongoose', 'Monkey', 'Moose', 'Mouse', 'Mule', 'Muskox', 'Naked Mole Rat', 'Narwhal', 'Okapi', 'Opossum', 'Orangutan', 'Orca',
           'Otter', 'Ox', 'Panda', 'Pangolin', 'Panther', 'Persian Cat', 'Pig', 'Pika', 'Pitbull', 'Platypus', 'Polar Bear', 'Pony', 'Porcupine',
           'Porpoise', 'Possum', 'Prairie Dog', 'Puma', 'Quokka', 'Rabbit', 'Raccoon', 'Rat', 'Red Panda', 'Reindeer', 'Rhinoceros',
           'Russian Blue Cat', 'Seal', 'Sea Lion', 'Sheep', 'Shrew', 'Skunk', 'Sloth', 'Sperm Whale', 'Squirrel', 'Stoat', 'Sun Bear', 'Tapir',
           'Tasmanian Devil', 'Tiger', 'Vole', 'Wallaby', 'Walrus', 'Warthog', 'Weasel', 'Whale', 'Wild Boar', 'Wildcat', 'Wildebeest', 'Wolf',
           'Wolverine', 'Wombat', 'Yak', 'Zebra', 'Zebu', 'Corgi', 'Ginger Tabby Cat', 'Cocker Spaniel', 'Chow Chow', 'Giant River Otter',
           'Blue Whale', 'Humpback Whale', 'Beluga Whale', 'Black Bear', 'Brown Bear', 'Moon Bear', 'Arctic Fox', 'Flying Squirrel'}
BIRDS = {'Albatross', 'Bird', 'Blue Jay', 'Budgerigar', 'Canary', 'Cassowary', 'Chick', 'Chicken', 'Cockatoo', 'Condor', 'Cormorant', 'Crane',
         'Crow', 'Cuckoo', 'Dove', 'Duck', 'Eagle', 'Egret', 'Emu', 'Falcon', 'Finch', 'Flamingo', 'Goose', 'Grouse', 'Hawk', 'Hen', 'Heron',
         'Hornbill', 'Hummingbird', 'Ibis', 'Jabiru', 'Kestrel', 'Kingfisher', 'Kite', 'Kiwi', 'Macaw', 'Magpie', 'Mockingbird', 'Mynah',
         'Ostrich', 'Owl', 'Parakeet', 'Parrot', 'Peacock', 'Pelican', 'Penguin', 'Pheasant', 'Pigeon', 'Puffin', 'Quail', 'Raven', 'Robin',
         'Rooster', 'Seagull', 'Sparrow', 'Starling', 'Stork', 'Swallow', 'Swan', 'Toucan', 'Turkey', 'Vulture', 'Woodpecker'}
REPTILES = {'Alligator', 'Anaconda', 'Chameleon', 'Cobra', 'Crocodile', 'Gecko', 'Iguana', 'Lizard', 'Monitor Lizard', 'Python', 'Skink',
            'Snake', 'Terrapin', 'Tortoise', 'Turtle', 'Viper', 'Komodo Dragon', 'Giant Turtle'}
AMPHIBIANS = {'Axolotl', 'Frog', 'Newt', 'Salamander', 'Toad'}
FISH = {'Angelfish', 'Anglerfish', 'Arowana', 'Barracuda', 'Bass', 'Boxfish', 'Carp', 'Catfish', 'Clownfish', 'Cod', 'Dory', 'Eel', 'Fish',
        'Flounder', 'Goldfish', 'Grouper', 'Guppy', 'Haddock', 'Halibut', 'Herring', 'Koi Fish', 'Lionfish', 'Mackerel', 'Marlin', 'Needlefish',
        'Parrot Fish', 'Perch', 'Pike', 'Piranha', 'Pomfret', 'Pufferfish', 'Rockfish', 'Salmon', 'Sardine', 'Seahorse', 'Shark', 'Snapper',
        'Sole', 'Stonefish', 'Sunfish', 'Swordfish', 'Tilapia', 'Trout', 'Tuna', 'White Pomfret', 'Zebrafish', 'Dragonfish', 'Crocodilefish',
        'Frogfish', 'Hammerhead Shark', 'Great White Shark', 'Tiger Shark', 'Whale Shark'} # Whale shark is fish
INSECTS = {'Ant', 'Bee', 'Beetle', 'Butterfly', 'Caterpillar', 'Centipede', 'Cicada', 'Cockroach', 'Cricket', 'Dragonfly', 'Earwig', 'Firefly',
           'Flea', 'Fly', 'Fruit Fly', 'Grasshopper', 'Hornet', 'Housefly', 'Insect', 'Ladybug', 'Louse', 'Maggot', 'Mantis', 'Mealworm',
           'Millipede', 'Mosquito', 'Moth', 'Roach', 'Stick Insect', 'Termite', 'Wasp', 'Stag Beetle'} # Note: Centipede/Millipede aren't technically insects but often grouped
ARACHNIDS = {'Scorpion', 'Spider', 'Tarantula'}
MOLLUSCS = {'Abalone', 'Clam', 'Cuttlefish', 'Mussel', 'Octopus', 'Oyster', 'Scallop', 'Slug', 'Snail', 'Squid', 'Sea Slug', 'Giant Squid', 'Blue-Ringed Octopus', 'Sea Snail'}
CRUSTACEANS = {'Barnacle', 'Crab', 'Crayfish', 'Hermit Crab', 'Horseshoe Crab', 'Krill', 'Lobster', 'Prawn', 'Shrimp'}
OTHER_INVERTEBRATES = {'Earthworm', 'Flatworm', 'Jellyfish', 'Leech', 'Plankton', 'Sea Anemone', 'Sea Cucumber', 'Sea Urchin', 'Starfish', 'Worm', 'Box Jellyfish'} # Catch-all

# Characteristics / Groupings
HOUSE_PETS = {'Cat', 'Dog', 'Hamster', 'Gerbil', 'Guinea Pig', 'Rabbit', 'Ferret', 'Goldfish', 'Canary', 'Budgerigar', 'Parakeet', 'Cockatoo',
              'Parrot', 'Chinchilla', 'Mouse', 'Rat', 'Beagle', 'Chihuahua', 'Corgi', 'Golden Retriever', 'Japanese Spitz', 'Persian Cat',
              'Pitbull', 'Russian Blue Cat', 'Guppy', 'Koi Fish', 'Angelfish', 'Zebrafish', 'Hedgehog', 'Terrapin', 'Turtle', # Some turtles/terrapins are pets
              'Bearded Dragon'} # Example reptile pet
BARN_ANIMALS = {'Cow', 'Chicken', 'Goat', 'Horse', 'Pig', 'Sheep', 'Donkey', 'Duck', 'Goose', 'Llama', 'Alpaca', 'Ox', 'Turkey', 'Mule', 'Rooster', 'Hen'}
FURRY = MAMMALS - {'Whale', 'Dolphin', 'Porpoise', 'Manatee', 'Dugong', 'Hippopotamus', 'Rhinoceros', 'Naked Mole Rat', 'Walrus', 'Elephant'} # Approximation
FEATHERED = BIRDS
SCALY = REPTILES | FISH | {'Pangolin'} # Pangolins are mammals but have scales
CANINES = {'Dog', 'Wolf', 'Fox', 'Coyote', 'Dingo', 'Jackal', 'Akbash', 'Beagle', 'Chihuahua', 'Corgi', 'Dobermann', 'Golden Retriever', 'Greyhound',
           'Hound', 'Japanese Spitz', 'Pitbull', 'Wild Dog', 'Arctic Fox', 'Cocker Spaniel', 'Chow Chow'}
FELINES = {'Cat', 'Cheetah', 'Jaguar', 'Leopard', 'Lion', 'Liger', 'Lynx', 'Ocelot', 'Panther', 'Puma', 'Tiger', 'Wildcat', 'Bobcat', 'Cougar',
           'Persian Cat', 'Russian Blue Cat', 'Snow Leopard', 'Ginger Tabby Cat', 'White Tiger', 'Saber-Toothed Tiger'}
BIG_CATS = {'Cheetah', 'Jaguar', 'Leopard', 'Lion', 'Liger', 'Puma', 'Snow Leopard', 'Tiger', 'White Tiger', 'Saber-Toothed Tiger'} # Common usage, not strictly biological size
PRIMATES = {'Ape', 'Baboon', 'Chimpanzee', 'Gibbon', 'Gorilla', 'Human', 'Lemur', 'Monkey', 'Orangutan', 'Mandrill'}
BEAR_FAMILY = {'Bear', 'Black Bear', 'Brown Bear', 'Grizzly Bear', 'Panda', 'Polar Bear', 'Sloth Bear', 'Sun Bear', 'Moon Bear', 'Koala'} # Koala often associated, though marsupial
MARINE = {'Whale', 'Dolphin', 'Seal', 'Walrus', 'Shark', 'Octopus', 'Squid', 'Jellyfish', 'Crab', 'Lobster', 'Fish', 'Sea Lion', 'Manatee',
          'Sea Urchin', 'Starfish', 'Sea Cucumber', 'Sea Anemone', 'Coral', 'Krill', 'Prawn', 'Oyster', 'Mussel', 'Clam', 'Scallop', 'Eel',
          'Orca', 'Narwhal', 'Porpoise', 'Dugong', 'Sea Otter', 'Sea Turtle', 'Stingray', 'Seahorse', 'Giant Squid', 'Blue-Ringed Octopus',
          'Box Jellyfish', 'Sea Slug', 'Flatworm', 'Sperm Whale', 'Humpback Whale', 'Blue Whale', 'Beluga Whale', 'Hammerhead Shark', 'Great White Shark',
          'Tiger Shark', 'Whale Shark', 'Anglerfish', 'Clownfish', 'Cod', 'Grouper', 'Lionfish', 'Marlin', 'Pufferfish', 'Salmon', 'Sardine',
          'Swordfish', 'Tuna', 'Barracuda', 'Flounder', 'Needlefish', 'Parrot Fish', 'Crocodilefish', 'Stonefish', 'Frogfish', 'Sunfish',
          'Sea Snail', 'Cuttlefish', 'Abalone', 'Barnacle', 'Hermit Crab', 'Horseshoe Crab', 'Rockfish', 'White Pomfret'} # Add specific fish
FRESHWATER = {'Beaver', 'Otter', 'Piranha', 'Axolotl', 'Carp', 'Catfish', 'Goldfish', 'Guppy', 'Koi Fish', 'Pike', 'Trout', 'Tilapia', 'Perch',
              'Salamander', 'Newt', 'Frog', 'Crayfish', 'Zebrafish', 'Arowana', 'Angelfish', 'Giant River Otter'} # Some overlap (e.g., Salmon)
AQUATIC = MARINE | FRESHWATER | {'Penguin', 'Hippopotamus', 'Crocodile', 'Alligator', 'Platypus', 'Turtle', 'Terrapin', 'Swan', 'Duck', 'Goose', 'Flamingo'}
FLYING = BIRDS | {'Bat', 'Butterfly', 'Dragonfly', 'Fly', 'Mosquito', 'Moth', 'Bee', 'Wasp', 'Hornet', 'Ladybug', 'Beetle', 'Firefly', 'Fruit Fly', 'Housefly', 'Flying Squirrel', 'Pterodactyl'} # Approximation for insects
ZODIAC_CHINESE = {'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig'} # Note: 'Sheep' often used for 'Goat'
MYTHICAL_FICTIONAL = {'Dragon', 'Unicorn', 'Drop Bear', 'Vulcan', 'T-Rex', 'Dinosaur', 'Saber-Toothed Tiger', 'Liger', 'Dory'} # Liger is real but hybrid, Dory is specific character

# Subjective/Approximate
CUTE = {'Koala', 'Quokka', 'Panda', 'Red Panda', 'Rabbit', 'Kitten', 'Puppy', 'Chipmunk', 'Otter', 'Penguin', 'Hedgehog', 'Chinchilla', 'Sea Otter', 'Fennec Fox', 'Bunny', 'Lamb', 'Chick'} # Highly subjective!
FURRY = FURRY | CUTE # If something is often called cute, it's often furry if a mammal