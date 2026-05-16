import sys
import json
import re

def audit_article(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    findings = []
    
    # 1. Puffery and Cliche Ban
    puffery_words = ["delve", "tapestry", "resonate", "pivotal", "multifaceted", "underscores", "navigate", "commendably", "paradigm", "testament", "intricate", "transformative", "symphony", "dance", "mosaic", "cornerstone", "bedrock"]
    for word in puffery_words:
        if re.search(r'\b' + word + r'\b', content, re.IGNORECASE):
            findings.append(f"Found banned puffery/poetic word: {word}")

    cliches = ["stands as a testament to", "shaping the future of", "crucial milestone"]
    for cliche in cliches:
        if cliche.lower() in content.lower():
            findings.append(f"Found banned cliche: {cliche}")

    # 2. Punctuation Audit
    if '—' in content or '–' in content:
        findings.append("Found banned em-dash or en-dash.")

    # 3. Sentence Structure Enforcement (Starting with banned words)
    sentences = re.split(r'(?<=[.!?]) +', content)
    banned_starters = ["and", "but", "this", "which", "however", "therefore"]
    for s in sentences:
        words = s.strip().split()
        if words:
            first_word = words[0].lower()
            if first_word in banned_starters:
                findings.append(f"Sentence starts with banned transitive word: {first_word}")

    # 4. Negative Parallelism
    if re.search(r'not only.*but also', content, re.IGNORECASE):
        findings.append("Found banned negative parallelism (not only X, but also Y).")
    if re.search(r'this isn\'t.*this is', content, re.IGNORECASE):
        findings.append("Found banned negative parallelism (this isn't X. this is Y).")

    if not findings:
        result = {"status": "PASSED", "findings": []}
    else:
        result = {"status": "FAILED", "findings": findings}

    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "PASSED" else 1)

if __name__ == "__main__":
    audit_article(sys.argv[1])
