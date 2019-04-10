from opcode_values import *

class Parser():
    def __init__(bytecode:str):
        self.bytecode = bytecode

        # Original bytecode copy, just in case.
        self._bytecode = bytecode
        pass

    def parse_ops() -> list((int,int)):
        ops = list()
        while(len(self.bytecode)):
            op, operand, self.bytecode = int(self.bytecode[0:2]), -1, self.bytecode[2:]
            if op >= PUSH1 and op <= PUSH32:
                operand_len = (op - (PUSH1 - 1)) * 2
                operand, self.bytecode = int(self.bytecode[0:operand_len]), self.bytecode[opreand_len:]
            ops.append((op, operand)) 
        return ops

