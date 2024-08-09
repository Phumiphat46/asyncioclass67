import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Iterate through all json files in the directory.
    for path in pathlist:
        print(path)
        # Read the contents of the json file.
        async with aiofiles.open(path, mode = 'r') as f:
            contents = await f.read()

        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]

        move_file_path = f'{pokemonmove_directory}/{name}_moves.txt'
        # Open a new fil to write the list of moves into.
        async with aiofiles.open(move_file_path, mode = 'w') as f:
            await f.write('\n'.join(moves))
        
        print(f"Moves written to: {move_file_path}")

asyncio.run(main())
