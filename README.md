# Proyecto3-Teoria
Michelle Mejía 22596 y  Silvia Illescas 22376

# Simulador de Máquina de Turing

Este proyecto consiste en un simulador de Máquina de Turing (MT) desarrollado en Python. Permite cargar una configuración de MT desde un archivo YAML, simular el procesamiento de una entrada y determinar si es aceptada o rechazada.

---

## Funcionalidades

1. **Simulación de Máquinas de Turing reconocedoras**:
   - Procesa cadenas y determina si son aceptadas o rechazadas.
   - Muestra las descripciones instantáneas de cada paso de la simulación.

2. **Simulación de Máquinas de Turing alteradoras**:
   - Modifica las cadenas de entrada según las reglas definidas en el YAML.

---

## Estructura del Proyecto

- `main.py`: Punto de entrada principal para ejecutar las simulaciones.
- `turing_machine.py`: Implementación de la lógica de la Máquina de Turing.
- `parser.py`: Funciones para leer y procesar el archivo YAML.
- `mt_config.yaml`: Archivo de configuración de la Máquina de Turing (estados, transiciones, etc.).
- `README.md`: Documentación del proyecto.
- `.gitignore`: Archivos y carpetas ignorados en el repositorio.

---

## Requisitos

1. **Lenguaje de programación**: Python 3.8 o superior.
2. **Librerías**: Asegúrate de instalar las dependencias:
   pip install pyyaml

### Como usarlo 
git clone https://github.com/usuario/mi-repositorio.git
cd mi-repositorio

Define la máquina de Turing en el archivo mt_config.yaml.

Ejecuta
python main.py

El programa mostrará si las cadenas configuradas son aceptadas o rechazadas, junto con las descripciones instantáneas.

#### Video Demostrativo
https://www.youtube.com/watch?v=0tJJcpMhNOk

