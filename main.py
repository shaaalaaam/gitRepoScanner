import requests
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def fetch_user_repositories(github_url):
    username = github_url.split('/')[-1]
    repositories_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(repositories_url)
    repositories = []
    if response.status_code == 200:
        repositories_data = response.json()
        for repo_data in repositories_data:
            repositories.append(
                {'name': repo_data['name'], 'url': repo_data['clone_url']})
    return repositories


def preprocess_code(code, tokenizer, max_length):
    tokenized_chunks = []
    code_lines = code.split("\n")

    for line in code_lines:
        line_chunks = [line[i:i+max_length]
                       for i in range(0, len(line), max_length)]

        for chunk in line_chunks:
            tokenized_chunk = tokenizer.encode(
                chunk, max_length=max_length, truncation=True, padding='max_length')
            tokenized_chunks.extend(tokenized_chunk)

    return tokenized_chunks


def generate_prompt(code):
    prompt = f"Analyze the technical complexity of the following code:\n\n{code}\n\nComplexity analysis:"
    return prompt


def calculate_complexity_score(tokenized_code):
    complexity_score = len(tokenized_code)
    return complexity_score


def analyze_github_user(url):
    # Fetch user repositories
    repositories = fetch_user_repositories(url)

    # Initialize GPT-2 model and tokenizer
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    # Initialize variables to track the most complex repository
    most_complex_repository = None
    highest_complexity_score = float('-inf')

    # Iterate over repositories
    for repo in repositories:
        # Fetch code from the repository
        response = requests.get(repo['url'])
        code = response.text

        # Preprocess the code
        tokenized_code = preprocess_code(code, tokenizer, max_length=2048)

        # Generate prompt for code evaluation
        prompt = generate_prompt(code)

        # Generate response from GPT-2 model
        input_ids = tokenizer.encode(
            prompt, return_tensors='pt', max_length=1024, truncation=True)
        generated_tokens = model.generate(
            input_ids=input_ids,
            max_length=100,
            num_return_sequences=1,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_p=0.95,
            top_k=50,
            no_repeat_ngram_size=3
        )

        generated_response = tokenizer.decode(
            generated_tokens[0], skip_special_tokens=True)

        # Calculate complexity score
        complexity_score = calculate_complexity_score(tokenized_code)

        # Update the most complex repository if needed
        if complexity_score > highest_complexity_score:
            highest_complexity_score = complexity_score
            most_complex_repository = repo

    # Return the most complex repository and its complexity score
    return most_complex_repository, highest_complexity_score
# github_url = "https://github.com/shaaalaaam"
# repository, complexity_score = analyze_github_user(github_url)

# print("Most Complex Repository:")
# print(repository)
# print("Complexity Score:", complexity_score)


@app.route("/api/analyze", methods=["POST"])
def analyze_repository():
    url = request.json.get("url")
    print(url)
    if not url:
        return jsonify({"error": "Invalid request"}), 400

    try:
        repository, complexity_score = analyze_github_user(url)
        return jsonify({
            "mostComplexRepository": repository,
            "complexityScore": complexity_score
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
