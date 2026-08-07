# The 34 `thing` sites the master merge brought back

**2026-08-07.** `thing` was promoted to `gate.py` on 2026-08-03 and the board went to
zero. Merging 149 commits from `origin/master` on 2026-08-07 reintroduced **34
uncovered hits** across nine chapters, one appendix, the author's note and the author
bio. The gate was red from the merge commit `776df67` until `abada55`.

## The rule that governed the repair

**Wendell, 2026-08-07,** on a first table that swapped eight of the 34 for `it`, `what`,
or nothing:

> *"we need to replace the thing turning it to an it doesn't provide more clarity. The
> rule is that we're replacing 'the thing' because it's not giving people more
> specificity."*

**A pronoun is the same vagueness with fewer letters.** The deletion is worse, because it
hides that a noun was owed. Every site needed the noun that was actually meant, which
means every site needed reading before it needed editing:

> *"we need to look at these 34 in their context to make sure these changes aren't messing
> up the message their contexts are providing."*

**That instruction changed five of the 34**, and one of the five reversed the rule's own
letter. All five are below.

## What the context changed

**`ch1:70` had no noun to promote.** *"Most people arrive at allyship carrying two
things"* — the two are a wish and a set of questions, named in the next two sentences.
Nothing could be swapped in place, so the sentence names both loads up front and the
sentences after it stop announcing themselves as first and second.

A second defect surfaced in the rewrite: *"The questions never get said out loud"* is
agentless where the original was active. **`Nobody says the questions out loud`**, which
also matches ch1's existing construction at `:48` — *nobody has ever asked your opinion
about the rota.*

**`ch1:137` was wrong in the neuter before it was wrong in the noun.** *"keep everything
away from the player it guards until that thing proves harmless."* The next paragraph is
entirely about people: *Some of the people who hurt this person arrived offering help.*
And the bouncer checks **you**. → **`keep everyone away … until the newcomer proves
harmless.`**

**`ch1:149` is the one site where the rule's letter and the paragraph's logic pull
apart.** The paragraph is a ladder — same content, escalating audience:

> Saying what you noticed, to one person, is about as small as it gets… **Saying the
> [X] to somebody's face in front of other people** asks for far more.

**Naming a new noun breaks the ladder**, because what makes the second rung expensive is
the audience, not different material. The first table proposed *the unsaid charge*, which
quietly changes the content and destroys the comparison. The repair repeats the noun
phrase from the sentence before: **`Saying what you noticed to somebody's face, with
other people listening`**. No pronoun, no new noun, and the repetition is what makes the
ladder visible.

**`ch6:466` took `the map` and the sentence had to give up a copy.** *"because you also
know what the map is for, building the map so the next person can run it without you"*
puts the noun twice in eleven words. The earlier clause yields — **`because you also know
what it is for`** — and the noun lands once, where it does the work.

**`ch8:647` took `load`, not `weight`.** *"carries weight it has already agreed to carry,
and asking it to account for the weight is one more weight to carry"* is three. **`one
more load to carry`** picks up the next sentence — *Take load off without requiring the
account* — so the swap earns an echo instead of spending one.

## The other twenty-nine

| site | was | now |
|---|---|---|
| `ch1:48` | a say in how **things** run | how the work gets **scheduled** |
| `ch1:141` | three **things** about you | three **questions** about you |
| `ch1:143` | **things** you do / a **thing** you are | The first two **you do**. The third **you are** |
| `ch1:165` | the best **thing** that ever happened to that arrangement | the best **luck** that arrangement ever had |
| `ch1:310` | Writing **things** down | Writing **the charge** down |
| `ch2:441` | Move like the **thing** that cost Imani | **the one who** cost Imani |
| `ch2:443` | does the same **thing** | makes the same **error** |
| `ch2:445` | the only **thing** left | the only **move** left |
| `ch3:125` | The Shaman means one **thing** by it: somebody said the true **thing** | The Shaman's definition is **narrow**: somebody said the **unsaid charge** |
| `ch4:603` | the one **thing** it will not take as evidence | the one **signal** |
| `ch4:726` | saying the **thing** that needed saying | saying **what needed saying** |
| `ch5:605` | which **thing**, or why | **what they are holding**, or why |
| `ch8:641` | trains two **things** rather than one | two **capacities** |
| `ch9:512` | one **thing** that keeps not happening | one **outcome** |
| `ch9:526` | try this unfinished **thing** with me | try this with me **before it is finished** |
| `ch9:526` | the least useful **thing** a human being can hand you | the least useful **response** |
| `ch9:528` | asked for one **thing** | one **favour** |
| `ch9:570` | the first **thing** they do differently | the first **change** they make |
| `ON_THE_SHOULDERS_OF:56` | I did two **things** to it that count as departures | I made two **departures from their model** |
| `authors_note:19` | the only **thing** that moves anybody / the only **thing** the rules measure | the only **work** / the only **measure the rules have** |
| `about_the_author:5` | the two **things** he knows best | the two **fields** |

**And ×5, one per domain section** (`ch4 ch5 ch6 ch7 ch8`): *These are not four **things**
to study* → **These four are not a syllabus.**

## Verified

`gate` PASS on all four surfaces. `review.py` clean on all eight steps: voice, gate, diet
within baseline, em-dash within budget, seam, citations 0 uncredited, round-trip
byte-identical, empty-head. `shipcheck` **SHIPPABLE**, no blocker outstanding.

## Still open — ch3's two drifted glosses

Master's own `thing` sweep rewrote two of ch3's four domain glosses from nominal to clause
form:

- *Direct Action — the true **thing** said to the face* → **you say it to their face**
- *Skillful Organizing — the **thing** the group won't say* → **you say what the group
  won't**

ch3's template now carries **two clause-form glosses and two nominal**, while all twenty
in the five domain sections are nominal. This is a set that used to be consistent and is
not any more. **Restoring ch3's two to nominal form is a decision for Wendell**, not a
defect to fix quietly — master made the change deliberately under the same rule, and it
may be the better form.
