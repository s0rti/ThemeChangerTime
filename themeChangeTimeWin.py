from datetime import datetime
import os
import time
import winreg


def set_windows_theme():
    current_hour = datetime.now().hour

    if 8 <= current_hour < 20:
        theme_value = 1
    else:
        theme_value = 0


    registry_paths = [
        r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    ]


    value_names = ["AppsUseLightTheme", "SystemUsesLightTheme"]

    for path in registry_paths:
        try:

            reg_key = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_SET_VALUE
            )

            for value_name in value_names:

                try:
                    current_val, _ = winreg.QueryValueEx(reg_key, value_name)
                    if current_val == theme_value:
                        continue
                except FileNotFoundError:
                    pass


                winreg.SetValueEx(
                    reg_key, value_name, 0, winreg.REG_DWORD, theme_value
                )

            winreg.CloseKey(reg_key)
        except Exception as e:
            print(f"Ошибка при изменении реестра: {e}")


def main():
    print("Скрипт автосмены темы для Windows запущен и работает...")
    try:
        while True:
            set_windows_theme()

            time.sleep(900)
    except KeyboardInterrupt:
        print("\nРабота скрипта остановлена пользователем.")


if __name__ == "__main__":
    main()