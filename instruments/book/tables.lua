-- Size every table column by what is in it, not by how the author typed the rule.
--
-- ## The defect
--
-- The Five Channels table in Chapter 3 came out with its last column one syllable
-- per line — "The / Su- / per- / power" — while the column beside it ran a third
-- of the measure.
--
-- The cause is not Typst and not the table. It is this line in `manuscript/ch3.md`:
--
--     |---------|---------|-----------------|------------|---|
--
-- In a pandoc pipe table the dashes in the delimiter row **are a width spec**.
-- Nine, nine, seventeen, twelve, three, so pandoc assigns the last column 6% of
-- the measure and Typst honours it. At 9.6pt, 6% of a 6x9 text block is about
-- three characters, which is the width the word "Superpower" was given.
--
-- Every table in the book is specified this way, because nobody typing a
-- manuscript is writing a width spec when they hold down the hyphen key:
--
--     ch3:440   [ 9,  9, 17, 12,  3]  ->  18% 18% 34% 24%  6%
--     ch3:591   [16,  6]              ->  73% 27%
--     ch3:681   [ 3,  3,  3]          ->  33% 33% 33%
--     ch4:270   [ 6, 11, 31]          ->  12% 23% 65%     (and ch5, ch6, ch7, ch8)
--     APX-A:151 [ 8, 15]              ->  35% 65%
--     APX-E:111 [16,  6]              ->  73% 27%
--
-- So the widths are overwritten rather than respected. That is a deliberate
-- override of something the file technically says, and it is the right call here:
-- there is no case in this manuscript where a dash count is a considered decision
-- about a printed column, and one of them was unreadable.
--
-- ## The replacement
--
-- Two numbers per column:
--
--   width    the longest cell in it, which is what the column wants
--   floor    the longest single word, which is what it cannot go below without
--            breaking a word across lines
--
-- Shares come from `width`. Then any column whose share is under its floor is
-- raised to the floor and the rest are renormalised over what is left. Without
-- that pass a table with one long column and one short one starves the short one
-- into exactly the defect this exists to fix.
--
-- Both builds load this. Pandoc's HTML writer emits the same shares as `<col
-- style="width: …">`, so the EPUB gets the proportions too, and a reader narrow
-- enough to ignore them falls back to its own layout.

local stringify = pandoc.utils.stringify

-- Usable measure in characters, at the table's 9.6pt. Passed in by the builder,
-- because the workbook trim is wider than the trade one and the floor is the one
-- number here that has to know the difference.
local MEASURE = 58

-- No column takes more than this, whatever its content says.
local CEILING = 0.6

local function scan(rows, width, floor)
  for _, row in ipairs(rows) do
    local col = 1
    for _, cell in ipairs(row.cells) do
      local span = cell.col_span or 1
      -- A spanning cell says nothing about any single column it covers.
      if span == 1 and width[col] then
        local s = stringify(cell.contents):gsub("%s+", " ")
        if #s > width[col] then width[col] = #s end
        for w in s:gmatch("[^%s%-–—/]+") do
          if #w > floor[col] then floor[col] = #w end
        end
      end
      col = col + span
    end
  end
end

local function fix_table(tbl)
  local ncol = #tbl.colspecs
  if ncol < 2 then return nil end

  local width, floor = {}, {}
  for i = 1, ncol do width[i], floor[i] = 1, 1 end

  scan(tbl.head.rows, width, floor)
  for _, body in ipairs(tbl.bodies) do
    scan(body.head, width, floor)
    scan(body.body, width, floor)
  end
  if tbl.foot then scan(tbl.foot.rows, width, floor) end

  local total = 0
  for i = 1, ncol do total = total + width[i] end
  if total == 0 then return nil end

  local share, pinned = {}, {}
  for i = 1, ncol do
    share[i] = width[i] / total
    pinned[i] = false
  end

  -- Two passes. One raises the starved columns; the second lets a column starved
  -- by the first raise get its floor too. A third gains nothing on a table this
  -- size, and everything is renormalised at the end regardless.
  for _ = 1, 2 do
    local free, taken = 0, 0
    for i = 1, ncol do
      if not pinned[i] and share[i] * MEASURE < floor[i] then
        share[i] = math.min(floor[i] / MEASURE, CEILING)
        pinned[i] = true
      end
      if pinned[i] then taken = taken + share[i] else free = free + share[i] end
    end
    if taken == 0 or taken >= 1 or free == 0 then break end
    local scale = (1 - taken) / free
    for i = 1, ncol do
      if not pinned[i] then share[i] = share[i] * scale end
    end
  end

  local sum = 0
  for i = 1, ncol do sum = sum + share[i] end
  for i = 1, ncol do
    tbl.colspecs[i] = { tbl.colspecs[i][1], share[i] / sum }
  end
  return tbl
end

function Pandoc(doc)
  local m = doc.meta["table-measure"]
  if m ~= nil then MEASURE = tonumber(stringify(m)) or MEASURE end
  return doc:walk({ Table = fix_table })
end
