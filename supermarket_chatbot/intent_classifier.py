from bot_modules import ProductDetailsBot, ChefBot, HealthBot, BudgetBot, GeneralBot

class IntentClassifier:
    def __init__(self):
        self.keywords = {
            "product": ProductDetailsBot(),
            "fruit": ProductDetailsBot(),
            "vegetable": ProductDetailsBot(),
            "recipe": ChefBot(),
            "cook": ChefBot(),
            "meal": ChefBot(),
            "healthy": HealthBot(),
            "health": HealthBot(),
            "diabetes": HealthBot(),
            "heart": HealthBot(),
            "cheap": BudgetBot(),
            "budget": BudgetBot(),
            "discount": BudgetBot()
        }
        self.default_bot = GeneralBot()

    def get_module(self, query):
        query = query.lower()
        for keyword, bot in self.keywords.items():
            if keyword in query:
                return bot
        return self.default_bot
