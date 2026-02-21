import time
import re
from pynput.keyboard import Controller

keyboard = Controller()

# --- CONFIGURATION ---
BPM = 220  #change this to change its speed most of the song is between 110 to 220
BEAT = 60 / (BPM * 2) 

def play_sheet(sheet):
    # 1. Clean the sheet
    sheet = sheet.replace('|', '').replace('\n', ' ')
    
    # 2. Tokenizer
    tokens = re.findall(r'\[.*?\]|\(.*?\)|[^_ ]', sheet)
    
    print(" Switch windows NOW!")
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # --- HANDLE CHORDS ---
        if token.startswith('[') or token.startswith('('):
            content = token[1:-1]
            for char in content:
                if char != ' ': keyboard.press(char)
            
            time.sleep(0.03) # Reduced hold time for speed
            
            for char in content:
                if char != ' ': keyboard.release(char)
                    
        # --- HANDLE DASHES ---
        elif token == '-':
            time.sleep(BEAT)

        # --- HANDLE SINGLE NOTES ---
        else:
            hold_multiplier = 1
            temp_i = i + 1
            while temp_i < len(tokens) and tokens[temp_i] == '-':
                hold_multiplier += 1
                temp_i += 1
            
            try:
                keyboard.press(token)
                time.sleep(0.03 * hold_multiplier) # Reduced hold time for speed
                keyboard.release(token)
            except:
                pass

        # Small gap between tokens
        time.sleep(BEAT)
        i += 1

# --- YOUR MUSIC SHEET ---
my_sheet = """

"""

if __name__ == "__main__":
    print("Starting in 5 seconds...")
    time.sleep(5)
    play_sheet(my_sheet)
