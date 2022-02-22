# aws-folder-backup

This will automatically back up a directory to S3 on a set schedule per crontab.

# Folder Backup

docker run -d -v /path/to/local/dir:/backup:ro --env-file backup.env

# Docker-Compose Example

version: "3.8"
services:

  backup:
      build: ./aws-folder-backup
      restart: always
      volumes:
        - /path/to/local/dir:/backup:ro
      env_file:
        - backup.env

# crontab
Default cron settings to run at 3AM on every Wednesday. This can be adjusted per crontab settings
 - * 3 * * 3 python /backup_service.py

 # .env file
AWS_ACCESS_KEY_ID="ADFAREFADFA"
AWS_SECRET_ACCESS_KEY="AFW$RFG#$TAEFEFAF#Q$FQEFQ#Q"
S3_BUCKET="s3-bucket-name"
S3_PATH="backup/key/path"

# S3 backup settings TODO
Use the following settings to set custom options for the backup process:
AWS_REGION=""
COMPRESSION_TYPE="zip | tar"
