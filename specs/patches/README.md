# Patches for `johnair01/bars-engine`

**These are fixes written here and applied there.** The site lives in a different owner's
repository and `add_repo` refuses a cross-owner add — *"cross-tier adds are not supported in
v1"* — so a manuscript session can clone and read `bars-engine` but cannot push to it. That
limit is recorded in `HANDOFF_ANNOUNCE_2026-08-10.md` §6 and it has not moved.

**So the deliverable is a patch, not a branch.** This is the same shape `OPSBACKLOG` C2 already
uses for the Myths Read chapter stamps.

**Apply from the root of a `bars-engine` clone:**

```
git apply --check /path/to/0001-...patch     # dry run, says nothing when it will apply
git am           /path/to/0001-...patch      # applies and commits
```

`git am` preserves the message and authorship. Use `git apply` instead if you would rather write
your own commit.

**`git am` does not run the pre-commit hook.** It runs the `applypatch` hooks only, so this repo's
husky `pre-commit` — and therefore `npm run check` — never fires on an applied patch. **Run the
checks yourself before pushing:**

```
npm ci
npm run check          # db:generate, verify:*, lint, tsc --noEmit
```

**If `git am` fails**, `git am --abort` puts you back exactly where you started; nothing is
half-applied. A conflict means `src/actions/leads.ts` moved after the base commit — the two new
files cannot conflict, since nothing else in the repo has those paths.

---

## `0001-superpower-result-email.patch`

**Written 2026-08-18. Blocks Kickstarter update #29.**
**Base: `7b46505` on `main`** — *"Fix Myths Read chapter stamps to match the shipped trade ebook
(#195)"*, 2026-08-18 13:47 −0700. Verified to apply clean to a fresh clone of `main`.

**The defect.** `src/actions/leads.ts` returned *"Saved. Your result is on its way to your
inbox"* and **contained no send path at all** — it imported `db`, `syncSubscriber` and the list
contract, and nothing else. The address was stored and tagged, and the person received nothing.

**Why it blocks the update.** The update points 371 backers at
`masteringallyship.com/superpower` as the one door onto the list. The reveal states its terms
*before* it asks for the address — *"I will send your result and the Face you ranked last"* —
which made this the only capture surface on the site that discloses the deal up front and the
only one that was breaking it. A fourth broken promise, inside the message whose whole argument
is that the promises are being kept now, is the one failure that message cannot absorb.

**What the patch does.**

| file | |
|---|---|
| `src/lib/email/templates/SuperpowerResultEmail.tsx` | new. The home Face, the Face ranked last, and Chapter 9's reason the second is worth more. Styling mirrors `ChapterOneEmail` so both sends read as one sender. **Nothing is sold in it** |
| `src/lib/email/superpower.ts` | new. Thin wrapper over the canonical `sendEmail`, the shape `awaken.ts` already uses |
| `src/actions/leads.ts` | wires the send in on the established persist-then-send order, and varies the returned message on the result the way `captureChapterOneLead` already does |

**The last part is the half that matters beyond this one bug.** An unconfigured or failing
provider no longer reports success it did not achieve: a skipped send says so, a failed send says
so, and only a real send says the result is on its way.

**Verified.** `tsc --noEmit` exit 0 and `eslint` exit 0 on a full `npm ci`, and the commit passed
the repo's own `precommit:check` — `db:generate`, `verify:server-action-types`,
`verify:prisma-schema`, `verify:transformation-registry-lockstep`, `lint`, `tsc --noEmit`,
`validate-manifest`. `npm run validate:launch-funnel` reports the same 3 pre-existing failures
before and after, all of them missing Obsidian vault documents unrelated to this change.

**What was checked and left alone.** `myths-read` has the same no-send shape and **makes no email
promise**, so it is not a defect and is not touched. `/awaken` writes to the database without
syncing to the ESP — real, and out of scope here.

**Status: applied and pushed** by Wendell on 2026-08-18. `origin/main` is at `e5a62b9e`.

---

## `0002-resend-audience-adapter.patch`

**Written 2026-08-18. Apply after `0001`.**
**Base: `e5a62b9e` on `main`** — verified to apply clean to a fresh clone of live `main`.

**Ruled 2026-08-18 — Wendell: *"set the kit key aside."*** `KIT_API_KEY` is not going to be set.
**Resend is the ESP.** Kit is closed as a question rather than deferred, so `OPSBACKLOG` A1 —
*"Kit account + list landing page… everything downstream waits on this"* — is answered by a
provider that was already live rather than by the account it names.

**Why.** `KIT_API_KEY` was never set in production. Vercel runtime logs on 2026-08-18 show
`[kit] not configured (KIT_API_KEY missing) — skipped sync` on `/nonprofit`, `/introductions` and
`/mastering-allyship/chapter-1` — and **no `[email] not configured` beside them**, which is how we
know Resend is live and Kit never was. Two vendors, one working.

**Resend covers what Kit was chosen for.** `resend@6.14.0`, already installed, exposes `contacts`,
`contactProperties`, `segments`, `topics`, `broadcasts`, `automations` and `events`. Broadcasts
serve the four-a-year promise; Automations replace `sequence:welcome`.

**The mapping.**

| Kit | Resend |
|---|---|
| tag | segment, resolved by name and created if absent |
| custom field | contact property |
| subscriber | contact |

**What did not move.** `list-contract.ts` is untouched. It is pure and decides policy before any
network call, so **the backer promise — roughly four broadcasts a year and no funnel — survived
the provider swap without an edit.** That is the whole return on having written it as a data
structure rather than a code-review comment.

**One real behavioural difference.** Kit created custom fields implicitly. **Resend rejects a
property value whose key was never declared**, so the adapter ensures the keys first and caches
them. It declares every key as `type: 'string'`, which is safe only because the input type is
`Record<string, string>` — widen one and you must widen the other.

**`kit.ts` is kept, not deleted**, with a header saying it is unwired and how to put it back.
Nothing imports it.

**Verified.** `tsc --noEmit` exit 0, `eslint` exit 0, and the commit passed the repo's own
`precommit:check`. Both degradation paths smoke-tested: unconfigured returns
`{ok:true, skipped:true}`, an empty address returns an error, and neither throws.

**What I could not check.** `resend.com` is blocked by this environment's egress proxy, so the
adapter is written against the installed SDK's type definitions rather than the API docs. The
method names and shapes are certain; **whether Automations or Broadcasts need a paid tier on your
plan is not**, and no call has been made against a live key.
