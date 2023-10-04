This is intentded to show how you can use a database in a container image to store data indefinitely.

**Note:** The db machine doesn't use a DockerFile, all of the configuration is in the compose.yaml file. 
Docker compose is a flexible tools that lets you configure/modify an image in a Dockerfile, but a separate Dockerfile for each container isn't required.

The db-storage folder is initially empty, but the container machine will write a bunch of database file there when it initializes the database.
