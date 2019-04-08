from define import *

import json
import math
import sys
import argparse

# Argparse initialized.
parser = argparse.ArgumentParser(description = \
        "Keypicker, transaction replay from EVM execution trace")
# Input file path positional(required) argument.
parser.add_argument('input_trace', type=str, help='Input JSON trace file')
# Output file path optional.
parser.add_argument('--dest', type=str, help=f'Output stats file path, defaults to {output_file_path}',
                    nargs=1, default=DEFAULT_OUT_PATH)
args = parser.parse_args()

# Will override output file path if any given.
outfile_path = args.dest


class Keypicker():
    def __init__(self):
        pass

    def init(json_path):
        with open(json_path) as json_file:
            self.json_data = json.load(json_file)
        self.bytecode=str(json_data["bytecode"])
        self.stack_data=json_data["stack"]
        self.memory_data=json_data["memory"]
        self.storage_data=json_data["storage"]

    def run():
        pass


if __name__ == "__main__":
    #keypicker = Keypicker(...)
    #keypicker.init(...)
    #keypicker.run()


