 #!/bin/bash
app="devops_showcase_app"
docker build -t ${app} .
docker run -d -p \
  --name=${app} \
  -v $PWD:/app ${app}
