class TuringMachine:
    def __init__(self, states, initial_state, final_states, tape_alphabet, input_alphabet, transitions):
        self.states = states
        self.initial_state = initial_state
        self.final_states = final_states
        self.tape_alphabet = tape_alphabet
        self.input_alphabet = input_alphabet
        self.transitions = transitions
        self.tape = []
        self.head_position = 0
        self.current_state = initial_state

    def load_tape(self, input_string):
        self.tape = list(input_string) + ['_']  # Agrega un símbolo blanco al final.
        self.head_position = 0

    def step(self):
        symbol = self.tape[self.head_position]
        key = (self.current_state, symbol)
        if key not in self.transitions:
            return False  # No hay transición válida.
        new_state, write_symbol, move = self.transitions[key]
        self.tape[self.head_position] = write_symbol
        self.head_position += 1 if move == 'R' else -1
        self.current_state = new_state
        return True

    def run(self):
        while self.current_state not in self.final_states:
            if not self.step():
                return False  # Input no aceptado.
        return True  # Input aceptado.
