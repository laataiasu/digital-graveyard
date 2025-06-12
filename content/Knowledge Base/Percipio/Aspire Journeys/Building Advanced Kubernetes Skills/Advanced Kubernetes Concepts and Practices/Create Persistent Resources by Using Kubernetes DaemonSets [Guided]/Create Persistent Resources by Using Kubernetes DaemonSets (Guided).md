# Create Persistent Resources by Using Kubernetes DaemonSets (Guided)

CKA.2-008: Create Persistent Resources by Using Kubernetes DaemonSets (Guided)
20 Minutes Remaining 
Identify a DaemonSet



Hints Enabled

No  Yes

You have been automatically signed in to WS2019 as the administrator.

Open the MobaXterm desktop application.
Establish a new SSH session to the k8s-master1 virtual machine as the administrator using Passw0rd! as the password, and then when prompted to save the password, select No.
Select the Type Text icon to enter the associated text into the terminal.

Expand this hint for guidance on establishing a new SSH session.
k8s-master1 is an Ubuntu Linux virtual machine. When you enter the password, you will not see the password in the terminal.

You will perform all cluster operations in this challenge on the k8s-master1 node by using the kubectl command-line tool.

Display the DaemonSets that are running in the cluster by using the kubectl get command and the --all-namespaces flag.
Expand this hint for guidance on displaying a DaemonSet.
Run the following command to display the DaemonSets that are running in the cluster:
kubectl get DaemonSets --all-namespaces
The following screenshot shows the output of the kubectl get DaemonSets --all-namespaces command:
The output of the get DaemonSets all-namespaces

There are two DaemonSet pods in the cluster.

A Kubernetes DaemonSet is an object that schedules a single pod to run on every node or subset of nodes in the cluster. Like a ReplicaSet or a Deployment, a DaemonSet will ensure that a single pod is scheduled on each node and will automatically schedule a pod on a new cluster node. A DaemonSet pod can also be scheduled to run on a master node by using taints, pod tolerations, and node affinity rules.

...less
Display detailed information about the kube-proxy DaemonSet in the kube-system namespace by using the kubectl describe command and the --namespace= flag.
You can use the shortname ds instead of the DaemonSets resource name, and you can use the shortname -n instead of --namespace= flag.

Expand this hint for guidance on displaying detailed information about a DaemonSet.
Run the following command to display detailed information about the kube-proxy DaemonSet:
kubectl describe ds kube-proxy -n kube-system
The following screenshot shows the output of the kubectl describe ds kube-proxy -n kube-system command:
The kube-proxy DaemonSet details

The kube-proxy DaemonSet will schedule and maintain a single pod named kube-proxy on each of the cluster nodes that contain the Node-Selector label kubernetes.io/os=linux.

You can use the label k8s-app=kube-proxy to identify the pods scheduled by the kube-proxy DaemonSet.

Display the kube-proxy pods and the nodes on which they are running by using the kubectl get command, the -l flag, the "k8s-app=kube-proxy" label, the -o wide option, and the all-namespaces flag.
Expand this hint for guidance on displaying the kube-proxy pods.
Run the following command to display the nodes on which the kube-proxy pods are running:
kubectl get pods -l "k8s-app=kube-proxy" -o wide --all-namespaces
The following screenshot shows the output of the kubectl get pods -l "k8s-app=kube-proxy" -o wide --all-namespaces command:
Thekube%20proxy%20nodes.JPG

You can use the -o wide (--output=wide) option to display detailed resource information.

You can use the shortname -l instead of the --label= label selector flag to specify a label query.

The kube-proxy schedules the pods in the control plane to run as a DaemonSet pod on each of the cluster nodes.

Display the labels for the k8s-worker1 node by using the kubectl describe command.
The k8s-worker1 configuration contains the matching DaemonSet Node-Selector label kubernetes.io/os=linux.

The information about the labels is displayed at the beginning of the command output.

The following screenshot shows the output of the kubectl describe node k8s-worker1 command:

The labels for the k8s-worker node

You can use a DaemonSet to create a persistent resource that runs a single pod application or daemon on all cluster nodes to monitor and collect log information.

Check your work
Confirm that you identified the DaemonSets that are running in the cluster.
Confirm that you displayed detailed information about the kube-proxy DaemonSet.
Confirm that you displayed a filtered list of DaemonSet pods by using a label.

---

CKA.2-008: Create Persistent Resources by Using Kubernetes DaemonSets (Guided)
16 Minutes Remaining 
Create a DaemonSet



Hints Enabled

No  Yes

Download the https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/logger.daemonset.yaml DaemonSet definition file by using the wget command.
Expand this hint for guidance on downloading a file.
Run the following command to download the DaemonSet definition file:
wget https://raw.githubusercontent.com/LODSContent/ChallengeLabs_Resources/master/CKA/logger.daemonset.yaml
Display the contents of the logger.daemonset.yaml file by using the cat command.
Expand this hint for guidance on displaying the contents of a file.
Run the following command to display the contents of the logger.daemonset.yaml definition file:
cat logger.daemonset.yaml
The logger.daemonset.yaml definition file is written in YAML (YAML Ain't Markup Language) format. It contains the configuration information for a DaemonSet object named logger that schedules a single pod to run on each node in the cluster. The cluster will run the fluentd logging application.

Fluentd is a lightweight log aggregation platform that you can use to collect node health metrics.

Create a DaemonSet by using the logger.daemonset.yaml file, the kubectl create command, and the -f flag.
Expand this hint for guidance on creating a DaemonSet.
Run the following command to create a DaemonSet by using a definition file:
kubectl create -f logger.daemonset.yaml
You use the -f flag after the create command to indicate the name of a file that contains the object configuration.

You cannot create a DaemonSet by using imperative commands, but you can update the running configuration of a DaemonSet by using the kubectl edit command.

Display the DaemonSets that are running in the cluster by using the kubectl get command and the --all-namespaces flag.
Although the logger DaemonSet is running in the default namespace, a DaemonSet is typically configured to run in a namespace other than the default namespace or the production namespace.

Display the logger pods and the nodes on which they are running by using the kubectl get command and the -o wide option, and then record the name of the pod that is running on k8s-worker3 in the following k8s-worker3 pod text box:

k8s-worker3 pod
logger-xc9kj

Delete the logger-xc9kj pod by using the kubectl delete command.

Expand this hint for guidance on deleting a pod.
Run the following command to delete a pod:
kubectl delete pod logger-xc9kj
It can take approximately 1–3 minutes for a resource to be deleted.

Display the logger pods by using the kubectl get command and the -o wide option.
The logger DaemonSet created a new pod on k8s-worker3. The DaemonSet will ensure that a single logger pod is always running on each of the cluster nodes.

Check your work
Confirm that you created a DaemonSet named logger by using a definition file.
Confirm that you verified that logger DaemonSet pods are running on all cluster nodes.
Confirm that you deleted a DaemonSet pod and that a replacement pod was created by the DaemonSet.

