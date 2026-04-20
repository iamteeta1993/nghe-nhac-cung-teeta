import random
import os
from midiutil import MIDIFile

# Đường dẫn Desktop
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
full_path = os.path.join(desktop_path, "nhac_co_hop_am.mid")

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(0, 0, 100) # Nhịp chậm lại cho chill

# Các hợp âm cơ bản (C, Am, F, G)
chords = [
    [60, 64, 67], # C Major
    [57, 60, 64], # A Minor
    [53, 57, 60], # F Major
    [55, 59, 62]  # G Major
]

print("--- Đang tạo nhạc có hợp âm... ---")

time = 0
for _ in range(8): # Tạo 8 vòng hợp âm
    current_chord = random.choice(chords)
    
    # Đánh 3 nốt của hợp âm cùng lúc
    for pitch in current_chord:
        MyMIDI.addNote(0, 0, pitch, time, 4, 80) # Mỗi hợp âm ngân dài 4 nhịp
    
    time += 4

with open(full_path, "wb") as output_file:
    MyMIDI.writeFile(output_file)

print(f"Xong! Ra Desktop nghe file 'nhac_co_hop_am.mid' xem có khác bọt không nhé!")


