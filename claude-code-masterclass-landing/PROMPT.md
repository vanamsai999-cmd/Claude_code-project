# Prompt: Claude Code Masterclass Landing Page

Hand this to a front-end UI developer (human or AI coding agent). Fill in the
**Fill these in first** block below before sending — everything else is ready to
use as-is.

---

## ⚠️ Fill these in first

Replace every `{{PLACEHOLDER}}` in the prompt. If you leave one blank, tell the
developer to render a visible `TODO` marker rather than inventing a fact — no
made-up testimonials, student counts, logos, or credentials.

| Placeholder | What it is |
| --- | --- |
| `{{BRAND_NAME}}` | Your name or business name shown in the nav |
| `{{INSTRUCTOR_NAME}}` | Who teaches the masterclass |
| `{{INSTRUCTOR_BIO}}` | 2–3 sentences: why you're the person to teach this |
| `{{INSTRUCTOR_PHOTO}}` | Path/URL to headshot, or `TODO` |
| `{{CHECKOUT_URL}}` | Stripe/Gumroad/Kajabi checkout link for the $97/mo plan |
| `{{START_DATE}}` | Cohort/kickoff date, or "Join any time" if evergreen |
| `{{FORMAT}}` | Live calls? Recorded? Community? Cadence and time zone |
| `{{TESTIMONIALS}}` | Real quotes + names + roles, or omit the section entirely |
| `{{SOCIAL_LINKS}}` | YouTube / X / LinkedIn / newsletter URLs |
| `{{CANCEL_POLICY}}` | e.g. "Cancel any time, no questions asked" |
| `{{GUARANTEE}}` | e.g. "30-day refund" — or delete the guarantee block |

---

## The prompt

> Build a single-page marketing site for a paid online masterclass.
>
> ### Product
>
> **{{BRAND_NAME}} presents the Claude Code Masterclass** — a membership that
> takes developers from *beginner or overwhelmed* to *genuinely confident* using
> Claude Code, Anthropic's agentic coding tool that runs in the terminal, the
> desktop app, the web, and IDE extensions.
>
> - **Price: $97/month.** {{CANCEL_POLICY}}
> - **Taught by:** {{INSTRUCTOR_NAME}} — {{INSTRUCTOR_BIO}}
> - **Format:** {{FORMAT}}
> - **Starts:** {{START_DATE}}
> - **Checkout:** every primary CTA links to `{{CHECKOUT_URL}}`
>
> ### Audience and the emotional arc
>
> The visitor is a working developer, indie hacker, or technical founder who has
> heard Claude Code is a step change but feels behind. They may have installed
> it, run a few prompts, gotten mediocre results, and quietly concluded they're
> using it wrong. They are not stupid and they hate being talked down to. They
> are also skeptical of AI-course hype.
>
> The page must move them along this arc, in this order:
>
> 1. **Recognition** — "that's exactly how I feel." Name the overwhelm precisely.
> 2. **Reframe** — the gap isn't talent, it's a workflow nobody taught them.
> 3. **Proof** — concrete, specific things they'll be able to do.
> 4. **Confidence** — this is a guided path with a real person, not 40 hours of video.
> 5. **Low-risk action** — $97/month, cancel any time, start today.
>
> ### Required sections, in order
>
> 1. **Sticky nav** — logo/wordmark left; anchor links (Curriculum, Pricing, FAQ)
>    center; a small "Join for $97/mo" button right. The button fades in only
>    after the hero scrolls past. Collapses to a hamburger under 768px.
>
> 2. **Hero** — the whole job of this section is recognition plus a price-visible
>    CTA.
>    - Eyebrow: a short credibility or urgency line (cohort date, or "For
>      developers who already installed Claude Code and still feel lost").
>    - H1: one clear promise, ≤ 12 words. Transformation, not features.
>      Draft to beat: *"Go from overwhelmed to genuinely dangerous with Claude Code."*
>    - Subhead: 1–2 sentences naming the specific pain and the specific outcome.
>    - Primary CTA button: **"Join the Masterclass — $97/month"** → `{{CHECKOUT_URL}}`
>    - Secondary CTA: ghost button, "See what's inside" → scrolls to curriculum.
>    - Under the CTAs: a single reassurance line ({{CANCEL_POLICY}}).
>    - Visual: an abstract, tasteful terminal motif — a mock Claude Code session
>      with a typed prompt and a few streaming output lines, monospace, animated
>      once on load with a caret. Respect `prefers-reduced-motion` (render the
>      final state immediately). Do **not** use stock photos of people at laptops.
>
> 3. **"Sound familiar?" — the pain section.** Three or four short cards, each a
>    real thought the visitor has had. Examples to adapt: *"I get great demos and
>    then it edits the wrong file."* / *"I don't know when to trust it and when to
>    check every line."* / *"Everyone's shipping with agents and I'm still
>    copy-pasting into a chat window."* Keep it honest and specific; no fear-mongering.
>
> 4. **The transformation — before/after.** Two columns, "Where you are now" vs.
>    "Where you'll be in 30 days." 4–5 paired rows. This is the emotional spine
>    of the page; give it room and strong typographic contrast.
>
> 5. **Curriculum / what's inside.** 5–6 modules as an accordion (first one open
>    by default). Each module: number, title, one-line outcome, 3–4 bullet
>    sub-topics. Suggested spine, adapt freely:
>    - *Module 1 — Your first hour*: install, permissions and safe defaults, the
>      mental model of an agentic coding tool.
>    - *Module 2 — Prompting for real codebases*: scoping tasks, giving context,
>      knowing what to hand over and what to keep.
>    - *Module 3 — CLAUDE.md, memory, and project setup*: making Claude fluent in
>      your repo.
>    - *Module 4 — Skills, subagents, and MCP*: extending Claude Code past the defaults.
>    - *Module 5 — Real workflows*: refactors, test suites, code review, debugging
>      a bug you can't reproduce.
>    - *Module 6 — Shipping with confidence*: reviewing agent output, git hygiene,
>      guardrails, and knowing when to say no.
>
> 6. **What you get with membership.** Icon grid, 4–6 tiles — e.g. live sessions,
>    recordings, private community, prompt/config library, office hours, new
>    modules as Claude Code ships features. Only list what actually exists.
>
> 7. **Instructor.** {{INSTRUCTOR_PHOTO}}, {{INSTRUCTOR_NAME}}, {{INSTRUCTOR_BIO}},
>    {{SOCIAL_LINKS}}. Warm and human — this is the trust section.
>
> 8. **Social proof.** Render {{TESTIMONIALS}} as 2–3 cards with name, role, and
>    photo if available. **If no testimonials are supplied, omit this section
>    entirely** rather than using placeholder quotes.
>
> 9. **Pricing.** The conversion section. One card, centered, clearly the only
>    option — do not invent a fake three-tier comparison table.
>    - Large `$97` with a `/month` in muted, smaller type beside it.
>    - A checklist of 6–8 included items, reusing the membership tiles.
>    - CTA: **"Start today — $97/month"** → `{{CHECKOUT_URL}}`
>    - Below: {{CANCEL_POLICY}} and {{GUARANTEE}}, plus accepted payment methods.
>    - Optional subtle badge: "Locked-in rate — your price never goes up."
>    - Give the card a soft accent glow/border so it reads as the page's focal point.
>
> 10. **FAQ.** Accordion, 6–8 entries. Must answer the real objections:
>     "Do I need to be an experienced developer?", "What if I've never used the
>     terminal?", "Does this work with my language/stack?", "How much time per
>     week?", "Do I need a paid Claude plan?", "What if I cancel?",
>     "Will this be outdated in three months?", "Live or self-paced?"
>
> 11. **Final CTA band.** Full-width accent background, one headline restating the
>     transformation, one button, one reassurance line. No new information.
>
> 12. **Footer.** Copyright, {{SOCIAL_LINKS}}, contact email, privacy and terms
>     links, and a plain-language line clarifying that this is an independent
>     course and not affiliated with or endorsed by Anthropic.
>
> ### Design direction
>
> - **Tone:** confident, calm, developer-native. Think a well-made docs site or
>   dev-tool homepage — not a Facebook-ads course funnel. No countdown timers, no
>   fake scarcity, no "$1,997 value" strikethroughs, no neon gradient blobs.
> - **Palette:** dark-first. Deep neutral background (near-black, slightly warm),
>   off-white body text, and **one** saturated accent used only for CTAs, active
>   states, and the pricing card. Muted secondary text for supporting copy.
> - **Type:** one geometric or neo-grotesque sans for UI and headings, one
>   monospace for code, terminal motifs, and module numbers. Tight tracking on
>   large headings. Generous line-height (1.6+) on body copy. Cap measure at ~68ch.
> - **Space:** large and confident — 96–128px section padding on desktop, 56–64px
>   on mobile. Whitespace is the main signal that this isn't a cheap course.
> - **Motion:** restrained. Fade-and-rise on section entry (≤ 400ms), a subtle
>   lift on card hover, the one-time hero terminal type-out. Everything gated
>   behind `prefers-reduced-motion: reduce`.
> - **Depth:** 1px hairline borders and low-opacity surface fills rather than
>   heavy drop shadows.
>
> ### Copywriting rules
>
> - Write all copy; don't leave lorem ipsum.
> - Second person. Short sentences. Concrete verbs.
> - Lead with outcomes ("ship a refactor you'd actually merge"), not features
>   ("6 modules of video").
> - Never claim affiliation with or endorsement by Anthropic.
> - No invented numbers — no student counts, ratings, "as seen in" logos, or
>   earnings claims. If a stat isn't supplied, cut the sentence.
> - Every CTA says the price. The visitor should never wonder what it costs.
>
> ### Technical requirements
>
> - Single responsive page. Breakpoints at 640 / 768 / 1024 / 1280px; verify at
>   375px wide with no horizontal scroll.
> - Semantic HTML: one `<h1>`, ordered heading levels, `<section>` with
>   `aria-labelledby`, real `<button>`/`<a>` elements.
> - Accessibility: WCAG AA contrast throughout (check the accent on dark),
>   visible focus rings, keyboard-operable accordions with correct
>   `aria-expanded`/`aria-controls`, alt text on every image, skip-to-content link.
> - Performance: no heavy libraries for animation or icons — inline SVG and CSS.
>   Self-host or `font-display: swap` the fonts. Lazy-load below-fold images.
>   Target Lighthouse ≥ 95 on performance and accessibility.
> - SEO/social: descriptive `<title>` and meta description, Open Graph and Twitter
>   card tags, canonical URL, and `Course`/`Offer` JSON-LD carrying the $97/month
>   price.
> - Analytics: leave a clearly commented placeholder in `<head>`, and fire a
>   `cta_click` event from every CTA with the section name as a property.
> - Ship clean, commented, componentized code with design tokens (colors, spacing,
>   type scale) defined once as CSS custom properties so the palette can be
>   reskinned from a single block.
>
> ### Deliverable
>
> A working page I can open in a browser and deploy as a static site. Include a
> short README listing every placeholder still to be filled and where the copy
> lives.

---

## Notes for whoever sends this

- **Trim before you send.** If the masterclass has no community or no live calls,
  delete those bullets — an over-promising brief produces an over-promising page.
- **Stack.** Add one line naming your preference (plain HTML/CSS/JS, Next.js +
  Tailwind, Astro…). Without it, the developer will pick, and static HTML + CSS
  is the safest default for a single landing page.
- **Using this with an AI coding agent?** Paste the "The prompt" section as-is,
  then iterate section by section ("redo the hero, make the headline harder")
  rather than asking for whole-page rewrites.
