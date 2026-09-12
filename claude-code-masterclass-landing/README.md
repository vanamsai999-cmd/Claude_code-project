# Claude Code Masterclass — Landing Page

Landing page for the Claude Code masterclass ($97/month, beginner-or-overwhelmed
→ confident).

## Contents

| File | What it is |
| --- | --- |
| [`PROMPT.md`](./PROMPT.md) | The original brief — hand this to a developer or an AI coding agent to rebuild or restyle the page |
| `index.html` | The page. Semantic HTML, all copy written, no build step |
| `styles.css` | All styling. Every colour, size, and spacing value is a CSS custom property in the `:root` block at the top |
| `main.js` | Nav state, mobile menu, accordions, scroll reveals, the hero terminal animation, and CTA analytics |

## Running it

Open `index.html` in a browser. That's it — no dependencies, no build, no server
required. To deploy, upload the three files to any static host (Netlify, Vercel,
Cloudflare Pages, GitHub Pages, S3).

## Before you publish: fill in the placeholders

Every unfilled value renders as a dashed, orange `{{TOKEN}}` on the page so
nothing ships half-done. Find them all with:

```sh
grep -o '{{[A-Z_]*}}' index.html | sort -u
```

| Placeholder | Uses | What to put there |
| --- | --- | --- |
| `{{SITE_URL}}` | 6 | Canonical URL, used in Open Graph, Twitter card, and JSON-LD |
| `{{CHECKOUT_URL}}` | 5 | Stripe/Gumroad/Kajabi link for the $97/mo plan — every CTA points here |
| `{{CANCEL_POLICY}}` | 4 | e.g. "Cancel any time, no questions asked" |
| `{{BRAND_NAME}}` | 4 | Your name or business name (nav, footer, JSON-LD provider) |
| `{{FORMAT}}` | 3 | Live or recorded? Cadence and time zone |
| `{{SOCIAL_LINKS}}` | 2 | Replace the span with real `<a>` links |
| `{{INSTRUCTOR_NAME}}` | 2 | Who teaches it |
| `{{GUARANTEE}}` | 2 | e.g. "30-day refund" — or delete the surrounding text |
| `{{INSTRUCTOR_BIO}}` | 1 | 2–3 sentences on why you're the person to teach this |
| `{{INSTRUCTOR_PHOTO}}` | 1 | Swap the placeholder avatar for an `<img>` (the markup is commented in place) |
| `{{START_DATE}}` | 1 | Human-readable, e.g. "March 4" or "Join any time" |
| `{{START_DATE_ISO}}` | 1 | Same date as `YYYY-MM-DD`, for JSON-LD |
| `{{TIME_COMMITMENT}}` | 1 | e.g. "two to three hours a week" (FAQ) |
| `{{CONTACT_EMAIL}}` | 1 | Footer contact link |
| `{{PRIVACY_URL}}` / `{{TERMS_URL}}` | 1 each | Footer legal links |

You'll also want to add an `og-image.png` (1200×630) next to `index.html`.

## Also needs a decision

- **Testimonials are omitted, not written.** The markup is commented out in
  `index.html` under `SOCIAL PROOF`. Uncomment and fill it in when you have 2–3
  real quotes with names, roles, and permission to quote. Don't ship invented ones.
- **The membership tiles over-promise by default.** Delete any tile in the
  `MEMBERSHIP` section — and the matching line in the pricing checklist — that
  isn't actually part of your offer.
- **Analytics.** Drop your snippet into the commented block in `<head>`. Every
  CTA already fires a `cta_click` event with a `section` property
  (`hero` / `nav` / `pricing` / `final`); see `trackCta()` in `main.js`. Plausible,
  GA4, and GTM dataLayer are wired; add others there.

## Reskinning

All design tokens are in one `:root` block at the top of `styles.css` — colours,
type scale, spacing, radii. Changing `--accent` and `--bg` restyles the whole
page. Two notes if you change the palette:

- `--text-faint` and the `--accent-deep` gradient end were chosen so that
  every piece of normal-size text clears WCAG AA (4.5:1). Re-check contrast if
  you darken either.
- The page is deliberately dark in both light and dark system themes.

## Verified

Checked in headless Chromium at 1280 / 1024 / 768 / 375px:

- No horizontal overflow at any of those widths
- Keyboard: skip link is the first tab stop; accordions toggle with Enter and
  Space; collapsed panels are out of the tab order and the accessibility tree
- One `<h1>`, no skipped heading levels, all nine sections labelled, landmarks present
- All normal-size text at or above 4.5:1 contrast
- `prefers-reduced-motion`: the terminal renders its final state immediately and
  scroll reveals are disabled
- Valid `Course` JSON-LD carrying the $97.00 USD monthly price
- No console or page errors
