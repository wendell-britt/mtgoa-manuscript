# Patches for `johnair01/bars-engine`

**These are fixes written here and applied there.** The site lives in a different owner's
repository and `add_repo` refuses a cross-owner add — *"cross-tier adds are not supported in
v1"* — so a manuscript session can clone and read `bars-engine` but cannot push to it. That
limit is recorded in `HANDOFF_ANNOUNCE_2026-08-10.md` §6 and it has not moved.

**So the deliverable is a patch, not a branch.** This is the same shape `OPSBACKLOG` C2 already
uses for the Myths Read chapter stamps.

**Apply from the root of a `bars-engine` clone:**

```
git am /path/to/0001-superpower-result-email.patch
```

`git am` preserves the message and authorship. Use `git apply` instead if you would rather write
your own commit.

---

## `0001-superpower-result-email.patch`

**Written 2026-08-18. Blocks Kickstarter update #29.**

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
syncing to Kit — real, and out of scope here.
