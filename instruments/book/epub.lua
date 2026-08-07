-- The EPUB counterpart to devices.lua.
--
-- Far less to do here: pandoc's HTML writer keeps div classes, so every frame
-- device arrives as `<div class="marginalia">` and `instruments/book/epub.css`
-- does the rest. Only the component openers need work, and they need it because
-- of how pandoc splits an EPUB.
--
-- `--split-level=1` cuts a new file at every level-1 heading. Anything emitted
-- *before* that heading lands at the end of the previous chapter, so a chapter
-- label cannot be a sibling paragraph above the title — it has to live inside the
-- heading. It does, as a block-level span, which also means the navigation reads
-- "Chapter 3 The Shaman" rather than a bare "The Shaman". The subtitle stays
-- outside the heading, where it does not go into the navigation.

function Header(el)
  if el.level ~= 1 then return nil end

  local kind = el.classes[1] or "front"
  local id = el.identifier

  -- The generated contents is a print component. An EPUB reader has its own
  -- table of contents, and pandoc writes a nav document besides, so a third one
  -- is a page the reader taps past.
  if kind == "contents" then return {} end

  -- Same for the half title. It is a leaf that protects the title page from the
  -- cover; an ebook has no leaves, and two consecutive screens carrying nothing
  -- but the title reads as a mistake.
  if id == "half-title" then return {} end

  local label = el.attributes["label"]
  local subtitle = el.attributes["subtitle"]

  local head = pandoc.List()
  if label and label ~= "" and (kind == "chapter" or kind == "appendix") then
    head:insert(pandoc.Span({ pandoc.Str(label) }, pandoc.Attr("", { "c-label" })))
    head:insert(pandoc.Space())
  end
  head:extend(el.content)

  -- Both decks, in the order the printed page sets them: the plain clause from
  -- the H1, then the italic subtitle. Neither goes inside the heading, so neither
  -- reaches the navigation, where they would triple the length of every entry.
  local out = pandoc.List()
  out:insert(pandoc.Header(1, head, pandoc.Attr(id, { kind })))
  for _, deck in ipairs({ { el.attributes["clause"], "c-clause" },
                          { subtitle, "c-subtitle" } }) do
    if deck[1] and deck[1] ~= "" then
      out:insert(pandoc.Div({ pandoc.Plain({ pandoc.Str(deck[1]) }) },
                            pandoc.Attr("", { deck[2] })))
    end
  end
  return out
end
