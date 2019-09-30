FROM python:3
ADD main.py /
EXPOSE 1000
CMD [ "python", "main.py" ]