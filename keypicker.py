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
        #need to be done
        print("0x0b SIGNEXTEND")

    #Comparison and Bitwise Logic Ops
    elif op=="10":
        stack[0] = (stack[0]<stack[1]) if 1 else 0
        print("0x10 LT")

    elif op=="11":
        stack[0] = (stack[0]>stack[1]) if 1 else 0
        print("0x11 GT")

    elif op=="12":
        #signed LT
        print("0x12 SLT")

    elif op=="13":
        #signed GT
        print("0x13 SGT")

    elif op=="14":
        stack[0] = (stack[0]==stack[1]) if 1 else 0
        print("0x14 EQ")

    elif op=="15":
        stack[0] = (stack[0]==0) if 1 else 0
        print("0x15 ISZERO")

    elif op=="16":
        #bitwise AND
        print("0x16 AND")

    elif op=="17":
        #bitwise OR
        print("0x17 OR")

    elif op=="18":
        #bitwise XOR
        print("0x18 XOR")

    elif op=="19":
        #bitwise NOT
        print("0x19 NOT")

    elif op=="1a":
        #retrieve a byte
        print("0x1a BYTE")

    #SHA3
    elif op=="20":
        print("0x20 SHA3")

    #Environmental Information
    #need more information for all those opcodes....
    elif op=="30":
        print("0x30 ADDRESS")

    elif op=="31":
        print("0x31 BALANCE")

    elif op=="32":
        print("0x32 ORIGIN")

    elif op=="33":
        print("0x33 CALLER")

    elif op=="34":
        print("0x34 CALLVALUE")

    elif op=="35":
        print("0x35 CALLDATALOAD")

    elif op=="36":
        print("0x36 CALLDATASIZE")

    elif op=="37":
        #memory op
        print("0x37 CALLDATACOPY")

    elif op=="38":
        print("0x38 CODESIZE")

    elif op=="39":
        #memory op
        print("0x39 CODECOPY")

    elif op=="3a":
        print("0x3a CPDECOPY")

    elif op=="3b":
        print("0x3b EXTCODESIZE")

    elif op=="3c":
        #memory op
        print("0x3c EXTCODECOPY")

    elif op=="3d":
        print("0x3d RETURNDATASIZE")

    elif op=="3e":
        print("0x3e RETURNDATACOPY")

    #Block Information
    elif op=="40":
        #hash of one of the 256 most recent complete blocks
        print("0x40 BLOCKHASH")

    elif op=="41":
        print("0x41 COINBASE")

    elif op=="42":
        print("0x42 TIMESTAMP")

    elif op=="43":
        print("0x43 NUMBER")

    elif op=="44":
        print("0x44 DIFFICULTY")

    elif op=="45"
        print("0x45 GASLIMIT")

    #Stack, Memory, Storage and Flow Ops
    elif op=="50":
        print("0x50 POP")

    elif op=="20":
        print("0x20 SHA3")

    elif op=="51":
        print("0x51 MLOAD")

    elif op=="52":
        print("0x52 MSTORE")

    elif op=="53":
        print("0x53 MSTORE8")

    elif op=="54":
        stack[0]=storage[stack[0]]
        print("0x54 SLOAD")

    elif op=="55":
        print("0x55 SSTORE")

    elif op=="56":
        print("0x56 JUMP")

    elif op=="57":
        print("0x57 JUMPI")

    elif op=="58":
        print("0x58 PC")

    elif op=="59":
        print("0x59 MSIZE")

    elif op=="5a":
        print("0x5a GAS")

    elif op=="5b":
        #that's all
        print("0x5b JUMPDEST")

    #Push Ops
    elif op=="60":
        print("0x60 PUSH1")

    elif op=="61":
        print("0x61 PUSH2")

    elif op=="62":
        print("0x62 PUSH3")

    elif op=="63":
        print("0x63 PUSH4")

    elif op=="64":
        print("0x64 PUSH5")

    elif op=="65":
        print("0x65 PUSH6")

    elif op=="66":
        print("0x66 PUSH7")

    elif op=="67":
        print("0x67 PUSH8")

    elif op=="68":
        print("0x68 PUSH9")

    elif op=="69":
        print("0x69 PUSH10")

    elif op=="6a":
        print("0x6a PUSH11")

    elif op=="6b":
        print("0x6b PUSH12")

    elif op=="6c":
        print("0x6c PUSH13")

    elif op=="6d":
        print("0x6d PUSH14")

    elif op=="6e":
        print("0x6e PUSH15")

    elif op=="6f":
        print("0x6f PUSH16")

    elif op=="70":
        print("0x70 PUSH17")

    elif op=="71":
        print("0x71 PUSH18")

    elif op=="72":
        print("0x72 PUSH19")

    elif op=="73":
        print("0x73 PUSH20")

    elif op=="74":
        print("0x74 PUSH21")

    elif op=="75":
        print("0x75 PUSH22")

    elif op=="76":
        print("0x76 PUSH23")

    elif op=="77":
        print("0x77 PUSH24")

    elif op=="78":
        print("0x78 PUSH25")

    elif op=="79":
        print("0x79 PUSH26")

    elif op=="7a":
        print("0x7a PUSH27")

    elif op=="7b":
        print("0x7b PUSH28")

    elif op=="7c":
        print("0x7c PUSH29")

    elif op=="7d":
        print("0x7d PUSH30")

    elif op=="7e":
        print("0x7e PUSH31")

    elif op=="7f":
        print("0x7f PUSH32")

    #Duplication Ops
    elif op=="80":
        stack[0]=stack[0]
        print("0x80 DUP1")

    elif op=="81":
        stack[0]=stack[1]
        print("0x81 DUP2")

    elif op=="82":
        stack[0]=stack[2]
        print("0x82 DUP3")
        
    elif op=="83":
        stack[0]=stack[3]
        print("0x83 DUP4")
        
    elif op=="84":
        stack[0]=stack[4]
        print("0x84 DUP5")
        
    elif op=="85":
        stack[0]=stack[5]
        print("0x85 DUP6")

    elif op=="86":
        stack[0]=stack[6]
        print("0x86 DUP7")
        
    elif op=="87":
        stack[0]=stack[7]
        print("0x87 DUP8")
        
    elif op=="88":
        stack[0]=stack[8]
        print("0x88 DUP9")
        
    elif op=="89":
        stack[0]=stack[9]
        print("0x89 DUP10")
        
    elif op=="8a":
        stack[0]=stack[10]
        print("0x8a DUP11")
        
    elif op=="8b":
        stack[0]=stack[11]
        print("0x8b DUP12")
        
    elif op=="8c":
        stack[0]=stack[12]
        print("0x8c DUP13")
        
    elif op=="8d":
        stack[0]=stack[13]
        print("0x8d DUP14")
        
    elif op=="8e":
        stack[0]=stack[14]
        print("0x8e DUP15")
        
    elif op=="8f":
        stack[0]=stack[15]
        print("0x8f DUP16")
        
    #Exchange Ops
    elif op=="90":
        print("0x90 SWAP1")

    elif op=="91":
        stack[0], stack[1]=stack[1], stack[0]
        print("0x91 SWAP2")

    elif op=="92":
        stack[0], stack[2]=stack[2], stack[0]
        print("0x92 SWAP3")

    elif op=="93":
        stack[0], stack[3]=stack[3], stack[0]
        print("0x93 SWAP4")

    elif op=="94":
        stack[0], stack[4]=stack[4], stack[0]
        print("0x94 SWAP5")

    elif op=="95":
        stack[0], stack[5]=stack[5], stack[0]
        print("0x95 SWAP6")

    elif op=="96":
        stack[0], stack[6]=stack[6], stack[0]
        print("0x96 SWAP7")

    elif op=="97":
        stack[0], stack[7]=stack[7], stack[0]
        print("0x97 SWAP8")

    elif op=="98":
        stack[0], stack[8]=stack[8], stack[0]
        print("0x98 SWAP9")

    elif op=="99":
        stack[0], stack[9]=stack[9], stack[0]
        print("0x99 SWAP10")

    elif op=="9a":
        stack[0], stack[10]=stack[10], stack[0]
        print("0x9a SWAP11")

    elif op=="9b":
        stack[0], stack[11]=stack[11], stack[0]
        print("0x9b SWAP12")

    elif op=="9c":
        stack[0], stack[12]=stack[12], stack[0]
        print("0x9c SWAP13")

    elif op=="9d":
        stack[0], stack[13]=stack[13], stack[0]
        print("0x9d SWAP14")

    elif op=="9e":
        stack[0], stack[14]=stack[14], stack[0]
        print("0x9e SWAP15")

    elif op=="9f":
        stack[0], stack[15]=stack[15], stack[0]
        print("0x9f SWAP16")

    #Logging Ops
    #no need to do
    elif op=="a0":
        print("0xa0 LOG0")

    elif op=="a1":
        print("0xa1 LOG1")

    elif op=="a2":
        print("0xa2 LOG2")

    elif op=="a3":
        print("0xa3 LOG3")

    elif op=="a4":
        print("0xa4 LOG4")

    #System Ops
    elif op=="f0":
        print("0xf0 CREATE")

    elif op=="f1":
        print("0xf1 CALL")

    elif op=="f2":
        print("0xf2 CALLCODE")

    elif op=="f3":
        print("0xf3 RETURN")

    elif op=="f4":
        print("0xf4 DELETEGATECALL")

    elif op=="fa":
        print("0xfa STATICCALL")

    elif op=="fd":
        print("0xfd REVERT")

    elif op=="fe":
        #nothing
        print("0xfe INVALID")

    elif op=="ff":
        print("0xff SELFDESTRUCT")

    i=i+2
    print("\tStack: ", stack)
    print("\tMemory: ", memory)
    print("\tStorage: ", storage)
    print("}\n")
