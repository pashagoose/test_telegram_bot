# Jason Statham Quotes Bot
1) Гуськов Павел Максимович
2) Бот отсылает по запросу цитаты Джейсона Стетхема
3) Amazon
4) Для автоматического перезапуска бота использовал watchtower и docker-compose. Контейнер с watchtower мониторит репозиторий на dockerhub, пингует его раз в какое-то время и сравнивает два образа на равенство. Если образы неравны, то он перезапускает рабочий контейнер. Вот содержимое  _docker-compose.yml_:
```
version: "3"

services:
        jason_statham:
                image: SECRET_USERNAME/jason_statham_bot
                environment:
                        TELEGRAM_BOT_TOKEN: "SECRET_TOKEN"

        watchtower:
                image: containrrr/watchtower
                volumes:
                        - /var/run/docker.sock:/var/run/docker.sock
                command: --interval 10
```
