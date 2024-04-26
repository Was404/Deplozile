import subprocess
import json
import logging
from tqdm import tqdm
from res.strings import FILE_PATH_ON_DEVICE, START_MESSAGE, DESTINATION_PATH_ON_PC, GIT_LINK

logging.basicConfig(filename='logs.log', level=logging.DEBUG)

try:
    with open('res\keyevents.json') as f:
        key_events_data = json.load(f)
except:
    logging.error("No keyevents data in /res!")        


slovar = {
    "1": "download_file_from_android",
    "2": "Hack_my_phone",
    "3": "Create_backup",
    "4": "Snif_data"
}    

def LoggerOn():
    # Настраиваем логгер
    
    # Записываем логи
    logging.debug('Это сообщение уровня DEBUG')
    logging.info('Это сообщение уровня INFO')
    logging.warning('Это сообщение уровня WARNING')
    logging.error('Это сообщение уровня ERROR')
    logging.critical('Это сообщение уровня CRITICAL')
    
def LoggerDisable():      
        logging.info('Loggining DISABLE')  
        # Отключаем логирование
        logging.disable(logging.CRITICAL)
        
    
def is_adb_available():
    try:
        logging.debug('start up adb attempt')
        subprocess.run(["adb", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.warning(e)
        return False
    
def download_file_from_android(file_path_on_device, destination_path_on_pc):
    logging.debug('pull attempt')
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
        logging.error(f"Произошла ошибка при скачивании файла: {e}")

def Create_backup():# Не готоВ!! НУжны опции
    print('Данная функция не работает как надо, но она уже запущена я хз че будет\n!! ENTER CTRL + C !!')
    subprocess.run("adb backup", shell=True, check=True)
# Укажите путь к файлу на устройстве Android и путь на ПК, куда файл будет скачан

# adb backup [опции] <приложения>
# хочу добавить кнопку для бэкапа
# adb restore c:\android\backup.ab восстановление бэкапа
# adb shell screenrecord --size 1280x720 --bit-rate 6000000 --time-limit 20 --verbose /sdcard/video.mp4 это запись видео тайм лимит можно убрать(макс 180сек)
# pm list packages список установленных приложений
# am kill com.android.browser
# am kill-all
# am start -a android.intent.action.CALL tel:8918231875 он реально позвонит по указанному телефону
# am start -a android.intent.action.VIEW 'http:/xakep.ru'
# input keyevent 82 https://xakep.ru/2016/05/12/android-adb/

def Hack_my_phone():
    logging.debug('start up Hack_my_phone attempt')
    print(key_events_data["key_events"]["key_wakeup"])
    subprocess.run(key_events_data["key_events"]["key_wakeup"], shell=True, check=True)
    logging.debug('Hack_my_phone finished')

def Main_menu():
    logging.debug('start up Main_menu attempt')
    print(slovar)
    answer = int(input())
    match answer:
        case 1:
            download_file_from_android(FILE_PATH_ON_DEVICE, DESTINATION_PATH_ON_PC)
        case 2:
            Hack_my_phone()
        case 3:
            LoggerDisable()    
        case _:
            Main_menu()


if __name__ == "__main__":
    print(START_MESSAGE)
    print("check new version:", GIT_LINK)
    download_file_from_android(FILE_PATH_ON_DEVICE, DESTINATION_PATH_ON_PC)
    Main_menu()
