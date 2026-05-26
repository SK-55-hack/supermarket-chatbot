import random

class ProductDetailsBot:
    def handle(self, query):
        categories = {
            "Fruits": ["Bananas", "Apples", "Oranges", "Blueberries"],
            "Vegetables": ["Carrots", "Spinach", "Broccoli", "Bell Peppers"],
            "Dairy": ["Milk", "Cheese", "Yogurt", "Butter"],
            "Grains": ["Rice", "Quinoa", "Pasta", "Oats"],
            "Snacks": ["Granola Bars", "Chips", "Nuts", "Crackers"]
        }
        reply = "Here are some items we offer:\n"
        for category, items in categories.items():
            reply += f"- {category}: {', '.join(items)}\n"
        reply += "\nNeed something specific? Let me know!"
        return reply

class ChefBot:
    def handle(self, query):
        if "breakfast" in query.lower():
            return "How about overnight oats with berries and yogurt?"
        elif "dinner" in query.lower():
            return "Grilled chicken with roasted veggies is a healthy dinner idea!"
        elif "quick" in query.lower():
            return "Make a veggie stir-fry with tofu and noodles for a quick meal."
        recipes = [
            "Try quinoa salad with chickpeas and avocado.",
            "Cook spaghetti aglio e olio with garlic and olive oil.",
            "Lentil soup with carrots and herbs is both healthy and affordable."
        ]
        return random.choice(recipes)

class HealthBot:
    def handle(self, query):
        if "diabetes" in query.lower():
            return "Choose whole grains, lean proteins, and avoid added sugars."
        elif "heart" in query.lower():
            return "Focus on low-fat dairy, lots of greens, and fiber-rich foods."
        tips = [
            "Swap sugary drinks for herbal tea or water.",
            "Snack on nuts or fruit instead of processed snacks.",
            "Use whole grains like brown rice and quinoa for extra fiber."
        ]
        return random.choice(tips)

class BudgetBot:
    def handle(self, query):
        if "cheap" in query.lower() or "affordable" in query.lower():
            return "Lentils, rice, and seasonal vegetables are budget-friendly meal options."
        offers = [
            "Buy 1 Get 1 free on selected pasta this week!",
            "Fresh produce discounts: apples at $0.99/lb and carrots at $0.79/lb.",
            "Save on store-brand products—up to 15% cheaper than name brands."
        ]
        return random.choice(offers)

class GeneralBot:
    def handle(self, query):
        return "Hi there! I can help you with product details, recipes, health tips, or budget-friendly options."
