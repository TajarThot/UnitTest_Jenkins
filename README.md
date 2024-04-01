# UnitTest_Jenkins
This is a python unittesting code integrated with jenkins and nginx
# Prerequisites:
* Jenkins Installed
* Nginx Installed
* Domain Name
* Python3 Installed
# Step1 
We write a python script for the UnitTest of our website.
# Step2
Now save this script at the location:
/var/lib/jenkins/workspace/unittesting/pytest.py
# Step3
start your jenkins server and bind our jenkins ip address with the Domain Name you own.
# Step4
Now edit the nginx default file with our code which reroute the traffic on port 8080 internally. (No need to add port number with our address now)
# Step5
Now create a new build on jenkins after login and create a new build with pipeline option.
# Step6
Now make a declarative pipline script for our unittest and start the build.
