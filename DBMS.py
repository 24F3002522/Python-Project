# -*- coding: utf-8 -*-
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
@page {
    size: A4;
    margin: 1.6cm 1.4cm 1.8cm 1.4cm;
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages) "  |  DBMS Practice Quiz Solutions";
        font-size: 8px;
        color: #888;
    }
}
* { box-sizing: border-box; }
body {
    font-family: 'DejaVu Sans', 'Noto Sans', Arial, sans-serif;
    color: #1e2430;
    font-size: 11px;
    line-height: 1.5;
}
.coverpage {
    text-align: center;
    padding-top: 3.5cm;
}
.coverpage h1 {
    font-size: 30px;
    background: linear-gradient(135deg,#0f766e,#0891b2);
    -webkit-background-clip: text;
    color: #0f766e;
    margin-bottom: 6px;
}
.coverpage .subtitle {
    font-size: 15px;
    color: #475569;
    margin-bottom: 30px;
}
.coverpage .bandbox {
    display: inline-block;
    background: linear-gradient(135deg,#0f766e,#0891b2);
    color: white;
    padding: 14px 30px;
    border-radius: 10px;
    font-size: 13px;
    margin-top: 20px;
}
.coverpage .info-table {
    margin: 40px auto 0 auto;
    border-collapse: collapse;
    font-size: 11.5px;
}
.coverpage .info-table td {
    padding: 7px 16px;
    border-bottom: 1px solid #e2e8f0;
    text-align: left;
}
.coverpage .info-table td.k { color: #64748b; font-weight: bold; width: 220px;}
.toc-title, .section-title {
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    background: linear-gradient(135deg,#0f766e,#0891b2);
    padding: 8px 14px;
    border-radius: 6px;
    margin: 22px 0 14px 0;
    page-break-after: avoid;
}
.answer-key-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 10px;
    margin-bottom: 10px;
}
.answer-key-table th {
    background: #0f766e;
    color: white;
    padding: 6px 5px;
    text-align: left;
}
.answer-key-table td {
    padding: 5px 5px;
    border-bottom: 1px solid #e2e8f0;
    vertical-align: top;
}
.answer-key-table tr:nth-child(even) td { background: #f0fdfa; }
.tag {
    display: inline-block;
    font-size: 8.5px;
    font-weight: bold;
    padding: 2px 7px;
    border-radius: 10px;
    color: white;
}
.tag-mcq { background:#2563eb; }
.tag-msq { background:#7c3aed; }
.tag-sa  { background:#ea580c; }
.tag-extra { background:#0891b2; }
.tag-comp { background: #059669; }

.qcard {
    border: 1px solid #d7dee8;
    border-left: 6px solid #2563eb;
    border-radius: 8px;
    padding: 12px 14px;
    margin-bottom: 16px;
    page-break-inside: avoid;
}
.qcard.msq { border-left-color: #7c3aed; }
.qcard.sa { border-left-color: #ea580c; }
.qcard.extra { border-left-color: #0891b2; }
.qcard.comp { border-left-color: #059669; }

.qhead {
    display: block;
    font-size: 13px;
    font-weight: bold;
    color: #0f172a;
    margin-bottom: 4px;
}
.qmeta { color:#64748b; font-size: 9.5px; margin-bottom:6px; }
.qstem { margin: 6px 0 8px 0; color:#1e2430; }
.options { margin: 6px 0 10px 4px; padding-left: 16px; }
.options li { margin-bottom: 3px; }
.options li.correct { font-weight: bold; color: #065f46; }

.answerbox {
    background: #ecfdf5;
    border: 1.5px solid #10b981;
    border-radius: 6px;
    padding: 8px 12px;
    margin: 8px 0;
    font-weight: bold;
    color: #065f46;
}
.answerbox .lbl { color:#059669; font-size:9.5px; display:block; margin-bottom:2px; font-weight:bold; }

.explain {
    background: #fffbeb;
    border-left: 3px solid #f59e0b;
    border-radius: 4px;
    padding: 8px 12px;
    margin-top: 8px;
}
.explain .lbl { color:#b45309; font-size: 9.5px; font-weight: bold; display:block; margin-bottom: 4px;}
.explain p { margin: 4px 0; }

.verifybox {
    background: #eff6ff;
    border: 1px dashed #3b82f6;
    border-radius: 4px;
    padding: 5px 10px;
    margin-top: 7px;
    font-size: 9.5px;
    color: #1e40af;
}

.code, code {
    font-family: 'DejaVu Sans Mono', monospace;
    background: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 9.5px;
}
pre.code-block {
    font-family: 'DejaVu Sans Mono', monospace;
    background: #0f172a;
    color: #e2e8f0;
    padding: 8px 10px;
    border-radius: 6px;
    font-size: 9px;
    overflow-x: auto;
    margin: 6px 0;
    white-space: pre-wrap;
}
.missingbox {
    background: #fef2f2;
    border: 1.5px solid #ef4444;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 10px;
}
.missingbox .t { color:#b91c1c; font-weight:bold; font-size:12px; display:block; margin-bottom:3px;}
table.small-data {
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 9.5px;
}
table.small-data th, table.small-data td {
    border: 1px solid #cbd5e1;
    padding: 3px 8px;
}
table.small-data th { background:#e0f2fe; }
.note-inline {
    background:#f0f9ff; border-left:3px solid #0284c7; padding:4px 8px; margin:5px 0; border-radius:3px; font-size:9.5px; color:#0c4a6e;
}
</style>
</head>
<body>
"""

TAIL = """
</body>
</html>
"""
