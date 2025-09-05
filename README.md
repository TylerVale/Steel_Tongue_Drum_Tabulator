# Steel_Tongue_Drum_Tabulator
A simple program to convert MIDI files into tabs for a cheap steel tongue drum, but may work for other instruments as well. From a MIDI input, the program will output numbered musical notation/jianpu. I am not a musician and I don't know whether numbered musical notation is universal across all labeled instruments or what. I used the booklets that came with a cheap steel tongue drum to create the tables that this program is based on.

Requires PrettyMIDI (pip install mido pretty_midi)

Instructions:

Program accepts a MIDI file as an argument from the command line 
* Create tabulator.py
* Place MIDI file of choosing in same directory 
* From CLI: python tabulator.py your_midi_file.mid
* Outputs the results in a .txt file

