FROM python:3
ADD server.py /
EXPOSE 1000
CMD [ "python", "server.py" ]
