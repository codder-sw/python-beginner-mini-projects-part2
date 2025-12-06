import os
# import the standard library module `os` which provides a way to use operating system
# services such as running shell/PowerShell commands. We will use os.system(...) below
# to invoke PowerShell text-to-speech from Python.

if __name__ == '__main__':
    # This conditional makes sure the following block runs only when this file is executed
    # directly (e.g., `python main.py`) and NOT when the file is imported as a module
    # into another Python script. `__name__` equals "__main__" only for direct execution.

    print("Welcome to Robospeaker 1.1 created by shivam")
    # Print a welcome message to the console so the user knows the program started.

    while True:
        # Start an infinite loop so the program keeps asking the user for text
        # until they explicitly request to quit (we break out of the loop below).

        x = input("Enter what you want me to pronounce (or 'q' to quit): ")
        # Read a line of text typed by the user from standard input and save it
        # in the variable `x`. input(...) prints the prompt and waits for the user.

        if x.lower() == "q":
            # Convert the user's input to lowercase and compare to "q".
            # This makes quitting case-insensitive: 'q', 'Q', 'q\n', etc. all work.
            break
            # Break exits the `while True` loop; the program will continue after the loop.

        command = f'powershell -Command "Add-Type -AssemblyName System.Speech; '\
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\');"'
        # Build a single string `command` that, when passed to os.system(...), runs
        # a PowerShell command to perform text-to-speech using .NET's System.Speech library.
        #
        # Explanation of the string structure:
        # - `powershell -Command " ... "` tells the shell to run a PowerShell command.
        # - `Add-Type -AssemblyName System.Speech;` loads the System.Speech assembly
        #    so we can use the SpeechSynthesizer class.
        # - `(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('...');`
        #    creates a SpeechSynthesizer object and calls its Speak() method with the
        #    text to speak. We put the Python string `x` inside the single quotes.
        #
        # Note: This form interpolates `{x}` directly into the command. If `x` contains
        # single quotes `'` or other special characters, the PowerShell parser may fail.
        # You should escape quotes in `x` (see discussion below).

        os.system(command)
        # os.system(...) executes the constructed command string in the underlying
        # operating system shell. On Windows this will invoke PowerShell and speak
        # the text. os.system returns the process exit code (we ignore it here).

    print("Thank you for using Robospeaker!")
    # After exiting the loop (user typed 'q'), print a closing message and the script ends.
