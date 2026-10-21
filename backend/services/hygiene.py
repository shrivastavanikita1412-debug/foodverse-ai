def score_hygiene(checks: dict) -> dict:
    total = len(checks)
    passed = sum(bool(value) for value in checks.values())
    score = round(passed / total * 100) if total else 0
    return {"module":"hygiene-checklist", "score":score, "passed_checks":passed, "total_checks":total, "checks":checks, "label":"Checklist score only", "disclaimer":"Not a regulatory inspection or official compliance certification."}
