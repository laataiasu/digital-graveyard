import os
import shutil

# Define categories and their files
categories = {
    "Technology & Computing": [
        "AI for Trading.md", "Artificial intelligence.md", "Computer Science.md",
        "Blockchain.md", "Cryptocurrency.md", "Decentralized Finance.md",
        "Digital Garden.md", "Digital Graveyard.md", "Information System.md",
        "Tokopedia DevCamp.md", "youtube-channel", "c.py"
    ],
    "Economics & Finance": [
        "Economy.md", "Investment.md", "Quant.md", "Trading.md", "Data-driven.md",
        "Derivative.md", "Post-scarcity.md", "Randomness.md", "Statistics.md",
        "Fat-tailed distribution.md"
    ],
    "Philosophy & Ethics": [
        "Deontological Ethics.md", "Teleological Ethics.md", "Deterministic Fatalism.md",
        "Epistemology.md", "Mental Model.md", "Don Juan of knowledge.md", "Übermensch.md",
        "Contradiction.md", "Paradox.md", "Self-Conscious.md", "Meta-awareness.md",
        "Transcendence.md", "Takwil.md"
    ],
    "Psychology & Self": [
        "Anxiety.md", "Depression.md", "Resignation.md", "Growth Mindset.md",
        "Eclectic intelligence.md", "Masochist.md", "Audacity.md", "Illusion of control.md",
        "Commitment Bias.md", "Flâneur.md"
    ],
    "Religion & Spirituality": [
        "Allah.md", "Muslim.md", "Solat.md", "Sharia.md", "Gharar.md", "Ghuraba.md",
        "Syubhat.md", "Idul Adha.md", "Idul Fitri.md", "Ramadhan.md", "Takwil.md"
    ],
    "Politics & Society": [
        "Anarchism.md", "Revolutionary Complex.md", "Boycott.md", "Genocide.md",
        "Manufacturing Consent.md", "Social Credit System.md", "Piracy.md",
        "Internet Condom.md", "Esport.md", "Porn.md", "Suicide.md", "Family.md",
        "Woman.md"
    ],
    "Culture & Media": [
        "fiction-character", "I would prefer not to.md", "Meme.md", "Arbeit macht frei.md",
        "Don Juan of knowledge.md", "Sepak Takraw.md", "Luddite.md", "Flâneur.md"
    ],
    "Metaphysics & Abstract Concepts": [
        "Omniscient.md", "Uncertainty.md", "Chaos.md", "Fractal.md", "Utopia.md"
    ]
}

# Move files into their categories
for category, files in categories.items():
    os.makedirs(category, exist_ok=True)
    for filename in files:
        # Handle filenames with quotes or spaces
        clean_name = filename.strip("'\" ")
        if os.path.exists(clean_name):
            try:
                shutil.move(clean_name, os.path.join(category, clean_name))
                print(f"Moved: {clean_name} -> {category}/")
            except Exception as e:
                print(f"Error moving {clean_name}: {e}")
        else:
            print(f"File not found: {clean_name}")
