import sys

PUSH = [0x5f + i for i in range(0x21)]

MSTORE = 0x52
MLOAD  = 0x51

SSTORE = 0x55
SLOAD  = 0x54

PC     = 0x58

bytecode = str()

def op(op, val = None):
    global bytecode

    def to_str_hex(arg):
        return hex(arg).lstrip('0x')

    bytecode += to_str_hex(op)
    if val != None:

        # fit the string val in the operation's value format
        # e.g. PUSH32 -> value must be a word (32 bytes -> 256 bit -> 64 hexes)
        #      then val should be 64 characters long hexadecimal digits
        if op in PUSH:
            zero_padded_len = PUSH.index(op) * 2
            assert len(str(val)) <= zero_padded_len
            val = to_str_hex(val).zfill(zero_padded_len)

        bytecode += val

if __name__ == "__main__":

    op(PUSH[32], 0x1010)
    op(PUSH[32], 0x1)
    op(SLOAD)
    op(PUSH[32], 0x1010)
    op(PUSH[32], 0x1)
    op(SSTORE)

    # to flush JSON trace
    op(PC)
    op(PC)

    print(bytecode)
    exit(0)
