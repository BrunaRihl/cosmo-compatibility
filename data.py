from datetime import date

signs = {
    "Aries": {
        "start": date(2023, 3, 21),
        "end": date(2023, 4, 19)
    },
    "Taurus": {
        "start": date(2023, 4, 20),
        "end": date(2023, 5, 20)
    },
    "Gemini": {
        "start": date(2023, 5, 21),
        "end": date(2023, 6, 20)
    },
    "Cancer": {
        "start": date(2023, 6, 21),
        "end": date(2023, 7, 22)
    },
    "Leo": {
        "start": date(2023, 7, 23),
        "end": date(2023, 8, 22)
    },
    "Virgo": {
        "start": date(2023, 8, 23),
        "end": date(2023, 9, 22)
    },
    "Libra": {
        "start": date(2023, 9, 23),
        "end": date(2023, 10, 22)
    },
    "Scorpio": {
        "start": date(2023, 10, 23),
        "end": date(2023, 11, 21)
    },
    "Sagittarius": {
        "start": date(2023, 11, 22),
        "end": date(2023, 12, 21)
    },
    "Capricorn": {
        "start": date(2023, 12, 22),
        "end": date(2023, 1, 19)
    },
    "Aquarius": {
        "start": date(2023, 1, 20),
        "end": date(2023, 2, 18)
    },
    "Pisces": {
        "start": date(2023, 2, 19),
        "end": date(2023, 3, 20)
    },
}


data = [
    {
        "question": "What is your greatest attribute?",
        "answer": {
            "aries": "Courage",
            "taurus": "Persistence",
            "gemini": "Intelligence",
            "cancer": "Empathy",
            "leo": "Passion",
            "virgo": "Precision",
            "libra": "Diplomacy",
            "scorpio": "Intensity",
            "sagittarius": "Adventure",
            "capricorn": "Determination",
            "aquarius": "Originality",
            "pisces": "Intuition"
        }
    },
    {
        "question": "How do you deal with emotional challenges?",
        "answer": {
            "aries": "Taking action and confronting them directly.",
            "taurus": "Seeking comfort and emotional stability.",
            "gemini": "Talking to others to gain different perspectives.",
            "cancer": "Retreating to a safe space to process emotions.",
            "leo": "Expressing oneself confidently and seeking attention and support.",
            "virgo": "Analyzing the situation in detail to find practical solutions.",
            "libra": "Striving for emotional balance and trying to find harmony.",
            "scorpio": "Delving deep into emotions and seeking to understand the reasons behind them.",
            "sagittarius": "Facing challenges with optimism and seeking new perspectives.",
            "capricorn": "Keeping calm and finding rational solutions to overcome obstacles.",
            "aquarius": "Finding innovative ways to deal with emotions and seeking independence.",
            "pisces": "Surrendering to emotions and seeking creative ways to deal with them."
        }
    }

]

sign_description = {
    "aries": """
    Aries (March 21 - April 19):
    Aries is a fire sign ruled by Mars. 
    People of this sign are known for their energy, 
    courage, and impulsiveness. They are natural leaders, 
    often acting with determination and enthusiasm.
    """,
    "taurus": """
    Taurus (April 20 - May 20):
    Taurus is an earth sign ruled by Venus. 
    Taureans are practical, patient, and value stability. 
    They are known for their loyalty and appreciation for material comfort.
    """,
    "gemini": """
    Gemini (May 21 - June 20):
    Gemini is an air sign ruled by Mercury. 
    People of this sign are communicative, adaptable, and often have quick minds. 
    They are curious and appreciate variety.
    """,
    "cancer": """
    Cancer (June 21 - July 22):
    Cancer is a water sign ruled by the Moon. 
    Cancerians are highly sensitive and emotional. 
    They value family, home, and have a strong intuition.
    """,
    "leo": """
    Leo (July 23 - August 22):
    Leo is a fire sign ruled by the Sun. 
    Leos are charismatic, confident, and have a commanding presence. 
    They value creativity and often take on leadership roles.
    """,
    "virgo": """
    Virgo (August 23 - September 22):
    Virgo is an earth sign ruled by Mercury. 
    Virgos are analytical, methodical, and have a critical eye for detail. 
    They value organization and efficiency.
    """,
    "libra": """
    Libra (September 23 - October 22):
    Libra is an air sign ruled by Venus. 
    Librans are diplomatic, fair-minded, and value harmony in relationships. 
    They are known for their elegance and sense of style.
    """,
    "scorpio": """
    Scorpio (October 23 - November 21):
    Scorpio is a water sign ruled by Pluto (formerly Mars). 
    Scorpios are intense, passionate, and often possess a mysterious aura. 
    They value authenticity and loyalty.
    """,
    "sagittarius": """
    Sagittarius (November 22 - December 21):
    Sagittarius is a fire sign ruled by Jupiter. 
    Sagittarians are optimistic, adventurous, and have an expansive mind. 
    They value freedom and the pursuit of knowledge.
    """,
    "capricorn": """
    Capricorn (December 22 - January 19):
    Capricorn is an earth sign ruled by Saturn. 
    Capricorns are ambitious, disciplined, and take a pragmatic approach to life. 
    They value responsibility and long-term success.
    """,
    "aquarius": """
    Aquarius (January 20 - February 18):
    Aquarius is an air sign ruled by Uranus (formerly Saturn). 
    Aquarians are visionary, humanitarian, and value originality. 
    They are progressive and have an innovative mind.
    """,
    "pisces": """
    Pisces (February 19 - March 20):
    Pisces is a water sign ruled by Neptune (formerly Jupiter). 
    Pisceans are intuitive, sensitive, and often have an artistic nature. 
    They value compassion and spirituality.
    """
}
