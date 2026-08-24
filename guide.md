---
layout: default
title: Theme guide
---

# THCabina — Theme guide

Everything you need to set up THCabina, in the order you will need it.
Written for merchants: no code required at any step.

Theme version **1.0.0** · Preset **THCabina** · [Support](support.html)

---

## 1. Before you buy

**THCabina is built for stores that let shoppers try items on.** The product page has a dedicated
place — a *try-on slot* — where you install the virtual try-on app of your choice, and product cards
can carry a try-on button that takes the shopper straight to it.

**The slot is a place for an app, not an app itself.** THCabina does not include a virtual try-on
app, and it is not tied to any particular one. Until you install one:

- the try-on area on the product page stays empty, and
- the try-on button does not appear on product cards.

**Everything else in the theme works with no apps installed at all**: product pages, collections,
search, cart, checkout, blog, and every other page. If you never install a try-on app, you still have
a complete store — you are simply not using the feature the theme is named for.

## 2. Install the theme and apply the preset

1. In your Shopify admin, go to **Online Store → Themes**.
2. Find THCabina in your theme library and click **Customize**.
3. The theme ships with one preset, **THCabina**, tuned for apparel. It is applied when you install
   the theme, so what you see on a new store is what you saw in the demo.

To start over at any point, re-apply the THCabina preset from the theme editor. This resets colors,
fonts and spacing; it does not touch your products or pages.

## 3. Tell the theme about your product options

**This is the one step you must not skip.** THCabina never guesses which of your product options is
the color and which is the size — guessing breaks as soon as a store uses another language or another
naming habit. You declare it once, and every block reads it from there.

Go to **Theme settings → Product options**:

| Setting | What it means | Default |
| --- | --- | --- |
| **Color option** | Which option position holds the color. Option 1, Option 2, Option 3, or None. | Option 2 |
| **Size option** | Which option position holds the size. | Option 1 |
| **Default size system** | Apparel or Footwear. Used by the size chart when nothing more specific is set. | Apparel |

The position is what matters, not the name. If your products are set up as Option 1 = Size,
Option 2 = Color, the defaults above are already right. If yours are the other way round, swap the
two settings.

**If you leave an option set to None, the blocks that depend on it render nothing.** That is
deliberate: an empty area is better than a wrong swatch.

### Color swatches

Swatches come from Shopify's own option values. In **Settings → Products → Options**, give each color
value a swatch (a color or an image). THCabina renders whatever you set there — there is no separate
swatch list to maintain in the theme.

### Selling a color as its own product (combined listings)

If you sell each color as a separate product and link them with Shopify's combined listings, the
color swatch links to the matching product instead of switching a variant. Nothing to configure: the
theme follows what Shopify tells it.

## 4. Product metafields

THCabina reads a small set of metafields in the `thcabina` namespace. All of them are optional: a
product without them renders normally, just with fewer rows.

| Metafield | Type | Where it shows |
| --- | --- | --- |
| `thcabina.materials` | Rich text | A row in the Accordion block |
| `thcabina.care` | Rich text | A row in the Accordion block |
| `thcabina.fit` | Rich text | A row in the Accordion block |
| `thcabina.badge` | Single line text | The Badge block, and the badge on product cards |
| `thcabina.size_chart` | Page reference | The page opened by the Size chart block |
| `thcabina.size_system` | Single line text (`apparel` or `footwear`) | Which measurements the size chart announces |

To create them: **Settings → Custom data → Products → Add definition**, using exactly the names
above. Then fill them in on each product, in the Metafields area at the bottom of the product page.

Metafields belonging to your apps stay with those apps. THCabina does not read them, and does not
need them.

## 5. Theme settings

Everything presentational lives in **Theme settings**, so it travels when you copy your configuration
to another storefront (see section 10).

**Colors.** Set the palette once and every page follows: background, surface (cards and panels),
text, muted text, accent, and border. Colors are named by role, never by position, so an accent stays
an accent wherever it is used. Keep enough contrast between text and background — the theme picks
readable text on your accent color, but the palette is yours to choose.

**Typography.** Two fonts: Display for headings, Primary for body text, both from Shopify's font
library.

**Layout.** Page width (Narrow or Wide) and Page margin (10–100 px) set how much room the content
has. The theme is fluid: it adapts continuously between phone and desktop rather than snapping at
fixed sizes.

**Input corner radius** (0–10 px) rounds buttons and fields.

**Product card.** Show try-on button puts a try-on button on every product card. It links to the
product page, scrolled to the try-on slot. Turn it off if you have no try-on app installed.

## 6. The product page

Open a product in the theme editor. The page is made of one Product section plus two more below it.

**Media layout** (a setting on the Product section):

- **Split** — media on both sides, content in the middle. This is the default, and it is the layout
  the try-on slot is designed for.
- **Grid** — all media beside the content column.

Either way, every image, video and 3D model is on the page at once. There is no carousel to click
through.

**Blocks** — drag them into any order you like:

| Block | What it shows |
| --- | --- |
| Brand | The product vendor |
| Title | The product title |
| Rating | Star rating, from your reviews app |
| Price | Price, compare-at price, volume discounts, subscription plans, taxes and unit price |
| Buy buttons | Quantity selector, Add to cart, and accelerated checkout (Shop Pay, Apple Pay, Google Pay) |
| Size chart | Opens the page in `thcabina.size_chart`, announced in the right measurement system |
| Accordion | Materials, care and fit rows, from the metafields above |
| Badge | The text in `thcabina.badge` |
| Description | The product description |
| Pickup availability | Per-variant store pickup |

The variant picker and the try-on slot are always there — they are part of the page, not blocks you
can remove.

You can add up to **12 blocks** to the product page, which leaves room for your try-on app block plus
one more. Below the product, two sections show Product recommendations and Complementary products,
both chosen by Shopify from your catalog.

**Prices that keep up.** If you use volume discounts, the price updates as the shopper changes
quantity. Quantity rules (minimum, maximum, increment) are respected by the quantity selector.
Subscription plans show their own price. All of this comes from Shopify — set it up there and the
theme follows.

## 7. Adding your virtual try-on app

1. Install a virtual try-on app from the Shopify App Store.
2. In the theme editor, open a product page and click **Add block** inside the product content
   column.
3. Under **Apps**, pick the block your try-on app provides.
4. Drag it where you want it in the column, and save.

While the slot is empty, the theme editor shows a reminder in that spot: *Install a virtual try-on
app and drag its block here.* Your customers never see that message — it exists only in the editor.

The try-on button on product cards links to the product page, scrolled to the content column where
you placed the app block. If you have no try-on app, turn the button off in
**Theme settings → Product card**.

## 8. Collections, search and cart

**Collection pages** have filters, sorting and pagination. In the section settings: Products per page
(8–36), Products per row, Enable sorting, Enable filtering. The filters themselves come from
Shopify's Search & Discovery app or from your product data — the theme renders what is there.
Campaign tracking parameters (`utm_*`, Google and Facebook click IDs) survive every filter change, so
your analytics stay intact.

**Search** has the same settings, plus predictive search in the header: products, collections, pages
and articles suggested as the shopper types, on desktop and on mobile.

**Cart** is a full page: quantities change in place, discounts are shown line by line, and shoppers
can add to cart from anywhere without leaving the page they are on.

## 9. Header, footer and the other pages

**Header** — logo, main menu with multi-level dropdowns, customer account menu, cart count and
search. Country, currency and language selectors appear once you have set up markets and languages in
your admin.

**Footer** — up to five blocks, in any order: Newsletter, Menu, Text, Social & Follow on Shop
(Instagram, Facebook, TikTok, YouTube, Pinterest, plus the Follow on Shop button), and Payment icons.

**Every other page** — home, collection list, blog, article, contact, gift card (with a scannable
code and Apple Wallet), password and 404 are all built from sections you can add, reorder and remove.

**Custom Liquid** — a section where you can paste your own Liquid or HTML if you need something the
theme does not offer. Duplicate your theme before you experiment there: what you write in it is yours
to maintain, and theme updates do not apply to code you have edited yourself.

**Five languages out of the box** — English, French, Italian, German and Spanish, for both the
storefront and the theme editor. Add them under **Settings → Languages**.

## 10. Running several storefronts (Shopify Plus)

To give a second storefront the same look:

1. On the configured storefront, open **Online Store → Themes → ⋯ → Edit code** and open
   `config/settings_data.json`.
2. Copy its contents.
3. On the new storefront, install THCabina, open the same file, paste, and save.
4. Reopen the theme editor to confirm the settings arrived.

This copies theme settings — colors, fonts, layout, product options — because THCabina keeps all its
presentational configuration there. It does not copy your sections' content, your products or your
menus, which belong to each store.

**Note on licensing:** Shopify licenses a theme to a single store. Plus merchants need a separate
theme license for each storefront where the theme is used.

## 11. Updates

Shopify installs theme updates for you and carries your customizations over automatically. What each
version changed is in the release notes on the theme's Theme Store page.

If you have edited the theme's code yourself, updates do not apply to your copy — that is Shopify's
rule for every theme, not just this one. Duplicate your theme before editing code, and keep a note of
what you changed.

## 12. FAQ

**The try-on area is empty. Is the theme broken?**
No. THCabina provides the place; the try-on app provides the feature. Install a virtual try-on app
and add its block to the product page (section 7).

**My size chart does not show up.**
Three things have to be true: the product has a `thcabina.size_chart` metafield pointing to a page,
the size system is one the theme knows (`apparel` or `footwear`), and the Size chart block is on the
page. If any is missing, the block renders nothing rather than a broken chart.

**Swatches are not appearing.**
Check **Theme settings → Product options → Color option**: it must point at the option position that
actually holds the color, and that option's values must have swatches assigned in
**Settings → Products → Options**.

**Will I lose my customizations when the theme updates?**
No. Shopify carries settings over automatically for themes installed from the Theme Store.

**Can I use THCabina on more than one store?**
Each store needs its own license. See section 10.

**Which languages are included?**
English, French, Italian, German and Spanish. You can add or edit any translation under
**Settings → Languages**.

## 13. Support

Questions about the theme, setup help and bug reports: **[contact us](support.html)**.

We reply within two business days. What is covered and what is not is set out in the
[support policy](support-policy.html).
