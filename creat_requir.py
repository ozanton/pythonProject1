#!!!!! сщздаем конфиг окружения
import subprocess

# установленные пакеты
installed_packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')

# список пакетов в файл
with open('requirements.txt', 'w') as f:
    for package in installed_packages:
        f.write(package + '\n')