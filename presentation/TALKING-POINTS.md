# Talking points, *How prepared is Kenya for a disease outbreak?*

**Six presenters, three slides, two people per slide.**
Companion script for `covid-capacity-deck.html`.

Runtime **12 minutes** presenting plus 5 minutes Q&A, so roughly **two minutes each**.
Every figure quoted below is on the slide behind you, so you never have to remember
a number. You do have to be able to defend it.

---

## 0. Before you start, a 3-minute pre-flight

| Check | How |
|---|---|
| Deck opens | Double-click `covid-capacity-deck.html`. No internet needed: every library and all the data sit inside the file. |
| Full screen | Press **F** once slide 1 is up. Do this before the audience is watching. |
| Navigation | **right arrow / space** forward, **left arrow** back, **1 / 2 / 3** jump to a slide. |
| Slide 1 filter | Reset it to **"All 8,932"** before you present, or Speaker 2's reveal is spoilt. |
| Slide 2 wave | Reset it by pressing **"Release the wave"**, which replays from zero. |
| Slide 3 link | Have `outbreak-stress-capacity.vercel.app` open in another tab in case anyone asks to see the model live. |
| Contingency | It runs in any browser on any machine, including a phone. Email it to two people. |

**One rule for all six of you.** If you are asked a number you do not know, say
*"I don't have that to hand, I'll follow up."* Do not estimate out loud. The
credibility of this project rests on us separating what we measured from what we
assumed. Guessing at the podium destroys that in one sentence.

---

## The four questions, answered once

Speaker 1 opens with WHY and WHEN. Speaker 2 owns WHAT. Speaker 3 owns HOW.
Speaker 6 closes by tying WHEN back to the next outbreak.

| | The answer |
|---|---|
| **WHAT** | A county-by-county stress test of Kenya's inpatient capacity. It turns a register of 8,932 buildings into one decision number per county: how far an outbreak can spread before that county runs out of beds. |
| **WHY** | Because national averages hide county collapse. Kenya's national bed rate looks defensible, and 31 of 47 counties still run out before a 1 in 20 wave. Planning at national level guarantees you fail the counties that fall first, and 31.6 million people live in them. |
| **WHEN** | The data is from **August 2017, three years before COVID-19 arrived.** The answer was available before the emergency, and the same method is available now, before the next one. This is a pre-outbreak instrument, not a post-mortem. |
| **HOW** | Open public data, a transparent calculation, and an explicit statement of what we assumed. Anyone can re-run it, challenge the assumptions and get a different answer, which is what makes it evidence rather than opinion. |

---

# SLIDE 1, SITUATION AND TASK

> Narrative job: make the room feel the question before anybody mentions method.

## Speaker 1, *the situation* (~2 min)

**You own WHY and WHEN. You set the stakes. Do not mention methodology at all.**

**Open on the date, not on yourself.** Let the headline sit for a beat first.

> "On the 13th of March 2020, Kenya confirmed its first COVID-19 case, a traveller
> who had arrived from London a week earlier. Within days, every county government
> in this country needed an answer to the same question."

Then, slowly:

> "If this spreads, do we have the beds?"

**Points to land:**

- Nobody could answer it, because **capacity had never been assessed against an outbreak, county by county.**
- The cost of not knowing: **5,689 Kenyans died**, from 344,162 confirmed cases.
- The uncomfortable part: **the answer already existed.** The Master Health Facility List had been public since 2017. Nobody had asked it this question.
- Frame it: *"This is not a story about a virus. It is a story about a question that was answerable three years early, and wasn't asked."*

**Hand off:** *"So what was actually in that spreadsheet? [Name] will show you."*

---

## Speaker 2, *the data and the task* (~2 min)

**You own WHAT. You drive the rotating facility cloud. This is the most
persuasive thirty seconds in the deck, so rehearse it.**

**Run the interaction, do not describe it.**

1. Start on **"All 8,932"**. Let the cloud turn for a moment.
   > "Every point here is one health facility on Kenya's national register. Eight thousand, nine hundred and thirty-two of them. This is the number that makes national summaries sound reassuring."

2. Click **"Those with inpatient beds."** *Pause. Let the block go dark before you speak, then point at the lit band.*
   > "Only that band at the top. **2,685** of them hold a single inpatient bed. Seven in ten are dispensaries and clinics. They matter enormously for primary care, and not at all when someone cannot breathe."

   The block is deliberately built so height equals count: the lit strip really is three tenths of the whole. If someone asks, say exactly that.

3. Then the sentence that sets up everything after it:
   > "So the real question was never how many facilities Kenya has. It was how many beds, and **where they are**."

**Now state the task and the hypothesis:**

- The task: turn a register of *buildings* into a falsifiable claim about *people*.
- Read the hypothesis off the slide.
- **Emphasise this:** the thresholds were fixed *before* we touched the data. *"We wrote down what would prove us wrong before we could see whether it would."*
- If anyone asks why there is no p-value: **this is a capacity threshold, not a significance test.** You are not testing whether a difference is real, you are testing whether a system clears a bar.

**Hand off:** *"[Name] will show you what we did with that."*

---

# SLIDE 2, ACTION

> Narrative job: show the method as a story, not as arithmetic. Nobody needs the
> equation. They need to watch the country fall over.

## Speaker 3, *how we got there* (~2 min)

**You own HOW. Three sentences of method, then get out of the way.**

**Walk the three numbered beats on the left. Keep it plain.**

1. > "First we counted every bed. Inpatient beds and cots, across all 8,932 facilities. **60,814 places** for the whole country."
2. > "Then we counted the people each county has to cover, from the 2019 census. **47.56 million** Kenyans."
3. > "Then we asked the only question that matters: **for each county, how many of its people can fall ill before its beds are gone?**"

**Then the credibility beat, and this is the one to land:**

> "Before we trusted any of it, we checked the register against the outside world.
> It gives Kenya **12.8 inpatient beds per 10,000 people.** The World Health
> Organisation put Kenya at **13.3** for 2019. Within four percent. The register is
> telling the truth about beds, so everything after this rests on something solid."

- If you have a spare fifteen seconds, add the intuition: *"A bed is a queue. What matters is not how many people arrive, it is how long each one stays. That is the whole calculation."*
- Do **not** put the formula on the table. If someone wants it, it is in the README and in the interactive version, and Speaker 6 will point them there.

**Hand off:** *"So we let the wave move. [Name]."*

---

## Speaker 4, *the wave* (~2 min)

**You own the moment the room goes quiet. You drive the animation. Practise the
timing, because your words have to match what is moving on screen.**

**Press "Release the wave" and then stop talking for three seconds.** Let them watch.

As the dots start turning red, narrate lightly, do not commentate:

> "Every dot is one county, placed at the point where its beds run out. The wave
> moves left to right. Kwale falls first, at under two percent."

As it approaches the dashed line:

> "That dashed line is a one in twenty wave. Five percent of the population infected.
> For context, a moderate flu season reaches one in five."

**When it stops, let the three numbers do the work. Read them out slowly:**

> "Five percent. **Thirty-one of forty-seven counties are out of beds.**
> **Thirty-one point six million Kenyans** live in those counties. That is two in
> every three people in this country."

**Then, if the room is with you, drag the scrubber past the line:**

> "And if it is worse than one in twenty, every county in Kenya is gone by ten percent."

**Then hand the meaning to slide 3:**

> "Sixteen counties are still standing at that point. Which ones, and why, is the
> whole finding. [Name]."

⚠️ If the animation does not play (a cold laptop, a slow projector), the slide still
lands on the final numbers by itself. Just read them. Do not apologise for it and do
not start clicking.

---

# SLIDE 3, RESULT

> Narrative job: deliver the verdict, then prove it was not luck.

## Speaker 5, *the verdict* (~2 min)

**You own the RESULT. Be direct. The hedging comes from Speaker 6, and it lands
much better in that order.**

> "The answer was no. Not in one way. In four, and they are four different
> problems that need four different fixes."

**Take them through the findings panel one at a time. The *pattern* matters more
than any single number:**

| The finding | What it actually means |
|---|---|
| **Not enough, in total.** The country's beds are gone once **1 in 22** Kenyans has been infected. | An absolute shortfall. **No redistribution fixes this.** Only building capacity does. |
| **It sits in the wrong places.** The worse served half gets **9.2 beds per 10,000** against a national 12.8. | Even if the total were adequate, 24 million people are on the wrong side of the average. This one *is* fixable by redistribution. |
| **Too much of it is in one building.** **13 counties** keep over a third of their beds in a single facility. | A fragility that per-person rates cannot see at all. |
| **Most counties have nowhere to refer to.** **32 of 47** hold no Level 5 or 6 referral hospital. | The counties that fall first also have the fewest options when they do. |

- Make the third one concrete: *"Isiolo keeps 58% of its beds in one building. If that hospital is overwhelmed, or becomes the outbreak site itself, Isiolo does not lose a third of its capacity. It loses its capacity."*
- Tie the last two together: *"So the places that run out earliest are also the places with nowhere to send anyone. Those two failures compound, they do not average out."*

**Hand off:** *"Now, a model that agrees with itself proves nothing. [Name] will show you what happened when reality checked our work."*

---

## Speaker 6, *the check and the close* (~2 min)

**You own CREDIBILITY. You are the one who says what is wrong with our own work,
which is exactly why the recommendation at the end gets believed.**

**Open on the paired bars. Point at each pair as you say it, and let the length
of the bars do the work. The whole beat is that they nearly match.**

> "We built this from a 2017 spreadsheet. Three years later, COVID-19 measured the
> same system independently, with different methods. Here is what it found."

- Pair one: we said **60,814 inpatient beds.** A COVID-era surge-capacity study in PLOS One counted **64,181.** **5.2% apart**, from completely separate sources.
- Pair two: we said **12.8 beds per 10,000.** WHO reported **13.3.** **3.9% apart.**
- Pair three: we said **32 of 47 counties have no referral hospital.** COVID found **25 of 47 had no ICU unit at all**, and just **22% of Kenyans lived within two hours of an available one.** Different instrument, same structural fault, found three years early.

**The line that makes this land, and it is on the slide:**

> "Nothing here was fitted to anything. We did not calibrate our numbers against
> theirs, we could not have, ours came first. **The agreement is the evidence.**"

**Now own the limitation before anyone can use it against you. Say this:**

> "One thing we should be straight about. This is a count of beds. The register
> carries no record of oxygen, intensive care or staffing, so this is an
> **optimistic** reading of capacity. And that turned out to matter: during COVID,
> only **58% of Kenya's hospital beds** were in hospitals with oxygen, and the
> country had **537 ICU beds and 256 ventilators** for 47.6 million people. Wherever
> we are wrong, reality is worse than what we have shown you, not better."

**Then the one recommendation. Slow down here.**

> "If you take one name away from this presentation, take **Kwale.** 867,000 people.
> **333 inpatient beds.** That is 3.8 per 10,000 against a national 12.8. No referral
> hospital, and 47% of what it does have sitting inside a single building. Kwale is
> the most exposed county under **every assumption we tested.** Change all of them,
> and the ranking still puts Kwale first. That conclusion does not depend on our
> choices, it follows from capacity alone. **So it is the one to act on.**"

**Point at the link on the slide before you close:**

> "And you do not have to take our scenario. Every parameter, the county map and the
> full triage board are live at **outbreak-stress-capacity.vercel.app**. Change our
> assumptions, and see whether the answer changes."

**Close:**

> "This took open data and one calculation. The next outbreak will not send a warning
> either. But the question is already answerable, for every county, today. That is
> the point."

---

## Q&A, the eight questions you will actually get

Assign an owner to each so nobody talks over anybody.

| # | Question | Owner | Answer |
|---|---|---|---|
| 1 | *"Your data is from 2017, isn't it obsolete?"* | 2 | Partly, and that is the point. The fault lines it exposed were still there in 2020, and COVID measured them independently to within about five percent. Which counties have referral hospitals, and how concentrated their beds are, changes over decades, not years. A current export would sharpen it and we would welcome one. |
| 2 | *"Did you account for ICU beds and oxygen?"* | 6 | **No, and we say so.** The register has no service-level detail at all, so this is a bed count and therefore an optimistic bound. During COVID only 58% of Kenya's beds were in hospitals with oxygen, and there were 537 ICU beds nationally. That makes the real picture worse than ours, not better. |
| 3 | *"Why no p-value?"* | 2 | Because this is a threshold claim, not a difference between groups, so there is no null distribution to test against. We fixed the falsification thresholds in advance instead, which is a stronger commitment, because it means we could not tune the result afterwards. |
| 4 | *"How sensitive is this to your assumptions?"* | 4 | The *count* moves a great deal: across the nine parameter combinations we tested, the number of failing counties ranges from 3 to 47. The *ordering* barely moves, because those constants apply to every county equally. So treat the ranking as the finding and the exact count as a scenario. Kwale is last in all nine runs. |
| 5 | *"Aren't you ignoring that patients cross county lines?"* | 5 | Yes, deliberately, and it is a real limitation. We model counties as closed systems. Since 32 of 47 have no referral hospital, that overstates isolation for small counties near large ones, and understates the load on the receiving county. Cross-county referral is the obvious next piece of work. |
| 6 | *"Isn't Turkana obviously worse off than Mombasa?"* | 5 | On beds per person, yes. But arid counties fail differently. Turkana has 13.6 people per square kilometre, so its binding constraint is distance, not bed count, and a bed 200km away is not a bed. We do not rank them on the same axis, and we say so. |
| 7 | *"Did you count private hospitals?"* | 2 | All of them. Public facilities, meaning Ministry of Health, public institutions and armed forces, hold 56.3% of inpatient capacity. We track the split because private capacity follows income and density rather than planning, and does not respond to an outbreak the way public capacity does. |
| 8 | *"Is this actionable, or just interesting?"* | 6 | Actionable in one specific way. Most of our findings depend on assumptions you can argue with. **Kwale does not.** It is last under every specification we tested. If you fund one thing, that is where the evidence is unambiguous. |

---

## Timing card, tear this off

| Slide | Speaker | Owns | Cue to hand off |
|---|---|---|---|
| 1 | **1**, situation | WHY / WHEN | *"So what was in that spreadsheet?"* |
| 1 | **2**, data and task | WHAT | *"What did we do with that?"* |
| 2 | **3**, how we got there | HOW | *"So we let the wave move."* |
| 2 | **4**, the wave | The moment | *"Which counties are still standing, and why."* |
| 3 | **5**, the verdict | Result | *"A model that agrees with itself proves nothing."* |
| 3 | **6**, the check and close | Credibility | end |

**Sources for every figure quoted:** Kenya Master Health Facility List (2 August
2017, n = 8,932); 2019 Kenya Population and Housing Census (KNBS); Barasa, Ouma &
Okiro, *Assessing the hospital surge capacity of the Kenyan health system in the
face of the COVID-19 pandemic*, PLOS One, 20 July 2020; WHO Global Health Observatory.
