import os
import winreg

def ModifyPATH():
    # Путь к папке ADB
    adb_path = os.getcwd()
    key = None  # Define key outside the try block
    try:
        # Открываем ключ реестра для изменения PATH
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 0, winreg.KEY_ALL_ACCESS)
        
        # Получаем текущее значение переменной PATH
        path_value, _ = winreg.QueryValueEx(key, 'Path')

        # Добавляем путь к папке ADB
        if adb_path not in path_value:
            path_value += os.pathsep + adb_path
            # Устанавливаем новое значение переменной PATH
            winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, path_value)
            print("Путь к папке ADB успешно добавлен в переменную PATH")
        else:
            print("PATH already modified for ADB")

        return True

    except Exception as e:
        print("An error occurred:", e)
        return False

    finally:
        # Всегда закрываем ключ реестра
        winreg.CloseKey(key)

# Пример использования функции
#ModifyPATH()
