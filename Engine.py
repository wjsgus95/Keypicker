from opcode_values import *
from constants import *

import math

class Engine():
    def __init__(self, json_data) -> None:
        self.bytecode=str(json_data["bytecode"])
        self.stack_data=json_data["stack"]
        self.memory_data=json_data["memory"]
        self.storage_data=json_data["storage"]

        self.stack = list()
        self.memory = 0x00
        self.storage = dict()

        self.op_dict = dict()

    # Configure operation dictionary.
    def configure_op_dict(self) -> None:

        ## Clear operation queue.
        #self.op_dict[STOP] = lambda operand: self.op_queue.clear()

        ## Confiure arithmetic operations.
        #self.op_dict[ADD] = lambda operand: stack[0]=(stack[0]+stack[1])%maximum
        #self.op_dict[MUL] = lambda operand: stack[0]=(stack[0]*stack[1])%maximum
        #self.op_dict[SUB] = lambda operand: stack[0]=(stack[0]-stack[1])%maximum
        #self.op_dict[DIV] = lambda operand: stack[0] = 0 if stack[1] == 0 else stack[0]=(math.floor(stack[0]/stack[1]))%maximum)
        #self.op_dict[SDIV] = lambda operand: 
        #self.op_dict[MOD] = lambda operand: 
        #self.op_dict[SMOD] = lambda operand: 
        #self.op_dict[ADDMOD] = lambda operand: 
        #self.op_dict[MULMOD] = lambda operand: 
        #self.op_dict[EXP] = lambda operand: 
        #self.op_dict[SIGEXTEND] = lambda operand: 

        ## Configure logic operations.
        #self.op_dict[LT] = lambda operand: 
        #self.op_dict[GT] = lambda operand: 
        #self.op_dict[SLT] = lambda operand: 
        #self.op_dict[SGT] = lambda operand: 
        #self.op_dict[EQ] = lambda operand: 
        #self.op_dict[ISZERO] = lambda operand: 
        #self.op_dict[AND] = lambda operand: 
        #self.op_dict[OR] = lambda operand: 
        #self.op_dict[XOR] = lambda operand: 
        #self.op_dict[NOT] = lambda operand: 
        #self.op_dict[BYTE] = lambda operand: 
        #self.op_dict[SHL] = lambda operand: 
        #self.op_dict[SHR] = lambda operand: 
        #self.op_dict[SAR] = lambda operand: 

        ## Configure PUSH operations.
        #for PUSH in range(PUSH1, PUSH32+1):
        #    self.op_dict[PUSH] = lambda operand: self.stack.insert(0, operand)

    def run_ops(self, op_queue) -> None:
        self.op_queue = op_queue
        while len(self.op_queue):
            op, operand = op_queue.pop()
            self.run_single_op(op, operand)

    def run_single_op(self, op, operand) -> None:
        #self.op_dict[op](operand)
        if op==STOP:
            print("0x00 STOP")
            print("\tStack: ", stack)
            print("\tMemory: ", memory)
            print("\tStorage: ", storage)
            print("}\n")
            break

        elif op==ADD:
            stack[0]=(stack[0]+stack[1])%maximum
            print("0x01 ADD")

        elif op==MUL:
            stack[0]=(stack[0]*stack[1])%maximum
            print("0x02 MUL")

        elif op==SUB:
            stack[0]=(stack[0]-stack[1])%maximum
            print("0x03 SUB")

        elif op==DIV:
            if stack[1]==0:
                stack[0]=0
            else:
                stack[0]=(math.floor(stack[0]/stack[1]))%maximum
            print("0x04 DIV")

        elif op==SDIV:
            if stack[1]==0:
                stack[0]=0
            elif stack[0]==-maximum/2 and stack[1]==-1:
                stack[0]=-maximum/2
            else:
                stack[0]=abs((math.floor(stack[0]/stack[1])))%maximum
            print("0x05 SDIV")

        elif op==MOD:
            if stack[1]==0:
                stack[0]=0
            else:
                stack[0]=stack[0]%stack[1]
            print("0x06 MOD")

        elif op==SMOD:
            if stack[1]==0:
                stack[0]=0
            else:
                stack[0]=abs(stack[0]%stack[1])
            print("0x07 SMOD")

        elif op==ADDMOD:
            if stack[2]==0:
                stack[0]=0
            else:
                stack[0]=(stack[0]+stack[1])%stack[2]
            print("0x08 ADDMOD")

        elif op==MULMOD:
            if stack[2]==0:
                stack[0]=0
            else:
                stack[0]=(stack[0]*stack[1])%stack[2]
            print("0x09 MULMOD")

        elif op==EXP:
            stack[0]=pow(stack[0], stack[1])%maximum
            print("0x0a EXP")

        elif op==SIGNEXTEND:
            #need to be done
            print("0x0b SIGNEXTEND")

        #Comparison and Bitwise Logic Ops
        elif op==LT:
            stack[0] = (stack[0]<stack[1]) if 1 else 0
            print("0x10 LT")

        elif op==GT:
            stack[0] = (stack[0]>stack[1]) if 1 else 0
            print("0x11 GT")

        elif op==SLT:
            #signed LT
            print("0x12 SLT")

        elif op==SGT:
            #signed GT
            print("0x13 SGT")

        elif op==EQ:
            stack[0] = (stack[0]==stack[1]) if 1 else 0
            print("0x14 EQ")

        elif op==ISZERO:
            stack[0] = (stack[0]==0) if 1 else 0
            print("0x15 ISZERO")

        elif op==AND:
            #bitwise AND
            print("0x16 AND")

        elif op==OR:
            #bitwise OR
            print("0x17 OR")

        elif op==XOR:
            #bitwise XOR
            print("0x18 XOR")

        elif op==NOT:
            #bitwise NOT
            print("0x19 NOT")

        elif op==BYTE:
            #retrieve a byte
            print("0x1a BYTE")

        #SHA3
        elif op==SHA3:
            print("0x20 SHA3")

        #Environmental Information
        #need more information for all those opcodes....
        elif op==ADDRESS:
            print("0x30 ADDRESS")

        elif op==BALANCE:
            print("0x31 BALANCE")

        elif op==ORIGIN:
            print("0x32 ORIGIN")

        elif op==CALLER:
            print("0x33 CALLER")

        elif op==CALLVALUE:
            print("0x34 CALLVALUE")

        elif op==CALLDATALOAD:
            print("0x35 CALLDATALOAD")

        elif op==CALLDATASIZE:
            print("0x36 CALLDATASIZE")

        elif op==CALLDATACOPY:
            #memory op
            print("0x37 CALLDATACOPY")

        elif op==CODESIZE:
            print("0x38 CODESIZE")

        elif op==CODECOPY:
            #memory op
            print("0x39 CODECOPY")

        elif op==GASPRICE:
            print("0x3a GASPRICE")

        elif op==EXTCODESIZE:
            print("0x3b EXTCODESIZE")

        elif op==EXTCODECOPY:
            #memory op
            print("0x3c EXTCODECOPY")

        elif op==RETURNDATASIZE:
            print("0x3d RETURNDATASIZE")

        elif op==RETURNDATACOPY:
            print("0x3e RETURNDATACOPY")

        #Block Information
        elif op==BLOCKHASH:
            #hash of one of the 256 most recent complete blocks
            print("0x40 BLOCKHASH")

        elif op==COINBASE:
            print("0x41 COINBASE")

        elif op==TIMESTAMP:
            print("0x42 TIMESTAMP")

        elif op==NUMBER:
            print("0x43 NUMBER")

        elif op==DIFFICULTY:
            print("0x44 DIFFICULTY")

        elif op==GASLIMIT:
            print("0x45 GASLIMIT")

        #Stack, Memory, Storage and Flow Ops
        elif op==POP:
            print("0x50 POP")

        elif op==MLOAD:
            print("0x51 MLOAD")

        elif op==MSTORE:
            print("0x52 MSTORE")

        elif op==MSTORE8:
            print("0x53 MSTORE8")

        elif op==SLOAD:
            stack[0]=storage[stack[0]]
            print("0x54 SLOAD")

        elif op==SSTORE:
            print("0x55 SSTORE")

        elif op==JUMP:
            print("0x56 JUMP")

        elif op==JUMPI:
            print("0x57 JUMPI")

        elif op==PC:
            print("0x58 PC")

        elif op==MSIZE:
            print("0x59 MSIZE")

        elif op==GAS:
            print("0x5a GAS")

        elif op==JUMPDEST:
            #that's all
            print("0x5b JUMPDEST")

        #Push Ops
        elif op >= PUSH1 and op <= PUSH32:
            print("PUSH")
        """
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
        """

        #Duplication Ops
        elif op >= DUP1 and op <= DUP16:
            print("DUP")
        """
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
        """

        #Exchange Ops
        elif op >= SWAP1 and op <= SWAP16:
            print("SWAP")
        """
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
        """

        #Logging Ops
        #no need to do
        elif op==LOG0:
            print("0xa0 LOG0")

        elif op==LOG1:
            print("0xa1 LOG1")

        elif op==LOG2:
            print("0xa2 LOG2")

        elif op==LOG3:
            print("0xa3 LOG3")

        elif op==LOG4:
            print("0xa4 LOG4")

        #System Ops
        elif op==CREATE:
            print("0xf0 CREATE")

        elif op==CALL:
            print("0xf1 CALL")

        elif op==CALLCODE:
            print("0xf2 CALLCODE")

        elif op==RETURN:
            print("0xf3 RETURN")

        elif op==DELEGATECALL:
            print("0xf4 DELETEGATECALL")

        elif op==STATICCALL:
            print("0xfa STATICCALL")

        elif op==REVERT:
            print("0xfd REVERT")

        elif op==0xfe:
            #nothing
            print("0xfe INVALID")

        elif op==SELFDESTRUCT:
            print("0xff SELFDESTRUCT")


    