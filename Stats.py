from Keypicker import (
    outfile_path
)

import Engine
import json

# Maybe we can produce additional stats later?
class Stats():
    # Produce stats directly from Engine instance.
    def __init__(self, engine) -> None:
        self.outfile_path = outfile_path
        self.engine = engine

    def print_stats(self) -> None:
        # TEST
        data = dict()

        data['bytecode'] = ''
        data['stack'] = self.engine.stack
        data['memory'] = self.engine.memory
        data['storage'] = self.engine.storage

        with open(self.outfile_path, 'w') as out_json:
            json.dump(data, out_json)

