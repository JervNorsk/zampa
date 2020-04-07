#!/usr/bin/env bash

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

echo "Configuring bot"
cat config.tmp.py \
  | sed "s/%BOT_API%/$BOT_API/g" \
  \
  | sed "s/%OWNER%/$OWNER/g" \
  | sed "s/%STAFF_GROUP%/$STAFF_GROUP/g" \
  | sed "s/%ADMIN_ID%/$ADMIN_ID/g" \
  | sed "s/%LOG_CHANNEL%/$LOG_CHANNEL/g" \
  \
  | sed "s/%MYSQL_USERNAME%/$MYSQL_USERNAME/g" \
  | sed "s/%MYSQL_PASSWORD%/$MYSQL_PASSWORD/g" \
  | sed "s/%MYSQL_DATABASE%/$MYSQL_DATABASE/g" \
  > config.py

python3 bot.py