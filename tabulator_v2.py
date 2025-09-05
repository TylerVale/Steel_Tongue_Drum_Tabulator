import argparse
import pretty_midi

# Mapping from MIDI note names to drum numbers
note_to_number = {
    "C2": "1",
    "D2": "2",
    "E2": "3",
    "F2": "4",
    "G2": "5",
    "A2": "6",
    "B2": "7",
    "C3": "1·",
    "D3": "2·",
    "E3": "3·",
    "F3": "4·",
    "G3": "5·",
    "A3": "6·",
    "B3": "7·",
    "C4": "1··",
}

def midi_to_tabs(filename):
    """Convert a MIDI file into steel drum tabs."""
    midi = pretty_midi.PrettyMIDI(filename)

    melody = []
    for instrument in midi.instruments:
        if not instrument.is_drum:  # ignore percussion tracks
            for note in instrument.notes:
                pitch = pretty_midi.note_number_to_name(note.pitch)  # e.g. "C4"
                melody.append(pitch)

    # Map to tabs
    tabs = [note_to_number.get(n, "?") for n in melody]
    return melody, tabs

def format_tabs_by_bars(tabs, notes_per_bar=4, bars_per_line=4):
    """
    Format tabs into bars with measure numbers.
    - notes_per_bar: how many notes per bar (default 4)
    - bars_per_line: how many bars per printed line (default 4)
    """
    lines = []
    bar_count = 1

    for i in range(0, len(tabs), notes_per_bar * bars_per_line):
        chunk = tabs[i:i + notes_per_bar * bars_per_line]
        bars = []
        for j in range(0, len(chunk), notes_per_bar):
            bar_notes = chunk[j:j + notes_per_bar]
            bar_str = " | ".join(bar_notes)
            bars.append(f"[{bar_count}] {bar_str}")
            bar_count += 1
        lines.append(" || ".join(bars))  # double barline between groups of bars
    return "\n".join(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MIDI to Steel Drum Tabs")
    parser.add_argument("midi_file", help="Path to the MIDI file")
    parser.add_argument("-o", "--output", default="tabs.txt", help="Output file name")
    args = parser.parse_args()

    melody, tabs = midi_to_tabs(args.midi_file)

    formatted_tabs = format_tabs_by_bars(tabs, notes_per_bar=4, bars_per_line=4)

    # Write to text file
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(formatted_tabs)

    print(f"✅ Tabs written to {args.output}")
