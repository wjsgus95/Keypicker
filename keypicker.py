import json
import math
import sys
import argparse

# Default output file path.
output_file_path='result.stats'

# Argparse initialized.
parser = argparse.ArgumentParser(description = \
        "Keypicker, transaction replay from EVM execution trace")
# Input file path positional(required) argument.
parser.add_argument('input_trace', type=str, help='Input JSON trace file')
# Output file path optional.
parser.add_argument('--dest', type=str, help=f'Output stats file path, defaults to {output_file_path}',
                    nargs=1, default=output_file_path)
args = parser.parse_args()

# Override output file path if any given.
output_file_path = args.dest

maximum=pow(2, 256)

#with open('state.json') as json_file:
#    json_data=json.load(json.file)
with open(args.input_trace) as json_file:
    json_data=json.load(json_file)

bytecode=str(json_data["bytecode"])
stack_data=json_data["stack"]
memory_data=json_data["memory"]
storage_data=json_data["storage"]

l=len(bytecode)
i=2
stack=[]
memory=0x0
storage={}
while i<l:
    op=bytecode[i]+bytecode[i+1]
    print("{")
    
    if op=="00":
        print("0x00 STOP")
        print("\tStack: ", stack)
        print("\tMemory: ", memory)
        print("\tStorage: ", storage)
        print("}\n")
        break

    elif op=="01":
        stack[0]=(stack[0]+stack[1])%maximum
        print("0x01 ADD")

    elif op=="02":
        stack[0]=(stack[0]*stack[1])%maximum
        print("0x02 MUL")

    elif op=="03":
        stack[0]=(stack[0]-stack[1])%maximum
        print("0x03 SUB")

    elif op=="04":
        if stack[1]==0:
            stack[0]=0
        else:
            stack[0]=(math.floor(stack[0]/stack[1]))%maximum
        print("0x04 DIV")

    elif op=="05":
        if stack[1]==0:
            stack[0]=0
        elif stack[0]==-maximum/2 and stack[1]==-1:
            stack[0]=-maximum/2
        else:
            stack[0]=abs((math.floor(stack[0]/stack[1])))%maximum
        print("0x05 SDIV")

    elif op=="06":
        if stack[1]==0:
            stack[0]=0
        else:
            stack[0]=stack[0]%stack[1]
        print("0x06 MOD")

    elif op=="07":
        if stack[1]==0:
            stack[0]=0
        else:
            stack[0]=abs(stack[0]%stack[1])
        print("0x07 SMOD")

    elif op=="08":
        if stack[2]==0:
            stack[0]=0
        else:
            stack[0]=(stack[0]+stack[1])%stack[2]
        print("0x08 ADDMOD")

    elif op=="09":
        if stack[2]==0:
            stack[0]=0
        else:
            stack[0]=(stack[0]*stack[1])%stack[2]
        print("0x09 MULMOD")

    elif op=="0a":
        stack[0]=pow(stack[0], stack[1])%maximum
        print("0x0a EXP")

    elif op=="0b":
        x=0b0
            
        

    i=i+2
    print("\tStack: ", stack)
    print("\tMemory: ", memory)
    print("\tStorage: ", storage)
    print("}\n")
