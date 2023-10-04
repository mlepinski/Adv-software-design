This directory is intentionally empty for this example.

When the container machine runs, the "volumes" command in the compose.yaml file instructs the container machine
to put all of the mysql database files here. (If you look up the Docker image documentation for a particular database online
then it should explain what directory the database image is configured to write its database files. You then use the volumes
command to connect that to a directory in the container to a folder on your machine.)
