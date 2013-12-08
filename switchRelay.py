import wiringpi2 as wiringpi 
import sys

wiringpi.wiringPiSetupGpio()

relayArg = sys.argv[1]
stateArg = sys.argv[2]

print "Switching relay " + relayArg + " to " + ` int(stateArg)`

relayA = 24
relayB = 25

on  = 1
off = 0
if relayArg == 'A' or relayArg == 'a':
	selectedRelay = relayA
else:
	selectedRelay = relayB

if int(stateArg) == 1:
	relayValue = 1
else:
	relayValue = 0 

OUTPUT = 1
wiringpi.pinMode(selectedRelay,OUTPUT)

initialState = wiringpi.digitalRead(selectedRelay)
wiringpi.digitalWrite(selectedRelay,relayValue)
currentState = wiringpi.digitalRead(selectedRelay)

if(initialState == currentState):
	print "Target state was already set. No action taken"
else:
	print "Switched"
#print "Initial state"
#print initialState
#print "Current state"
#print currentState
