# Signals and Systems with Python Project

This project generates digital signals using Python.  
It demonstrates signal waves such as sinusoidal and  square waves can be generated, modified, and plotted.  
The project also includes signal operations such as time-shifting and time-scaling:

This project contains files:
- signals.py
- Run.py
- README.md
- test_signals.py
- pyproject.toml
- pytest_results.png


signals.py file has functions for Sinusoidal Wave Signal, Square Wave Signal, time-shifting and time-scaling. Variables such as frequency, duration, sample rate and amplitude are defined. 

Run.py file imports functions from signals.py and plots graph according to the input of values for frequency, duration, sample rate and amplitude. 

README.md file (this file) contains general information on the project itself. 

test_signals.py includes automated unit tests for each function in `signals.py`.  
  Each function is tested with one normal case and one edge case using `pytest`.

pyproject.toml defines project metadata and dependencies.  
  This file allows the project to be packaged or built cleanly with `setuptools`.

pytest_results.png is a screenshot proof that all automated tests passed successfully using pytest.

