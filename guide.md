---
layout: default
title: Theme guide
---

# Solea — Theme guide

Everything you need to set up Solea, in the order you will need it.
Written for merchants: no code required at any step.

Theme version **1.0.0** · Preset **Solea** · [Support](https://aruthu.github.io/thcabina-docs/support.html)

---

## 1. Before you buy

**Solea is built for stores that let shoppers try items on.** The product page has a dedicated
place — a *try-on slot* — where you install the virtual try-on app of your choice, and product cards
can carry a try-on button that takes the shopper straight to it.

**The slot is a place for an app, not an app itself.** Solea does not include a virtual try-on
app, and it is not tied to any particular one.

**The app is bought separately.** The try-on app used on the demo store is **Cabina**, built by the
same author as this theme — but it is a separate product on its own subscription, billed by the app
and not covered by your theme purchase. The slot is an open standard place: any virtual try-on app
that ships a theme app block drops into it, and you are free to use another one, or none.

Until you install one:

- the try-on area on the product page stays empty, and
- the try-on button does not appear on product cards.

**Everything else in the theme works with no apps installed at all**: product pages, collections,
search, cart, checkout, blog, and every other page. If you never install a try-on app, you still have
a complete store — you are simply not using the feature the theme is named for.

## 2. Install the theme and apply the preset

1. In your Shopify admin, go to **Online Store → Themes**.
2. Find Solea in your theme library and click **Customize**.
3. The theme ships with one preset, **Solea**, tuned for apparel. It is applied when you install
   the theme, so what you see on a new store is what you saw in the demo.

To start over at any point, re-apply the Solea preset from the theme editor. This resets colors,
fonts and spacing; it does not touch your products or pages.

## 3. Tell the theme about your product options

**This is the one step you must not skip.** Solea never guesses which of your product options is
the color and which is the size. Guessing breaks the moment a store runs in another language, or
simply names its options differently. You declare it once, and every block reads it from there.

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

### If some products are set up differently

These two settings are the **store default**. Option positions are fixed when a product is created,
so a catalog that grew over time — or one that sells clothing **and** shoes — usually has a few
products that disagree: Size is Option 1 on your shirts and Option 2 on your sneakers.

You override the default on those products, and only on those:

| Metafield | Type | What it says |
| --- | --- | --- |
| `thcabina.color_option` | Integer, 0 to 3 | Which option position holds the color **on this product** |
| `thcabina.size_option` | Integer, 0 to 3 | Which option position holds the size **on this product** |

Create them the same way as the metafields in section 4, as **Integer** with a minimum of 0 and a
maximum of 3, then fill them in from **Bulk edit** on the products that need it. `0` means "this
product has no option with that meaning", and the theme renders nothing for it — the same as setting
the theme setting to None.

Products without the metafield keep using the store default, so a catalog that is already consistent
needs none of this. The theme still never guesses from the option names: it reads what you declared,
first on the product, then on the store.

### Color swatches

Swatches come from Shopify's own option values. In **Settings → Products → Options**, give each color
value a swatch (a color or an image). Solea renders whatever you set there — there is no separate
swatch list to maintain in the theme.

### Selling a color as its own product (combined listings)

If you sell each color as a separate product and link them with Shopify's combined listings, the
color swatch links to the matching product instead of switching a variant. Nothing to configure: the
theme follows what Shopify tells it.

## 4. Product metafields

**Worn photo.** Add a file metafield `thcabina.worn_image` (type: File, one image) with a photo of
the product worn. The product gallery then opens on a before/after frame — the main photo against
the worn one, with a slider between them — and a dedicated thumbnail. Leave it empty and the gallery
opens on the main photo as usual. On phones the gallery is swiped: one photo per swipe, a `1 / 6`
counter in the corner, and the thumbnails underneath still jump to any photo.

Solea reads a small set of metafields in the `thcabina` namespace. All of them are optional: a
product without them renders normally, just with fewer details on the page.

| Metafield | Type | Where it shows |
| --- | --- | --- |
| `thcabina.materials` | Rich text | A row in the Accordion block |
| `thcabina.care` | Rich text | A row in the Accordion block |
| `thcabina.fit` | Rich text | A row in the Accordion block |
| `thcabina.badge` | Single line text | The Badge block, and the badge on product cards |
| `thcabina.size_chart` | Page reference | The page opened by the Size chart block |
| `thcabina.size_system` | Single line text (`apparel` or `footwear`) | Which measurements the size chart announces |
| `thcabina.color_option` | Integer, 0 to 3 | Overrides the store default for this product — see section 3 |
| `thcabina.size_option` | Integer, 0 to 3 | Overrides the store default for this product — see section 3 |

`thcabina.size_system` is the one to fill in as soon as you sell two categories. The theme setting in
section 3 is only the fallback: set the metafield to `footwear` on every shoe, and
your shirts and your sneakers announce their own measurements on the same storefront. Pair it with
`thcabina.size_chart`, which is per product too, so each one opens its own size guide page.

To create them: **Settings → Custom data → Products → Add definition**, using exactly the names
above. Then fill them in on each product, in the Metafields area at the bottom of the product page.

Metafields belonging to your apps stay with those apps. Solea does not read them, and does not
need them.

## 5. Theme settings

Everything that controls how the store looks lives in **Theme settings**, so it travels when you copy
your configuration to another storefront (see section 10).

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

Open a product in the theme editor. The page is made of one Product section, plus two more sections below it.

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
| Size chart | Opens the page you set in `thcabina.size_chart`, labeled with the right measurement system |
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

**The cart** is a full page: quantities change in place, and discounts are shown line by line.
Shoppers can also add to cart from anywhere in the store without leaving the page they are on.

**Free shipping bar.** Under **Theme settings → Cart → Free shipping threshold**, enter the amount
(in your store currency) above which you ship for free. The cart and the cart drawer then show how
much is still missing, with a progress bar, and a confirmation once the threshold is reached. Leave
the field empty to hide the bar. The bar does not show to shoppers paying in another currency, where
the comparison would be wrong.

## 9. Header, footer and the other pages

**Header** — logo, main menu with multi-level dropdowns, customer account menu, cart count and
search. Country, currency and language selectors appear once you have set up markets and languages in
your admin.

**Footer** — up to five blocks, in any order: Newsletter, Menu, Text, Social & Follow on Shop
(Instagram, Facebook, TikTok, YouTube, Pinterest, plus the Follow on Shop button), and Payment icons.

**Every other page** — home, collection list, blog, article, contact, gift card (with a scannable
code and Apple Wallet), password and 404 are all built from sections you can add, reorder and remove.

**Custom Liquid** — a section where you can paste your own Liquid or HTML if you need something the
theme does not offer. What you put in it is yours to maintain and is not covered by theme support; if
it breaks a page, empty the field and the page comes back. Theme updates still reach you normally:
this is a setting, not an edit to the theme's code.

**Five languages out of the box** — English, French, Italian, German and Spanish, for both the
storefront and the theme editor. Add them under **Settings → Languages**.

## 10. Running several storefronts (Shopify Plus)

To give a second storefront the same look:

1. On the configured storefront, open **Online Store → Themes → ⋯ → Edit code** and open
   `config/settings_data.json`.
2. Copy its contents.
3. On the new storefront, install Solea, open the same file, paste, and save.
4. Reopen the theme editor to confirm the settings arrived.

This copies theme settings — colors, fonts, layout, product options — because Solea keeps all of
its look-and-feel configuration there. It does not copy your sections' content, your products or your
menus, which belong to each store.

**Note on licensing:** Shopify licenses a theme to a single store. Plus merchants need a separate
theme license for each storefront where the theme is used.

## 11. Updates

Most updates install themselves: Shopify replaces your published theme with the new version and
carries your customizations over — layout, section and block order, settings, images and text. You do
not have to do anything.

Some updates need your approval first. Shopify shows a notice on **Online store → Themes**, adds the
new version as an unpublished theme, and you publish it once you have looked it over. This happens
when an update changes something that cannot be carried over silently.

What each version changed is in the release notes on the theme's Theme Store page.

If you have edited the theme's code yourself, updates do not apply to your copy — that is Shopify's
rule for every theme, not just this one. Duplicate your theme before editing code, and keep a note of
what you changed.

## 12. FAQ

**The try-on area is empty. Is the theme broken?**
No. Solea provides the place; the try-on app provides the feature. Install a virtual try-on app
and add its block to the product page (section 7).

**My size chart does not show up.**
Three things have to be true: the product has a `thcabina.size_chart` metafield pointing to a page,
the size system is one the theme knows (`apparel` or `footwear`), and the Size chart block is on the
page. If any of the three is missing, the block renders nothing rather than a broken chart.

**Swatches are not appearing.**
Check **Theme settings → Product options → Color option**: it must point at the option position that
actually holds the color, and that option's values must have swatches assigned in
**Settings → Products → Options**.

**Will I lose my customizations when the theme updates?**
No. Shopify carries your settings over for themes installed from the Theme Store, whether the update
installs itself or waits for your approval. The exception is a theme whose code you edited yourself:
that copy stops receiving updates.

**Can I use Solea on more than one store?**
Each store needs its own license. See section 10.

**Which languages are included?**
English, French, Italian, German and Spanish. You can add or edit any translation under
**Settings → Languages**.

## 13. Support

Questions about the theme, setup help and bug reports: **[contact us](https://aruthu.github.io/thcabina-docs/support.html)**.

We reply within two business days. What is covered and what is not is set out in the
[support policy](support-policy.html).
