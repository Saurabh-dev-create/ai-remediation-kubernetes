from prometheus_client import Counter
from prometheus_client import start_http_server

# Total incidents detected
INCIDENTS_TOTAL = Counter(
    "incidents_total",
    "Total incidents detected"
)

# Total successful remediations
REMEDIATIONS_TOTAL = Counter(
    "remediations_total",
    "Total successful remediations"
)

# Total failed remediations
REMEDIATION_FAILURES_TOTAL = Counter(
    "remediation_failures_total",
    "Total failed remediations"
)

# Total Slack notifications sent
NOTIFICATIONS_TOTAL = Counter(
    "notifications_total",
    "Total Slack notifications sent"
)


def start_metrics_server():
    start_http_server(8000)

    print(
        "📊 Prometheus metrics exposed on port 8000"
    )