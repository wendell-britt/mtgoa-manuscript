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
    "#opener(kind: %s, label: %s, title: %s, subtitle: %s, id: %s)",
    q(kind == "contents" and "front" or kind),
    q(el.attributes["label"]),
    q(stringify(el.content)),
    q(el.attributes["subtitle"]),
    q(el.identifier))

  -- The contents is the one component with no authored body. Its page follows
  -- the opener immediately, and it is generated from the opener marks rather
  -- than from `#outline`, because the openers are designed pages, not headings.
  if kind == "contents" then
    call = call .. "\n#contents-page()"
  end
  return pandoc.RawBlock("typst", call)
end
