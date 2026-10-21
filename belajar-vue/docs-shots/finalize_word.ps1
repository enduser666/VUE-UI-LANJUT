$ErrorActionPreference = 'Stop'
$docx = "C:\Users\HP\Documents\P UI 2\belajar-vue\Laporan_Praktikum_PUI_Lanjut_Modul0-1.docx"
$pdf  = "C:\Users\HP\Documents\P UI 2\belajar-vue\docs-shots\preview.pdf"

# lebar area konten = 21 cm - 4 cm - 3 cm = 14 cm; tabel disetel 13.4 cm
$TARGET_W = 13.4 * 28.3464567   # -> poin

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$doc = $word.Documents.Open($docx, $false, $false)

# ---------- normalisasi lebar tabel ----------
$fixed = 0
foreach ($t in $doc.Tables) {
    $t.AllowAutoFit = $false
    $t.PreferredWidthType = 3          # wdPreferredWidthPoints
    $t.PreferredWidth = $TARGET_W
    $n = $t.Columns.Count
    $w = @()
    for ($i = 1; $i -le $n; $i++) { $w += $t.Columns.Item($i).Width }
    $sum = 0
    foreach ($x in $w) { $sum += $x }
    if ($sum -le 0) { $sum = 1 }
    for ($i = 1; $i -le $n; $i++) {
        $t.Columns.Item($i).SetWidth(($TARGET_W * $w[$i - 1] / $sum), 0)  # wdAdjustNone
    }
    $t.Rows.Alignment = 1               # wdAlignRowCenter
    $t.Rows.AllowBreakAcrossPages = $false
    $fixed++
}
Write-Output "Tabel dinormalisasi: $fixed"

# ---------- perbarui seluruh field (termasuk TOC) ----------
for ($i = 0; $i -lt 2; $i++) {
    $doc.Fields.Update() | Out-Null
    foreach ($toc in $doc.TablesOfContents) { $toc.Update() }
    $doc.Repaginate()
}

$pages = $doc.ComputeStatistics(2)
$words = $doc.ComputeStatistics(0)
$chars = $doc.ComputeStatistics(3)

Write-Output "Halaman : $pages"
Write-Output "Kata    : $words"
Write-Output "Karakter: $chars"
Write-Output "Gambar  : $($doc.InlineShapes.Count)"
Write-Output "Tabel   : $($doc.Tables.Count)"
Write-Output "TOC     : $($doc.TablesOfContents.Count)"

$doc.Save()
$doc.ExportAsFixedFormat($pdf, 17)

$doc.Close(0)
$word.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
Write-Output "SELESAI"
