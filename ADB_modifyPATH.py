import os
import winreg

def ModifyPATH():
    # Путь к папке ADB
    adb_path = os.getcwd()

    # Получаем текущее значение переменной PATH
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEMCurrentControlSetControlSession ManagerEnvironment', 0, winreg.KEY_ALL_ACCESS)
    path_value, _ = winreg.QueryValueEx(key, 'Path')

    # Добавляем путь к папке ADBS
    if adb_path not in path_value:
        path_value += os.pathsep + adb_path
    else:
        return True

    # Устанавливаем новое значение переменнойS PATH
    winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, path_value)

    # Закрываем реестр
    winreg.CloseKey(key)
    return("Путь к папке ADB успешно добавлен в переменную PATH")

ModifyPATH()
