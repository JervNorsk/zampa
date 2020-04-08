#!/usr/bin/env bash

if [[ $DEBUG == 'true' ]]
then
    set -x
fi

if [[ $USE_INTERNAL_MYSQL == "true" ]]
then
    mkdir /srv/docker/database -p
    echo "
    CREATE USER '$MYSQL_USERNAME'@'localhost' IDENTIFIED BY '$MYSQL_PASSWORD';
    GRANT ALL PRIVILEGES ON * . * TO '$MYSQL_USERNAME'@'localhost';
    FLUSH PRIVILEGES;

    CREATE DATABASE $MYSQL_DATABASE;
    " > /srv/docker/database/entrypoint.sql

    service mysql start

    echo "Configuring MySQL"
    mysql < /srv/docker/database/entrypoint.sql

    echo "Dumping MySQL"
    mysql $MYSQL_DATABASE < SQL/admin_nebulabot.sql
fi

echo "Configuring bot"
cat config.tmp.py \
  | sed "s;%SOURCE%;$SOURCE;g" \
  | sed "s;%AUTHOR%;$AUTHOR;g" \
  | sed "s;%VERSION%;$VERSION;g" \
  \
  | sed "s;%BOT_API%;$BOT_API;g" \
  | sed "s;%BOT_USER%;$BOT_USER;g" \
  | sed "s;%BOT_NAME%;$BOT_NAME;g" \
  \
  | sed "s;%MYSQL_SERVER%;$MYSQL_SERVER;g" \
  | sed "s;%MYSQL_USERNAME%;$MYSQL_USERNAME;g" \
  | sed "s;%MYSQL_PASSWORD%;$MYSQL_PASSWORD;g" \
  | sed "s;%MYSQL_DATABASE%;$MYSQL_DATABASE;g" \
  \
  | sed "s;%STAFF_GROUP%;$STAFF_GROUP;g" \
  | sed "s;%ADMIN_ID%;$ADMIN_ID;g" \
  | sed "s;%OWNER%;$OWNER;g" \
  | sed "s;%LOG_CHANNEL%;$LOG_CHANNEL;g" \
  \
  | sed "s;%YANDEX_API%;$YANDEX_TOKEN;g" \
  | sed "s;%OPENWEATHER_API%;$OPENWEATHER_TOKEN;g" \
  > config.py

python3 bot.py