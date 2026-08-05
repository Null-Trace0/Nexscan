import os
from datetime import datetime


def generate_html(data, risk, recommendations, findings):

    os.makedirs("exports", exist_ok=True)

    html = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>NexScan Security Report</title>

<style>

*{{
    margin:0;
    padding:0;
    box-sizing:border-box;
}}

body{{
    background:#0d1117;
    color:#e6edf3;
    font-family:Segoe UI,Arial,sans-serif;
    padding:40px;
}}

.container{{
    max-width:1200px;
    margin:auto;
}}

.header{{
    background:linear-gradient(135deg,#161b22,#1f2937);
    border:1px solid #30363d;
    border-radius:14px;
    padding:40px;
    text-align:center;
    margin-bottom:30px;
    box-shadow:0 10px 30px rgba(0,0,0,.35);
}}

.header h1{{
    font-size:42px;
    color:#58a6ff;
    letter-spacing:2px;
}}

.header p{{
    margin-top:10px;
    color:#8b949e;
    font-size:17px;
}}

.summary{{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:20px;
    margin-bottom:35px;
}}

.card{{
    background:#161b22;
    border:1px solid #30363d;
    border-radius:12px;
    padding:22px;
    text-align:center;
    transition:.2s;
}}

.card:hover{{
    transform:translateY(-4px);
    border-color:#58a6ff;
    box-shadow:0 10px 25px rgba(88,166,255,.18);
}}

.card h3{{
    color:#8b949e;
    margin-bottom:12px;
    font-size:15px;
}}

.card p{{
    font-size:24px;
    font-weight:bold;
}}

.low{{color:#3fb950;}}
.medium{{color:#f2cc60;}}
.high{{color:#ff9800;}}
.critical{{color:#ff4d4d;}}

.section-title{{
    margin:40px 0 15px;
    font-size:28px;
    color:#58a6ff;
    border-left:6px solid #58a6ff;
    padding-left:15px;
}}

table{{
    width:100%;
    border-collapse:collapse;
    overflow:hidden;
    border-radius:10px;
}}

th{{
    background:#238636;
    color:white;
    padding:14px;
    font-size:15px;
}}

td{{
    padding:14px;
    text-align:center;
    border-bottom:1px solid #30363d;
}}

tr:nth-child(even){{
    background:#161b22;
}}

tr:nth-child(odd){{
    background:#21262d;
}}

tr:hover{{
    background:#30363d;
}}

.finding{{
    background:#161b22;
    border-left:6px solid #58a6ff;
    padding:18px;
    border-radius:10px;
    margin-bottom:18px;
    transition:.2s;
}}

.finding:hover{{
    border-left-color:#3fb950;
    transform:translateX(4px);
}}

.finding h3{{
    margin-bottom:10px;
}}

ul{{
    list-style:none;
    margin-top:20px;
}}

li{{
    background:#161b22;
    border-left:5px solid #3fb950;
    margin:12px 0;
    padding:16px;
    border-radius:8px;
}}

.footer{{
    text-align:center;
    margin-top:50px;
    color:#8b949e;
    font-size:14px;
}}

</style>

</head>

<body>

<div class="container">

<div class="header">

<h1>NEXSCAN</h1>

<p>Security Assessment Report</p>

<p>
Generated :
{datetime.now().strftime("%d %B %Y %H:%M:%S")}
</p>

</div>

<div class="summary">

<div class="card">
<h3>🎯 Target</h3>
<p>{data['target']}</p>
</div>

<div class="card">
<h3>📡 Status</h3>
<p>{data['status'].upper()}</p>
</div>

<div class="card">
<h3>⚠ Risk Level</h3>
<p class="{risk.lower()}">{risk}</p>
</div>

<div class="card">
<h3>🔓 Open Ports</h3>
<p>{len(data['ports'])}</p>
</div>

</div>

<h2 class="section-title">Open Ports</h2>

<table>

<tr>

<th>Port</th>
<th>Service</th>
<th>Version</th>

</tr>
"""
    for p in data["ports"]:

        html += f"""
<tr>

<td>{p['port']}</td>

<td>{p['service']}</td>

<td>{p['version'] if p['version'] else 'Unknown'}</td>

</tr>
"""

    html += """
</table>

<h2 class="section-title">Vulnerability Analysis</h2>
"""

    if findings:

        for finding in findings:

            severity = finding["severity"].lower()

            html += f"""
<div class="finding">

<h3 class="{severity}">
{finding['severity']}
</h3>

<p><b>Software:</b> {finding['software']}</p>

<br>

<p>{finding['issue']}</p>

</div>
"""

    else:

        html += """
<div class="finding">

<h3 class="low">No Known Vulnerabilities</h3>

<p>No known vulnerabilities were identified based on the detected service versions.</p>

</div>
"""

    html += """
<h2 class="section-title">Security Recommendations</h2>

<ul>
"""

    if recommendations:

        for rec in recommendations:

            html += f"""
<li>✔ {rec}</li>
"""

    else:

        html += """
<li>No recommendations available.</li>
"""

    html += f"""
</ul>

<div class="footer">

<hr style="margin:40px 0;border:1px solid #30363d;">

<p><strong>NexScan v1.0</strong></p>

<p>Automated Port Scanner & Security Assessment Tool</p>

<p>Generated on {datetime.now().strftime("%d %B %Y %H:%M:%S")}</p>

</div>

</div>

</body>

</html>
"""

    with open("exports/report.html", "w", encoding="utf-8") as f:
        f.write(html)