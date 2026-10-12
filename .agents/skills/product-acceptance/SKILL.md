---
name: product-acceptance
description: After product implementation or authorized release, independently inspect every page/state/feature/flow and actual UI against PRD/mockups/architecture, fix and retest before owner review.
metadata:
  standard_version: 1.0.0
---
# Product acceptance
Read product-definition and full approved inputs. Bind evidence to exact source/build/environment/URL/browser/device/viewport/locale. Use ALL required concrete page instances, nested nodes, tabs/modals and states as denominator. PASS/FAIL/BLOCKED/NA_WITH_REASON; untested never passes.
Open actual desktop/mobile screenshots and inspect against mockups: layout/hierarchy/spacing/fonts/colors/contrast/original imagery/controls/readability/overlap/clipping/zoom/focus/reduced motion. DOM-only checks or builder self-report are not visual acceptance. Click every CTA and verify real outcomes, success/error/empty/loading/timeout/denied permissions/cancel/back/refresh/deep links/storage denied/double actions. Safely verify applicable auth/RLS/data/model/API/form/payment; no unauthorized charges/messages/private records or weakened permissions.
Track defects with severity, reproduction, expected/actual, screenshot/trace, fixing commit and RETEST. Review actual visitor value and architecture/privacy/locale/performance/SEO. No internally accepted verdict with incomplete coverage, uninspected UI, open P0/P1 or unaccepted P2. Fix and rerun regressions before owner review.
Separate built, preview-tested, internally accepted, owner-reviewed, deployed and LIVE_VERIFIED. After separately authorized deployment inspect actual live version/hash and all routes/critical flows; stale preview proof is insufficient. Preserve old site where requested. No repeated backup instead of implementation. Progress is NOT_READY until passed; never repeatedly ask the owner to request review.
Pinned full standard/templates: minyajing-rgb/GGC-AI-Spirituality-Research @ b50cc78567641341419c45a5759811b70f9d0456, .agents/skills/product-acceptance/SKILL.md and skills/product-delivery/.
