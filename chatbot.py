from transformers import pipeline
from intent_classifier import IntentClassifier

class SupermarketChatbot:
    def __init__(self):
        self.classifier = IntentClassifier()
        self.memory = []
        self.generator = pipeline("text-generation", model="gpt2")

    def add_to_memory(self, speaker, message):
        self.memory.append((speaker, message))

    def get_memory(self):
        return self.memory[-10:]  # Last 10 messages

    def generate_ai_suggestion(self, query):
        context = "\n".join(f"{s}: {m}" for s, m in self.get_memory())
        prompt = context + f"\nUser: {query}\nBot:"
        output = self.generator(prompt, do_sample=True, max_new_tokens=50)[0]['generated_text']
        return output.replace(prompt, '').strip().split('\n')[0]

    def get_response(self, query):
        self.add_to_memory("User", query)
        bot_module = self.classifier.get_module(query)
        base_reply = bot_module.handle(query)
        ai_suggestion = self.generate_ai_suggestion(query)
        reply = f"{base_reply}\n\n(AI Suggestion): {ai_suggestion}"
        self.add_to_memory("Bot", reply)
        return reply




    


    

