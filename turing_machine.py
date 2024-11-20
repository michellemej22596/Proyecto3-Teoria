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
        self.tape = list(input_string) + ['_']
        self.head_position = 0
        self.current_state = self.initial_state

    def step(self):
        # Asegurarse de que la posición del cabezal no está fuera de los límites de la cinta.
        if self.head_position < 0 or self.head_position >= len(self.tape):
            print("Error: El cabezal se ha salido de los límites de la cinta.")
            return False

        # Obtener el símbolo actual bajo el cabezal.
        symbol = self.tape[self.head_position]

        # Verificar si hay una transición válida para el estado actual y el símbolo.
        if self.current_state not in self.transitions or symbol not in self.transitions[self.current_state]:
            print(f"No hay transición válida para el estado {self.current_state} y el símbolo '{symbol}'")
            return False

        # Obtener el nuevo estado, el símbolo para escribir y el movimiento del cabezal.
        new_state, write_symbol, move = self.transitions[self.current_state][symbol]

        # Descripción instantánea antes del paso.
        print(f"Estado actual: {self.current_state}, Símbolo leído: '{symbol}', Cinta: {''.join(self.tape)}, Posición del cabezal: {self.head_position}")

        # Escribir el nuevo símbolo en la cinta.
        self.tape[self.head_position] = write_symbol

        # Mover el cabezal a la izquierda o derecha.
        if move == 'R':
            self.head_position += 1
        elif move == 'L':
            self.head_position -= 1

        # Si el cabezal se mueve más allá del final de la cinta, añadir un símbolo en blanco.
        if self.head_position >= len(self.tape):
            self.tape.append('_')
        elif self.head_position < 0:
            # Esto maneja el caso en que el cabezal va más allá del principio de la cinta.
            self.tape.insert(0, '_')
            self.head_position = 0

        # Actualizar el estado actual.
        self.current_state = new_state

        # Descripción instantánea después del paso.
        print(f"Nuevo estado: {self.current_state}, Cinta después del paso: {''.join(self.tape)}, Posición del cabezal: {self.head_position}")

        return True

    def run(self):
        while self.current_state not in self.final_states:
            if not self.step():
                return False  # Input no aceptado.
        print(f"Cadena aceptada en estado final: {self.current_state}")
        return True  # Input aceptado.
