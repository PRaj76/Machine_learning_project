## Start Machine Leareing Project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Render Account](https://dashboard.render.com/loging)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documention](https://git-scm.com/docs/gittutorial)

Creating Conda evvironment
```
conda create -p venv python==3.7 -y
```
```

conda activate venv/
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

> Note: To ignore file or folder from git we can write name of file/folder in gitignore file

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
To setup CT/CD pipline in Render we need 3 information

1. RENDER_EMAIL: pankajraj7651@gmail.com
2. RENDER_API_KEY: rnd_af0b8fI4zTKZbmuhthlkrvFP9ZJa
3. RENDER_APP_NAME: ml-regression-app

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
docker run -p 5000:5000 -e PORT=5000 1b44012229e7  
```

To check running container in docker
```
docker ps
```

To stop docker conatiner
```
docker stop  <continer_id>
```

```
python setup.py install
```

