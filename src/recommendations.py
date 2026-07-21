def get_recommendation(room, style):

    recommendations = {

        "bedroom": {

            "Modern": {

                "wall": "Light Grey",

                "floor": "Wood Flooring",

                "lighting": "Warm LED",

                "furniture": "Queen Bed, Wardrobe"
            },

            "Minimalist": {

                "wall": "White",

                "floor": "Oak Wood",

                "lighting": "Natural Light",

                "furniture": "Simple Bed"
            }

        },

        "home-office": {

            "Minimalist": {

                "wall": "White",

                "floor": "Wood",

                "lighting": "Desk Lamp",

                "furniture": "Office Desk, Ergonomic Chair"
            },

            "Modern": {

                "wall": "Grey",

                "floor": "Wood",

                "lighting": "LED Panel",

                "furniture": "Office Desk"
            }

        }

    }

    return recommendations.get(room, {}).get(style, {})