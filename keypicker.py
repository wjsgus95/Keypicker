import json
import math

maximum=pow(2, 256)

with open('state.json') as json_file:
    json_data=json.load(json.file)

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

    else if op=="01":
        stack[0]=(stack[0]+stack[1])%maximum
        print("0x01 ADD")

    else if op=="02":
        stack[0]=(stack[0]*stack[1])%maximum
        print("0x02 MUL")

    else if op=="03":
        stack[0]=(stack[0]-stack[1])%maximum
        print("0x03 SUB")

    else if op=="04":
        if stack[1]==0:
            stack[0]=0
        else:
            stack[0]=(math.floor(stack[0]/stack[1]))%maximum
        print("0x04 DIV")

    else if op=="05":
        if stack[1]==0:
            stack[0]=0
        else if stack[0]==-maximum/2 and stack[1]==-1:
            stack[0]=-maximum/2
        else:
            stack[0]=abs((math.floor(stack[0]/stack[1])))%maximum
        print("0x05 SDIV")

    else if op=="06":
        if stack[1]==0:
            stack[0]=0
        else:
            stack[0]=stack[0]%stack[1]
        print("0x06 MOD")

    else if op=="07":
        if stack[1]==0:
            stack[0]=0
        else:
            stack[0]=abs(stack[0]%stack[1])
        print("0x07 SMOD")

    else if op=="08":
        if stack[2]==0:
            stack[0]=0
        else:
            stack[0]=(stack[0]+stack[1])%stack[2]
        print("0x08 ADDMOD")

    else if op=="09":
        if stack[2]==0:
            stack[0]=0
        else:
            stack[0]=(stack[0]*stack[1])%stack[2]
        print("0x09 MULMOD")

    else if op=="0a":
        stack[0]=pow(stack[0], stack[1])%maximum
        print("0x0a EXP")

    else if op=="0b":
        x=0b0
            
        

    i=i+2
    print("\tStack: ", stack)
    print("\tMemory: ", memory)
    print("\tStorage: ", storage)
    print("}\n")
