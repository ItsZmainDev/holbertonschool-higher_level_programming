def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Erreur : le template doit être une chaîne de caractères.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Erreur : attendees doit être une liste de dictionnaires.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        output = template
        for key in placeholders:
            value = attendee.get(key, "N/A")
            output = output.replace("{{" + key + "}}", str(value))
        with open(f"output_{idx}.txt", "w") as f:
            f.write(output)
