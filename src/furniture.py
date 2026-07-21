def get_furniture(room):

    furniture = {

        "bedroom":[
            ("Bed",25000),
            ("Wardrobe",18000),
            ("Side Table",5000),
            ("Ceiling Light",4000),
            ("Curtains",3500)
        ],

        "living-room":[
            ("Sofa",35000),
            ("Coffee Table",8000),
            ("TV Unit",15000),
            ("Carpet",6000),
            ("Lighting",5000)
        ],

        "kitchen":[
            ("Cabinets",50000),
            ("Dining Table",20000),
            ("Chimney",12000),
            ("Lights",4000)
        ],

        "bathroom":[
            ("Mirror",4000),
            ("Cabinet",7000),
            ("Shower",12000),
            ("Lighting",3000)
        ],

        "home-office":[
            ("Office Desk",15000),
            ("Office Chair",10000),
            ("Bookshelf",12000),
            ("Lamp",2500)
        ],

        "pool":[
            ("Pool Chair",15000),
            ("Umbrella",8000),
            ("Outdoor Light",6000)
        ]

    }

    return furniture.get(room,[])