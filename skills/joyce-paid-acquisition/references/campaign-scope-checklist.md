# Campaign scope and launch checklist

This is a reusable scope for cold-start tests, not a fixed campaign template. Record each item as **verified**, **not available**, **not applicable**, or **open**, with a link/screenshot and date. Do not silently treat an unchecked item as complete.

## 1. Product and market

- One product per campaign brief. Specify offer, product maturity, truthful promise, landing page, and primary success action (e.g. completed reservation or purchase intent, not just a click).
- Separate English/US and Chinese/Chinese-speaking APAC cells. Specify exact countries/regions, currency, local time, age 22–55 default, all-gender default, language, audience signal, exclusions, audience expansion, and estimated reach. Check the destination from the target geography and a real mobile connection.
- Check all network connection types are included; if the platform exposes no network filter, record "no filter available / all connections". Check device/OS restrictions, placements, and creative-safe zones.
- Avoid claiming a household-income or interest suggestion is a hard restriction when automated audience expansion is on.

## 2. Experiment and spend

- State the question being tested and the one primary success metric. Distinguish direction-finding from a randomized A/B experiment. Keep image and video in separately identifiable cells, with separate language markets and attribution codes.
- Choose campaign objective and optimization event that match available measurement. If optimizing landing-page views while judging reservation intent downstream, say so explicitly. Check attribution window/model, bidding, budget distribution, total cap, account currency, schedule/time zone, learning-period implications, and end-date expiry.
- Record guardrails for broken page/form, incorrect locale, unexpectedly high spend, or failed event delivery. Do not infer willingness to pay from CTR or clicks alone.

## 3. Creative and destination

- Inventory and quality-check every uploaded asset: source, rights, dimensions, crop, resolution, spelling, CTA, current URL/QR code, brand identity, mobile readability, video sound/subtitles, and target language. Confirm the platform shows the intended count after save/reload.
- Fill available text/headline/description/CTA options with real, differentiated copy. Verify each claim against the live product and landing page. Review previews across feed, stories, and vertical video placements; do not substitute a local montage for a platform preview.
- Verify Facebook/Instagram/Page identity, display URL, final URL, HTTPS, mobile load, locale, price/offer clarity, privacy notice, form/booking completion, and thank-you state. Browser add-ons or chat buttons should have a staffed destination and a measurement purpose.

## 4. Attribution and measurement

- Use unique UTMs per product, market, language, format, test cell, and creative where supported. Preserve source/medium/campaign/content through redirects and reservation or checkout; record platform campaign/ad/ad-set IDs when available.
- Instrument the funnel: landing view → CTA click → reservation/checkout start → plan/price selection → form submission or purchase intent → confirmed reservation or paid purchase. Deduplicate repeated submissions and distinguish test traffic from real users.
- Verify first-party events end-to-end. If using Meta Pixel/CAPI or another platform API, verify the correct product data source, event mapping, browser/server deduplication, consent/privacy text, and test events before claiming platform conversion attribution. Never send chat contents, sensitive relationship details, or raw private contact data into ad events unnecessarily.
- Reconcile platform clicks and landing sessions, then completed reservations and purchases. Note attribution-window and cross-device limitations; do not present a diagnostic click as a real customer conversion.

## 5. Preview, approval, launch, review

- Give Joyce a reviewable platform preview/editor link plus creative overview and a compact table of final settings, unresolved gaps, and expected spend. Wait for approval of this version before publishing.
- After publication, reopen the exact campaign, ad set, and ads to verify review status, on/off status, schedule, destination, asset count, and actual delivery. Do not report "live" from a saved draft or publish click alone.
- At 24/48/72 hours (or agreed cadence), report spend, impressions, reach, frequency, CTR, CPC, landing-page views, CTA rate, reservation/paid intent, cost per qualified action, creative/market split, measurement issues, and decision. Keep low-sample conclusions tentative.
