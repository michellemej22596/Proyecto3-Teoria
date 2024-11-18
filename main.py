from parser import load_yaml
from turing_machine import TuringMachine

if __name__ == "__main__":
    config = load_yaml('mt_config.yaml')
    tm = TuringMachine(
        states=config['states'],
        initial_state=config['initial_state'],
        final_states=config['final_states'],
        tape_alphabet=config['tape_alphabet'],
        input_alphabet=config['input_alphabet'],
        transitions=config['transitions']
    )

    for input_string in config['inputs']:
        tm.load_tape(input_string)
        result = tm.run()
        print(f"Input: {input_string} -> {'Accepted' if result else 'Rejected'}")
        print(f"Tape: {''.join(tm.tape)}")
