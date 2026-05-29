from analyzer_agent.providers.ollama_provider import OllamaProvider


def analyze_incident(incident_data):
    # Load prompt template
    with open("analyzer_agent/prompts/rca_prompt.txt", "r") as file:
        prompt_template = file.read()

    # Create final prompt
    final_prompt = prompt_template.format(
        incident=incident_data
    )

    # Initialize provider
    provider = OllamaProvider()

    # Return AI analysis
    return provider.analyze(final_prompt)


if __name__ == "__main__":
    sample_incident = """
Pod: broken-app
Reason: CrashLoopBackOff

Logs:
Starting app...
"""

    response = analyze_incident(sample_incident)

    print("\n🧠 AI RCA Analysis:\n")
    print(response)