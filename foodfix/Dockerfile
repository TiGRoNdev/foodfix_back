FROM centos:7

# Local directory with project source
ENV DOCKPROJ_SRC=.
# Directory in container for all project files
ENV DOCKPROJ_SRCHOME=/src
# Directory with app source code
ENV DOCKPROJ_SRVPROJ=/srv/backend_server

RUN yum -y update && \
    yum -y install yum-utils && \
    yum -y groupinstall development && \
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y install python36u python36u-devel python36u-pip && \
    yum -y install mariadb mariadb-devel && \
    yum clean all

WORKDIR $DOCKPROJ_SRCHOME

RUN pip3.6 install uwsgi

# Copy all library code to SRCDIR
COPY $DOCKPROJ_SRC $DOCKPROJ_SRCHOME
WORKDIR $DOCKPROJ_SRCHOME

RUN mkdir -p /var/log/uwsgi/
RUN chmod 766 /var/log/uwsgi/

# Mount mysql volumes
VOLUME ["/var/lib/mysql", "/var/lib/mysql/mysql.sock", "$DOCKPROJ_SRVPROJ"]

WORKDIR /
RUN rm -rf /src rm -rf /var/cache/yum

# Copy requirements.txt code to SRCDIR
COPY $DOCKPROJ_SRC/requirements.txt $DOCKPROJ_SRVPROJ/requirements.txt
WORKDIR $DOCKPROJ_SRVPROJ
RUN pip3.6 install -r requirements.txt

# Copy application source code to SRCDIR
COPY $DOCKPROJ_SRC $DOCKPROJ_SRVPROJ
WORKDIR $DOCKPROJ_SRVPROJ

RUN python3.6 manage.py collectstatic --settings=foodfix.settings --noinput

EXPOSE 80/tcp

CMD uwsgi -y $DOCKPROJ_SRVPROJ/uwsgi.yml
