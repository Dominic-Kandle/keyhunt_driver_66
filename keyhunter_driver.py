import os
import spliter
import time
import random

hex_start_range = "0000000000000000000000000000000000000000000000020000000000000000"
hex_end_range = "000000000000000000000000000000000000000000000003ffffffffffffffff"
target_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"

int_start_range = int(hex_start_range, 16)
int_end_range = int(hex_end_range, 16)

segments = 100
threads = 2

range_list = spliter.rangeIntializer(int_start_range, int_end_range, segments)

index = 0


while(True):
    # index = random.randint(0, segments)

    if index > segments - 1:
         index = 0
   
    str_command = f"solver -m address -t {threads} -R -n 4096 -f puzzles\\66.txt -r {hex(range_list[index][0])[2:]}:{hex(range_list[index][1])[2:]} -l compress"
    os.system(str_command)
    os.system('\x03')
    os.system('cls')
    index += 1



