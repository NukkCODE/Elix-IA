import json
import os

class SimpleAI:
    def __init__(self, knowledge_file="knowledge_base.json"):
        self.knowledge_file = knowledge_file
        self.knowledge_base = self.load_knowledge_base()

    def load_knowledge_base(self):
        if os.path.exists(self.knowledge_file):
            with open(self.knowledge_file, 'r') as f:
                return json.load(f)
        else:
            return {}

    def save_knowledge_base(self):
        with open(self.knowledge_file, 'w') as f:
            json.dump(self.knowledge_base, f, indent=4)

    def learn(self, question, answer):
        self.knowledge_base[question] = answer
        self.save_knowledge_base()

    def ask(self, question):
        if question in self.knowledge_base:
            # Séparation des réponses par des points-virgules
            responses = self.knowledge_base[question].split(';')
            return responses
        else:
            return ["Je ne sais pas. Que devrais-je dire à cela?"]

# Fonction principale pour interagir avec l'IA
def main():
    ai = SimpleAI()

    print("Bonjour! Je suis une IA simple. Posez-moi des questions ou dites-moi quelque chose.")

    while True:
        user_input = input("Vous: ")

        if user_input.lower() == 'exit':
            ai.save_knowledge_base()
            print("Au revoir!")
            break

        # Vérifier si l'IA sait déjà la réponse
        if user_input in ai.knowledge_base:
            responses = ai.ask(user_input)
            print("IA:", responses)
        else:
            # Si l'IA ne sait pas, elle demande à l'utilisateur et apprend
            print("Elix-IA: Je ne sais pas. Que devrais-je dire à cela?")
            new_answer = input("Vous: ")
            ai.learn(user_input, new_answer)
            print("Elix-IA: Merci! Maintenant je saurai quoi répondre à cette question.")

if __name__ == "__main__":
    main()
