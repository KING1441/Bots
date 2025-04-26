
TOKEN = 'Your_Discord_Token'

import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

number_emojis = {
    0: "⬜", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
    4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣"
}

@client.event
async def on_ready():
    print(f'Minesweeper Bot is online as {client.user}!')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # !minesweeper Command
    if message.content.startswith('!minesweeper'):
        try:
            parts = message.content.split()
            rows, cols, mines = map(int, parts[1:])

            if rows * cols <= mines:
                await message.channel.send("Too many mines! 💥")
                return

            board = [[0 for _ in range(cols)] for _ in range(rows)]

            # Place mines
            placed = 0
            while placed < mines:
                r = random.randint(0, rows - 1)
                c = random.randint(0, cols - 1)
                if board[r][c] != -1:
                    board[r][c] = -1
                    placed += 1

            # Calculate numbers
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == -1:
                        continue
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == -1:
                                count += 1
                    board[r][c] = count

            # Create hidden board with spoiler tags
            board_message = ""
            for row in board:
                for cell in row:
                    emoji = "💣" if cell == -1 else number_emojis[cell]
                    board_message += f"||{emoji}||"
                board_message += "\n"

            await message.channel.send(board_message)

        except (IndexError, ValueError):
            await message.channel.send("Use it like this: `!minesweeper rows cols mines` (example: `!minesweeper 5 5 5`)")

    # !Make_Map Command (No spoiler tags)
    elif message.content.startswith('!Make_Map'):
        try:
            parts = message.content.split()
            rows, cols, mines = map(int, parts[1:])

            if rows * cols <= mines:
                await message.channel.send("Too many mines! 💥")
                return

            board = [[0 for _ in range(cols)] for _ in range(rows)]

            # Place mines
            placed = 0
            while placed < mines:
                r = random.randint(0, rows - 1)
                c = random.randint(0, cols - 1)
                if board[r][c] != -1:
                    board[r][c] = -1
                    placed += 1

            # Calculate numbers
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == -1:
                        continue
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == -1:
                                count += 1
                    board[r][c] = count

            # Create visible board (without spoiler tags)
            board_message = ""
            for row in board:
                for cell in row:
                    emoji = "💣" if cell == -1 else number_emojis[cell]
                    board_message += emoji
                board_message += "\n"

            await message.channel.send(f"Here is your **Minesweeper Map**:\n{board_message}")

        except (IndexError, ValueError):
            await message.channel.send("Use it like this: `!Make_Map rows cols mines` (example: `!Make_Map 5 5 5`)")

client.run(TOKEN)
