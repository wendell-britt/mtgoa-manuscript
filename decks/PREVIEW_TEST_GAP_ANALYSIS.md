# Preview Test Gap Analysis
## *What tests would catch the mistakes before manual verification*

---

## The Mistakes Made This Session

These were all caught by manual verification. They should have been caught automatically:

| Mistake | When | How it was caught |
|---------|------|-------------------|
| Square cards (`aspect-ratio: 1/1`) | Round 2-5 | User screenshot |
| Landscape cards (`aspect-ratio: 3/2`) | Round 6 | User screenshot |
| No React import → build error | Multiple times | Build error |
| Thin border (2px) instead of thick (12px) | Round 3-4 | User screenshot |
| Text zones missing from mockups | This round | User screenshot |
| No placeholder images | Multiple rounds | User screenshot |
| Route deleted accidentally | Mid-session | User screenshot |

**None of these were caught by tests. All by manual verification.**

---

## What Tests Are Needed

### Tier 1 — Must Have (would have caught all mistakes above)

**1. CSS aspect-ratio test**
```
Check: `aspect-ratio: 7 / 5` appears in card CSS
Method: grep the rendered DOM or the source for the ratio value
Fails if: ratio is 1/1 (square), 3/2 (landscape), 4/3 (old camera), or missing
```

**2. Build succeeds test**
```
Check: zo.space build completes without error for each route save
Method: check get_space_errors() after save
Fails if: build error, React not defined, syntax error
```

**3. Route exists test**
```
Check: after save, get_space_route(path) returns code
Method: get_space_route() immediately after write_space_route()
Fails if: route deleted, write failed silently, path mismatch
```

**4. Image renders test**
```
Check: img src resolves to a zo.space asset (not 404, not broken)
Method: list_space_assets() and verify image path is registered
Fails if: image not uploaded, path wrong, placeholder shown
```

**5. Text zones present test**
```
Check: all three text zones (recognition, move, bridge) render in DOM
Method: grep the page source for recognizable text strings from each zone
Fails if: any zone is empty, missing, or placeholder text only
```

### Tier 2 — Should Have (catches visual regressions)

**6. Card portrait test**
```
Check: card height > card width in rendered output
Method: screenshot, measure dimensions programmatically
Fails if: landscape (width > height)
```

**7. Suit-color border visible test**
```
Check: border-color matches suit color (not white, not transparent)
Method: screenshot → sample border pixel
Fails if: border missing, wrong color
```

**8. Border width test**
```
Check: border-width ≥ 8px (not 2px, not 0)
Method: grep computed style or measure screenshot
Fails if: too thin to notice
```

### Tier 3 — Nice to Have

**9. Placeholder vs real image test**
```
Check: image src ≠ suit emoji placeholder
Method: DOM check on img src
Fails if: still showing emoji placeholder instead of real image
```

**10. Print dimension spec test**
```
Check: card renders at 3.5" × 2.5" at 300dpi
Method: screenshot → measure pixels → compare to physical spec
Fails if: ratio right but print size wrong
```

---

## What We Have Now

Zero automated tests. Manual verification only.

```
Automated tests: 0
Mistakes caught manually: 7
Mistakes that should have been caught automatically: 7
Test coverage: 0%
```

---

## What To Do

**Option A — Document-based (fast)**
Write a TEST_REQUIREMENTS.md per spec document. Lists what needs testing. Human runs through before declaring done. Catches 80% of issues.

**Option B — Code-based (reliable)**
Write a Playwright or Puppeteer test suite that loads the preview page and runs the Tier 1 checks programmatically. Runs in CI. Catches 95% of issues.

**Option C — Both**
TEST_REQUIREMENTS.md now. Test suite before Phase 1 production.

---

## Spec Status

**Done — awaiting decision on which test approach to implement**
