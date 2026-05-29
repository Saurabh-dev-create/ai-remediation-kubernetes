from analyzer_agent.analyzer import analyze_incident
from executor_agent.executor import restart_deployment
from notifier_agent.slack_notifier import send_slack_notification
from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException

# Load Kubernetes config
config.load_kube_config()

# Core API
v1 = client.CoreV1Api()

# Watch object
w = watch.Watch()

print("🚀 Monitoring Kubernetes Pods...\n")

detected_pods = set()
try:
    for event in w.stream(v1.list_namespaced_pod,
                          namespace="ai-remediation"):

        pod = event['object']

        pod_name = pod.metadata.name

        pod_status = pod.status.phase

        print(f"Pod: {pod_name} | Status: {pod_status}")

        # Container statuses
        if pod.status.container_statuses:

            for container_status in pod.status.container_statuses:

                state = container_status.state

                # Detect CrashLoopBackOff
                if state.waiting:

                    reason = state.waiting.reason

                    if reason == "CrashLoopBackOff" and pod_name not in detected_pods:
                        
                        detected_pods.add(pod_name)
                        print("\n🚨 INCIDENT DETECTED 🚨")
                        print(f"Pod: {pod_name}")
                        print(f"Reason: {reason}")

                        # Fetch logs
                        logs = v1.read_namespaced_pod_log(
                           name=pod_name,
                           namespace="ai-remediation"
                        )

                        print("\n📜 Logs:")
                        print(logs)

                        # Prepare incident data
                        incident_data = f"""
                    Pod: {pod_name}
                    Reason: {reason}

                    Logs:
                    {logs}
                    """

                        print("\n🧠 Sending incident to AI Analyzer...\n")
                        
                        # Stop event stream while AI analyzes
                        w.stop()
                        # Run AI analysis
                        analysis = analyze_incident(incident_data)

                        print("\n🤖 AI Root Cause Analysis:\n")
                        print(analysis)
                        print("\n Executing remediation action...\n")

                        restart_deployment("broken-app")

                        print("\n✅ Auto-remediation completed successfully.")
                        slack_message = f"""
                        Kubernetes Auto-Remediation Alert

                        Pod: {pod_name}
                        Reason: {reason}

                        AI Root Cause Analysis: 
                        {analysis}

                        Action Taken:
                        Restarted deployment: broken-app

                        Status:
                        Auto-remediation completed successfully.
                        """

                        print("\n Sending Slack notification...\n")

                        send_slack_notification(slack_message)
except ApiException as e:
    print(f"\n Kubernetes API Error: {e}")