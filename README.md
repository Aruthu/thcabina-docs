# thcabina-docs

Documentazione e supporto pubblici del tema **THCabina**, serviti da GitHub Pages:
<https://aruthu.github.io/thcabina-docs/>

I due URL che finiscono in `config/settings_schema.json` del tema:

| Campo | Valore |
| --- | --- |
| `theme_documentation_url` | `https://aruthu.github.io/thcabina-docs/guide.html` |
| `theme_support_url` | `https://aruthu.github.io/thcabina-docs/support.html` |

**Non compilarli finché le pagine non rispondono davvero**: un URL plausibile ma morto passa
inosservato, il segnaposto `.invalid` no.

## Cosa c'è

| File | Cos'è |
| --- | --- |
| `index.md` | Landing: cos'è il tema, i link |
| `guide.md` | Guida merchant — **generata**, non si modifica qui |
| `support-policy.md` | Policy di supporto — **generata**, non si modifica qui |
| `support.html` | Il modulo di contatto |
| `thanks.html` | Pagina dopo l'invio |
| `sync.py` | Rigenera le due pagine generate dai sorgenti |

## Rigenerare le pagine

I sorgenti autorevoli sono in `THCabina/docs/`. Qui si rigenera:

```
python sync.py C:/THCabina
```

Lo script aggiunge il front matter, riscrive i link `.md` in `.html` e sostituisce
`[[SUPPORT_FORM_URL]]` con la pagina del modulo. Se resta un `[[SEGNAPOSTO]]` lo segnala.

## Attivare il modulo di contatto

Il form usa [FormSubmit](https://formsubmit.co): nessun backend, allegati e risposta automatica
inclusi. Tre passi:

1. In `support.html`, sostituire `[[SUPPORT_EMAIL]]` nell'attributo `action` con l'indirizzo che deve
   ricevere le richieste.
2. Inviare il form una prima volta: FormSubmit manda una mail di conferma a quell'indirizzo, e il
   canale resta inattivo finché non si clicca il link. Da quel momento gli invii arrivano.
3. Togliere il riquadro **"This form is not live yet."** in cima alla pagina.

La risposta automatica è già scritta nel campo nascosto `_autoresponse` — è un requisito di
ammissione al Theme Store, non un vezzo. Il testo di riferimento sta in
`THCabina/docs/contact-form-spec.md`.

Se un giorno si passa a un helpdesk vero, cambia una riga: l'attributo `action` del form.

## Perché un repo separato

Il repo del tema è privato e il suo codice non si distribuisce fuori dallo Shopify Theme Store. Qui
c'è solo documentazione, che invece deve essere pubblica e linkabile dal listing.
