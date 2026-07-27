# Grant Filing Dossier Prompt

Use this prompt when preparing, filing, recording, or closing a formal grant application.

First read:

`/Users/grig/.agents/docs/methodologies/grant-filing-dossier-methodology.md`

Then check the active project for project-local defaults at:

`{PROJECT_ROOT}/.dev/ai/processes/grant-filing-dossier/`

If present, read:

- `README.md`
- `style-guide.md`
- `distributed-creatives-defaults.md` or equivalent project defaults

## Operating Mode

You are creating or updating a grant filing dossier.

Do not scatter grant records across loose attachment folders, chat summaries, Desktop downloads, or browser-only state. Every formal grant gets one dossier with a complete filing record.

## Required Actions

For a new grant:

1. Create `YYYY-grantor-program-name/`.
2. Create required folders:
   - `form-record/`
   - `filed-materials/attachments/`
   - `filed-materials/submitted-application/`
   - `source-assets/`
   - `results/`
   - `archive/`
3. Create `README.md` and `application-record.md` from templates.
4. Record grantor, program, applicant, deadline, amount, project, and application URL.
5. Apply project-local filename and attachment style rules.

For attachment preparation:

1. Read the project-local style guide before designing PDFs.
2. Use recipient-facing filenames.
3. Store source assets.
4. Store superseded versions in `archive/`.
5. Verify PDF size and extractable text where possible.

For submitted grants:

1. Save the submitted application print or receipt into `filed-materials/submitted-application/`.
2. Create `form-record/submission-confirmation.md`.
3. Extract text from the submitted application print when possible.
4. Record submission timestamp, submitted by, submission ID, submission URL, print URL, form status, grant status, amount requested, attachment list, and agreement values.
5. Record funder-normalized attachment filenames if the portal changes display names.
6. Generate SHA-256 checksums for submitted PDFs.
7. Update `results/README.md` to pending review.

For decisions:

1. Record decision date.
2. Record award or denial.
3. Record award amount, conditions, contract/payment steps, and reporting obligations.
4. Preserve denial records as organizational knowledge.

## Verification

Before finishing, verify:

- all referenced paths exist;
- no stale pre-submission language remains after filing;
- uploaded filenames match the project-local naming rule;
- submitted application print is saved;
- extracted text or extraction failure note exists;
- checksums exist;
- result tracker is current.

