import os

def generate_invitations(template, attendees):
    # Type checks
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Empty input checks
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, person in enumerate(attendees, start=1):
        # Replace each placeholder, using .get() and defaulting to "N/A"
        filled_template = template
        filled_template = filled_template.replace("{name}", str(person.get("name", "N/A") or "N/A"))
        filled_template = filled_template.replace("{event_title}", str(person.get("event_title", "N/A") or "N/A"))
        filled_template = filled_template.replace("{event_date}", str(person.get("event_date", "N/A") or "N/A"))
        filled_template = filled_template.replace("{event_location}", str(person.get("event_location", "N/A") or "N/A"))

        # Write to file
        output_filename = f"output_{idx}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as output_file:
                output_file.write(filled_template)
        except Exception as e:
            print(f"Error writing to {output_filename}: {e}")

