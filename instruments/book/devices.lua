-- Map the typeset source's structure onto the Typst book design.
--
-- Pandoc's Typst writer drops div classes and heading attributes on the floor —
-- `::: {.marginalia}` and `::: {.postcard}` both come out as a bare `#block[...]`,
-- and a heading's `label=` and `subtitle=` vanish entirely. Everything
-- `instruments/typeset.py` worked out would be thrown away in the conversion.
-- This filter carries it across by emitting raw Typst calls that
-- `instruments/book/mtgoa.typ` defines.
--
-- The EPUB needs no equivalent: pandoc's HTML writer keeps classes, so a div
-- arrives as `<div class="marginalia">` and the stylesheet takes it from there.

local stringify = pandoc.utils.stringify

-- Typst string literal. Backslash first, or the escapes escape each other.
local function q(s)
  local out = tostring(s or ""):gsub("\\", "\\\\"):gsub('"', '\\"')
  return '"' .. out .. '"'
end

local DEVICE = {
  marginalia      = "dev-marginalia",
  epigraph        = "dev-epigraph",
  handbook        = "dev-handbook",
  signature       = "dev-signature",
  postcard        = "dev-postcard",
  sectionsubtitle = "dev-sectionsubtitle",
  centered        = "dev-centered",
}

function Div(el)
  local cls = el.classes[1]
  if cls == "scenebreak" then
    return pandoc.RawBlock("typst", "#scenebreak()")
  end
  local fn = DEVICE[cls]
  if fn == nil then return nil end

  local out = pandoc.List()
  out:insert(pandoc.RawBlock("typst", "#" .. fn .. "["))
  out:extend(el.content)
  out:insert(pandoc.RawBlock("typst", "]"))
  return out
end

function Header(el)
  if el.level ~= 1 then return nil end

  local kind = el.classes[1] or "front"
  local call = string.format(
    "#opener(kind: %s, label: %s, title: %s, clause: %s, subtitle: %s, " ..
    "toctitle: %s, id: %s)",
    q(kind == "contents" and "front" or kind),
    q(el.attributes["label"]),
    q(stringify(el.content)),
    q(el.attributes["clause"]),
    q(el.attributes["subtitle"]),
    q(el.attributes["toctitle"]),
    q(el.identifier))

  -- The contents is the one component with no authored body. Its page follows
  -- the opener immediately, and it is generated from the opener marks rather
  -- than from `#outline`, because the openers are designed pages, not headings.
  if kind == "contents" then
    call = call .. "\n#contents-page()"
  end
  return pandoc.RawBlock("typst", call)
end

-- A paragraph whose whole content is bold is a pseudo-heading, and Typst cannot
-- see that it is one.
--
-- `mtgoa.typ` already sets `show heading: set block(sticky: true)`, so no real
-- section title is ever stranded at the foot of a page with its text overleaf.
-- But the book writes many of its sub-headings as `**bold text**` paragraphs
-- rather than as `###` headings — `The method:`, `Try this now.`, the five
-- `Neutral Channel:` labels — and pandoc renders those as `#strong[...]`, which
-- is not a heading element, so the sticky rule never applies to them. The 2026-08-09
-- proofread found nine pages ending on one.
--
-- Wrapping them in a sticky block is the whole fix: sticky only does anything to
-- a block that would otherwise fall last on a page, so a pseudo-heading mid-page
-- is untouched and one at the foot moves down to sit with the text it heads.
function Para(el)
  local n = #el.content
  while n > 0 and (el.content[n].t == "Space" or el.content[n].t == "SoftBreak") do
    n = n - 1
  end
  if n ~= 1 or el.content[1].t ~= "Strong" then return nil end

  local out = pandoc.List()
  out:insert(pandoc.RawBlock("typst", "#block(sticky: true)["))
  out:insert(el)
  out:insert(pandoc.RawBlock("typst", "]"))
  return out
end
