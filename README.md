Nebula Docker Server
---

### Requirements
* Needs __docker-ce__ on host machine
* Needs __docker-compose__ on host machine

### Configuration
Change the `.env` file on root folder

```properties
#########################################################################
#                            DOCKER CONFIG                              #
#########################################################################
DEV_USERNAME=developer
DEV_PASSWORD=test
VCS_TYPE=git
VCS_REPOSITORY=https://github.com/Infocom-Telegram-Community/nebula.git

#########################################################################
#                            GENERAL CONFIG                             #
#########################################################################
SOURCE=https://github.com/Infocom-Telegram-Community/nebula.git
AUTHOR=JervNorsk
VERSION=0.0.1

#########################################################################
#                            BOT CONFIG                                 #
#########################################################################
BOT_TOKEN=<token>
BOT_ID=@nebuladevbot
BOT_NAME=NebulaDevBot

#########################################################################
#                            DATABASE CONFIG                            #
#########################################################################
MYSQL_SERVER=localhost
MYSQL_USERNAME=developer
MYSQL_PASSWORD=test
MYSQL_DATABASE=bot

USE_INTERNAL_MYSQL=true

#########################################################################
#                            TELEGRAM CONFIG                            #
#########################################################################
STAFF_GROUP=-<group_id>
ADMIN_ID=[<user_id>, ...]
OWNER=[<user_id>, ...]
LOG_CHANNEL=-<channel_id>

#########################################################################
#                            API CONFIG                                 #
#########################################################################
YANDEX_TOKEN=<token>
OPENWEATHER_TOKEN=<token>
```

####Start
Use these steps for build and start the server:
1. `docker-compose -f images/docker-compose.yml build`
1. `docker-compose run devBot`