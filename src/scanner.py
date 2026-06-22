from src.keywords import RESERVED_WORDS


class PureDFAScanner:
    def __init__(self):
        self.reserved_words = RESERVED_WORDS

        self.transitions = {}
        self.accept_states = {}
        self.dead_state = "q_dead"
        self.start_state = "q0"

        self.state_counter = 1

        self.transitions[self.start_state] = {}
        self.transitions[self.dead_state] = {}

        self._build_dfa()

    def _new_state(self):
        state = f"q{self.state_counter}"
        self.state_counter += 1
        self.transitions[state] = {}
        return state

    def _build_dfa(self):
        for word in self.reserved_words:
            current_state = self.start_state

            for symbol in word:
                if symbol not in self.transitions[current_state]:
                    new_state = self._new_state()
                    self.transitions[current_state][symbol] = new_state

                current_state = self.transitions[current_state][symbol]

            self.accept_states[current_state] = word

    def delta(self, state, symbol):
        if state in self.transitions and symbol in self.transitions[state]:
            return self.transitions[state][symbol]

        return self.dead_state

    def is_delimiter(self, char):
        delimiters = [
            " ", "\n", "\t",
            ";", ",", ".", ":", 
            "(", ")", "{", "}", "[", "]",
            "+", "-", "*", "/", "%", "=",
            "<", ">", "!", "&", "|", "^", "~",
            "\"", "'"
        ]

        return char in delimiters

    def scan_file(self, input_path):
        with open(input_path, "r", encoding="utf-8") as file:
            source_code = file.read()

        found_keywords = []
        full_history = []

        current_state = self.start_state
        current_token = ""

        line = 1
        column = 1

        token_start_line = 1
        token_start_column = 1

        reading_token = False

        for char in source_code:
            if self.is_delimiter(char):
                if reading_token:
                    self._close_token(
                        current_token,
                        current_state,
                        token_start_line,
                        token_start_column,
                        found_keywords,
                        full_history
                    )

                current_state = self.start_state
                current_token = ""
                reading_token = False

                if char == "\n":
                    line += 1
                    column = 1
                else:
                    column += 1

                continue

            if not reading_token:
                reading_token = True
                token_start_line = line
                token_start_column = column
                current_state = self.start_state
                current_token = ""

            previous_state = current_state
            current_state = self.delta(current_state, char)
            current_token += char

            full_history.append({
                "token": current_token,
                "char": char,
                "from": previous_state,
                "to": current_state,
                "line": line,
                "column": column
            })

            column += 1

        if reading_token:
            self._close_token(
                current_token,
                current_state,
                token_start_line,
                token_start_column,
                found_keywords,
                full_history
            )

        return found_keywords, full_history

    def _close_token(
        self,
        token,
        final_state,
        line,
        column,
        found_keywords,
        full_history
    ):
        if final_state in self.accept_states:
            reserved_word = self.accept_states[final_state]

            if token == reserved_word:
                found_keywords.append({
                    "word": token,
                    "line": line,
                    "column": column,
                    "final_state": final_state
                })

        full_history.append({
            "token": token,
            "char": "DELIMITADOR",
            "from": final_state,
            "to": self.start_state,
            "line": line,
            "column": column,
            "closed": True
        })

    def get_transition_table(self):
        rows = []

        for state in self.transitions:
            for symbol in self.transitions[state]:
                rows.append({
                    "state": state,
                    "symbol": symbol,
                    "next_state": self.transitions[state][symbol]
                })

        return rows