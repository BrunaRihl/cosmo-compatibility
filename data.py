from datetime import date

"""
Dictionary of zodiac sign dates.
Each sign has a start date and an end date.
Will be used to identify a person's zodiac sign
based on the provided date of birth.
"""
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


"""
'data' is a list of dictionaries, each containing a 'question'
and its corresponding 'answer' options for different zodiac signs.
This data structure is used to gather user input and provide
personality insights based on their zodiac sign.
"""
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
            "gemini": "Talking to others for different perspectives.",
            "cancer": "Retreating to a safe space to process emotions.",
            "leo": "Expressing confidently, seeking attention and support.",
            "virgo": "Analyzing the situation to find practical solutions.",
            "libra": "Striving for emotional balance, trying to find harmony.",
            "scorpio": "Exploring emotions deeply, seeking understanding.",
            "sagittarius": "Seeking new perspectives with optimism.",
            "capricorn": "Staying calm, finding rational solutions.",
            "aquarius": "Seeking new ways to handle emotions with independence",
            "pisces": "Embracing emotions, finding creative coping strategies."
        }
    },
    {
        "question": "Describe your approach to life in a few words:",
        "answer": {
            "aries": "Entrepreneurial",
            "taurus": "Balanced",
            "gemini": "Communicative",
            "cancer": "Sensitive",
            "libra": "Social",
            "leo": "Charismatic",
            "virgo": "Analytical",
            "scorpio": "Courageous",
            "sagittarius": "Spontaneous",
            "capricorn": "Practical",
            "aquarius": "Innovative",
            "pisces": "Creative"
        }
    },
    {
        "question": "Describe your communication style in one word:",
        "answer": {
            "aries": "Direct",
            "taurus": "Calm",
            "gemini": "Expressive",
            "cancer": "Empathetic",
            "leo": "Assertive",
            "virgo": "Logical",
            "libra": "Diplomatic",
            "scorpio": "Profound",
            "sagittarius": "Enthusiastic",
            "capricorn": "Practical",
            "aquarius": "Innovative",
            "pisces": "Sensitive"
        }
    },
    {
        "question": "What activity do you prefer in your free time?",
        "answer": {
            "aries": "Practice a sport",
            "taurus": "Read a book",
            "gemini": "Attend social events",
            "cancer": "Explore a new place",
            "leo": "Create something new",
            "virgo": "Work on personal projects",
            "libra": "Meet new people",
            "scorpio": "Investigate interesting topics",
            "sagittarius": "Go on an adventure",
            "capricorn": "Focus on professional growth",
            "aquarius": "Try new things",
            "pisces": "Meditate or reflect"
        }
    },
    {
        "question": "Choose the best fit for your relationship preferences:",
        "answer": {
            "aries": "Passionate and intense",
            "taurus": "Stable and loyal",
            "gemini": "Communicative and curious",
            "cancer": "Deep and intense",
            "leo": "Social and outgoing",
            "virgo": "Balanced and fair",
            "libra": "Harmonious and cooperative",
            "scorpio": "Intense and passionate",
            "sagittarius": "Open to new ideas",
            "capricorn": "Stable and loyal",
            "aquarius": "Innovative and independent",
            "pisces": "Empathetic and sensitive"
        }
    },
    {
        "question": "How do you deal with unexpected changes?",
        "answer": {
            "aries": "Adapt quickly and embrace the change.",
            "taurus": "Assess the situation and then make adjustments.",
            "gemini": "Appreciate the novelty and seek new possibilities",
            "cancer": "Get emotionally shaken, yet find support to cope.",
            "leo": "Face the change with confidence and determination.",
            "virgo": "Analyze details and create a plan to handle the change.",
            "libra": "Seek balance, find ways to handle change harmoniously.",
            "scorpio": "Explore the reasons behind and adapt intensely.",
            "sagittarius": "Seize the opportunity as a new adventure.",
            "capricorn": "Maintain composure and devise a strategic response.",
            "aquarius": "View change as a chance for growth and innovation.",
            "pisces": "Feel change deeply, seek emotional connection with it."
        }
    },
    {
        "question": "How do you approach challenges in teamwork?",
        "answer": {
            "aries": "Take the lead and take immediate action.",
            "taurus": "Contribute with my experience and stability.",
            "gemini": "Share ideas and collaborate with diverse views.",
            "cancer": "Focus on creating an environment of emotional support.",
            "leo": "Inspire the group to achieve ambitious goals.",
            "virgo": "Pay attention to details and organize tasks.",
            "libra": "Seek to balance opinions and find consensus solutions.",
            "scorpio": "Dive deep into issues and seek solutions intensely.",
            "sagittarius": "Bring enthusiasm and long-term perspective.",
            "capricorn": "Offer a practical and methodical approach.",
            "aquarius": "Introduce innovation and new ways of doing things.",
            "pisces": "Contribute with sensitivity and empathy to the group."
        }
    },
    {
        "question": "How do you handle pressure?",
        "answer": {
            "aries": "Harness the adrenaline and focus on meeting deadlines.",
            "taurus": "Remain calm and work consistently.",
            "gemini": "Break the work into stages and maintain agility.",
            "cancer": "Seek emotional support and carefully organize my time.",
            "leo": "See pressure as an opportunity to showcase my ability.",
            "virgo": "Meticulously organize my time and resources.",
            "libra": "Seek to balance quality with efficiency.",
            "scorpio": "Concentrate intensely and face challenges head-on.",
            "sagittarius": "Stay positive, focus on problem-solving.",
            "capricorn": "Plan strategically and keep my focus on the goal.",
            "aquarius": "Innovate, find new approaches to deal with pressure.",
            "pisces": "Trust my intuition, get creative to handle situations."
        }
    },
    {
        "question": "How do you motivate yourself to face daily challenges?",
        "answer": {
            "aries": "Competing and surpassing limits.",
            "taurus": "Stabilizing and achieving personal goals.",
            "gemini": "Experiencing and learning.",
            "cancer": "Creating an emotionally secure environment.",
            "leo": "Shining and being recognized.",
            "virgo": "Pursuing perfection and efficiency.",
            "libra": "Seeking balance and harmony.",
            "scorpio": "Delving and transforming.",
            "sagittarius": "Adventuring and growing personally.",
            "capricorn": "Pursuing long-term goals.",
            "aquarius": "Innovating and pursuing new ideas.",
            "pisces": "Connecting emotionally and empathizing with others."
        }
    }
]

"""
'sign_description' is a dictionary containing detailed descriptions of each
zodiac sign. Each sign's description includes information about their ruling
element, characteristics, and values. This data structure can be used to
provide users with insights into their zodiac sign's traits
and tendencies at the end of the test.
"""
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
    People of this sign are communicative, adaptable, and often
    have quick minds.
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
    Capricorns are ambitious, disciplined, and take a pragmatic
    approach to life.
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
