import mido

class FindMidiPort:
    def findPort(self) -> str:
        print("Input Ports:")
        for port in mido.get_input_names():
            print(port)

        portNumber = input("Enter your DDJ-FLX6 Controller Port Number:")
        try:
            portNumber = int(portNumber)
        except:
            print(f"{portNumber} is not a valid Number")

        return mido.get_input_names()[portNumber]