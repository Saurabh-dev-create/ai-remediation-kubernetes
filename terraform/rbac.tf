resource "kubernetes_service_account" "monitor_agent" {

  metadata {
    name      = "monitor-agent"
    namespace = kubernetes_namespace.ai_remediation.metadata[0].name
  }
}

resource "kubernetes_role" "monitor_agent_role" {

  metadata {
    name      = "monitor-agent-role"
    namespace = kubernetes_namespace.ai_remediation.metadata[0].name
  }

  rule {
    api_groups = [""]
    resources  = ["pods", "pods/log"]
    verbs      = ["get", "list", "watch"]
  }

  rule {
    api_groups = ["apps"]
    resources  = ["deployments"]
    verbs      = ["get", "list", "watch", "patch"]
  }
}

resource "kubernetes_role_binding" "monitor_agent_binding" {

  metadata {
    name      = "monitor-agent-rolebinding"
    namespace = kubernetes_namespace.ai_remediation.metadata[0].name
  }

  subject {
    kind      = "ServiceAccount"
    name      = kubernetes_service_account.monitor_agent.metadata[0].name
    namespace = var.namespace
  }

  role_ref {
    api_group = "rbac.authorization.k8s.io"
    kind      = "Role"
    name      = kubernetes_role.monitor_agent_role.metadata[0].name
  }
}
