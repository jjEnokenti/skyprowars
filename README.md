# SkyproWars


### Для запуска игры необходимо перейти в папку infra из корневого каталога:
    cd infra
### Далее ввести команду для постороения и заупска контейнеров:
    sudo docker-compose up -d --build
### Для остановки контейнеров:
    sudo docker-compose down
### Для удаления образов:
    sudo docker rmi $(sudo docker images -a -q)
