FROM python:latest

# Permet à Python d'afficher tout ce qui est imprimé dans l'application plutôt que de le mettre en mémoire tampon.
#ENV PYTHONUNBUFFERED 1


#RUN apt-get update && apt-get -y install apache2

# Création of the workdir
#RUN mkdir /code

WORKDIR /code

# Add requirements.txt file to container
ADD requirements.txt /code/

# Install requirements
RUN pip install --upgrade pip \ 
&& pip install -r /code/requirements.txt

# Add the current directory(the web folder) to Docker container
ADD . /code/

EXPOSE 8001

#CMD "python manage.py runserver 80"

CMD ["python", "manage.py", "runserver", "8001"]
