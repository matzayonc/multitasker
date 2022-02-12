FROM archlinux

RUN pacman -Sy
RUN pacman --noconfirm -S python3 ffmpeg