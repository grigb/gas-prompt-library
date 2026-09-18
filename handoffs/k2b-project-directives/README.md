# K2B Project-Specific Directives

This directory stores project-bound K2B execution directives.

Rule:
- `general/` is for reusable prompts only.
- Project-specific directives (absolute project roots, project WO IDs, one-off recovery prompts) belong here.

Projects currently tracked:
- `docker-lab/`
- `lan-platform/`
- `universalmanifest/`

If a directive becomes generally reusable, move it into `general/` after removing project-bound paths.
