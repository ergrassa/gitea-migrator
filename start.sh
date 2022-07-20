echo "${CRON_SPEC} python ${PROJ_DIR}/migrate.py ${GITHUB_TOKEN} ${GITEA_TOKEN} ${GITHUB_ORG} ${GITEA_URL} ${GITEA_ORG} >> ${LOG_FILE} 2>&1" > ${PROJ_DIR}/crontab
touch ${LOG_FILE} # Needed for the tail
crontab ${PROJ_DIR}/crontab
crontab -l