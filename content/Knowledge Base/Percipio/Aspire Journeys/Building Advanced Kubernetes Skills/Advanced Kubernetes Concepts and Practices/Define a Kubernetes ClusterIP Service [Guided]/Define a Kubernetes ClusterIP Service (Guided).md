# Define a Kubernetes ClusterIP Service (Guided)

CKA.2-001: Define a Kubernetes ClusterIP Service (Guided)
28 Minutes Remaining 
Identify Services in a cluster



Hints Enabled

No  Yes

You have been automatically signed in to WS2019 as the administrator.

Open the MobaXterm desktop application.
Establish a new SSH session to the k8s-master1 virtual machine as the administrator using Passw0rd! as the password, and then when prompted to save the password, select No.
Select the Type Text icon to enter the associated text into the terminal.

Expand this hint for guidance on establishing a new SSH session.
k8s-master1 is an Ubuntu Linux virtual machine. When you enter the password, you will not see the password in the terminal.

You will perform all cluster operations in this challenge on the k8s-master1 node by using the kubectl command-line tool.

Display the services running in the cluster by using the kubectl get command.
Expand this hint for guidance on displaying the Services running in a cluster.
You can use the shortname svc instead of the services resource name.

There is one Service type running in the cluster—the default ClusterIP Service named kubernetes.

Services provide connectivity between resources and enable communication between various Kubernetes cluster components and applications within and outside of a cluster. The ClusterIP Service is one of four Service types in Kubernetes.

Display the running configuration of the kubernetes ClusterIP Service by using the kubectl describe command.
Expand this hint for guidance on displaying the running configuration of a Service.
The ClusterIP Service running configuration shows the Service IP address, the Service endpoint IP address, and the port number.

Display the Service endpoints currently defined in the cluster by using the kubectl get command.
Expand this hint for guidance on displaying the Service endpoints.
Endpoints track the IP addresses and port numbers of the objects to which a Service forwards traffic.

Determine the node to which the kubernetes ClusterIP Service forwards requests by using the kubectl get command and the -o wide flag.
Expand this hint for guidance on displaying the IP address of a node.
The -o wide (--output=wide) flag displays detailed resource information. You can use this flag to determine the IP address of a resource—in this case, the k8s-master1 node.

The ClusterIP Service provides communication between cluster components and the cluster API server. API requests to the ClusterIP Service IP address 10.96.0.1 are forwarded to the pod that contains the Kubernetes API server—the kube-apiserver Service—that is listening on port 6443 on the k8s-master1 master node.

Check your work
Confirm that you identified the default Services that are running in the cluster.
Confirm that you displayed the running configuration of a ClusterIP Service.
Confirm that you displayed the Service endpoints.

---

CKA.2-001: Define a Kubernetes ClusterIP Service (Guided)
25 Minutes Remaining 
Define a ClusterIP Service



Hints Enabled

No  Yes

Create a Deployment by using the https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/webserver.nginx.deployment.yaml Deployment definition file and the kubectl create command.
Expand this hint for guidance on creating a Deployment by using a definition file.
The Deployment definition file contains the configuration information for a Deployment object named webserver and two replica pods that run an nginx web server. The web server will listen for HTTP requests on port 80.

You can use the -f flag after the create command to indicate the name of a file that contains the object configuration.

Determine the nodes on which the replica pods are running by using the kubectl get command and the -o wide flag.

Record the IP address of one of the webserver pods in the IP Address text box.

IP Address

Retrieve the HTTP banner information from the pod at <IPAddress> by using the curl command.

Expand this hint for guidance on retrieving the HTTP header information from a web server.
You can use the curl command and the -I option to retrieve HTTP header information from a web server. The webserver Deployment is accessible from within the cluster by using the IP address of the pod; however, pods are ephemeral and pod IP addresses are dynamic. To ensure access to an application in a pod, you can use a Service.

You can create a ClusterIP Service to ensure access to a pod or a set of pods in a cluster. When a ClusterIP Service is created, it is assigned a static virtual IP address that does not change during the lifespan of the Service.

Create a ClusterIP Service for the webserver deployment by using the kubectl expose command.
Expand this hint for guidance on creating a ClusterIP Service.
You can define a Service by using the imperative expose command. You can also define a Service by using a Service definition file. This is known as a declarative approach.

Check your work
Confirm that you created a Deployment named webserver.
Confirm that you retrieved HTTP header information from the webserver Deployment.
Confirm that you created a ClusterIP Service for the webserver Deployment.

---

CKA.2-001: Define a Kubernetes ClusterIP Service (Guided)
19 Minutes Remaining 
Describe a ClusterIP Service



Hints Enabled

No  Yes

Display the services that are running in the cluster by using the kubectl get command, and then record the IP address of the webserver ClusterIP Service in the ClusterIP Service IP Address text box.

ClusterIP Service IP Address
10.109.62.131

Retrieve HTTP header information from the webserver Deployment by using the IP address 10.109.62.131 and the curl -I command.

The webserver Deployment is accessible by using the IP address of the ClusterIP Service.

Retrieve detailed information about the webserver ClusterIP service by using the kubectl describe command.
The webserver ClusterIP Service uses a selector—displayed in the output of the describe command as Selector: run=webserver—to couple with any cluster pods whose running configuration contains the pod template label run=webserver. A selector is a label that the Service uses to couple pods to the Service.

Display the endpoints of the webserver ClusterIP Service by using the kubectl get command.
Expand this hint for guidance on displaying Service endpoints.
Run the following command to display the endpoints of the webserver ClusterIP Service:

kubectl get endpoints webserver

The following screenshot shows the output of the kubectl get endpoints webserver command:The webserver endpoints
The endpoints of the webserver ClusterIP Service point to the replica pods of the webserver Deployment.

Retrieve detailed information about the webserver deployment by using the kubectl describe command.
The template for the webserver Deployment pod contains the label run=webserver.

The webserver pod label

The ClusterIP Service uses a selector mechanism and labels to couple the Service to pods rather than using direct IP address and port mapping. A ClusterIP Service can load-balance requests across multiple pods.

You can use a ClusterIP Service to provide communication between pods in a cluster network in which a pod or set of pods running as a front-end database needs to communicate with a back-end database pod.

Check your work
Confirm that you displayed the endpoints of the webserver ClusterIP Service.
Confirm that you retrieved HTTP header information from the webserver replica pods by using the IP address of the ClusterIP Service.
Confirm that you displayed the label information in the ClusterIP Service configuration and the webserver Deployment configuration.

---

