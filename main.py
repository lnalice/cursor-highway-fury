"""pygbag entry point for browser execution via WebAssembly."""

import asyncio
import pygame

pygame.init()

from game import Game  # noqa: E402

async def main():
    game = Game()
    await game.run_async()

asyncio.run(main())
