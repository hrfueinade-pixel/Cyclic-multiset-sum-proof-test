-- Give prose exclusions room without changing the maintained Markdown tables.
function Table(tbl)
  local labels = {}
  for _, row in ipairs(tbl.head.rows) do
    for _, cell in ipairs(row.cells) do
      labels[#labels + 1] = pandoc.utils.stringify(cell.contents)
    end
  end
  local header = table.concat(labels, " ")
  local widths
  if header:match("Cycle length") and header:match("Exclusion") then
    widths = {0.14, 0.18, 0.68}
  elseif header:match("Necessary equation") then
    widths = {0.12, 0.12, 0.27, 0.49}
  end
  if widths then
    for i, width in ipairs(widths) do
      tbl.colspecs[i][2] = width
    end
  end
  return tbl
end
