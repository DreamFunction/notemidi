# notemidi

Language:
* English
* 中文 请查看[README.zh.md](README.zh.md)。

This project is synchronized across Gitee, GitHub, and GitCode.  
(Gitee username: dream-function; GitHub/GitCode username: dreamfunction)

#### Introduction

**A lightweight tool library for converting human-friendly music notation to MIDI data.**

notemidi allows you to write music in the most natural way: `('C4', 4)` represents a C4 (MIDI 60) quarter note. It translates this "text notation" into MIDI‑ready data (pitch number + duration in seconds).

##### ✨ Core Features

- **Text notation**: `('C4', 4)` for a quarter note C4
- **Dotted notes**: `'4.'` for a dotted quarter note
- **Rests**: `'r'` or `None`
- **Additive durations**: `'2+2+4'` sums to 8 beats

##### 📦 Relationship with MIDI Libraries

notemidi is **not** another MIDI I/O library (like `mido`, `python-rtmidi`). Instead it:

- Focuses on the "human input" layer
- Outputs standardised `(pitch, duration)` data that can be consumed by any MIDI or audio library

#### Installation

`pip install notemidi` or copy the code directly into your project.

#### Usage

**The core function of this module is `translate`** (for most use cases, other functions are not needed). You can also find a `DEFAULT` constant inside the module whose value is `'translate'`.

```python
def translate(mlist, bpm=120, wnote=4):
    """
    Convert a human‑friendly melody list to a list of (MIDI pitch, seconds).
    
    Parameters:
        mlist: List of (note_name, duration) tuples
            note_name: 'C4', 'c4', 'F#3', 'r', 'R', None, or a MIDI number
            duration: number (4=quarter, 8=eighth) or string ('4.'=dotted, '2+2+4'=additive)
        bpm: Beats per minute, default 120
        wnote: Beats per whole note, default 4 (i.e. 4/4 time)
    
    Returns:
        List of [(midi, seconds), ...]; rests are represented as None for the pitch.
    
    Raises:
        TypeError: invalid input type
        ValueError: invalid duration or tuple length not 2
        KeyError: unknown note name
    """

#### Appendix(Other Functions)

def translate_dot(dur, bpm=120, wnote=4):
    """
    Convert a dotted duration string (e.g., '4.') to seconds.
    
    Parameters:
        dur: dotted duration string (e.g., '4.' for dotted quarter note)
        bpm: beats per minute
        wnote: beats per whole note (default 4)
    
    Returns:
        Corresponding duration in seconds.
    
    Raises:
        TypeError: invalid format (not a digit followed by '.')
        ValueError: duration <= 0
    """

def translate_duration(dur, bpm=120, wnote=4):
    """
    Convert a plain numeric duration (e.g., 4) to seconds.
    
    Parameters:
        dur: numeric duration (e.g., 4 for quarter note, relative to whole note)
        bpm: beats per minute
        wnote: beats per whole note (default 4)
    
    Returns:
        Corresponding duration in seconds.
    
    Raises:
        TypeError: dur is not a number
        ValueError: dur <= 0
    """

def translate_note(note):
    """
    Convert a note name to MIDI pitch number; return None for rests.
    
    Parameters:
        note: note name ('C4', 'c4', 'F#3'), 'r'/'R'/None for rest, or a MIDI number
    
    Returns:
        MIDI pitch number, or None (rest).
    
    Raises:
        ValueError: input is not a string, number, or None
        KeyError: note name not found in mapping table
    """

def translate_tie(dur, bpm=120, wnote=4):
    """
    Parse an additive duration string (e.g., '2+2+4') and return total seconds.
    
    Parameters:
        dur: additive expression string, parts separated by '+',
             each part can be a plain number or a dotted string
        bpm: beats per minute
        wnote: beats per whole note
    
    Returns:
        Total duration in seconds.
    
    Raises:
        ValueError: empty expression, consecutive '+', leading/trailing '+', or invalid part
    """

#### Contributing

Issues and Pull Requests are welcome.
