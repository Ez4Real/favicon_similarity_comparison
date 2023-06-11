import imagehash
from utils import original_favicons, phishing_favicons

def compare_favicon_hashes(fav1, fav2):
    hash1 = imagehash.average_hash(fav1)
    hash2 = imagehash.average_hash(fav2)
    return hash1 == hash2


# Compare favicons using hashes
match_found = False
for (original_favicon, original_filename) in original_favicons:
    for (phishing_favicon, phishing_filename) in phishing_favicons:
        if compare_favicon_hashes(original_favicon, phishing_favicon):
            match_found = True
            print(f"-!- Hash Match Found: Original {original_filename} and Phishing {phishing_filename} -!-")

if not match_found:
    print("--- No hash matches found. ---")

