import logging
import azure.functions as func
from datetime import datetime, timedelta
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    today = datetime.utcnow().date()
    year = today.year
    month = today.month

    # Find last day of the month
    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)

    last_day = next_month - timedelta(days=1)

    # Find last Saturday
    last_saturday = last_day
    while last_saturday.weekday() != 5:  # Saturday = 5
        last_saturday -= timedelta(days=1)

    result = {
        "is_last_saturday": today == last_saturday.date(),
        "today": str(today),
        "last_saturday": str(last_saturday.date())
    }

    return func.HttpResponse(
        json.dumps(result),
        mimetype="application/json"
    )
