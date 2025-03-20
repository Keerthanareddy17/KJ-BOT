import requests
from bs4 import BeautifulSoup

# List of target URLs
urls = [
    "https://kristujayanti.edu.in/",
    "https://www.kristujayanti.edu.in/about/profile.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Sciences/department-forensicscience/MSc-Forensic-Science.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Commerce-Management/economics/bsc_economics.php",
    "https://www.kristujayanti.edu.in/about/history.php",
    "https://www.kristujayanti.edu.in/about/Governing-Body.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Commerce-Management/economics/economics.php",
    "https://www.kristujayanti.edu.in/about/autonomous.php",
    "https://www.kristujayanti.edu.in/home/Jayantian-Code-Conduct.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Commerce-Management/Professional-Management-Studies/bba-Aviation-Management.php",
    "https://www.kristujayanti.edu.in/research/research-centres.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Commerce-Management/Professional-Management-Studies/bba-Business-Analytics.php",
    "https://www.kristujayanti.edu.in/placements/index.php",
    "https://www.kristujayanti.edu.in/studentlife/art_culture.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Commerce-Management/commerce/commerce.php",
    "https://www.kristujayanti.edu.in/studentlife/jayantian-extension-services.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Sciences/department-cs-pg/",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Sciences/department-physical-sciences/BSc-STCS.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Sciences/department-lifescience/Lifescintro.php",
    "https://www.kristujayanti.edu.in/collaborations/collaborations.php",
    "https://www.kristujayanti.edu.in/campus/academic_arena.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Sciences/department-cs-ug/computer_science.php",
    "https://www.kristujayanti.edu.in/academics/College-Arts-Science-Commerce/Faculty-Sciences/department-cs-ug/bca.php",
    "https://www.kristujayanti.edu.in/home/contact-us.php",
    "https://www.kristujayanti.edu.in/achivements/college.php",
]

# File to store scraped data
output_file = "scraped_data.txt"

with open(output_file, "w", encoding="utf-8") as file:
    for url in urls:
        try:
            print(f"Scraping: {url}")

            # Request the page
            response = requests.get(url)
            if response.status_code != 200:
                print(f"❌ Failed to fetch {url}")
                continue

            # Parse HTML
            soup = BeautifulSoup(response.text, "html.parser")

            # Extract text from <p> and heading tags <h1>-<h6>
            paragraphs = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"])
            text_content = "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

            # Write to file
            file.write(f"\n\n===== {url} =====\n\n")
            file.write(text_content + "\n")

        except Exception as e:
            print(f"⚠️ Error scraping {url}: {e}")

print("\n✅ Scraping complete! Data saved in 'scraped_data.txt'.")
