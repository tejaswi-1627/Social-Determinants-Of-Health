"""
SDoH Clinical Note Analyzer - Rule-Based System
Extracts SDoH factors from full clinical notes
"""

from rules_solutions import SDOH_DATA
import json


def detect_sdoh_from_clinical_notes(text):
    """
    Detect SDoH categories from real clinical notes using keyword matching.
    """
    text_lower = text.lower()
    detected = []

    for category, data in SDOH_DATA.items():
        for keyword in data["keywords"]:
            if keyword.lower() in text_lower:
                detected.append(category)
                break   # stop checking more keywords

    return detected


def get_solutions(problems):
    """
    Return the solutions for detected SDoH problems
    """
    return {p: SDOH_DATA[p]["solutions"] for p in problems}


def generate_json_output(problems):
    """
    Frontend-friendly JSON output
    """
    output = []

    for p in problems:
        output.append({
            "category": p.replace("_", " ").title(),
            "solutions": SDOH_DATA[p]["solutions"]
        })

    return json.dumps(output, indent=4)


def print_report(problems, solutions):
    """
    Pretty console report
    """
    print("\n" + "="*70)
    print("🏥 SOCIAL DETERMINANTS OF HEALTH - ANALYSIS REPORT")
    print("="*70 + "\n")

    if not problems:
        print("✅ No SDoH issues detected.\n")
        return

    print(f"🚨 DETECTED SDoH FACTORS: {len(problems)}\n")

    for i, p in enumerate(problems, 1):
        print(f"{i}. {p.replace('_',' ').title()}")

    print("\n" + "-"*70)
    print("💡 SOLUTIONS & RECOMMENDATIONS:\n")

    for p in problems:
        print(f"📌 {p.replace('_',' ').title()}:")
        for s in solutions[p]:
            print(f"   • {s}")
        print()

    print("="*70)
    print("JSON output for frontend:")
    print("="*70)
    print(generate_json_output(problems))
    print("="*70 + "\n")


def main():

    print("\n" + "="*70)
    print("🏥 SDoH CLINICAL NOTE ANALYZER")
    print("="*70)
    print("\nEnter full clinical note (press Enter twice to finish):\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    clinical_note = " ".join(lines)

    if not clinical_note.strip():
        print("\n❌ No input provided.")
        return

    problems = detect_sdoh_from_clinical_notes(clinical_note)
    solutions = get_solutions(problems)

    print_report(problems, solutions)


if __name__ == "__main__":
    main()
