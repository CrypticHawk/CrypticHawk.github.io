import csv

# Read deals from CSV
deals = []
with open('deals.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        deals.append(row)

# HTML Template
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TechSaverSA | Best Tech Deals in South Africa</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>TechSaverSA</h1>
    <nav>
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="contact.html">Contact</a>
      <a href="privacy.html">Privacy</a>
    </nav>
  </header>
  <main>
    <section class="intro">
      <h2>Find the Best Tech Deals in South Africa</h2>
      <p>Curated laptop, phone, and gaming deals from top online stores. Updated daily. Click through to save money!</p>
    </section>
    <section class="deals">
      {deals_section}
    </section>
  </main>
  <footer>
    <p>&copy; 2025 TechSaverSA. All rights reserved.</p>
  </footer>
</body>
</html>
'''

# Generate deals HTML
deals_section = ""
for deal in deals:
    deals_section += f'''
      <article class="deal">
        <h3>{deal['title']} - {deal['price']}</h3>
        <p>{deal['description']}</p>
        <a href="{deal['affiliate_url']}" target="_blank" class="cta">View Deal</a>
      </article>
    '''

# Fill in the template
final_html = html_template.format(deals_section=deals_section)

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("index.html updated with latest deals!")
