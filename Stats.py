from Keypicker import (
    outfile_path
)

import Engine
import json

class Stats():
    # Produce stats directly from Engine instance.
    def __init__(self, engine) -> None:
        self.outfile_path = outfile_path
        self.engine = engine

    def print_stats(self) -> None:
        # TEST
        print(self.engine.stack)

