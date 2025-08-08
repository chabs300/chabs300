
"""
main.py
Author: Paul Pircher
Date: August 8, 2025
Description: This file serves as the entry point the vehicle track 
interaction (VTI) simulations. It runs the given setup with the parameters
configured in simulation_setup.py and starts the simulation process.
"""

def main():
    """ 
    Main function to start the simulation process.
    It loads the data and then each individual function available can be called.
    """
    import logging
    import sys
    import time
    from datetime import datetime

    # Configure logging to file and console
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("simulation.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    start_time = time.time()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f"Simulation main.py started on {now}")

    # ... simulation code goes here ...

    # Finishing the simulation
    end_time = time.time()
    elapsed = end_time - start_time
    logging.info(f"Simulation finished. Total runtime: {elapsed:.2f} seconds.")


if __name__ == "__main__":
    main()




