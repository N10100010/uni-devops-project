# DevOps - Project

### MAIN REPO
This is the main repository. In ./TestApp are the infrastructure files and the app-code in a seperate sub-repository.

#### How to clone? 
Due to the fact that we have submodules in here, we need to clone recursively.
`git clone --recurse-submodules`

#### How to run?
Go into the TestApp folder and run
`docker-compose up`

This will start the server.

#### How to access?
Browser: Enter http://0.0.0.0:56733/
