# game-of-life 
An implementation of Conways game of life with RGB, using pygame for display

## Struckture
The project is split into two files.  
##### `main.py`
* initialization
* contains main class `Game` for field calculation
* calling the output functions


##### `pg_output.py`  
* handling of the window and it's content in `MultiSquare`
* color and appearence of those blocks in `Changes`

## Settings
You can set the the amount of calculated objects and the way the windows and its blocks are scaled.  
Those settings are adjustable in `settings.ini`.
‌
There is also a way to change the RGB style and colour of the simulation by changing the `colour` parameter of `prod()` in `pg_output.py`, but thats a bit more tricky ;)

### How to install
`pip install -r requirements.txt`  
I do highly recommend to use [_virtial-environments_](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment) for installing packages!

