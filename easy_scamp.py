# easy_scamp.py
#  Created：2026-03-19
#  Updated：2026-04-11
# Copyright (c) 2026 DreamFunction
# SPDX-License-Identifier: MIT

"""
easy_scamp - Convert human-friendly melodies to SCAMP-compatible format

This module provides a simple translate() function that converts a list
containing note names, rests, and durations (with dotted and additive syntax)
into a list of (MIDI pitch, seconds) tuples required by SCAMP.

Example:
    >>> from easy_scamp import translate
    >>> melody = [('C4', 4), ('E4', 4), ('G4', 4), ('r', 2)]
    >>> data = translate(melody, bpm=120)
    >>> print(data)
    [(60, 0.5), (64, 0.5), (67, 0.5), (None, 1.0)]
"""

__version__ = '0.1.0'
__all__ = ['__all__','__version__','DEFAULT','NOTES_MAP','translate','translate_dot','translate_duration','translate_note','translate_tie']

DEFAULT = 'translate'
NOTES_MAP = {
    'C0': 12, 'C#0': 13, 'D0': 14, 'D#0': 15, 'E0': 16, 'F0': 17, 'F#0': 18, 'G0': 19, 'G#0': 20, 'A0': 21, 'A#0': 22, 'B0': 23,
    'C1': 24, 'C#1': 25, 'D1': 26, 'D#1': 27, 'E1': 28, 'F1': 29, 'F#1': 30, 'G1': 31, 'G#1': 32, 'A1': 33, 'A#1': 34, 'B1': 35,
    'C2': 36, 'C#2': 37, 'D2': 38, 'D#2': 39, 'E2': 40, 'F2': 41, 'F#2': 42, 'G2': 43, 'G#2': 44, 'A2': 45, 'A#2': 46, 'B2': 47,
    'C3': 48, 'C#3': 49, 'D3': 50, 'D#3': 51, 'E3': 52, 'F3': 53, 'F#3': 54, 'G3': 55, 'G#3': 56, 'A3': 57, 'A#3': 58, 'B3': 59,
    'C4': 60, 'C#4': 61, 'D4': 62, 'D#4': 63, 'E4': 64, 'F4': 65, 'F#4': 66, 'G4': 67, 'G#4': 68, 'A4': 69, 'A#4': 70, 'B4': 71,
    'C5': 72, 'C#5': 73, 'D5': 74, 'D#5': 75, 'E5': 76, 'F5': 77, 'F#5': 78, 'G5': 79, 'G#5': 80, 'A5': 81, 'A#5': 82, 'B5': 83,
    'C6': 84, 'C#6': 85, 'D6': 86, 'D#6': 87, 'E6': 88, 'F6': 89, 'F#6': 90, 'G6': 91, 'G#6': 92, 'A6': 93, 'A#6': 94, 'B6': 95,
    'C7': 96, 'C#7': 97, 'D7': 98, 'D#7': 99, 'E7': 100, 'F7': 101, 'F#7': 102, 'G7': 103, 'G#7': 104, 'A7': 105, 'A#7': 106, 'B7': 107,
    'C8': 108, 'C#8': 109, 'D8': 110, 'D#8': 111, 'E8': 112, 'F8': 113, 'F#8': 114, 'G8': 115, 'G#8': 116, 'A8': 117, 'A#8': 118, 'B8': 119,

    'c0': 12, 'c#0': 13, 'd0': 14, 'd#0': 15, 'e0': 16, 'f0': 17, 'f#0': 18, 'g0': 19, 'g#0': 20, 'a0': 21, 'a#0': 22, 'b0': 23,
    'c1': 24, 'c#1': 25, 'd1': 26, 'd#1': 27, 'e1': 28, 'f1': 29, 'f#1': 30, 'g1': 31, 'g#1': 32, 'a1': 33, 'a#1': 34, 'b1': 35,
    'c2': 36, 'c#2': 37, 'd2': 38, 'd#2': 39, 'e2': 40, 'f2': 41, 'f#2': 42, 'g2': 43, 'g#2': 44, 'a2': 45, 'a#2': 46, 'b2': 47,
    'c3': 48, 'c#3': 49, 'd3': 50, 'd#3': 51, 'e3': 52, 'f3': 53, 'f#3': 54, 'g3': 55, 'g#3': 56, 'a3': 57, 'a#3': 58, 'b3': 59,
    'c4': 60, 'c#4': 61, 'd4': 62, 'd#4': 63, 'e4': 64, 'f4': 65, 'f#4': 66, 'g4': 67, 'g#4': 68, 'a4': 69, 'a#4': 70, 'b4': 71,
    'c5': 72, 'c#5': 73, 'd5': 74, 'd#5': 75, 'e5': 76, 'f5': 77, 'f#5': 78, 'g5': 79, 'g#5': 80, 'a5': 81, 'a#5': 82, 'b5': 83,
    'c6': 84, 'c#6': 85, 'd6': 86, 'd#6': 87, 'e6': 88, 'f6': 89, 'f#6': 90, 'g6': 91, 'g#6': 92, 'a6': 93, 'a#6': 94, 'b6': 95,
    'c7': 96, 'c#7': 97, 'd7': 98, 'd#7': 99, 'e7': 100, 'f7': 101, 'f#7': 102, 'g7': 103, 'g#7': 104, 'a7': 105, 'a#7': 106, 'b7': 107,
    'c8': 108, 'c#8': 109, 'd8': 110, 'd#8': 111, 'e8': 112, 'f8': 113, 'f#8': 114, 'g8': 115, 'g#8': 116, 'a8': 117, 'a#8': 118, 'b8': 119,
}

def translate_dot(dur,bpm=120,wnote=4):
    """
    def translate_dot(dur, bpm=120, wnote=4):
    
    Convert a dotted duration string (e.g., '4.') to seconds.
    
    Args:
        dur: Dotted duration string, e.g., '4.' for dotted quarter note
        bpm: Beats per minute
        wnote: Number of beats per whole note (default 4 for 4/4 time)
    
    Returns:
        Seconds corresponding to the dotted duration
    
    Raises:
        TypeError: Invalid format (not a digit followed by '.')
        ValueError: Duration <= 0
    """
    if not dur[:-1].isdigit():
        raise TypeError("Duration string must be digits followed by '.'")
    if float(dur[:-1])<=0:
        raise ValueError("Duration must be greater than zero")

    return (wnote)*(1/(float(dur[:-1])))*1.5*(60/(bpm))

def translate_duration(dur,bpm=120,wnote=4):
    """
    def translate_duration(dur, bpm=120, wnote=4):

    Convert a plain numeric duration to seconds.
    
    Args:
        dur: Numeric duration, e.g., 4 for quarter note (relative to whole note)
        bpm: Beats per minute
        wnote: Number of beats per whole note (default 4)
    
    Returns:
        Seconds corresponding to the duration
    
    Raises:
        TypeError: dur is not a number
        ValueError: dur <= 0
    """
    if not isinstance(dur,(int,float)):
        raise TypeError("Duration must be a number")
    if dur<=0:
        raise ValueError("Duration must be greater than zero")
    
    return (wnote)*(1/(dur))*(60/(bpm))

def translate_note(note):
    """
    def translate_note(note):

    Convert a note name to MIDI pitch number; returns None for rests.
    
    Args:
        note: Note name (e.g., 'C4', 'c4', 'F#3'), or 'r'/'R'/None for rest, or MIDI number
    
    Returns:
        MIDI pitch number, or None (rest)
    
    Raises:
        ValueError: Input is not a string, number, or None
        KeyError: Note name not found in mapping
    """
    if note=='r' or note=='R' or note==None:
        return None

    if not isinstance(note,(str,int,float)):
        raise ValueError("Note name must be a string, number, or None")

    result = NOTES_MAP.get(note)
    if result==None:
        raise KeyError("Note name not found")
    else:
        return result

def translate_tie(dur,bpm=120,wnote=4):
    """
    def translate_tie(dur, bpm=120, wnote=4):

    Parse an additive duration string (e.g., '2+2+4') and return total seconds.
    
    Args:
        dur: Addition expression string, parts separated by '+', each part can be plain number or dotted string
        bpm: Beats per minute
        wnote: Number of beats per whole note
    
    Returns:
        Total seconds
    
    Raises:
        ValueError: Empty expression, consecutive '+', leading/trailing '+', or invalid part
    """
    dlist = dur.split('+')
    total_dur = 0
    for i in dlist:
        if i=='':
            raise ValueError("Invalid tie expression: consecutive '+', leading/trailing '+'")
        if not i.isdigit() and not i.endswith('.') :
            raise ValueError("Duration string must be a number or dotted (e.g., '4.')")
        if float(i)<=0:
            raise ValueError("Duration must be greater than zero")

        if i.endswith('.'):
            total_dur += translate_dot(i,bpm=bpm,wnote=wnote)
        elif i.isdigit():
            total_dur += translate_duration(float(i),bpm=bpm,wnote=wnote)
    return total_dur

def translate(mlist,bpm=120,wnote=4):
    """
    def translate(mlist, bpm=120, wnote=4):

    Convert a human-friendly melody list to a SCAMP-compatible (MIDI pitch, seconds) list.
    
    Args:
        mlist: List of (note, duration) tuples
            note: 'C4', 'c4', 'F#3', 'r', 'R', None, or MIDI number
            duration: number (4=quarter, 8=eighth) or string ('4.'=dotted, '2+2+4'=additive)
        bpm: Beats per minute, default 120
        wnote: Beats per whole note, default 4 (4/4 time)
    
    Returns:
        List of [(midi, seconds), ...], with None for rests
    
    Raises:
        TypeError: Invalid input type
        ValueError: Invalid duration or tuple length not 2
        KeyError: Unknown note name
    """
    if not isinstance(mlist,list):
        raise TypeError("Music list must be a list")
    if not isinstance(bpm,(int,float)):
        raise TypeError("bpm must be a number")
    if not isinstance(wnote,(int,float)):
        raise TypeError("wnote must be a number")
    
    result = []
    for i in range(len(mlist)):
        if not isinstance(mlist[i],tuple):
            raise TypeError("Each element of music list must be a tuple")
        if len(mlist[i])!=2:
            raise ValueError("Each tuple must have length 2 (note, duration)")

        result.append([0,0])

        if isinstance(mlist[i][0],(int,float)):
            result[i][0] = mlist[i][0]
        elif isinstance(mlist[i][0],str):
            result[i][0] = translate_note(mlist[i][0])

        if isinstance(mlist[i][1],(int,float)):
            result[i][1] = translate_duration(mlist[i][1],bpm=bpm,wnote=wnote)
        elif isinstance(mlist[i][1],str):
            if mlist[i][1].endswith('.'):
                result[i][1] = translate_dot(mlist[i][1],bpm=bpm,wnote=wnote)
            elif '+' in mlist[i][1]:
                result[i][1] = translate_tie(mlist[i][1],bpm=bpm,wnote=wnote)
            else:
                raise ValueError("Invalid duration string")
        
        result[i] = tuple(result[i])
    return result
