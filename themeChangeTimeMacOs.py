from datetime import datetime
import subprocess
import time


def set_macos_theme():
    current_hour = datetime.now().hour

    if 8 <= current_hour < 20:
        mode = "false"
    else:
        mode = "true"

    script = f'tell application "System Events" to tell appearance preferences to set dark mode to {mode}'
    subprocess.run(['osascript', '-e', script])


def main():
    print("Скрипт автосмены темы запущен и работает в фоне...")
    try:
        while True:
            set_macos_theme()

            time.sleep(1000)
    except KeyboardInterrupt:
        print("\nРабота скрипта остановлена пользователем.")


if __name__ == "__main__":
    main()
