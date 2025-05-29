# TO-bot

TO-bot is a Discord bot designed to help Tournament Organizers (TOs) stay on top of their weekly responsibilities. The bot sends reminders to TOs about important tasks such as posting registration links, sharing schedules, and fulfilling their assigned roles for the week.

## Features
- Sends automated reminders to Tournament Organizers in your Discord server.
- Customizable messages for different responsibilities (e.g., posting registration, sharing schedules, etc.).
- Helps keep your tournament organized and on track.

## Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/HannahConnolly/TO-bot
   cd TO-bot
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure your bot:**
   - Create a new Discord bot at https://discord.com/developers/applications
   - Copy your bot token and add it to your environment variables or a `.env` file (see below).

5. **Run the bot:**
   ```sh
   python main.py
   ```

## Environment Variables
Create a `.env` file in the project root with the following content:
```
DISCORD_TOKEN=your-bot-token-here
```

## Usage
- Add the bot to your Discord server using the OAuth2 URL from the Discord Developer Portal.
- The bot will automatically send reminders to the TOs as configured in the code.

## Customization
- Edit `main.py` to customize the reminder messages and schedule.
- You can add more features, such as role assignment or custom commands, by extending the bot's code.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
