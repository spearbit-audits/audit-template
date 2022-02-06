# Template for Security Reviews

This is the Spearbit template repository for security reviews.

Create GitHub issues with the `finding` template and use the appropriate severity labels (see below).

## Workflow


- Leave initial comments / findings on the GitHub pull requests. This can be used to collaboratively
  discuss among the security review team and the client asynchronously.

- Once a finding from a pull request review is finalized, this can be converted into a GitHub issue with tags:

  1. Severity: Critical Risk  (for issues with high impact and high likelihood)
  2. Severity: High Risk,
  3. Severity: Medium Risk
  4. Severity: Low Risk,
  5. Severity: Gas Optimization,
  6. Severity: Informational.

| Severity level        | Impact: High | Impact: Medium | Impact: low |
|-----------------------|--------------|----------------|-------------|
| **Likelihood:high**   | Critical     | High           | Medium      |
| **Likelihood:medium** | High         | Medium         | Low         |
| **Likelihood:low**    | Medium       | Low            | Low         |

- These issues can then be written well, polished, properly typeset, etc. This task is mainly aimed at the non-lead security researchers and apprentices in the project. Please follow the [style guidelines](https://hackmd.io/@spearbit/S1T63tOqt).

    - These issues are semi-automatically compiled into a PDF report. See [report template](https://github.com/spearbit-audits/report-template).

    - Use the [script](https://github.com/spearbit-audits/compile-issues) to collect issues from the repository into a markdown file. This allows the GitHub issues to be the single source of truth. Therefore, all the edits can be made directly in the issue.

    - Use the [script](https://github.com/spearbit-audits/compile-review-comments) to collect review comments from a specified PR into a markdown file.


