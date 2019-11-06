# Battleship AI
Engine and AI for classic boardgame "Battleship" in command line format

## Rules
The rules used for this version of the game are as follows:

### Goal
Sink all of opponents ships before they can sink all of yours

### Setup
Each player places ships in grid

#### Ships:
Consists of following ships in format (name, size)
- (Carrier, 5)
- (Battleship, 4)
- (Cruiser, 3)
- (Submarine, 3)
- (Destroyer, 2) 

### Turns
Players take turns declaring grid coordinates
 - other player must respond with hit or miss (ship present on coordinate)
 - other player must declare if a ship is sunk (all coordinates which ship occupies are hit)


## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run main.py for current test(Human vs simple AI)

## Todo:
- Design and implement more efficient AI
- Script for data collection and running game in bulk

 