---
date: 1970-01-01
---

# Define a Kubernetes NodePort Service (Guided)

CKA.2-002: Define a Kubernetes NodePort Service (Guided)
29 Minutes Remaining 
Create a pod Deployment



Hints Enabled

No  Yes

You have been automatically signed in to WS2019 as the administrator.

Open the MobaXterm desktop application.
Establish a new SSH session to the k8s-master1 virtual machine as the administrator using Passw0rd! as the password, and then when prompted to save the password, select No.
Select the Type Text icon to enter the associated text into the terminal.

Expand this hint for guidance on establishing a new SSH session.
k8s-master1 is an Ubuntu Linux virtual machine. When you enter the password, you will not see the password in the terminal.

You will perform all cluster operations in this challenge on the k8s-master1 node by using the kubectl command-line tool.

Download the https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/webserver.deployment.yaml Deployment definition file by using the wget command.
Expand this hint for guidance on downloading a Deployment definition file.
Run the following command to download the Deployment definition file:

wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/webserver.deployment.yaml
Display the contents of the webserver.deployment.yaml file by using the cat command.
Expand this hint for guidance on displaying the contents of a file.
Run the following command to display the contents of the webserver.deployment.yaml definition file:

cat webserver.deployment.yaml
The webserver.deployment.yaml definition file is written in YAML (YAML Ain't Markup Language) format. It contains the configuration information for a Deployment object named webserver and two replica pods that run an nginx web server.

The Deployment definition file

The Deployment definition also includes the label app: webserver. A label contains a key/value pair that you can use to organize and identify Kubernetes objects.

Create a Deployment by using the webserver.deployment.yaml Deployment definition file, the kubectl create command, and the -f flag.
Expand this hint for guidance on creating a Deployment.
Run the following command to create the webserver Deployment by using a definition file:

kubectl create -f webserver.deployment.yaml
You use the -f flag after the create command to indicate the name of a file that contains the object configuration.

Display the pods that are running in the cluster by using the kubectl get command.
Expand this hint for guidance on displaying the pods that are running in a cluster.
Run the following command to display the pods that are running in the cluster:

kubectl get pods
If the kubectl get pods command returns a status of ContainerCreating for one of the pods, run the command again. This status indicates that a pod is still in the creation stage.

Pods in Creating State

Check your work
Confirm that you reviewed the contents of a Deployment definition file.
Confirm that you created a Deployment by using a definition file.

---

CKA.2-002: Define a Kubernetes NodePort Service (Guided)
27 Minutes Remaining 
Create a NodePort Service



Hints Enabled

No  Yes

Display the services that are running in the cluster by using the kubectl get command.
Expand this hint for guidance on displaying the Services that are running in a cluster.
Run the following command to display the Services that are running in a cluster:

kubectl get services

The following screenshot shows the output of the kubectl get services command:The output of the get services command
You can use the shortname svc instead of the services resource name.

There is one Service type running in the cluster—the default ClusterIP Service named kubernetes.

Services provide connectivity between resources and enable communication between various Kubernetes cluster components and applications within and outside of the cluster. The default kubernetes ClusterIP Service is one of four Service types in Kubernetes, and it is used by cluster components to communicate with the cluster API server—the kube-apiserver Service.

...less
Download the https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/npservice.yaml NodePort Service definition file by using the wget command.

Display the contents of the npservice.yaml file by using the cat command.

The npservice.yaml NodePort Service definition file contains the configuration information needed to create a NodePort Service.

The npservice definition file

Key	Value
name	npservice
selector	app: webserver
port	80
targetPort	80
nodePort	30001
Create a NodePort Service that will allow external access to the application running on the webserver pods by using the npservice.yaml Service definition file, the kubectl create command, and the -f flag.
A NodePort Service creates a statically defined port—the NodePort—on all cluster nodes to provide external access to an application in a cluster. The NodePort service does not use IP address mapping to pods as pods are ephemeral and pod IP addresses are dynamic. Instead, the NodePort Service is loosely coupled to pods by using a selector to match the Service selector label key pair to the same label key pair that is defined in a pod.

You can also create a NodePort Service by using the imperative expose command and the syntax kubectl expose deployment Deployment_Name --type=NodePort --name=NodePort_Service_Name.

...less
Check your work
Confirm that you reviewed the contents of a NodePort Service definition file.
Confirm that you created a NodePort Service by using a definition file.

---

CKA.2-002: Define a Kubernetes NodePort Service (Guided)
23 Minutes Remaining 
Access an application



Hints Enabled

No  Yes

Display the IP addresses of the worker nodes in the cluster by using the kubectl get command, the -o wide option, and the grep command.
Expand this hint for guidance on displaying the IP addresses of the worker nodes in a cluster.
Run the following command to display the IP addresses of the worker nodes in the cluster:

kubectl get nodes -o wide | grep worker
Open Microsoft Edge.

Go to http://192.168.1.31:30001 to display the webserver application in the browser.

The Windows Server 2016 node and the Kubernetes cluster node are on the same network subnet: 192.168.1.0/24.

Open a second browser tab, and then go to http://192.168.1.32:30001.

Open a third browser tab, and then go to http://192.168.1.33:30001.

The webserver application is accessible from any of the three worker nodes in the cluster.

The webserver application

A NodePort Service assigns a static port of 30000-32767 to all of the cluster nodes that are visible outside of the cluster pod network. The Service forwards a request to a pod, regardless of the node on which the pod is running, and then by using a round-robin algorithm, the Service can forward traffic to a single pod in a set of replica pods.

You can use a NodePort Service to provide access to the applications that are hosted in a cluster—for example, a demo application or an internal database—in a production network. Typically, you use a third-party load-balancing and ingress solution to expose a cluster resource to the internet.

...less
Check your work
Confirm that you displayed the IP addresses of the worker nodes.
Confirm that you accessed the webserver application from all of the worker nodes.