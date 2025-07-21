import json

# Capture current globals so we can inspect variable values
saved_globals = {g: globals()[g] for g in list(globals())}

# Display variables starting with 'jv_'
var_prefix = 'jv_'
for name in sorted(saved_globals):
    if name.startswith(var_prefix):
        print(f"[{name} --> {saved_globals[name]}]")

# Example record constructed from Matillion variables
portfolio_data = [
    {
        "INVESTMENTID": jv_investmentid,
        "PORTFOLIONAAM": jv_json_portfolionaam,
    }
]


def is_filled(value):
    """Return True when value is not None and not an empty string."""
    return value is not None and value != ""


def make_json_from_portfolio(records):
    """Build PortfolioInvestment JSON from a list of records."""
    json_items = []
    for rec in records:
        if not is_filled(rec.get("INVESTMENTID")):
            raise ValueError("INVESTMENTID mag niet leeg zijn")
        if not is_filled(rec.get("PORTFOLIONAAM")):
            raise ValueError("PORTFOLIONAAM mag niet leeg zijn")

        json_items.append({
            "InvestmentCode": rec["INVESTMENTID"],
            "PortfolioIsPlanning": True,
            "PortfolioName": rec["PORTFOLIONAAM"],
        })
    return json.dumps(json_items, indent=4)


# Generate the JSON string
json_output = make_json_from_portfolio(portfolio_data)

# Update the Matillion variable with the resulting JSON
context.updateVariable('jv_json', json_output)

# Print the variables again for logging
saved_globals = {g: globals()[g] for g in list(globals())}
for name in sorted(saved_globals):
    if name.startswith(var_prefix):
        print(f"[{name} --> {saved_globals[name]}]")
