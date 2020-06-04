# Lown Syntax Reference

## Headers

| Lown     | HTML         |
|----------|--------------|
| `[h1 …]` | `<h1>…</h1>` |
| `[h2 …]` | `<h2>…</h2>` |
| `[h3 …]` | `<h3>…</h3>` |

## Emphasis

| Lown        | HTML                         |
|-------------|------------------------------|
| `[b …]`     | `<strong>…</strong>`         |
| `[i …]`     | `<em>…</em>`                 |
| `[u …]`     | `<u>…</u>`                   |
| `[s …]`     | `<s>…</s>`                   |
| `[ins …]`   | `<ins>…</ins>`               |
| `[del …]`   | `<del>…</del>`               |
| `[big …]`   | `<div class="big">…</div>`   |
| `[small …]` | `<div class="small">…</div>` |

## Lists

| Lown         | HTML                  |
|--------------|-----------------------|
| `[ol]…[/ol]` | `<ol>…</ol>`          |
| `[ul]…[/ul]` | `<ul>…</ul>`          |
| `[li item]`  | `<li>item</li>`       |
| `[dl]…[/dl]` | `<dl>…</dl>`          |
| `[dt …]`     | `<dt>…</dt>`          |
| `[dd …]`     | `<dd>…</dd>`          |

## Quotes

| Lown         | HTML                            |
|--------------|---------------------------------|
| `[q …]`      | `<q>…</q>`                      |
| `[bq]…[/bq]` | `<blockquote>…</blockquote>`    |
| `[@ …]`      | `<span class="author">…</span>` |

## Links and images

| Lown           | HTML                        |
|----------------|-----------------------------|
| `[url www… …]` | `<a href="www…">…</a>`      |
| `[img www… …]` | `</img src="www…" alt="…">` |

## Code and maths

| Lown             | HTML                                   |
|------------------|----------------------------------------|
| `[.py …]`        | `<code class="python">…</code>`        |
| `[.py]…[/.py]`   | `<pre class="python">…</code>`         |
| `[pre]…[/pre]`   | `<pre>…</pre>`                         |
| `[$ …]`          | `\(…\)`                                |
| `[$$]…[/$$]`     | `\[…\]`                                |

## Alignment and visibility

| Lown                 | HTML                                      |
|----------------------|-------------------------------------------|
| `[right]…[/right]`   | `<div style="text-align: right">…</div>`  |
| `[center]…[/center]` | `<div style="text-align: center">…</div>` |
| `[left]…[/left]`     | `<div style="text-align: left">…</div>`   |
| `[spoiler …]`        | `<span class="spoiler">…</span>`          |
| `[/hr]`              | `</hr>`                                   |
| `[/br]`              | `</br>`                                   |

## Emojis

| Lown       | Emoji |
|------------|-------|
| `:cactus:` | 🌵    |
| `:tv:`     | 📺    |
| …          | …     |

The complete list is available [here](src/emojis.csv).
