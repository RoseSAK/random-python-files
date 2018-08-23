import argparse
from datetime import datetime
import time

colours = ['Red', 'Green', 'White']  #, 'Blue', 'Yellow', 'Purple']

parser = argparse.ArgumentParser(description='Configure fairy lights programme')
parser.add_argument('--lights', '-l', type=int, help='the number of lights', nargs='?', default=20)
args = parser.parse_args()

num_lights = args.lights

loops = num_lights/len(colours)
extras = num_lights % len(colours)

lights = (loops*colours) + colours[:extras]

print('Number of lights:', len(lights))

while True:
	for light in lights: 
		print(light, 'On', str(datetime.now().strftime("%H:%M:%S")))
		time.sleep(1)
		print(light, 'Off', str(datetime.now().strftime("%H:%M:%S")))


