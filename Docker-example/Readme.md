To run this simple Docker example, use the following terminal command:

    docker compose up

Note: Depending on how docker was installed on your machine, you might use docker-compose instead of docker compose

This should automatically build the containers. 
However, you can force docker to rebuild the containers using:

    docker compose build

You can delete any containers that aren't currently running with:

    docker compose rm

finally, you can get an interactive terminal on either of the container machines as follows:

    docker exec -it MY_CONTAINER_NAME /bin/sh

Note that MY_CONTAINER_NAME should be the name of the running container where you want shell (terminal) access. 
When you start the containers using "docker compose up" it should print out the container names as they are starting. 
They often look like "docker-test-web-1" or something similar.
