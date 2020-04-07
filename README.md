Nebula Docker Server
---

### Requirements
* Needs __docker-ce__ on host machine
* Needs __docker-compose__ on host machine

### Configuration
Change the `.env` file on root folder

### Start
Use these steps for build and start the server:
1. `docker-compose -f images/docker-compose.yml build`
1. `BOT_API=<token> docker-compose -f images/docker-compose.yml run --rm python`