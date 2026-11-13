# API Security Risk Analysis Report

## 1. Executive summary
- API / demo name:
- Owner:
- Assessment date:
- Permission / scope:
- Overall result:
- Limitations:

## 2. API overview
Describe the intended purpose, documented endpoints, data types, and authentication model.

## 3. Assessment method
List approved requests and tools. State whether review was documentation-only, offline sample analysis, or an authorized controlled test.

## 4. Findings
| ID | Area | Evidence | Risk | Recommendation |
|---|---|---|---|---|
| A-01 | Data exposure | [Sanitized response field] | [Low/Medium/High] | [Specific fix] |

### Areas to consider
- Authentication: Are credentials/tokens handled securely?
- Authorization: Is access checked for each object and action?
- Data exposure: Are only necessary fields returned?
- Input validation: Are types, lengths, and allowed values checked?
- Rate limiting: Are documented limits and appropriate responses present?
- Error handling: Do errors avoid revealing secrets or internal implementation details?

## 5. Business impact
Explain what could happen if the finding were present in a real deployment. Clearly separate confirmed evidence from hypothetical impact.

## 6. Remediation
Prioritize least-privilege access, server-side authorization checks, minimal response fields, robust validation, safe error messages, and documented rate limits.

## 7. Limitations
List endpoints and tests not reviewed. Do not claim complete API security from a small sample.

## 8. Conclusion
Summarize the most important risks and the recommended next review.
