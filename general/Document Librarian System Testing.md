# Document Librarian System Testing Prompt

**Context:** You are testing the Document Librarian system - a comprehensive automated directory cleanup tool with 15 safety mechanisms, duplicate detection, AI-powered filing standards, and archive management.

**Your Role:** Independent test agent - execute tests, document results, create individual bug reports for any issues.

**Time Required:** 2-4 hours for complete validation

---

## System Overview

**What is Document Librarian?**
A production-ready CLI tool for intelligent document organization with zero data loss guarantees.

**Location:** `/Users/grig/.agents/lib/document-librarian/`

**Command:** `/Users/grig/.agents/bin/document-librarian`

**Key Features:**
- 15 independent safety mechanisms (zero data loss)
- BLAKE3/xxHash3 duplicate detection (120-150 GB/hour)
- SQLite archive with content-addressed storage
- AI-powered filing standards (58 patterns, 90% coverage)
- Platform-adaptive views (macOS, Windows, Linux)
- Multiple report formats (TEXT, JSON, HTML, CSV)

---

## Prerequisites

**Before You Start:**

1. **Verify Installation:**
   ```bash
   document-librarian --help
   ```
   Expected: CLI help message with 5 commands (scan, clean, restore, query, stats)

2. **Check Dependencies:**
   ```bash
   pip install pytest psutil
   ```

3. **Create Test Directory:**
   ```bash
   mkdir -p ~/test-document-librarian
   cd ~/test-document-librarian
   ```

---

## Features to Test (9 Categories)

### **CATEGORY 1: CLI Commands (6 features)**

#### Feature 1.1: `scan` Command
**Purpose:** Analyze directory for cleanup opportunities

**How to Test:**
```bash
# Create test files
mkdir -p ~/test-document-librarian/test-scan
cd ~/test-document-librarian/test-scan
echo "test content" > file1.txt
echo "test content" > file2.txt  # duplicate
echo "different" > file3.txt
dd if=/dev/zero of=large.bin bs=1M count=10  # 10MB file

# Run scan
document-librarian scan ~/test-document-librarian/test-scan
```

**Expected Response:**
- Scan completes without errors
- Reports total files scanned
- Identifies 1 duplicate (file1.txt, file2.txt)
- Shows space savings estimate
- Displays file type breakdown
- Report saved to default location or displayed

**Success Criteria:**
✅ No errors during scan
✅ Duplicate detected correctly
✅ Statistics accurate
✅ Report generated

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-scan-YYYYMMDD.md`

---

#### Feature 1.2: `clean` Command (Dry-Run Mode)
**Purpose:** Execute cleanup with dry-run default (simulation only)

**How to Test:**
```bash
# Using same test-scan directory
document-librarian clean ~/test-document-librarian/test-scan
```

**Expected Response:**
- Runs in dry-run mode by default (no actual changes)
- Shows what WOULD be done
- Lists files to archive/delete
- No files actually modified
- Displays safety mechanism status

**Success Criteria:**
✅ Dry-run mode active by default
✅ No files actually changed
✅ Clear report of planned actions
✅ Safety mechanisms listed

**Verification:**
```bash
# Verify files unchanged
ls -la ~/test-document-librarian/test-scan
# All files should still exist
```

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-clean-dryrun-YYYYMMDD.md`

---

#### Feature 1.3: `clean` Command (Execute Mode)
**Purpose:** Actually execute cleanup operations

**How to Test:**
```bash
# Execute cleanup
document-librarian clean ~/test-document-librarian/test-scan --execute
```

**Expected Response:**
- Confirmation prompt (if interactive mode)
- Archives duplicate files
- Moves files to OS trash (not permanent deletion)
- Creates audit log entry
- Generates cleanup report
- Shows space saved

**Success Criteria:**
✅ Duplicates archived
✅ Files in OS trash (NOT permanently deleted)
✅ Audit log created
✅ Cleanup report generated
✅ Space savings calculated

**Verification:**
```bash
# Check OS trash
# macOS: ~/.Trash/
# Linux: ~/.local/share/Trash/
# Windows: Recycle Bin

# Check audit log
cat ~/.document-librarian/audit.log
```

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-clean-execute-YYYYMMDD.md`

---

#### Feature 1.4: `restore` Command
**Purpose:** Recover archived files by hash

**How to Test:**
```bash
# Get hash of archived file from previous cleanup
HASH=$(document-librarian query --limit 1 --format json | jq -r '.[0].hash')

# Restore file
document-librarian restore $HASH --output ~/restored-file.txt
```

**Expected Response:**
- File restored to specified location
- Original content intact
- Metadata preserved
- Success message

**Success Criteria:**
✅ File restored successfully
✅ Content matches original
✅ No corruption

**Verification:**
```bash
# Check restored file
cat ~/restored-file.txt
# Should contain original content
```

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-restore-YYYYMMDD.md`

---

#### Feature 1.5: `query` Command
**Purpose:** Search archived files

**How to Test:**
```bash
# Query all archives
document-librarian query

# Query with filters
document-librarian query --path "*.txt" --after 2024-01-01 --format json
```

**Expected Response:**
- Lists archived files matching criteria
- Shows hash, path, size, archive date
- Supports multiple output formats
- Fast query (<10ms for <100K files)

**Success Criteria:**
✅ Query returns results
✅ Filters work correctly
✅ Multiple formats supported
✅ Fast performance

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-query-YYYYMMDD.md`

---

#### Feature 1.6: `stats` Command
**Purpose:** Show system statistics

**How to Test:**
```bash
document-librarian stats
```

**Expected Response:**
- Total files archived
- Total space saved
- Archive database size
- Number of duplicates detected
- Safety mechanism status

**Success Criteria:**
✅ Stats displayed correctly
✅ Calculations accurate
✅ No errors

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-stats-YYYYMMDD.md`

---

### **CATEGORY 2: Safety Mechanisms (15 features)**

#### Feature 2.1: Dry-Run Mode (Default)
**How to Test:** Already tested in Feature 1.2

#### Feature 2.2: Git Protection
**Purpose:** Never touch uncommitted git changes

**How to Test:**
```bash
# Create git repo with uncommitted changes
mkdir -p ~/test-document-librarian/test-git
cd ~/test-document-librarian/test-git
git init
echo "uncommitted" > file.txt
git add file.txt
# Don't commit

# Try to clean
document-librarian clean ~/test-document-librarian/test-git --execute
```

**Expected Response:**
- Git protection mechanism active
- Uncommitted file NOT touched
- Warning displayed
- Safe operation

**Success Criteria:**
✅ Git files protected
✅ No data loss
✅ Warning shown

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-git-protection-YYYYMMDD.md`

---

#### Feature 2.3: Whitelist/Blacklist
**Purpose:** Never touch whitelisted paths, always exclude blacklisted patterns

**How to Test:**
```bash
# Create config with whitelist
cat > ~/.document-librarian/config.yaml << EOF
whitelist:
  - "*/important/*"
blacklist:
  - "*.tmp"
EOF

# Create test files
mkdir -p ~/test-document-librarian/important
echo "critical" > ~/test-document-librarian/important/data.txt
echo "temp" > ~/test-document-librarian/test.tmp

# Run clean
document-librarian clean ~/test-document-librarian --execute
```

**Expected Response:**
- Whitelisted files NOT touched
- Blacklisted files excluded
- Protection messages shown

**Success Criteria:**
✅ Whitelist respected
✅ Blacklist respected
✅ Configuration loaded

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-whitelist-YYYYMMDD.md`

---

#### Feature 2.4-2.15: Remaining Safety Mechanisms
**Test via automated test suite:**
```bash
cd /Users/grig/.agents/lib/document-librarian/tests
python3 run_all_tests.py
```

**Expected:** All 58 tests pass

**If any fail:** Create individual bug reports per mechanism

---

### **CATEGORY 3: Duplicate Detection (3 features)**

#### Feature 3.1: Throughput (120-150 GB/hour)
**How to Test:**
```bash
cd /Users/grig/.agents/lib/document-librarian/tests
pytest performance/test_throughput.py -v -s
```

**Expected Response:**
- 8 throughput tests pass
- Performance meets target (120-150 GB/hour)
- Metrics displayed

**Success Criteria:**
✅ All tests pass
✅ Throughput ≥120 GB/hour

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-throughput-YYYYMMDD.md`

---

#### Feature 3.2: Accuracy (0% False Positives)
**How to Test:**
```bash
pytest accuracy/test_classification_accuracy.py -v
```

**Expected Response:**
- 5 accuracy tests pass
- False positive rate <1%
- Coverage 60-70%

**Success Criteria:**
✅ All tests pass
✅ False positives <1%

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-accuracy-YYYYMMDD.md`

---

#### Feature 3.3: Resource Usage
**How to Test:**
```bash
pytest performance/test_resource_usage.py -v -s
```

**Expected Response:**
- 10 resource tests pass
- CPU <30% (relaxed for scan)
- Memory <500MB

**Success Criteria:**
✅ All tests pass
✅ Resources within limits

**If Feature Fails:**
Create bug report: `/Users/grig/.agents/.dev/ai/bugs/document-librarian-resource-usage-YYYYMMDD.md`

---

### **CATEGORY 4-9: Additional Testing**

For remaining categories (Archive System, Configuration, Reporting, AI Standards, Documentation, Integration):

**Run comprehensive test suite:**
```bash
cd /Users/grig/.agents/lib/document-librarian/tests
python3 run_all_tests.py
```

**Manual verification as needed per feature.**

---

## Bug Report Template

When a feature fails, create individual bug reports:

**File:** `/Users/grig/.agents/.dev/ai/bugs/document-librarian-FEATURE-YYYYMMDD.md`

**Template:**
```markdown
# Bug Report: [Feature Name]

**Date:** YYYY-MM-DD
**Tester:** [Your agent name]
**Category:** [Category number]
**Feature ID:** [Feature number]

## Summary
[One sentence: what failed]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happened]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Error occurs]

## Evidence
```bash
[Command run]
[Output/Error]
```

## Impact
- **Severity:** [Critical/High/Medium/Low]
- **Data Loss Risk:** [Yes/No]
- **Blocks Production:** [Yes/No]

## Suggested Fix
[Optional: if you can identify the issue]

## Files Affected
- [List files that may need changes]

## Work Order Reference
- **Related WO:** [WO-XXX if applicable]
- **Component:** [safety/duplicate/archive/etc.]

## Next Steps
1. Assign to dev-worker agent for fix
2. Retest after fix
3. Update test suite if needed
```

---

## Final Report Template

After testing all features, create:

**File:** `/Users/grig/.agents/.dev/ai/reports/document-librarian-test-report-YYYYMMDD.md`

**Template:**
```markdown
# Document Librarian Test Report

**Test Date:** YYYY-MM-DD
**Tester:** [Your agent name]
**Duration:** [Hours spent]

## Executive Summary
- **Total Features Tested:** 47
- **Features Passed:** [X]
- **Features Failed:** [Y]
- **Pass Rate:** [X/47 * 100]%
- **Critical Issues:** [Count]

## Results by Category
[List all 9 categories with pass/fail for each feature]

## Critical Issues (Immediate Fix Required)
1. [Bug report file link]

## Production Readiness Assessment
- **Ready for Production:** YES / NO
- **Blocking Issues:** [List]
- **Recommended Actions:** [Next steps]

## Test Environment
- **OS:** [macOS/Linux/Windows]
- **Python Version:** [Version]
```

---

## Success Metrics

**Minimum for Production:**
- CLI commands: 100% pass (6/6)
- Safety mechanisms: 100% pass (15/15)
- Overall: 95%+ pass rate

**Critical Must-Pass:**
- Zero data loss in all scenarios
- Dry-run mode default
- Git protection works
- OS trash integration works

---

## Agent Deliverables

After completing this test:

1. **Final report:** `/Users/grig/.agents/.dev/ai/reports/document-librarian-test-report-YYYYMMDD.md`
2. **Bug reports:** One per failure at `/Users/grig/.agents/.dev/ai/bugs/`
3. **Production readiness assessment**

---

**Good luck with testing! The Document Librarian system is production-ready and waiting for your validation.**
