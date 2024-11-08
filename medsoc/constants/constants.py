LOCATION_COLS = [
    "Ballsbridge",
    "Blackrock",
    "Booterstown",
    "Bray",
    "Cabinteely",
    "Clonskeagh",
    "Clontarf",
    "City Centre - Northside",
    "City Centre - Southside",
    "Dalkey",
    "Deansgrange",
    "Donnybrook",
    "Drumcondra",
    "Dundrum",
    "Dun Laoighre",
    "Foxrock",
    "Glenageary",
    "Goatstown",
    "Kilmacud",
    "Kilmainham",
    "Merrion",
    "Milltown",
    "Mount Merrion",
    "Raheny",
    "Ranelagh",
    "Rathfarnam",
    "Rathmines",
    "Ringsend",
    "Sandymount",
    "Stillorgan",
    "Terenure",
    "UCD",
    "Windy Arbour",
]

LOCATION_LIMITS = {
    "Ballsbridge": ["Ballsbridge Village"],
    "Blackrock": [
        "Blackrock Dart",
        "Blackrock Main St.",
        "Blackrock Pedestrian Area",
        "Carysfort Avenue",
    ],
    "Booterstown": ["Booterstown Applegreen", "Booterstown Avenue", "Booterstown Dart"],
    "Bray": ["Bray Dart"],
    "Cabinteely": ["Cabinteely Village"],
    "Clonskeagh": [
        "Clonskeagh Applegreen",
        "Bird Avenue",
        "Roebuck Road",
        "Clonskeagh Mosque",
    ],
    "Clontarf": ["Clontarf"],
    "City Centre - Northside": [
        "Abbey St",
        "Capel St",
        "Connolly",
        "Henry St",
        "Jervis St",
        "Parnell Square",
    ],
    "City Centre - Southside": [
        "Aungier St",
        "Beckett Bridge",
        "Camden St",
        "Christchurch",
        "Clarendon St",
        "Dawson St",
        "D'olier St",
        "Earlsfort Terrace",
        "Fleet St",
        "Hanover Quay",
        "Ha'penny Bridge - Southside",
        "Harcourt St",
        "Kilmainham",
        "Leeson St (Upper + Lower)",
        "Merrion Square",
        "Nassau St",
        "South Great George's St",
        "Stephen's Green (Grafton + Leeson Ends)",
        "Pearse St",
        "Tara St",
        "Westmoreland St",
    ],
    "Dalkey": [
        "Dalkey Dart",
        "Dalkey Village",
    ],
    "Deansgrange": ["Deansgrange"],
    "Donnybrook": [
        "Donnybrook Church",
        "Donnybrook Fair",
        "Donnybrook Village",
        "Rte",
    ],
    "Drumcondra": ["Drumcondra"],
    "Dundrum": [
        "Balally Luas Stop",
        "Dundrum Luas Stop",
        "Dundrum Village",
    ],
    "Dun Laoighre": [
        "Dun Laoghaire Dart Station",
        "Dun Laoghaire Main St",
    ],
    "Foxrock": ["Foxrock Church"],
    "Glenageary": ["Glenageary"],
    "Goatstown": ["Goatstown"],
    "Kilmacud": ["Upper Kilmacud Road", "Kilmacud Luas"],
    "Merrion": [
        "Sydney Parade Dart",
        "Vincent's Hospital",
    ],
    "Milltown": ["Milltown", "Cowper Luas"],
    "Mount Merrion": ["Foster's Avenue", "Mount Merrion"],
    "Raheny": ["Raheny"],
    "Ranelagh": [
        "Beechwood (and Luas Stop)",
        "Ranelagh Centre",
        "Ranelagh Luas Stop",
    ],
    "Rathfarnam": ["Rathfarnam Shopping Centre", "Rathgar Village"],
    "Rathmines": ["Harold's Cross Road", "Rathmines Centre"],
    "Ringsend": ["Ringsend"],
    "Sandymount": ["Sandymount Dart", "Sandymount Village"],
    "Stillorgan": ["Stillorgan Centre", "Stillorgan Luas"],
    "Terenure": ["Terenure"],
    "UCD": [
        "Health Science Building",
        "James Joyce Library",
        "N11 Bus Stop",
        "UCD Village Hall",
    ],
    "Windy Arbour": ["Windy Arbour"],
}

COLUMNS_TO_DROP = [
    "Timestamp",
    "Email\n",
    "Name",
    "Your phone number",
    "Any dietary requirements/allergens for the breakfast eg Halal, Veg, etc.",
    "T-shirt size",
]

DTYPE_DICT = {
    "email": "string",
    "year": "string",
    "signup": "bool",
    "p1": "category",
    "p2": "category",
    "p3": "category",
}

SIGNUP_MAP = {
    "Yes": True,
    "No": False,
    "": False,
}

DF_COLUMNS = list(DTYPE_DICT.keys())

MAX_RUNS = 100
