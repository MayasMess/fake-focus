import random
import time
import warnings

from pynput import keyboard, mouse
from pynput.keyboard import Controller, Key
from rich.progress import Progress, SpinnerColumn, TextColumn

warnings.filterwarnings('ignore')

WAITING_TIME = 90
keyboard_controller = Controller()

fake_tasks = [
    "Processing", "Preparing", "Initializing", "Loading modules", "Compiling assets",
    "Optimizing dependencies", "Fetching resources", "Verifying integrity",
    "Resolving conflicts", "Synchronizing data", "Updating indexes", "Cleaning temporary files",
    "Calibrating parameters", "Assembling components", "Mapping architecture", "Analyzing patterns",
    "Establishing secure channel", "Decoding instructions", "Generating metadata",
    "Allocating memory blocks", "Compressing payload", "Encrypting secrets",
    "Activating neural core", "Training local model", "Bootstrapping quantum layer",
    "Predicting outcomes", "Extracting embeddings", "Deploying microagents", "Reticulating splines",
    "Running anomaly detection", "Validating synthetic data", "Compiling behavioral matrix",
    "Consulting the oracle", "Negotiating with servers", "Convincing AI to cooperate",
    "Debugging the universe", "Summoning extra RAM", "Crossing fingers", "Asking ChatGPT for help",
    "Cleaning digital dust", "Making things look faster", "Pretending to work harder"
]

# Variable globale pour suivre le dernier moment d’activité
last_activity = time.time()


def on_activity(_):
    """Callback appelé à chaque action clavier ou souris"""
    global last_activity
    last_activity = time.time()


def main() -> None:
    global last_activity

    # Listeners pour clavier et souris
    mouse_listener = mouse.Listener(on_move=on_activity, on_click=on_activity, on_scroll=on_activity)
    keyboard_listener = keyboard.Listener(on_press=on_activity)

    mouse_listener.start()
    keyboard_listener.start()

    while True:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description=f"{random.choice(fake_tasks)}...", total=None)
            while True:
                time.sleep(1)
                if time.time() - last_activity > WAITING_TIME:
                    keyboard_controller.press(Key.cmd)
                    keyboard_controller.release(Key.cmd)
                    time.sleep(0.5)
                    keyboard_controller.press(Key.cmd)
                    keyboard_controller.release(Key.cmd)
                    last_activity = time.time()
                    break


if __name__ == '__main__':
    main()
