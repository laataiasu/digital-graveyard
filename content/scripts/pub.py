import os
import re
from datetime import datetime

# Create output directory
output_dir = "docs"
os.makedirs(output_dir, exist_ok=True)

# Input list
entries = [
    ("2019_Korupsi dalam Perspektif Pancasila", "https://drive.google.com/open?id=1dwA0AfibVJHrH873BW9V7KOBZHslx4FL"),
    ("2019_Ekonomi Digital sebagai Salah Satu Pilar Pembangunan di Indonesia", "https://drive.google.com/open?id=1dxwmC3pfzaKg_f2LkOE-fMuAJ5-7TtZa"),
    ("2020_Angel Investor and Venture Capitalist as Financing Source of a New Business", "https://drive.google.com/open?id=1f2NT1GR5-MMDDiDp1dYO5jB-8k1MHsT_"),
    ("2020_Apresiasi Film Logan", "https://drive.google.com/open?id=1enMwshj6c3jIj2upbMHGx77_FQMpivOg"),
    ("2020_CLD & SFD Sistem Keamanan Siber pada suatu perusahaan E-Commerce", "https://drive.google.com/open?id=1ecaEPfVCG3I1DsbzYqObaS2dmKsmsm5M"),
    ("2020_Corporate Whistleblowers_What Should Manager Do", "https://drive.google.com/open?id=1ec_rcCYEw2s1RShs3UvJmMtuAhIItfsw"),
    ("2020_Iceberg Phenoment pada Kasus Penanaman Ganja di Aceh ", "https://drive.google.com/open?id=1eNneWFJoY9YvD8_PEioKacOksKGjeIlJ"),
    ("2021_Critique of Designing a Permissioned Blockchain Network for the Halal Industry Paper", "https://drive.google.com/open?id=1eN-dKrn3_ismJ2QE50PWrf466c4NgQhe"),
    ("2021_Dilema Etis pada Desain Human-computer Interaction", "https://drive.google.com/open?id=1eGGb69KAUFzgZNazn1z6Ah72p2csaHwN"),
    ("2021_Isu Cloud computing pada Pembelajaran Jarak Jauh (PJJ)", "https://drive.google.com/open?id=1eDRUXPj56bjbqb67RuVr8aBsGJlpdAsp"),
    ("2021_Repurchase Intention pada Live Streaming-Perspektif Self Determination Theory, Channel Expansion Theory, Flow Theory, dan Expectation Confirmation Theory", "https://drive.google.com/open?id=1e35U8VRV71S6QwKeYPjtLc2h4_zWNugc"),
    ("2021_Sistem Informasi Masjid di Indonesia - Paragraph Development", "https://drive.google.com/open?id=1e0k8zNEFOoF-D5fNi-UUhyKsnKMu5UC5"),
    ("2022_Manajemen Layanan TI pada PT Tokopedia", "https://drive.google.com/open?id=1e-HbeU8dLjTi10foio25IXJTzAxw9zR6"),
    ("2022_Perancangan Dasbor sebagai Pemantauan Metrik pada Platform Google BigQuery (Studi Kasus PT. XYZ)", "https://drive.google.com/open?id=1dywbxbOp8kNsarRlyCubzSa08Q6zlqjk"),
]

# Keyword-based tag suggestions (very basic)
keyword_tags = {
    "korupsi": ["ethics", "corruption"],
    "pancasila": ["philosophy", "ideology"],
    "ekonomi": ["economy"],
    "digital": ["technology", "digital"],
    "investor": ["finance", "startup"],
    "venture": ["finance", "startup"],
    "film": ["media", "film"],
    "keamanan": ["security", "cybersecurity"],
    "siber": ["cybersecurity"],
    "whistleblower": ["ethics", "management"],
    "ganja": ["law", "drugs"],
    "blockchain": ["technology", "blockchain"],
    "cloud": ["cloud", "technology"],
    "pembelajaran": ["education"],
    "repurchase": ["marketing", "ecommerce"],
    "live streaming": ["media", "ecommerce"],
    "masjid": ["religion", "information system"],
    "tokopedia": ["it management", "case study"],
    "dasbor": ["dashboard", "analytics"],
    "bigquery": ["data", "analytics"]
}

def extract_tags(title_lower):
    tags = set()
    for keyword, tag_list in keyword_tags.items():
        if keyword in title_lower:
            tags.update(tag_list)
    return list(tags) if tags else ["general"]

# Create individual markdown files and index
index_lines = ["# Index\n"]

for full_title, url in entries:
    year, title = re.match(r"(\d{4})_(.+)", full_title).groups()
    filename = re.sub(r'\W+', '-', title.lower()).strip('-') + ".md"
    date = f"{year}-01-01"
    tags = extract_tags(title.lower())
    
    md_content = f"""---
title: "{title}"
date: {date}
tags: [{', '.join(f'"{tag}"' for tag in tags)}]
---

[Read the document]({url})
"""

    # Write markdown file
    with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
        f.write(md_content)

    # Append to index
    index_lines.append(f"- [{title}](./{filename})")

# Write index file
with open(os.path.join(output_dir, "index.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(index_lines))

print("✅ Markdown files and index generated in './docs/' directory.")
