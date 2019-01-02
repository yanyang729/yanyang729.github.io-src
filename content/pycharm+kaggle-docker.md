Title: kaggle docker image with pycharm
Date: 2017-11-23 02:20
Modified: 2017-11-23 02:30
Category: Tutorial
Tags: python, pycharm, docker
Slug: 

Build your machine learning env once for all. 

## docker setup

On Mac:

1. install docker for mac
2. pull kaggle/python image. `http://blog.kaggle.com/2016/02/05/how-to-get-started-with-data-science-in-containers/`

## pycharm setup

1. add remote env. `https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-docker.html`
2. **API URL**: tcp://localhost:3375. (Took me tons of time to get this right). In the latest version, just leave certifs and excutable empty. You shall see prompt telling you that connection is sucessful

All set. That's it.

