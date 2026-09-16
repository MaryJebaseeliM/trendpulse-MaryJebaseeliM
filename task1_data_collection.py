import requests
import time
import os
import json
from datetime import datetime



# API endpoints
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header required by the task
HEADERS = {"User-Agent": "TrendPulse/1.0"}

# Category keywords
CATEGORIES = {
    "technology": [
        "AI", "software", "tech", "code", "computer",
        "data", "cloud", "API", "GPU", "LLM"
    ],
    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],
    "sports": [
        "NFL", "NBA", "FIFA", "sport", "game", "team",
        "player", "league", "championship"
    ],
    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "NASA", "genome"
    ],
    "entertainment": [
        "movie", "film", "music", "Netflix", "game",
        "book", "show", "award", "streaming"
    ]
}


def assign_category(title):
    """Assign a category based on keywords in the title."""

    title_lower = title.lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                return category

    return None


def fetch_story(story_id):
    """Fetch details of one Hacker News story."""

    try:
        response = requests.get(
            ITEM_URL.format(story_id),
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:
        print(f"Error fetching story {story_id}: {e}")
        return None


def main():

    # -------------------------------------------------
    # Step 1: Fetch the top 500 story IDs
    # -------------------------------------------------

    try:
        response = requests.get(
            TOP_STORIES_URL,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        # Fetch only the first 500 IDs
        story_ids = response.json()[:500]

        print(f"Fetched {len(story_ids)} top story IDs.")

    except requests.RequestException as e:
        print(f"Error fetching top story IDs: {e}")
        return


    # -------------------------------------------------
    # Storage for collected stories
    # -------------------------------------------------

    collected_stories = []

    # Keep track of stories collected for each category
    category_counts = {
        category: 0
        for category in CATEGORIES
    }


    # -------------------------------------------------
    # Step 2: Process each category
    # -------------------------------------------------

    for category in CATEGORIES:

        print(f"\nCollecting stories for category: {category}")

        for story_id in story_ids:

            # Stop once we have 25 stories
            # for the current category
            if category_counts[category] >= 25:
                break

            story = fetch_story(story_id)

            # If request failed, move to next story
            if not story:
                continue

            # Only process actual stories
            if story.get("type") != "story":
                continue

            # Make sure the story has a title
            if "title" not in story:
                continue

            # Determine category from title
            assigned = assign_category(story["title"])

            if assigned == category:

                # Avoid duplicate stories
                if any(
                    existing["post_id"] == story.get("id")
                    for existing in collected_stories
                ):
                    continue

                collected_stories.append({
                    "post_id": story.get("id"),
                    "title": story.get("title"),
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by"),
                    "collected_at": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                })

                category_counts[category] += 1

        # Wait 2 seconds BETWEEN categories
        time.sleep(2)


    # -------------------------------------------------
    # Step 3: Save results to JSON
    # -------------------------------------------------

    # Create data folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Create today's filename
    filename = (
        f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
    )

    # Save stories
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            collected_stories,
            file,
            indent=2,
            ensure_ascii=False
        )


    # -------------------------------------------------
    # Final output
    # -------------------------------------------------

    print(
        f"\nCollected {len(collected_stories)} stories. "
        f"Saved to {filename}"
    )

    print("\nStories collected by category:")

    for category, count in category_counts.items():
        print(f"{category}: {count}")


# Run the program
if __name__ == "__main__":
    main()

