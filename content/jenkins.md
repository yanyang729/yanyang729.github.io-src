Title: Jenkins on AWS
Date: 2017-10-11 03:20
Modified: 2017-10-11 03:20
Category: Tutorial
Tags: aws, jenkins
Slug: 

Use jenkins to deploy node.js server on AWS EC2

### Begin
- create instance
- ssh to instance

### Install jenkins
```bash
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
echo deb http://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list
sudo apt-get update
sudo apt-get install jenkins
sudo systemctl start jenkins

```

### Login jenkins from local
In the AWS terminal window, we'll use the cat command to display the password:
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

### setting
build -> execute shell


[reference](https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-16-04)