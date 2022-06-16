<<<<<<< HEAD
=======
# machine_learning_project
>>>>>>> fbc52b63634f09b96e7872cfa305e149d261edba
## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

<<<<<<< HEAD
1. HEROKU_EMAIL = pallavi.deepakgupta1990@gmail.com
2. HEROKU_API_KEY = d5bd6a1b-fd5a-415a-98ea-9d50b7502bee
3. HEROKU_APP_NAME = new-machine-learning-app
=======
1. HEROKU_EMAIL = anishyadav7045075175@gmail.com
2. HEROKU_API_KEY = e9171a6d-ccd3-44ea-a07b-45f85bf3d096
3. HEROKU_APP_NAME = ml-regression-app
>>>>>>> fbc52b63634f09b96e7872cfa305e149d261edba


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image

```
OR

```
docker image ls

```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
<<<<<<< HEAD
```
=======
```
>>>>>>> fbc52b63634f09b96e7872cfa305e149d261edba
