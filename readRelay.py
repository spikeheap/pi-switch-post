import wiringpi2 as wiringpi 
import sys

wiringpi.wiringPiSetupGpio()

relayArg = sys.argv[1]

relayA = 24
relayB = 25

if relayArg == 'A' or relayArg == 'a':
	selectedRelay = relayA
else:
	selectedRelay = relayB

OUTPUT = 1
wiringpi.pinMode(selectedRelay,OUTPUT)

initialState = wiringpi.digitalRead(selectedRelay)

print initialState
