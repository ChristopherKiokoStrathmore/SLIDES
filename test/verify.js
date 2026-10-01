/* Regression test: the app's arithmetic must match the committed county table.
   Run with `node test/verify.js` after changing the analysis or the data. */
const fs = require('fs');
const path = require('path');

const DATA = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data', 'web_data.json'), 'utf8'));
const WAVE = 84, PEAK = 2.5, UPLIFT = 1.20;
const F = DATA.features;
const NAT_POP = F.reduce((a, d) => a + d.properties.pop, 0);
const NAT_BEDS = F.reduce((a, d) => a + d.properties.beds, 0);

const p = { plan: 0.05, hosp: 0.05, occ: 0.65, los: 8 };
const breakAR = (pop, beds) =>
  beds * (1 - p.occ) * UPLIFT * WAVE / (pop * p.hosp * p.los * PEAK);

const rows = F.map(f => ({ ...f.properties, ar: breakAR(f.properties.pop, f.properties.beds) }))
              .sort((a, b) => a.ar - b.ar);

const asc = [...rows].sort((a, b) => a.beds / a.pop - b.beds / b.pop);
let cum = 0, wb = 0, wp = 0;
for (const r of asc) { if (cum + r.pop > NAT_POP / 2) break; cum += r.pop; wb += r.beds; wp += r.pop; }

const checks = [
  ['counties',            F.length,                                    47],
  ['national population', NAT_POP,                              47564296],
  ['national beds',       NAT_BEDS,                                60814],
  ['national break %',    +(breakAR(NAT_POP, NAT_BEDS) * 100).toFixed(1), 4.5],
  ['immediate counties',  rows.filter(r => r.ar < p.plan).length,      31],
  ['most exposed',        rows[0].county,                        'Kwale'],
  ['worse half beds/10k', +(wb / wp * 1e4).toFixed(1),                9.2],
  ['concentrated',        rows.filter(r => r.largest_share > 1/3).length, 13],
];

let failed = 0;
for (const [name, got, want] of checks) {
  const ok = got === want;
  if (!ok) failed++;
  console.log(`${ok ? 'ok  ' : 'FAIL'}  ${name.padEnd(20)} got ${got}${ok ? '' : `, want ${want}`}`);
}
console.log(failed ? `\n${failed} check(s) failed` : '\nall checks passed');
process.exit(failed ? 1 : 0);
