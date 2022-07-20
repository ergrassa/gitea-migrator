FROM python:3-alpine

ENV PROJ_DIR="/app"
ENV LOG_FILE="${PROJ_DIR}/app.log"

WORKDIR ${PROJ_DIR}

COPY migrate.py start.sh ${PROJ_DIR}

RUN pip install giteapy PyGithub
RUN chmod +x ${PROJ_DIR}/start.sh
CMD sh ${PROJ_DIR}/start.sh && ls -al ${PROJ_DIR} && cat ${PROJ_DIR}/crontab && crond && tail -f ${LOG_FILE}