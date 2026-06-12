resource "kubernetes_namespace" "ai_remediation" {
  metadata {
    name = var.namespace
  }
}