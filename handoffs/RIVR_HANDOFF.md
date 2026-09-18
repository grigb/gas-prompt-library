# RIVR Monorepo Handoff

---
agent_task_id: rivr_2026-02-19
project: rivr-monorepo
type: handoff
status: IN_PROGRESS
priority: MEDIUM
---

## Project Overview

RIVR is a social coordination platform built on a REA (Resource-Events-Agents) semantic graph model. It's designed for bioregional community organizing with features for groups, events, marketplace, governance, and work coordination.

**Current Status**: ~75-80% complete, core functionality working, auth fixed, needs polish

## What's Been Done

### ✅ Completed

1. **Infrastructure Setup**
   - PostgreSQL + PostGIS + pgvector running in Docker
   - MinIO object storage configured
   - Database migrations applied
   - Seed data loaded (68 agents, 78 resources, 231 ledger entries)

2. **Authentication Fixed**
   - Fixed critical Date serialization bug in `src/auth.ts`
   - Login/signup now working
   - JWT session strategy implemented
   - Removed problematic DrizzleAdapter

3. **UI Components**
   - 136 components migrated
   - 70+ pages accessible
   - shadcn/ui integrated
   - Responsive layout with bottom nav

4. **Hydration Fix**
   - Fixed NLPInput placeholder randomization causing hydration mismatch

### ⚠️ Known Issues

1. **Date Serialization Errors (NON-BLOCKING)**
   - Error: `TypeError: Received an instance of Date`
   - Occurs in some API endpoints when database returns timestamp fields
   - Pages still load, but some data fetching may fail
   - **Pattern to fix**: Any `.select()` without field restrictions on tables with timestamps needs to explicitly select fields OR convert Dates to strings

2. **Server Stability**
   - Dev server occasionally becomes unresponsive
   - May need periodic restart with `pkill -f "next dev" && pnpm dev`

3. **Missing API Keys**
   - Mapbox token needed for map tiles (currently placeholder)
   - Stripe keys needed for payments (test mode placeholders)
   - Google Maps/Places keys needed for autocomplete

4. **Lint Broken**
   - ESLint config has circular reference error
   - Does not affect runtime

## Immediate Next Actions

### Priority 1: Fix Date Serialization Errors

The auth.ts fix needs to be applied to other server actions:

```typescript
// BAD - returns all fields including Date objects
const [agent] = await db.select().from(agents).where(...).limit(1);

// GOOD - only select primitive fields
const [agent] = await db
  .select({ id: agents.id, name: agents.name, email: agents.email })
  .from(agents)
  .where(...)
  .limit(1);
```

Files likely needing fixes:
- `src/app/actions/*.ts` - All server actions
- `src/lib/queries/*.ts` - Database queries
- Any API routes that return database rows directly

### Priority 2: Complete Data Layer Wiring

Some pages may still use mock data instead of database queries:
- Review pages for mock data usage
- Replace with proper server action calls
- Test CRUD operations

### Priority 3: Test Coverage

- Unit tests exist but aren't integrated
- E2E tests (Playwright) present but limited
- Add test runner script to package.json

## Access Information

### URLs
- App: http://localhost:3002 (port 3000 was in use)
- Health: http://localhost:3002/api/health
- MinIO: http://localhost:9101 (minioadmin/minioadmin)
- Database: localhost:5432 (rivr/rivr_local_password)

### Test Account
- Email: `testuser123@example.com`
- Password: `TestPassword123!`

### Commands
```bash
# Start infrastructure
docker compose up -d

# Start dev server
export DATABASE_URL="postgresql://rivr:rivr_local_password@localhost:5432/rivr"
pnpm dev

# Database
pnpm db:migrate
pnpm db:seed

# Build
pnpm build
```

## Architecture Notes

### Database Schema (3 core tables)
- `agents` - People, orgs, events, places (hierarchical)
- `resources` - Documents, jobs, tasks, assets, etc.
- `ledger` - Immutable transaction log (47 verb types)

### Key Technologies
- Next.js 15 + React 19 + TypeScript
- PostgreSQL + PostGIS + pgvector
- Drizzle ORM
- NextAuth v5 (beta)
- Tailwind CSS + shadcn/ui
- MinIO (S3-compatible storage)

### File Structure
```
src/
  app/              # Next.js App Router pages
  components/       # React components
  db/               # Database schema, migrations
  lib/              # Utilities, integrations
  app/actions/      # Server actions
```

## Suggested Final Checks

1. Fix remaining Date serialization errors
2. Add real API keys for Mapbox, Stripe, Google
3. Complete data layer wiring (remove mock data)
4. Add proper error boundaries
5. Add loading states
6. Test all CRUD operations
7. Verify permissions system
8. Production build test

## Files Modified During This Session

- `src/auth.ts` - Fixed Date serialization, removed DrizzleAdapter
- `src/components/nlp-input.tsx` - Fixed hydration mismatch
- `docker-compose.yml` - Port configuration
- `.env` - Environment variables

---
agent_task_id: rivr_2026-02-19
