# Elements Simulation Using Cellular Automata

This project simulates the interactions between different elements using Cellular Automata (CA). It includes the generation of caves and simulating fluids, such as water, sand, and fire, with different rules governing their behavior. The simulation also allows for manually adding elements to observe their interactions.

## Installation

To run the simulation, you need Python installed on your system along with the Pygame library.

1. **Install Python** : [official website](https://www.python.org/downloads/).

2. **Install Pygame** : Pygame can be installed using pip. Open your terminal or command prompt and run the following command:
   
   ```
   pip install pygame
   ```

3. **Download the Code** : Download the provided Python script (`main.py`) to your local machine.

4. **Run the Script** : Navigate to the directory containing the script in your terminal or command prompt and execute the script using Python:

   ```
   python elements_simulation.py
   ```

## Usage

- Upon running the script, a Pygame window will open displaying the simulation environment.

- Elements can be added to the simulation by clicking and dragging the mouse:
  - **Wood**: Click and drag to add wood elements.
  - **Fire**: While holding the mouse button, move over wood elements to ignite them.
  - **Sand**: Press the spacebar key and click to add sand elements.
  - **Water**: Press the down arrow key and click to add water elements.

- The simulation will automatically update the elements positions and interactions based on predefined rules.

- You can observe the behavior of different elements and their interactions in the simulation.


## Simulation Components

1. **Conway's Game of Life**:
   - The simulation starts with generating Conway's Game of Life structures using Cellular Automata with specific rules.

2. **Fluid Simulation**:
   - **Water**: Moves downwards and spreads horizontally, interacting with other elements.
   - **Sand**: Falls downwards and can pile up, affecting the flow of water.
   - **Fire**: Spreads randomly and interacts with wood, turning it into fire or ash.

3. **Additional Elements**:
   - **Wood**: Stationary element that can catch fire.
   - **Ash**: Result of burned wood.
   - **Smoke**: Rises upwards and dissipates over time.
