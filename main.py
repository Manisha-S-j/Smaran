from flask import Flask, render_template, request, redirect, url_for
import math, os

app = Flask(__name__)

# Demo in-memory reminders (so templates render)
reminders = [
    {"title": "Medicine", "time": "10:00", "status": "Missed"},
    {"title": "Meal", "time": "14:00", "status": "Pending"},
]

# Carbon calculation constants (demo values)
E_CLOUD_JOULES = 0.50
E_LOCAL_JOULES = 0.08
CO2_PER_JOULE = 0.00000027

def compute_carbon_savings(num_inferences_per_day, days):
    per_inf_energy_saved = max(0.0, E_CLOUD_JOULES - E_LOCAL_JOULES)
    energy_saved_total = per_inf_energy_saved * num_inferences_per_day * days
    co2_saved_total = energy_saved_total * CO2_PER_JOULE
    energy_eff_pct = round((1.0 - (E_LOCAL_JOULES / E_CLOUD_JOULES)) * 100, 1) if E_CLOUD_JOULES > 0 else 0
    per_inf_co2_saved = per_inf_energy_saved * CO2_PER_JOULE
    return round(co2_saved_total, 8), round(energy_saved_total, 3), round(per_inf_co2_saved, 10), energy_eff_pct

@app.route('/')
def index():
    return render_template('index.html', reminders=reminders)

@app.route('/sustainability')
def sustainability():
    # mock metrics used to show quick summary
    default_n = 20
    default_days = 30
    co2_saved, energy_saved, per_inf_co2, eff_pct = compute_carbon_savings(default_n, default_days)
    return render_template('sustainability.html',
                           co2_saved=co2_saved,
                           energy_saved=energy_saved,
                           energy_efficiency=eff_pct,
                           total_predictions=default_n*default_days)

@app.route('/carbon-calculator', methods=['GET','POST'])
def carbon_calculator():
    result = None
    defaults = {"num_inferences_per_day": 20, "days": 30}
    if request.method == 'POST':
        try:
            n = int(request.form.get('num_inferences_per_day', defaults['num_inferences_per_day']))
            d = int(request.form.get('days', defaults['days']))
            n = max(0, min(n, 100000))
            d = max(0, min(d, 3650))
            co2_saved, energy_saved, per_inf_co2, eff_pct = compute_carbon_savings(n, d)
            phones_charged_eq = round((energy_saved / 10000), 4)
            trees_planted_eq = round(co2_saved / 21.77, 6)
            result = {
                "num_inferences_per_day": n,
                "days": d,
                "co2_saved": co2_saved,
                "energy_saved_joules": energy_saved,
                "per_inf_co2": per_inf_co2,
                "efficiency_pct": eff_pct,
                "phones_charged_eq": phones_charged_eq,
                "trees_planted_eq": trees_planted_eq
            }
        except Exception:
            result = None
    return render_template('carbon.html', result=result, defaults=defaults)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
