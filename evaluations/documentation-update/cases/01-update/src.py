DEFAULT_TIMEOUT_SECONDS = 30


def run_job(publish=None):
    warnings = []
    if publish is not None:
        try:
            publish()
        except RuntimeError:
            warnings.append("Publication unavailable")
    return {"status": "completed", "warnings": warnings}


def review_prompt():
    return "Prefer test coverage of at least 80 percent."
