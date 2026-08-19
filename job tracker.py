import sqlite3
import csv
from datetime import date

DB = "jobs.db"


def db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            status TEXT DEFAULT 'Applied',
            date TEXT,
            notes TEXT
        )
    """)
    return conn


def add_job():
    company = input("Company: ").strip()
    role = input("Job Role: ").strip()
    notes = input("Notes: ").strip()

    if not company or not role:
        print("Company and role are required!")
        return

    conn = db()
    conn.execute(
        "INSERT INTO jobs (company, role, status, date, notes) VALUES (?, ?, ?, ?, ?)",
        (company, role, "Applied", date.today().isoformat(), notes)
    )
    conn.commit()
    conn.close()

    print("✅ Job added successfully!")


def view_jobs():
    conn = db()
    jobs = conn.execute("SELECT * FROM jobs ORDER BY id DESC").fetchall()
    conn.close()

    if not jobs:
        print("\nNo applications found.")
        return

    print("\n" + "=" * 75)
    print(f"{'ID':<5}{'Company':<20}{'Role':<25}{'Status':<15}")
    print("=" * 75)

    for job in jobs:
        print(f"{job[0]:<5}{job[1][:18]:<20}{job[2][:23]:<25}{job[3]:<15}")

    print("=" * 75)


def update_status():
    view_jobs()

    try:
        job_id = int(input("\nEnter Job ID: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    print("""
1. Applied
2. Screening
3. Interview
4. Offer
5. Rejected
6. Withdrawn
""")

    statuses = {
        "1": "Applied",
        "2": "Screening",
        "3": "Interview",
        "4": "Offer",
        "5": "Rejected",
        "6": "Withdrawn"
    }

    choice = input("Choose status: ")

    if choice not in statuses:
        print("❌ Invalid status.")
        return

    conn = db()
    cursor = conn.execute(
        "UPDATE jobs SET status = ? WHERE id = ?",
        (statuses[choice], job_id)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount:
        print("✅ Status updated!")
    else:
        print("❌ Job not found.")


def search_jobs():
    keyword = input("Search company or role: ").strip()

    conn = db()
    jobs = conn.execute("""
        SELECT * FROM jobs
        WHERE company LIKE ? OR role LIKE ?
        ORDER BY id DESC
    """, (f"%{keyword}%", f"%{keyword}%")).fetchall()
    conn.close()

    if not jobs:
        print("No matching jobs found.")
        return

    for job in jobs:
        print(
            f"\n#{job[0]} | {job[1]} | {job[2]}"
            f"\nStatus: {job[3]}"
            f"\nApplied: {job[4]}"
            f"\nNotes: {job[5]}"
        )


def statistics():
    conn = db()

    total = conn.execute("SELECT COUNT(*) FROM jobs").fetchone()[0]

    print("\n📊 APPLICATION STATISTICS")
    print("-" * 35)
    print(f"Total Applications: {total}")

    statuses = conn.execute("""
        SELECT status, COUNT(*)
        FROM jobs
        GROUP BY status
    """).fetchall()

    for status, count in statuses:
        percentage = (count / total * 100) if total else 0
        print(f"{status:<12}: {count} ({percentage:.1f}%)")

    conn.close()


def export_csv():
    conn = db()
    jobs = conn.execute("SELECT * FROM jobs").fetchall()
    conn.close()

    if not jobs:
        print("Nothing to export.")
        return

    with open("jobs_export.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["ID", "Company", "Role", "Status", "Date", "Notes"]
        )
        writer.writerows(jobs)

    print("✅ Exported to jobs_export.csv")


def delete_job():
    view_jobs()

    try:
        job_id = int(input("\nEnter Job ID to delete: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    conn = db()
    cursor = conn.execute(
        "DELETE FROM jobs WHERE id = ?",
        (job_id,)
    )
    conn.commit()
    conn.close()

    print("✅ Job deleted!" if cursor.rowcount else "❌ Job not found.")


def main():
    while True:
        print("""
╔══════════════════════════════════════╗
║       💼 JOB APPLICATION TRACKER     ║
╠══════════════════════════════════════╣
║ 1. Add Job Application               ║
║ 2. View Applications                 ║
║ 3. Update Application Status         ║
║ 4. Search Jobs                       ║
║ 5. View Statistics                   ║
║ 6. Export to CSV                     ║
║ 7. Delete Application                ║
║ 8. Exit                              ║
╚══════════════════════════════════════╝
""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            update_status()
        elif choice == "4":
            search_jobs()
        elif choice == "5":
            statistics()
        elif choice == "6":
            export_csv()
        elif choice == "7":
            delete_job()
        elif choice == "8":
            print("Thanks for using Job Tracker! 👋")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()