## Django

!!!warning 튜플안의 value가 하나일 때는 뒤에 `,`를 제대로 찍지 않으면 적용이 안된다.

## django server

<b>start server</b> `python manage.py runserver`
<b>quit server</b> `ctrl + c`
<b>first migration</b> `python manage.py migrate`

> migration file is just <b>python file</b> that <b>modifies shape of database</b>

<b>create admin</b> `python manage.py createsuperuser`
<b>create application</b> `python mangage.py startapp <application name>`

> config/settings.py의 `INSTALLED_APPS`안에 생성한 application 추가
> ex)`"houses.apps.HousesConfig"`

> `models.py, admin.py` 입력 후 아래와 같이 db에 적용

<b> make migration</b> `python manage.py makemigrations`
<b>migration</b> `python manage.py migrate`

## Django start project

`django-admin startproject config <folder name>` 현재 폴더는 `.`

## Poetry (virtual environment)

`poetry init` : poetry 초기화
`poetry add <library name>` : library 설치
`poetry shell` : 가상환경 안으로 들어가기
`exit` : 가상환경 밖으로 나오기

## Change python version

1. `brew install python`
2. `which python3` : 위치 확인 `/opt/homebrew/bin/python3`
3. `ls -l /opt/homebrew/bin/python*` : 설치되어있는 파이썬 전부 확인
4. `ln -s -f /opt/homebrew/bin/python3.9 /opt/homebrew/bin/python3` or `ln -s -f /opt/homebrew/bin/python3.9 /opt/homebrew/bin/python` : 파이썬 3.9로 변경
5. `python --version` or `python3 --version`
