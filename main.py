from parser import load_yaml
from turing_machine import TuringMachine

def run_machine(yaml_file):
    # Cargar la configuración de la Máquina de Turing desde el archivo YAML.
    config = load_yaml(yaml_file)
    print("Configuración cargada:", config)  # Imprimir la configuración para verificar que se lee correctamente.

    # Crear una instancia de la Máquina de Turing con la configuración cargada.
    tm = TuringMachine(
        states=config['states'],
        initial_state=config['initial_state'],
        final_states=config['final_states'],
        tape_alphabet=config['tape_alphabet'],
        input_alphabet=config['input_alphabet'],
        transitions=config['transitions']
    )

    # Ejecutar la simulación para cada cadena de entrada proporcionada en la configuración.
    for input_string in config['inputs']:
        print(f"\nSimulando entrada: {input_string}")
        tm.load_tape(input_string)
        result = tm.run()
        print(f"Resultado: {'Aceptada' if result else 'Rechazada'}")
        print(f"Cinta final: {''.join(tm.tape)}")

if __name__ == "__main__":
    print("Selecciona la Máquina de Turing a ejecutar:")
    print("1. Máquina de Turing Reconocedora")
    print("2. Máquina de Turing Alteradora")

    choice = input("Ingresa el número de la opción deseada: ")

    if choice == "1":
        run_machine('mt_config.yaml')  # Archivo YAML para la máquina reconocedora.
    elif choice == "2":
        run_machine('mt_alt.yaml')  # Archivo YAML para la máquina alteradora.
    else:
        print("Opción no válida.")
