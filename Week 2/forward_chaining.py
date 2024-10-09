class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion


class ExpertSystem:
    def __init__(self):
        self.rules = []
        self.facts = dict()
        self.ruled_out = set()
        self.decision = None

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact, value):
        self.facts[fact] = value


    def ask_user_for_fact(self, fact):
        response = input(f"Is the band {fact}? (yes/no): ").strip().lower()
        if response == 'yes':
            self.add_fact(fact, True)
        elif response == "no":
            self.add_fact(fact, False)

    def rule_out_false(self):
        for rule in self.rules:
            for condition in self.facts:
                if self.facts[condition] is False:
                    self.ruled_out.add(condition)


    def infer(self):
        while not self.decision:
            for rule in self.rules:
                if all(condition in self.facts for condition in rule.conditions):
                    self.decision = rule.conclusion
                    print(f"Inferred: {rule.conclusion}")
                elif any(condition not in self.facts for condition in rule.conditions):
                    for condition in rule.conditions:
                        if condition not in self.facts:
                            self.ask_user_for_fact(condition)
                            break  # Ask one fact at a time


# Example usage
if __name__ == "__main__":
    # Create an expert system
    es = ExpertSystem()
    # Add rules
    es.add_rule(Rule(["Modern Metal", "British", "Currently Touring"], "Sylosis"))
    es.add_rule(Rule(["Modern Metal", "British"], "Architects"))
    es.add_rule(Rule(["Deathcore", "American", "Currently Touring"], "Fit For An Autopsy"))
    es.add_rule(Rule(["Deathcore", "American"], "Whitechapel"))
    es.add_rule(Rule(["Metalcore", "American", ""], "Killswitch Engage"))
    es.add_rule(Rule(["Modern Metal", "American"], "All That Remains"))
    es.add_rule(Rule(["Metalcore", "British"], "While She Sleeps"))
    es.add_rule(Rule(["Metalcore", "Australian"], "Polaris"))
    # Perform inference
    es.infer()
    # Print final facts
    print("Final facts:", es.facts)
