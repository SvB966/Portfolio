###
# Variables are directly accessible:
#   print(myvar)
# Updating a variable:
#   context.updateVariable('myvar', 'new-value')
###

import json

# Copy and display job variables for debugging
_glob = {name: val for name, val in globals().items()}
for name, val in _glob.items():
    if name.startswith('jv_'):
        print(f"[{name} --> {val}]")

# Input data, typically coming from previous transformation step
records = [
    {
        "INVESTMENTID": jv_investmentid,
        "PORTFOLIONAAM": jv_json_portfolionaam
    }
]

def is_filled(value):
    """Return True if value is not None and not empty."""
    return value is not None and value != ''


def build_portfolio_json(rows):
    """Build JSON payload for PortfolioInvestment API."""
    result = []
    for row in rows:
        item = {}
        if is_filled(row.get('INVESTMENTID')):
            item['InvestmentCode'] = row['INVESTMENTID']
        if is_filled(row.get('PORTFOLIONAAM')):
            item['PortfolioName'] = row['PORTFOLIONAAM']
        # always mark portfolio as planning
        item['PortfolioIsPlanning'] = True
        result.append(item)
    return json.dumps(result, indent=4)

json_output = build_portfolio_json(records)
context.updateVariable('jv_json', json_output)

# Display updated variables after JSON generation
_glob = {name: val for name, val in globals().items()}
for name, val in _glob.items():
    if name.startswith('jv_'):
        print(f"[{name} --> {val}]")
