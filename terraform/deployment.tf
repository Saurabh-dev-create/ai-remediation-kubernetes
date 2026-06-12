resource "kubernetes_deployment" "monitor_agent" {

  metadata {
    name      = "monitor-agent"
    namespace = kubernetes_namespace.ai_remediation.metadata[0].name

    labels = {
      app = "monitor-agent"
    }
  }

  spec {

    replicas = 1

    selector {
      match_labels = {
        app = "monitor-agent"
      }
    }

    template {

      metadata {
        labels = {
          app = "monitor-agent"
        }
      }

      spec {
        service_account_name = kubernetes_service_account.monitor_agent.metadata[0].name
        container {

          image = var.image
          name  = "monitor-agent"

          port {
            container_port = 8000
          }

          env {
            name = "OPENAI_API_KEY"

            value_from {
              secret_key_ref {
                name = "ai-remediation-secrets"
                key  = "OPENAI_API_KEY"
              }
            }
          }

          env {
            name = "SLACK_WEBHOOK_URL"

            value_from {
              secret_key_ref {
                name = "ai-remediation-secrets"
                key  = "SLACK_WEBHOOK_URL"
              }
            }
          }
          env {
               name  = "LLM_PROVIDER"
               value = "openai"
          }
        }
      }
    }
  }
}