# Define the rule-based knowledge base
knowledge_base = {
    "symptoms": {
        "Symptom1": ["Disease1", "Disease2"],
        "Symptom2": ["Disease1"],
        "Symptom3": ["Disease2", "Disease3"],
        # Add more symptoms and corresponding diseases as needed
    },
    "treatments": {
        "Disease1": "Treatment1",
        "Disease2": "Treatment2",
        "Disease3": "Treatment3",
        # Add more diseases and corresponding treatments as needed
    }
}

# Function to provide diagnosis based on symptoms
def diagnose(symptoms):
    possible_diseases = set()
    for symptom in symptoms:
        if symptom in knowledge_base["symptoms"]:
            possible_diseases.update(knowledge_base["symptoms"][symptom])
    
    if len(possible_diseases) == 0:
        return "Unknown"
    else:
        return possible_diseases

# Function to provide treatment based on diagnosis
def get_treatment(disease):
    if disease in knowledge_base["treatments"]:
        return knowledge_base["treatments"][disease]
    else:
        return "Unknown"

# Main program loop
while True:
    user_input = input("Enter symptoms (comma-separated) or 'quit' to exit: ")
    
    if user_input.lower() == "quit":
        break
    
    symptoms = [symptom.strip() for symptom in user_input.split(",")]
    
    diagnosis = diagnose(symptoms)
    
    print("Diagnosis:", diagnosis)
    
    if len(diagnosis) == 1:
        treatment = get_treatment(diagnosis.pop())
        print("Treatment:", treatment)
    else:
        print("Multiple possible diseases. Consult a medical professional for accurate diagnosis.")
