# DJ Controller to XBox Gamepad
This repo will allow you to use the Pioneer DDJ-FLX6 as an Xbox gamepad. Feel free to fork this repo and modify it to add support for other MIDI devices =)

---

## Installation
This project requires Python 3.12 or higher

Look at the [requirements.txt](https://github.com/KodiakTE/DJControllerToGamepad/blob/main/requirements.txt) file to see the packages that need to be installed in your environment. 

Example: `pip install mido`

## Getting Started
Run the project with `python startup.py`

The console will print all your midi devices and then ask you to pick the port that your DDJ-FLX6 resides.
```
Input Ports:
DDJ-FLX6 0
Enter your DDJ-FLX6 Controller Port Number: 0
Gamepad Has Started
```

The console will now show you when you press a button that maps to a controller input. You can also uncomment [this line](https://github.com/KodiakTE/DJControllerToGamepad/blob/8b19a3910284b6239238aa2fbc3bb5def217f3c0/src/startup.py#L23) to see all the midi messages that the controller is sending.

Press the back button on the DJ contoller to exit the program

## Control Schematics
### Important: Left Midi pad must be set to `Hot Cue` and Right Midi pad must be set to `Sampler`

More Coming soon!