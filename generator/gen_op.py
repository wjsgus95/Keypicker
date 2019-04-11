import sys
from opcode_values import *

bytecode = str()

def op(op, val = None):
    global bytecode

    def to_str_hex(arg):
        return hex(arg).lstrip('0x').zfill(2)

    bytecode += to_str_hex(op)
    if val != None:

        # fit the string val in the operation's value format
        # e.g. PUSH32 -> value must be a word (32 bytes -> 256 bit -> 64 hexes)
        #      then val should be 64 characters long hexadecimal digits
        PUSH = [i for i in range(PUSH1, PUSH32+1)]
        if op in PUSH:
            zero_padded_len = (op - (PUSH1 - 1)) * 2
            #assert len(str(val)) <= zero_padded_len
            val = to_str_hex(val).zfill(zero_padded_len)

        bytecode += val

if __name__ == "__main__":

    #op(PUSH1, 0x10)
    op(PUSH32, 0x10)
    op(PUSH32, 0x15)
    op(ADD)
    #op(PUSH32, 0x1010)
    #op(SIGNEXTEND)
    #op(CREATE)
    #op(ADDRESS)
    #op(BALANCE)
    #op(CODESIZE)

    # to flush JSON trace
    op(CODESIZE)
    op(SUB)
    op(PC)

    op(ADD)
    op(SDIV)

    print(bytecode)
    exit(0)
