"""
Learning Goals
Getting acquainted with Python's documentation 
for dict.
"""

SONG_RESULT = {"Bubble dancer": 93.4, "The Game": 92.03, "Vertex": 75.3,
               "Lemmings on the Run": 86.2, "Da Roots": 96.02,
               "Charlene": 75.3, "Disconnected": 86.3, "Fly away": 87.32,
               "Hybrid": 63.9, "My favourite game": 89.45, "Oasis": 59.5,
               "Remember December": 96.3, "The beginning": 90.45,
               "Tribal Style": 87.45, "Why Me": 97.38, "Xuxa": 63.84,
               "Zodiac": 83.43, "Queen of Light": 75.12, "Mouth": 98.34,
               "Pandemonium": 79.31}

def calculate_average(song_result = SONG_RESULT):

    song_time = list(song_result.values())
    total_time = 0
    for time in song_time:
        total_time += time
    time_ave = total_time/(len(song_time))
    #print(time_ave)
    return time_ave
        
def main():

    time_ave = calculate_average()
    print(time_ave)
    
if __name__ == "__main__":
    main()
