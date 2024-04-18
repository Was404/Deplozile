import subprocess
from tqdm import tqdm
from res.strings import FILE_PATH_ON_DEVICE, START_MESSAGE, DESTINATION_PATH_ON_PC
def is_adb_available():
    try:
        subprocess.run(["adb", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
def download_file_from_android(file_path_on_device, destination_path_on_pc):
    
    adb_command = f"adb pull {file_path_on_device} {destination_path_on_pc}"
    adb_check_devices = "adb devices"
    subprocess.run(adb_check_devices, shell=True, check=True)
    try:
        if not is_adb_available():
            raise RuntimeError("ADB недоступен. Пожалуйста, убедитесь, что Android Debug Bridge установлен и добавлен в PATH.")
        
        subprocess.run(adb_command, shell=True, check=True)
        print(f"Файл успешно скачан на ПК: {destination_path_on_pc}")
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка при скачивании файла: {e}")

# Укажите путь к файлу на устройстве Android и путь на ПК, куда файл будет скачан

if __name__ == "__main__":
    
    print(START_MESSAGE)
    download_file_from_android(FILE_PATH_ON_DEVICE, DESTINATION_PATH_ON_PC)
