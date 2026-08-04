# Kenya outbreak capacity — county triage

An interactive map that triages Kenya's 47 counties by the cumulative attack rate
at which their surge inpatient capacity is exhausted. Move the scenario controls
and the counties re-triage; the hypothesis is re-tested on every change.

Built from the Kenya Master Health Facility List (August 2017, n=8,932) and the
2019 Kenya Population and Housing Census.

## Run it

```bash
python3 -m http.server 8000     # then open http://localhost:8000
```

Or just double-click `index.html` — the data, the map geometry and D3 are all
bundled, so it works offline from `file://`. The only network request is for
webfonts, and it falls back to system sans if those don't load.

## Deploy

**GitHub Pages** — push to `main`; `.github/workflows/pages.yml` publishes the
repo root. Enable Pages under Settings → Pages → Source: GitHub Actions.

**Netlify / Vercel / Cloudflare Pages** — no build command, publish directory `.`.

**Any static host** — upload `index.html` and `vendor/`. Nothing else is needed
at runtime; `data/`, `src/` and `test/` are build-time only.

## Rebuild after changing the analysis

`index.html` embeds a *snapshot* of the data. Change the numbers upstream and the
page will quietly keep showing the old ones until you rebuild.

```bash
python3 src/prep_data.py        # county_capacity.csv + geojson -> data/web_data.json
python3 src/build.py            # data + template            -> index.html
node test/verify.js             # confirm the app still matches the notebook
```

`src/prep_data.py` expects `county_capacity.csv` and `kenya_counties.geojson` in
the working directory — run it from `data/`, or edit the paths at the top.

## The model

For each county, the attack rate at which peak inpatient demand exactly exhausts
surge-available beds:

```
                beds x (1 - occupancy) x 1.20 x 84
attack rate* = -------------------------------------
                pop x hospRate x lengthOfStay x 2.5
```

The step from peak admissions per day to concurrent beds is Little's Law
(L = λW): beds occupied equals arrival rate times length of stay.

Fixed constants: 84-day wave, peak daily incidence at 2.5x the wave average,
20% surge uplift from cancelling electives and converting wards.

**Only two of the seven inputs are measured.** Beds and population come from the
source data. Occupancy, surge uplift and the peak factor are assumptions;
hospitalisation rate and length of stay are pathogen properties the user sets.

## What the tool cannot tell you

The facility list carries no ICU, oxygen, isolation or laboratory information —
the `Service_names` column is empty in all 8,932 rows — and no staffing data.
Kenya's binding constraints during COVID were oxygen and critical-care staffing
rather than general beds, so **every figure here is an optimistic bound**.

Two further caveats worth stating alongside any result:

- Hospitalisation rates in the literature come largely from populations with a
  median age near 40. Kenya's is around 20, so an imported rate likely overstates
  admissions. This pushes the opposite way from the beds-only limitation; the
  magnitudes are unknown and they should not be assumed to cancel.
- Counties are modelled as closed systems, but 32 of 47 have no Level 5/6
  referral facility, so severe cases cross boundaries in reality.

This is a static peak calculation, not an epidemic model. There is no
transmission dynamic and no depletion of susceptibles — the wave shape is
imposed by two constants rather than emerging from an SEIR process.

## Layout

```
index.html                  built artifact - do not edit by hand
vendor/d3.min.js            D3 v7.8.5, bundled for offline use
data/web_data.json          embedded payload: geometry + county metrics
data/county_capacity.csv    county table from the analysis notebook
data/kenya_counties.geojson source boundaries
src/app.template.html       the app, with a __DATA__ placeholder
src/prep_data.py            builds web_data.json
src/build.py                builds index.html
test/verify.js              regression test against the notebook's numbers
```

## Sources

County boundaries are a community GitHub dataset, adequate for analysis but not
authoritative. For publication, substitute official boundaries — OCHA's Kenya
admin boundaries on HDX, or the IEBC/KNBS county shapefiles — and re-run
`test/verify.js` to confirm nothing shifted.
