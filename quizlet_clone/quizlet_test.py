import json
import random
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Card:
    term: str
    definition: str

class QuizletTest:
    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.score = 0
        self.questions = 0

    def ask_written(self, card: Card, ask_for_term: bool = True) -> bool:
        if ask_for_term:
            answer = input(f"Definition: {card.definition}\nTerm: ")
            correct = answer.strip().lower() == card.term.lower()
        else:
            answer = input(f"Term: {card.term}\nDefinition: ")
            correct = answer.strip().lower() == card.definition.lower()
        print("Correct!" if correct else f"Incorrect. Answer: {card.term if ask_for_term else card.definition}")
        return correct

    def ask_multiple_choice(self, card: Card, ask_for_term: bool = True) -> bool:
        options = random.sample(self.cards, k=min(4, len(self.cards)))
        if card not in options:
            options[0] = card
        random.shuffle(options)
        choices = [c.term if ask_for_term else c.definition for c in options]
        prompt = card.definition if ask_for_term else card.term
        print(f"Question: {prompt}")
        for idx, choice in enumerate(choices, 1):
            print(f" {idx}. {choice}")
        try:
            selection = int(input("Select option: ")) - 1
        except ValueError:
            selection = -1
        correct = options[selection] == card if 0 <= selection < len(options) else False
        print("Correct!" if correct else f"Incorrect. Answer: {card.term if ask_for_term else card.definition}")
        return correct

    def run_test(self, num_questions: int = 10):
        print("Starting Quizlet-style test!\n")
        for _ in range(num_questions):
            card = random.choice(self.cards)
            mode = random.choice(['written', 'mc'])
            ask_for_term = random.choice([True, False])
            self.questions += 1
            if mode == 'written':
                correct = self.ask_written(card, ask_for_term)
            else:
                correct = self.ask_multiple_choice(card, ask_for_term)
            if correct:
                self.score += 1
            print()
        print(f"Test complete! Score: {self.score}/{self.questions}")


def load_cards(path: str) -> List[Card]:
    with open(path, 'r') as f:
        data: List[Dict[str, str]] = json.load(f)
    return [Card(**item) for item in data]

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Quizlet Test Mode Clone")
    parser.add_argument('file', help='JSON file containing cards')
    parser.add_argument('-n', '--num', type=int, default=10, help='number of questions')
    args = parser.parse_args()
    cards = load_cards(args.file)
    test = QuizletTest(cards)
    test.run_test(args.num)

if __name__ == '__main__':
    main()
