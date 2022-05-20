# Template for Security Reviews

This is the Spearbit template repository for security reviews.

Create GitHub issues with the `finding.md` template and use the appropriate severity labels (see below).

Please run the `create-labels.py` script locally when preparing the audit repository to remove Github's default labels and introduce custom ones in order to improve auditors workflow.

## Workflow

- Leave initial comments / findings on the GitHub pull requests. This can be used to collaboratively
  discuss among the security review team and the client asynchronously.

- Once a finding from a pull request review is finalized, it can be converted into a GitHub issue with the following tags:

  1. Severity: Critical Risk.
  2. Severity: High Risk.
  3. Severity: Medium Risk.
  4. Severity: Low Risk.
  5. Severity: Gas Optimization.
  6. Severity: Informational.
  7. Status: Acknowledged.
  8. Status: Fixed.
  9. Status: ReadyForReport.

| Severity level        | Impact: High | Impact: Medium | Impact: low |
| --------------------- | ------------ | -------------- | ----------- |
| **Likelihood:high**   | Critical     | High           | Medium      |
| **Likelihood:medium** | High         | Medium         | Low         |
| **Likelihood:low**    | Medium       | Low            | Low         |

- These issues should then be polished and properly typeset. This task is mainly aimed at non-lead security researchers and apprentices in the project. Please follow the [style guidelines](https://hackmd.io/@spearbit/S1T63tOqt).

  - Use the [report-generator](https://github.com/spearbit-audits/report-generator) to collect issues into a markdown file to be later compiled into a .pdf via LaTex. This allows the GitHub issues to be a single source of truth.
