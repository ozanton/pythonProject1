#!/bin/bash

# ��������� ������� ������ pipenv
if ! command -v pipenv &>/dev/null; then
    echo "������������� ����� pipenv"
    pip install pipenv
fi

# ��������� ����� pipenv
pipenv update

# ��������� � ����� �������
cd /myproject/weatherapi/

# ��������� ������� ������������ ���������
if [ ! -d venv ]; then
    echo "������ ����������� ���������"
    python3 -m venv venv
fi

# ���������� ����������� ���������
source venv/bin/activate

# ��������� ����
python run_current.py

# ������������ ������
if [ $? -ne 0 ]; then
    echo "������ ��� ������� run_current.py"
    exit 1
fi