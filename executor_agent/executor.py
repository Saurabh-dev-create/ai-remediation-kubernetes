from kubernetes import client, config


def restart_deployment(deployment_name, namespace="ai-remediation"):
    """
    Perform a rollout restart on a Kubernetes Deployment.
    """

    # Load kubeconfig
    config.load_kube_config()

    # Apps API client
    apps_v1 = client.AppsV1Api()

    # Patch deployment template annotations
    body = {
        "spec": {
            "template": {
                "metadata": {
                    "annotations": {
                        "kubectl.kubernetes.io/restartedAt": "auto-remediation"
                    }
                }
            }
        }
    }

    # Trigger rollout restart
    apps_v1.patch_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=body
    )

    print(f"✅ Deployment '{deployment_name}' restarted successfully.")