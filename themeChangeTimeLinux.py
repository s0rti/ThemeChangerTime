from datetime import datetime
import subprocess
import time


def set_linux_theme():
    current_hour = datetime.now().hour
  
    if 8 <= current_hour < 20:
        color_scheme = "prefer-light"
        gtk_theme = "Yaru"  
    else:
        color_scheme = "prefer-dark"
        gtk_theme = "Yaru-dark" 

    try:
        subprocess.run(
            [
                "gsettings",
                "set",
                "org.gnome.desktop.interface",
                "color-scheme",
                color_scheme,
            ],
            check=True,
        )
        subprocess.run(
            [
                "gsettings",
                "set",
                "org.gnome.desktop.interface",
                "gtk-theme",
                gtk_theme,
            ],
            check=True,
        )

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при смене темы: {e}")
    except FileNotFoundError:
        print(
            "Ошибка: утилита gsettings не найдена."
        )


def main():
    print("Скрипт автосмены темы запущен и работает в фоне...")
    try:
        while True:
            set_linux_theme()
            time.sleep(900)
    except KeyboardInterrupt:
        print("\nРабота скрипта остановлена пользователем.")


if __name__ == "__main__":
    main()
