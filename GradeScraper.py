import requests
import csv
from tabulate import tabulate

BASE = "https://bb.imperial.ac.uk"

def load_user_id():
    try:
        with open("user_id.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def save_user_id(uid):
    with open("user_id.txt", "w") as f:
        f.write(uid)

def load_cookies(filename="cookies.txt"):
    cookies = {}
    with open(filename, "r") as f:
        for line in f:
            if not line.startswith("#") and line.strip():
                parts = line.split("\t")
                if len(parts) >= 7:
                    cookies[parts[5]] = parts[6].strip()
    return cookies

def api_get(endpoint, cookies):
    response = requests.get(BASE + endpoint, cookies=cookies)
    if response.status_code != 200:
        raise Exception(f"API Error {response.status_code}: {response.text}")
    return response.json()

def find_scores(obj):
    results = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("score", "manualScore") and str(v) != "0.0" and str(v) != "0":
                results.append(v)
            else:
                results.extend(find_scores(v))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(find_scores(item))
    return results

def main():
    print("Loading cookies from cookies.txt...")
    cookies = load_cookies()

    print("Checking for saved user ID...")
    user_id = load_user_id()

    if user_id:
        print(f"Loaded saved user ID: {user_id}")
    else:
        print("No saved user ID found — discovering user ID...")
        user_info = api_get("/learn/api/public/v1/users/me", cookies)
        user_id = user_info.get("id")
        print(f"Discovered user ID: {user_id}")
        save_user_id(user_id)
        print("User ID saved for future runs.")

    print("Fetching course list...")
    course_data = api_get(f"/learn/api/v1/users/{user_id}/memberships?expand=course&limit=200", cookies)
    courses = course_data.get("results", [])

    results = []

    print("\nScraping course results...\n")

    for course in courses:
        course_name = course.get("course", {}).get("name")
        course_id = course.get("course", {}).get("id")

        grades_api = (
            f"/learn/api/v1/courses/{course_id}/gradebook/grades?"
            f"isExcludedFromCourseUserActivity=true&limit=100&userId={user_id}"
        )

        print(f"- {course_name}")
        try:
            grade_data = api_get(grades_api, cookies)
            scores = find_scores(grade_data)
            results.append([course_name, scores[0] if scores else "––"])
        except Exception as e:
            if "bb-rest-course-is-private" in str(e):
                print(f"  → Skipped (course private)")
                results.append([course_name, "PRIVATE"])
            else:
                print(f"  → Error: {e}")
                results.append([course_name, "ERROR"])

    print("\n===== Course Grades =====")
    print(tabulate(results, headers=["Course", "Score"], tablefmt="fancy_grid"))

    with open("marks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Course", "Score"])
        writer.writerows(results)

    print("\nSaved results to marks.csv\n")

if __name__ == "__main__":
    main()
