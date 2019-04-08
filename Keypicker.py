from define import *

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


class Keypicker():
    def __init__(self, m_bytecode=""):
        bytecode = m_bytecode
        pass

    def init(json):
        pass

    def run():
        pass


if __name__ == "__main__":
    #keypicker = Keypicker(...)
    #keypicker.init(...)
    #keypicker.run()


