# FUTURE_CS_03 — API Security Risk Analysis

## Objective
Review a sample/demo API's documented behavior and sample responses for authentication, authorization, data exposure, input validation, and rate-limiting risks.

## Safe testing boundary
Use only a public demo API intended for learning, a local mock API, or an API for which you have explicit permission. Do not enumerate hidden endpoints, bypass access controls, fuzz production systems, or send high-volume requests. This starter project uses a local fictional API example and offline review; it does not attack or probe a live service.

## Tools
- Postman or Insomnia for approved, low-impact requests
- Browser DevTools
- Google Docs / MS Word / PDF for the final report

## Review checklist
1. Identify the API owner, documentation, intended use, and authorized scope.
2. Determine whether authentication is required for sensitive operations.
3. Check whether a user can access only their own authorized records (authorization must be verified by the owner in a controlled test).
4. Look for unnecessary personal or confidential fields in sample responses.
5. Review documented input validation and error handling.
6. Review documented rate-limit behavior and response headers.
7. Record evidence, impact, and defensive recommendations.

## Repository contents
- `examples/mock_api_response.json` — fictional response for offline analysis
- `api_review.py` — offline data-exposure review of the sample JSON
- `report/api-security-risk-report.md` — report template

## Run
```bash
python api_review.py examples/mock_api_response.json
```
