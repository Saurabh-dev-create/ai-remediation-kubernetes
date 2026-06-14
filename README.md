## Amazon EKS Cluster Provisioning

The AI Remediation Platform is deployed on Amazon Elastic Kubernetes Service (EKS).

The Kubernetes cluster and networking infrastructure are provisioned using Terraform, including:

- Amazon EKS Cluster
- Managed Node Group
- VPC
- Public and Private Subnets
- NAT Gateway
- Core Kubernetes Addons
  - CoreDNS
  - kube-proxy
  - VPC CNI

### EKS Cluster Status
![EKS Cluster](docs/screenshots/01-eks-cluster/eks-cluster-console.png)

*Amazon EKS cluster successfully provisioned and running in ap-south-1.*