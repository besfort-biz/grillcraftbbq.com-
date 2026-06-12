# Deployment Guide

## Project Structure

```
grillcraftbbq.com/
├── index.html              # Language picker, auto-redirects to /en/
├── _redirects              # Cloudflare Pages rewrite rules
├── assets/
│   ├── css/style.css       # Shared styles (dark theme, product cards, responsive)
│   └── js/script.js        # Mobile nav toggle, hero carousel
├── en/                     # English (default)
│   ├── index.html
│   ├── produkte.html, gastronomie.html, ...
│   └── product-page/       # 31 product detail pages
├── fr/                     # French (same structure)
├── it/                     # Italian (same structure)
├── products.json           # Product data (edit this to add/update products)
├── generate-products.py    # Generates product pages from products.json
└── generate-lang.sh        # (legacy) Generates FR/IT from EN for main pages
```

## Deploy to Cloudflare Pages

### Option A: Manual Upload (Simplest)

1. Go to https://dash.cloudflare.com/ → Pages → Create a project
2. Connect to your Git repo, OR use **Direct Upload**:
   - Upload the entire `grillcraftbbq.com/` directory
   - The `_redirects` file is automatically used by Cloudflare Pages
3. Set custom domain: `grillcraftbbq.com`
4. No build command needed (static HTML)

### Option B: Git Integration

1. Push the `grillcraftbbq.com/` folder to a Git repo
2. In Cloudflare Pages, connect the repo
3. Build settings: Framework = None, Build command = empty, Output dir = `/`

## Domain Setup (Namecheap → Cloudflare)

1. At Namecheap, point nameservers to Cloudflare:
   - `darl.ns.cloudflare.com`
   - `inez.ns.cloudflare.com`
2. In Cloudflare Dashboard → DNS → Add these records:
   - `A` record for `@` pointing to `192.0.2.1` (Cloudflare proxy)
   - `CNAME` record for `www` pointing to `your-project.pages.dev`
3. In Cloudflare Pages → Custom domains → Add `grillcraftbbq.com`

## Formspree Setup

1. Go to https://formspree.io/ and sign up
2. Create a new form → note the Form ID (e.g., `xyzabc123`)
3. In `en/contact.html` (and `fr/contact.html`, `it/contact.html`), find:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
   Replace `YOUR_FORM_ID` with your actual Formspree form ID
4. Free tier: 50 submissions/month

## Updating Product Pages

All product data is in `products.json`. To regenerate:

```bash
python3 generate-products.py
```

This recreates all product pages for EN, FR, and IT.

## Adding a New Language

1. Create the language directory (e.g., `de/`)
2. Run `generate-lang.sh` (or copy pages and change URLs)
3. Add the language to `_redirects` (rewrite rules)
4. Add to language switcher in all existing pages

## Important Notes

- All internal links use extensionless URLs (`/en/produkte` not `/en/produkte.html`)
- The `_redirects` file handles serving the `.html` files for clean URLs
- Product images are served from the Wix CDN (`static.wixstatic.com`) — no rehosting needed
- All products show "Out of stock" — the site is a marketing/brochure site
- Body content for FR and IT pages is currently English — needs native translation

## File Size & Performance

- Total: ~136 HTML files + 2 assets = ~500KB uncompressed
- Cloudflare Pages serves with automatic compression and CDN caching
- No build step needed — upload and go
