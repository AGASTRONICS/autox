'''
Autox Entry Point
'''

import argparse
import subprocess
from lib import load_config

def start_services(services):
    """Start the selected services using docker-compose."""
    print(f"Starting services: {', '.join(services)}")

    # Build the docker-compose command with selected services
    services_arg = ' '.join(services)
    cmd = f'docker-compose up -d {services_arg}'
    
    subprocess.run(cmd, shell=True)


def main(args, config):
    import time
    import threading
    from autox.bot import run_bot

    if args.background:
        # Run the bot in a separate thread
        bot_thread = threading.Thread(target=run_bot)
        bot_thread.daemon = True  # This allows the thread to exit when the main program does
        bot_thread.start()
        print("Bot is now running in the background.")
        
        # Keep the main program running, you might want to handle signals to stop gracefully
        while True:
            time.sleep(1)  # Keep the main thread alive
    else:
        run_bot(config=config)  # Run the bot in the foreground if -background is not specified

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AutoX Trading Bot")
    parser.add_argument('--service', nargs='+', help='Specify which services to run with the bot (e.g., redis, postgres, nginx)')
    parser.add_argument('--config', type=str, help='Path to the configuration file')

    args = parser.parse_args()

    # Load configuration if provided
    config = {}
    if args.config:
        config = load_config(args.config)

    # Call main with args and config
    main(args, config)
