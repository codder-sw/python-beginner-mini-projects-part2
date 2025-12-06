import os

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 created by shivam")

    while True:
        x = input("Enter what you want me to pronounce (or 'q' to quit): ")

        if x.lower() == "q":
            break

        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; '\
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'

        os.system(command)

    print("Thank you for using Robospeaker!")
