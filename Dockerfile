FROM archlinux

RUN pacman -Sy
RUN pacman --noconfirm -S python3 python-pip ffmpeg

COPY ./requirements.txt /app/
WORKDIR /app

RUN pip install -r ./requirements.txt

COPY . /app/

CMD python3 main.py