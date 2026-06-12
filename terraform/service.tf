resource "kubernetes_service" "monitor_agent" {

  metadata {
    name      = "monitor-agent"
    namespace = kubernetes_namespace.ai_remediation.metadata[0].name

    labels = {
      app = "monitor-agent"
    }
  }

  spec {

    selector = {
      app = "monitor-agent"
    }

    port {
      port        = 8000
      target_port = 8000
      name        = "metrics"
    }
  }
}