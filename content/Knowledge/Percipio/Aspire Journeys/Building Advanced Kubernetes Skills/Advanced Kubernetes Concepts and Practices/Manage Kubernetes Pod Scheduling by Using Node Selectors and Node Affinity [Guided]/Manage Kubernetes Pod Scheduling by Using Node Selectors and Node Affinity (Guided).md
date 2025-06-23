---
date: 2001-01-01
---

# Manage Kubernetes Pod Scheduling by Using Node Selectors and Node Affinity (Guided)

CKA.2-007: Manage Kubernetes Pod Scheduling by Using Node Selectors and Node Affinity (Guided)
28 Minutes Remaining 
Schedule pods by using a node selector



Hints Enabled

No  Yes

You have been automatically signed in to WS2019 as the administrator.

Open the MobaXterm desktop application.
Establish a new SSH session to the k8s-master1 virtual machine as the administrator using Passw0rd! as the password, and then when prompted to save the password, select No.
Select the Type Text icon to enter the associated text into the terminal.

Expand this hint for guidance on establishing a new SSH session.
k8s-master1 is an Ubuntu Linux virtual machine. When you enter the password, you will not see the password in the terminal.

You will perform all cluster operations in this challenge on the k8s-master1 node by using the kubectl command-line tool.

Download the https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/ssd.deployment.yaml Deployment definition file by using the wget command.
Expand this hint for guidance on downloading a Deployment definition file.
Run the following command to download the Deployment definition file:

wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/ssd.deployment.yaml
Display the contents of the ssd.deployment.yaml file by using the cat command.
Expand this hint for guidance on displaying the contents of a file.
Run the following command to display the contents of the Deployment definition file:

cat ssd.deployment.yaml
The ssd.deployment.yaml definition file is written in YAML (YAML Ain't Markup Language) format. It contains the configuration information to create a Deployment object named database and two replica pods that run a redis database.

The ssd definition file

The Deployment definition also contains an element named nodeSelector that defines a key/value pair for a label named diskType: ssd. The kube-scheduler for the cluster will schedule the database replica pods to run only on nodes that contain the diskType=ssd label.

NodeSelector is a pod scheduling feature that you can use to schedule a pod or set of pods on a specific node or nodes whose labels match the nodeSelector label defined in a pod definition. You can use nodeSelector to manually schedule pods that may have specific resource requirements—for example, RAM size, CPU type, or disk type.

Pod scheduling is the process that determines the placement of new pods onto cluster nodes.

...less
Create a Deployment by using the ssd.deployment.yaml file, the kubectl create command, and the -f flag.
Expand this hint for guidance on creating a Deployment.
Run the following command to create a Deployment by using a definition file:

kubectl create -f ssd.deployment.yaml
You use the -f flag to instruct the create command to update the cluster state by using a configuration file passed to it as an argument. The file can be a local file or a remote file where the filename is expressed in the form of a URL.

Display the pods that are running in the cluster by using the kubectl get command.
Expand this hint for guidance on displaying the pods that are running in the cluster.
Run the following command to display the pods that are running in the cluster:

kubectl get pods

The following screenshot shows the output of the kubectl get pods command:The pending db replica pods
The pods in the database Deployment are in a Pending state as there are no nodes that contain the diskType: ssd label.

Add the label diskType=ssd to the k8s-worker2 node by using the kubectl label command.
Expand this hint for guidance on adding a label to a node.
Run the following command to update a node by adding a label:

kubectl label node k8s-worker2 diskType=ssd
A label is a key/value pair that you can attach to an object in a Kubernetes cluster.

Because the label command is an imperative command, it updates the running configuration of an object.

Display the labels for the k8s-worker2 node by using the kubectl describe command.
Expand this hint for guidance on displaying the labels for a node.
Run the following command to display the labels for a node:

kubectl describe node k8s-worker2

The following screenshot shows the output of the kubectl describe node k8s-worker2 command:The output of the kubectl describe command
Display the nodes on which there are database replica pods running by using the kubectl get command and the -o wide option.
Expand this hint for guidance on displaying nodes by using the -o wide option.
Run the following command to display the nodes on which there are database replica pods running:

kubectl get pods -o wide

The following screenshot shows the output of the kubectl get pods -o wide command:The get pods command
You can use the -o wide (--output=wide) option to display detailed resource information.

The database replica pods are running on the k8s-worker2 node.

Check your work
Confirm that you created a Deployment named database.
Confirm that you created a label on k8s-worker2 that matches the database Deployment nodeSelector label.
Confirm that the database replica pods are running on k8s-worker2.

---

CKA.2-007: Manage Kubernetes Pod Scheduling by Using Node Selectors and Node Affinity (Guided)
25 Minutes Remaining 
Schedule pods by using required node affinity



Hints Enabled

No  Yes

Add the label zone=west to the k8s-worker3 node by using the kubectl label command.

Download the https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/required.affinity.pod.yaml file by using the wget command.

Display the contents of the required.affinity.pod.yaml pod definition file by using the cat command.

The required.affinity.pod.yaml definition file contains the configuration for a pod object named nginx that runs an nginx image.

The nginx pod definition file

The pod definition file also contains a requiredDuringSchedulingIgnoredDuringExecution affinity rule and the key/value label zone=west. The intention of this affinity rule is for Kubernetes to schedule the pod on a node that contains the matching label zone=west.

Node affinity is similar to nodeSelector in that it constrains pod scheduling by using node labels and affinity rules that are defined in a pod. There are two node affinity variants: required and preferred. Node affinity is a more expressive and more capable alternative to nodeSelector.

Create a pod by using the required.affinity.pod.yaml file, the kubectl create command, and the -f flag.

Display the node on which the nginx pod is running by using the kubectl get command, and the -o wide option.

The nginx pod is running on the k8s-worker3 node as the node has the matching label zone=west, as required by the pod affinity rule.

The following screenshot shows the output of the kubectl get pods -o wide command:

nginx on k8s-worker3

You can use a required node affinity rule to ensure that a pod or set of pods is scheduled on a specific node type.

Check your work
Confirm that you added a label to k8s-worker3.
Confirm that you created a pod that contains a required affinity rule.
Confirm that the pod is running on the k8s-worker3 node, as required by the affinity rule.

---

CKA.2-007: Manage Kubernetes Pod Scheduling by Using Node Selectors and Node Affinity (Guided)
24 Minutes Remaining 
Schedule pods by using preferred node affinity



Hints Enabled

No  Yes

Download the https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/preferred.affinity.pod.yaml file by using the wget command.

Display the contents of the preferred.affinity.pod.yaml pod definition file by using the cat command.

The preferred.affinity.pod.yaml pod definition file contains the configuration information necessary to create a pod named httpd that runs an httpd image.

The preferred pod definition

The file also contains the preferredDuringSchedulingIgnoredDuringExecution affinity rule and the key/value pair zone=east. This affinity rule directs Kubernetes to attempt to place the pod on a node that contains the matching label zone=east.

Create a pod by using the preferred.affinity.pod.yaml file, the kubectl create command, and the -f flag.

Display the node on which the httpd pod is running by using the kubectl get command and the -o wide option.

The httpd pod is scheduled, although none of the nodes contain the zone=east label.

The following screenshot shows the output of the kubectl get pods -o wide command:

The command output showing the httpd pod scheduled

You can use a preferred node affinity rule to schedule a pod or set of pods that have a preference to run on a certain type of node but will run on any available node if the preferred type of node is not available.

Check your work
Confirm that you created a pod that contains a preferred affinity rule.
Confirm that the httpd pod was scheduled on a node, even though the pod preferred affinity rule was not satisfied.