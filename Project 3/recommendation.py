"""
PROJECT 3: AI RECOMMENDATION LOGIC
Food Recommendation System
"""

print("=" * 60)
print("🍽️ FOOD RECOMMENDATION SYSTEM 🍽️")
print("=" * 60)

# Food database
foods = [
    {
        "name": "Margherita Pizza",
        "cuisine": "Italian",
        "type": "Savory",
        "spice_level": 1,
        "ingredients": ["cheese", "tomato", "basil"]
    },
    {
        "name": "Sushi",
        "cuisine": "Japanese",
        "type": "Savory",
        "spice_level": 2,
        "ingredients": ["rice", "fish", "seaweed"]
    },
    {
        "name": "Tacos",
        "cuisine": "Mexican",
        "type": "Savory",
        "spice_level": 4,
        "ingredients": ["tortilla", "meat", "cheese", "salsa"]
    },
    {
        "name": "Chocolate Cake",
        "cuisine": "International",
        "type": "Sweet",
        "spice_level": 0,
        "ingredients": ["chocolate", "flour", "sugar", "eggs"]
    },
    {
        "name": "Biryani",
        "cuisine": "Pakistani",
        "type": "Savory",
        "spice_level": 5,
        "ingredients": ["rice", "meat", "spices", "onion"]
    },
    {
        "name": "Ice Cream",
        "cuisine": "International",
        "type": "Sweet",
        "spice_level": 0,
        "ingredients": ["milk", "sugar", "flavors"]
    },
    {
        "name": "Pad Thai",
        "cuisine": "Thai",
        "type": "Savory",
        "spice_level": 3,
        "ingredients": ["noodles", "shrimp", "peanuts", "eggs"]
    },
    {
        "name": "Falafel",
        "cuisine": "Middle Eastern",
        "type": "Savory",
        "spice_level": 2,
        "ingredients": ["chickpeas", "herbs", "spices"]
    }
]

print("\n📋 Available Cuisines:")
cuisines = set()
for food in foods:
    cuisines.add(food["cuisine"])

for cuisine in sorted(cuisines):
    print(f"   • {cuisine}")

print("\n" + "-" * 60)
user_cuisine = input("\n🎯 Which cuisine are you craving? ").strip().title()

matching_foods = []
for food in foods:
    if food["cuisine"] == user_cuisine:
        matching_foods.append(food)

print("\n" + "-" * 60)
if matching_foods:
    print(f"\n✅ Found {len(matching_foods)} food(s):\n")
    for food in matching_foods:
        spice_rating = "🔥" * food["spice_level"]
        print(f"🍽️ {food['name']}")
        print(f"   Type: {food['type']}")
        print(f"   Spice Level: {spice_rating}")
        print(f"   Ingredients: {', '.join(food['ingredients'])}")
        print()
else:
    print(f"\n❌ Sorry, no food found for '{user_cuisine}' cuisine.")

print("=" * 60)
print("🍽️ THANK YOU FOR USING FOOD RECOMMENDER! 🍽️")
print("=" * 60)
