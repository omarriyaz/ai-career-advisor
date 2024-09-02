# Function that generates a roadmap for someone looking to enter a specific field using the Ollama LLaMA model.

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the Ollama LLaMA model
model = OllamaLLM(model="llama3.1")

def parse_with_ollama(dom_chunks, parse_description):
    # Create a prompt using the ChatPromptTemplate
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)

def generate_roadmap(transcripts):
    # Define the description to parse from transcripts
    parse_description = (
        "Summarize a comprehensive roadmap for someone looking to enter the specified field. "
        "The roadmap should be a numbered list of the steps taken to break into the field."
        "Include key skills, resources to learn those skills, and projects that are essential for entering the field."
        "Generate Additional Project Ideas from the Project Ideas that are specified in the information given"
    )

    # Parse each transcript chunk using the LLM
    roadmap = parse_with_ollama(transcripts, parse_description)
    
    return roadmap
