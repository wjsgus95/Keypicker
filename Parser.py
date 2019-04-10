from opcode_values import *

class Parser():
    def __init__(self, bytecode:str):
        self.bytecode = bytecode.lstrip('0x')

        # Original bytecode copy, just in case.
        self._bytecode = bytecode
        pass

    # Parse the whole bytecode.
    def parse_ops(self) -> list((int,int)):
        ops = list()
        while(len(self.bytecode)):
            op, operand, self.bytecode = int(self.bytecode[0:2],16), None, self.bytecode[2:]
            #import ipdb; ipdb.set_trace()
            if op >= PUSH1 and op <= PUSH32:
                operand_len = (op - (PUSH1 - 1)) * 2
                operand, self.bytecode = int(self.bytecode[0:operand_len], 16), self.bytecode[operand_len:]
            ops.append((op, operand)) 
        return ops

