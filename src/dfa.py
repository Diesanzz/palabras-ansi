class DFA:
    def __init__(self, reserved_words):
        self.reserved_words = reserved_words
        self.transitions = {}
        self.accept_states = {}
        self.dead_state = "q_dead"
        self.state_counter = 0
        self.start_state = self._new_state()

        self._build_trie_dfa()

    def _new_state(self):
        state = f"q{self.state_counter}"
        self.state_counter += 1
        self.transitions[state] = {}
        return state

    def _build_trie_dfa(self):
        for word in self.reserved_words:
            current_state = self.start_state

            for char in word:
                if char not in self.transitions[current_state]:
                    new_state = self._new_state()
                    self.transitions[current_state][char] = new_state

                current_state = self.transitions[current_state][char]

            self.accept_states[current_state] = word

        self.transitions[self.dead_state] = {}

    def evaluate(self, token):
        current_state = self.start_state
        history = []

        for char in token:
            previous_state = current_state

            if char in self.transitions[current_state]:
                current_state = self.transitions[current_state][char]
            else:
                current_state = self.dead_state

            history.append({
                "char": char,
                "from": previous_state,
                "to": current_state
            })

            if current_state == self.dead_state:
                break

        is_reserved = current_state in self.accept_states and self.accept_states[current_state] == token

        return {
            "token": token,
            "is_reserved": is_reserved,
            "reserved_word": self.accept_states.get(current_state),
            "final_state": current_state,
            "history": history
        }

    def get_transition_table(self):
        rows = []

        for state, transitions in self.transitions.items():
            for char, next_state in transitions.items():
                rows.append((state, char, next_state))

        return rows