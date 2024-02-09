# use a official python image
FROM python:3.9-slim
# setting the working directory
WORKDIR /usr/src/app
# copy the requirements file to install depedencies
COPY requirements.txt .
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# create a not root user to run the app for improve the security, without superuser privileges
RUN useradd -m lumu
# changing the default user
USER lumu
# copy the code to the container and setting the user owner
COPY --chown=lumu:lumu . .
# expose the port for the app
EXPOSE 8043
# Define the command to run the application
CMD ["flask", "run", "--host=0.0.0.0:8043"]
