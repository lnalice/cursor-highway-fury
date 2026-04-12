"""pygbag entry point for browser execution via WebAssembly."""

import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game import Game

async def main():
    game = Game()
    await game.run_async()

asyncio.run(main())
