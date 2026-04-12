# remote development scripts

.SRC-DIR = $(dirname $PWD)/src
.$USER # username
.$REMOTE-UNIT = <IP Address>

## commands

push to remote - rsync -aP ${SRC-DIR}/* $USER@$REMOTE-UNIT:~/project/src
### Source - https://stackoverflow.com/a/9090859
### Posted by johnsyweb, modified by community. See post 'Timeline' for change history
### Retrieved 2026-04-12, License - CC BY-SA 4.0
pull from remote - rsync -chavzP --stats $USER@$REMOTE-UNIT:~/project/src ${SRC-DIR}
