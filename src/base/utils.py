def check_ncsu_email(email):
    """Check if the given email belongs to NCSU email id."""
    parts = email.split("@")
    if parts[-1] != "ncsu.edu":
        return False
    return True
