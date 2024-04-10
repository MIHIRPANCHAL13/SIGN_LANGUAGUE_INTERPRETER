import string

def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator)

def find_keywords(text):
    if text is None:
        print("No input text provided.")
        return

    # Remove punctuation
    text = remove_punctuation(text)

    # Split the text into words
    words = text.split()

    # List of words to exclude
    words_to_exclude = ['am', 'is', 'are','was','were']

    # Remove specific words from the list
    filtered_words = [word for word in words if word.lower() not in words_to_exclude]

    # List of keywords to check against
    mp4_dataset = ["april", "area", "argue", "around", "arrest", "art", "at", "auditorium", "august", "august-2", "autorickshaw", "avoid", "axe", "bail", "bake", "ball", "ballon", "banaras", "banglore", "bank", "barber", "basketball", "bat", "bath", "bath-2", "batmintion", "bear", "beat", "beautiful", "before", "behind", "bell", "bell-2", "below", "bench", "bend", "between", "beverages", "bhangada", "bhopal", "bible", "birthday", "bitter", "blind", "blow", "board", "boil", "bolt", "book", "boring", "boxing", "bread", "bread-2", "breakfast", "brick", "bridge", "bright", "brittle", "buddah", "bug", "building", "bullock-cart", "bus", "bus-stand", "butter", "butterfly", "cake", "calcutta", "can", "car", "card", "careful", "careless", "carpenter", "carry", "catch", "celebrate", "cement", "centimeter", "chalk", "chandigarh", "chapathi", "chase", "cheap", "chennai", "chennai-2", "cheque", "cheque-2", "chess", "chicken", "chief", "chocolate", "christian", "christian-2", "cinema", "circus", "city", "clap", "clean", "clinic", "clown", "cobbler", "cochin", "cockroach", "coffee", "coimbatore", "coin", "cold", "cold-drink", "comfortable", "common", "communicate", "compare", "complain", "control", "cook", "cook-2", "coolie", "coolie-2", "corn", "count", "court", "crack", "cricket", "crime", "crocodile", "cunning", "cunning-2", "curd", "curd-2", "curry", "curved", "cycle", "dam", "dance", "dangerous", "dark", "date", "date-2", "day", "deaf", "december", "deer", "delhi", "demand-draft", "designing", "desk", "devil", "dhobi", "different", "difficult", "dim", "dinner", "dirty", "dirty-2", "dish", "distance", "doll", "dollar", "dosa", "doubt", "down", "drama", "drum", "dry", "durga", "during", "duster", "east", "easy", "electrician", "elephant", "embroidery", "embroidery-2", "empty", "energetic", "entertainment", "equal", "eraser", "expensive", "expensive-2", "factory", "famous", "famous-2", "far", "far-2", "farmer", "fast", "fat", "february", "few", "fight", "file", "fill", "fine", "fisherman", "fishing-net", "flat", "flexible", "flute", "follow", "food", "fool", "foolish", "foot", "football", "footpath", "fox", "frank", "fresh", "friday", "friday-2", "friday-3", "friday-4", "from", "full", "full-2", "funny", "funny-2", "games", "ghee", "ghost", "giraffe", "goal", "good", "grain", "gram", "groundnut", "guitar", "guwahati", "hammer", "handicapped", "hanuman", "hanuman-2", "harbour", "hard", "hard-2", "harmonium", "hearing", "heavy", "here", "high", "hindu", "hippo", "hole", "holiday", "holiday", "hollow", "holy", "horn", "horse-cart", "hospital", "hot(to-feel)", "hot(to-feel)-2", "hot(to-taste)", "hot(to-touch)", "hotel", "house-fly", "how", "how-big", "how-many", "how-much", "hungry", "hut", "hyderabad", "icecream", "idli", "illiterate", "in", "inch", "in-front", "insect", "it", "its", "itself", "jail", "jailor", "jain", "jaipur", "jam", "january", "jealous", "jeep", "jesus", "jew", "judge", "judge-2", "juice", "july", "june", "justice", "kangaroo", "kanpur", "karate", "kilogram", "kilometer", "kite", "krishna", "ladder", "laddu", "lame", "lassi", "lawyer", "lead", "left", "less", "light", "lion", "liquid", "liquor", "litre", "little", "lizard", "long", "loose", "lorry", "lorry-2", "lorry-3", "lose", "loud", "low", "lucknow", "lucky", "lunch", "machine", "magic", "magic-2", "magic-3", "many", "march", "market", "mary", "masala", "mason", "may", "measure", "measure-2", "meat", "mechanic", "meter", "mile", "milk", "milkman", "milliliter", "mime", "monday", "monday-2", "monday-3", "monday-4", "monday-5", "monday-6", "money", "monkey", "month", "month-2", "more", "mosque", "mosquito", "mosquito", "motor", "movie", "mumbai", "museum", "muslim", "mute", "mysore", "nagpur", "nail", "narrow", "near", "necessary", "needle", "nervous", "new", "newborn", "next", "non-vegetarian", "north", "note", "notebook", "november", "nut", "oath", "oath-2", "october", "of", "office", "oil", "old(time)", "old", "olympics", "on", "only", "ooty", "opaque", "opposite", "our", "ourselves", "out", "over", "page", "paint", "paise", "paper", "pappad", "parsi", "patna", "paw", "pen", "pen-2", "pencil", "pencil-2", "pepper", "perfect", "permanent", "pickle", "picture", "picture-2", "pipe", "plan", "plug", "plumber", "police-station", "poor", "poor-2", "possible", "post-office", "pour", "pray", "present", "priest", "priest-2", "pull", "pune", "punishment", "puppet-show", "pure", "puri", "push", "questions", "quicks", "quran", "rabbit", "race", "railway-station", "ram", "rat", "real", "responsible", "restaurant", "rhinoceros", "rice", "rice-2", "rich", "right", "ripe", "road", "roar", "rotten", "rough", "rule", "ruler", "run", "saloon", "salt", "same", "sandwich", "satisfied", "saturday", "saturday-2", "saturday-3", "saw", "scales", "school-bag", "school-bus", "scissors", "scold", "scooter", "self", "selfish", "september", "september-2", "serve", "sewing-machine", "shake", "sharbat", "share", "sharpener", "shave", "shiva", "shop", "shop-2", "short", "shout", "show", "shy", "signal", "sikh", "sikh-2", "simla", "sing", "sink", "sitar", "skip", "slim", "slip", "slow", "small", "smooth", "snake", "soft", "solid", "solve", "some", "sometimes", "sorry", "soul", "south", "sow", "spanner", "spastic", "special", "spend", "spider", "spider-2", "spill", "spoil", "spoil-2", "sports", "spy", "stage", "stick", "stingy", "stir", "stitch", "store", "straight-forward", "strong", "strongest", "stubborn", "sugar", "sugar-2", "sunday", "sunday-2", "sunday-3", "supply", "surat", "surprise", "suspect", "sweep", "sweet", "sweetest", "sweets", "swim", "swing", "switch", "tabla", "table-tennis", "tail", "tailor", "tall", "taxi", "tea", "tear", "tease", "temperature", "temple", "temporary", "tennis", "that", "their", "them", "themselves", "there", "these", "they", "thin", "think", "thirsty", "this", "those", "thread", "through", "throw", "thursday", "thursday-2", "thursday-3", "thursday-4", "thursday-5", "tie", "tiffin", "tiger", "tight", "tired", "to", "toast", "tools", "tortoise", "tortoise-2", "touch", "towards", "town", "trade", "transparent", "transport", "travel", "trophy", "trunk", "try", "tuesday", "tuesday-2", "tuesday-3", "turn", "tusks", "ugly", "under", "unlucky", "up", "us", "vada", "vadodara", "van", "varanasi", "vegetarian", "vehicle", "visit", "volleyball", "vomit", "wait", "waiting", "want", "warm", "warn", "wash", "waste", "water-bottle", "way", "we", "weak", "weakest", "wear", "weaver", "wednesday", "wednesday-2", "wednesday-3", "week", "week-2", "weeking", "weeks", "weigh", "weight", "welcome", "welder", "west", "wet", "what", "what-time", "wheat", "wheat-2", "where", "which", "whistle", "who", "whose", "why", "wide", "win", "wipe", "wire", "wish", "with", "without", "wolf", "worry", "wrestling", "year", "young", "zebra", "zebra-crossing", "zoo",'accessibility', 'accommondation', 'allthebest', 'amazing', 'availability', 'begin', 'bestofluck',
                   'bestwish', 'busy',
                   'cheerful', 'communicate', 'complete', 'congratulation', 'connection', 'cool', 'cost', 'deaf', 'do',
                   'does', 'engaged', 'enjoy', 'experience', 'family', 'fine', 'finsih', 'from', 'future', 'go', 'goal',
                   'good', 'goodafternoon', 'goodmorning', 'goodnight', 'happy', 'hearing', 'heart',
                   'home', 'house', 'how', 'i', 'important', 'incredible', 'internet', 'itsgreatconnectionwithyou',
                   'joyful', 'love', 'main', 'me', 'meet', 'money', 'my',
                   'name', 'nicetomeetyou', 'normalpreview', 'note', 'now', 'office', 'pen', 'please', 'previous',
                   'price', 'property', 'race', 'recored', 'run', 'sad', 'see', 'seeyoutommorow', 'skill',
                   'sorry', 'start', 'target', 'tea', 'thankyou', 'thatday', 'thedatbefore', 'thepreviosday', 'think',
                   'thismoment', 'thistime', 'time', 'today', 'tomorrow', 'value',
                   'vision', 'walk', 'watch', 'water', 'welcome', 'went', 'when', 'where', 'who', 'why', 'win', 'work',
                   'yesterday', 'you', 'your',"anklets", "antarctica", "apple", "arm", "asia", "ask", "assembly", "australia", "baby", "back", "bad", "banana", "bandh", "bangladesh", "bangles", "banian", "bark", "beak", "belief", "belt", "birds-winds-fly(verb)", "birth", "bite", "black", "blood", "blouse", "blue", "body", "bold", "bone", "boy", "brain", "brave", "breathe", "brother", "brother-in-law", "buddha-purnima", "buffalo", "busy", "camel", "camera", "cap", "cassette", "cat", "certificate", "chart", "chat", "cheat", "chest", "chew", "chickoo", "children", "china", "christmas", "circle", "class-room", "clever", "cloth", "coat", "cock", "coconut", "college", "compact-disc", "computer", "concentrate", "cone", "confident", "continent", "copy", "corruption", "cosmetics", "country", "cow", "crayons", "cream", "crow", "crown", "custard-apple", "cutout", "dasara", "daughter", "decide", "dhothi", "discuss", "diwali", "dog", "donkey", "dress", "dubai", "duck", "eagle", "eat", "education", "egg", "elbow", "election", "enemy", "engagement", "england", "europe", "examination", "explain", "eye", "face", "faith", "false", "family", "father", "father-in-law", "fear", "feather", "festivals", "film", "fingers", "fioppy", "fish", "flag", "foot", "france", "friend", "frock", "frog", "fruits", "ganapathi", "germany", "girl", "gloves", "goat", "good", "government", "granddaughter", "grandmother", "grandson", "green", "group", "guilty", "gurunanak-jayanthi", "hair", "hand", "handkerchief", "happy", "hardworking", "head", "hear", "hearing-aid", "hearing-aid-2", "help", "hen", "hip", "holi", "hope", "horse", "husband", "idd", "india", "information", "instigate", "insult", "interest", "israel", "jackfruit", "kind", "king", "knee", "knowledge", "kurta", "laboratary", "lazy", "leader", "learn", "leg", "lemon", "library", "lie", "lips", "lipstick", "man", "mango", "map", "memorize", "minister", "model", "mother", "mother-in-law", "mouth", "nail-polish", "name", "national-anthem", "neck", "necklace", "neck-tie", "neighbour", "nepal", "north-america", "nose", "nose-stud", "orange", "orange-2", "ornaments", "over-head-projector", "owl", "pain", "pakistan", "pant", "papaya", "parent", "parliament", "parrot", "patience", "peacock", "percentage", "person", "point", "pomegranate", "pongal", "poster", "powder", "power", "president", "principal", "proud", "puja", "pyjama", "radio", "read", "record", "rectangle", "red", "relative", "reply", "result", "right", "ring", "round", "run", "russia", "sad", "salwar-kameez", "sari", "scent", "school", "see", "shappels", "sheep", "shirt", "shoe", "shooting", "shoulder", "singapore", "singapore-2", "sister", "sister-in-law", "size", "skin", "skirt", "sleep", "sly", "smell", "socks", "son", "sparrow", "sphere", "square", "squrriel", "sri-lanka", "stand", "student", "study", "sugarcane", "surname", "swallow", "sweat", "sweater", "sweetlime", "talk", "taste", "teacher", "teeth", "television", "tell", "thank-you", "thigh", "throat", "toes", "tongue", "triangle", "trouble", "trouble-2", "true", "trust", "turkey", "twins", "understand", "unifrom", "united-states-of-america", "university", "video-camera", "video-cassette-recorder", "waist", "walk", "watch", "watermelon", "wedding", "west-indies", "west-indies-2", "whale", "white", "wife", "woman", "work", "world", "write", "wrong", "yellow", "address", "africa", "age", "angle", "angry",
                   "come",
                   "cut",
                   "earth",
                   "Farm",
                   "find",
                   "give",
                   "grow",
                   "he",
                   "her",
                   "him",
                   "his",
                   "keep",
                   "know",
                   "land",
                   "leave",
                   "letter",
                   "like",
                   "list",
                   "miss",
                   "mountain",
                   "move",
                   "need",
                   "never",
                   "night",
                   "often",
                   "open",
                   "plant",
                   "play",
                   "put",
                   "river",
                   "sea",
                   "second",
                   "she",
                   "sound",
                   "state",
                   "stop",
                   "story",
                   "take",
                   "then",
                   "thing",
                   "tree",
                   "until",
                   "water",
                   "way",
                   "we",
                   "Will",
                   "word",
                   "about",
                   "above",
                   "add",
                   "after",
                   "again",
                   "air",
                   "all",
                   "always",
                   "any",
                   "big",
                   "call",
                   "change",
                   "close"
                   ]

    # Filter keywords based on the remaining words
    #keywords = [word.capitalize() for word in filtered_words if word in mp4_dataset]

    keywords = [word.lower() for word in filtered_words if word.lower() in mp4_dataset]

    return keywords