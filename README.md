## Django start project

`django-admin startproject config <folder name>` : 현재 폴더는 `.`

## Poetry (virtual environment)

`poetry init`
`poetry add <library name>`
`poetry shell` : 가상환경 안으로 들어가기
`exit` : 가상환경 밖으로 나오기

## Change python version

1. `brew install python`
2. `which python3` -> 위치 확인 `/opt/homebrew/bin/python3`
3. `ls -l /opt/homebrew/bin/python*` -> 설치되어있는 파이썬 전부 확인
4. `ln -s -f /opt/homebrew/bin/python3.9 /opt/homebrew/bin/python3` or `ln -s -f /opt/homebrew/bin/python3.9 /opt/homebrew/bin/python` -> 파이썬 3.9로 변경
5. `python --version` or `python3 --version` 으로 버전 확인
