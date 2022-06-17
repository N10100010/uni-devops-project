 #!/bin/bash
app="docker.test"
docker build -t ${app} .
docker run -d -p \
  --name=${app} \
  -v $PWD:/app ${app}
