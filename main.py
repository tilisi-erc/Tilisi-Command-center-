from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(title="Elshaddai's Enterprises")

ventures = [
    {"id":"RENTALS","name":"Majengo Rentals","loc":"Eldoret","cap":2500000,"val":3100000,"inc":140000,"icon":"🏠","status":"Active"},
    {"id":"KAHAWA","name":"Kahawa Farming","loc":"Nandi Hills","cap":800000,"val":950000,"inc":120000,"icon":"☕","status":"Growing"},
    {"id":"HARDWARE","name":"Hardware Store","loc":"Eldoret CBD","cap":1200000,"val":1450000,"inc":200000,"icon":"🔧","status":"Active"},
    {"id":"FISH","name":"Kandahari Fish Pond","loc":"Kandahari","cap":450000,"val":600000,"inc":85000,"icon":"🐟","status":"Active"},
    {"id":"KUKU","name":"Kuku Project","loc":"Majengo","cap":300000,"val":420000,"inc":65000,"icon":"🐔","status":"Active"},
    {"id":"BANANA","name":"Banana Plantation","loc":"Bunyore","cap":600000,"val":780000,"inc":90000,"icon":"🍌","status":"Growing"},
    {"id":"SUGAR","name":"Majengo Sugarcane","loc":"Majengo","cap":900000,"val":1100000,"inc":150000,"icon":"🎋","status":"Harvesting"},
    {"id":"POSHO","name":"Bunyore PoshoMill","loc":"Bunyore","cap":500000,"val":650000,"inc":110000,"icon":"🌽","status":"Active"},
    {"id":"PLASTIC","name":"Plastic Recycling","loc":"Eldoret","cap":1500000,"val":1800000,"inc":180000,"icon":"♻️","status":"Active"},
    {"id":"CHURCH","name":"St. Jordan Construction","loc":"St. Jordan","cap":2000000,"val":2200000,"inc":0,"icon":"⛪","status":"In Progress"},
    {"id":"GREEN","name":"Green House","loc":"Eldoret","cap":700000,"val":900000,"inc":95000,"icon":"🌱","status":"Active"},
    {"id":"DAIRY","name":"Dairy Production","loc":"Bunyore","cap":850000,"val":1050000,"inc":130000,"icon":"🐄","status":"Active"},
    {"id":"PIG","name":"Pig Farming","loc":"Kandahari","cap":400000,"val":550000,"inc":75000,"icon":"🐖","status":"Active"},
    {"id":"PHARMA","name":"Pharmacy","loc":"Eldoret","cap":1000000,"val":1350000,"inc":160000,"icon":"💊","status":"Active"},
]

@app.get("/", response_class=HTMLResponse)
def dashboard():
    total_cap = sum(v["cap"] for v in ventures)
    total_val = sum(v["val"] for v in ventures)
    total_inc = sum(v["inc"] for v in ventures)
    pnl = total_val - total_cap
    growth = (total_val/total_cap-1)*100

    cards_html = ""
    for v in ventures:
        diff = v["val"] - v["cap"]
        perc = (v["val"]/v["cap"]-1)*100
        cards_html += f'<div style="background:#0e1c36;border:1px solid #1e355e;border-radius:12px;padding:12px"><div style="display:flex;justify-content:space-between;font-size:10px;color:#94a3b8;font-weight:800"><span>{v["icon"]} {v["id"]}</span><span>{v["status"]}</span></div><div style="font-weight:800;margin:6px 0">{v["name"]}</div><div style="font-size:10px;color:#64748b">📍 {v["loc"]}</div><div style="display:flex;gap:10px;margin-top:8px"><div><div style="font-size:8px;color:#64748b">VALUE</div><div style="font-weight:800;font-size:13px">KES {v["val"]:,}</div></div><div><div style="font-size:8px;color:#64748b">INCOME</div><div style="font-weight:800;font-size:13px;color:#facc15">KES {v["inc"]:,}</div></div></div><div style="font-size:10px;color:#94a3b8;margin-top:6px">{diff:+,} • {perc:+.1f}%</div></div>'

    html = """
    <html><head><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Elshaddai's Enterprises</title></head><body style="background:#060d1e;color:#e2e8f0;padding:12px;font-family:system-ui">
    <div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #1e293b;margin-bottom:10px">
      <div style="font-weight:900">ELSHADDAI'S <span style="color:#facc15">ENTERPRISES</span> • HQ</div>
      <div style="border:1px solid #22c55e;color:#22c55e;border-radius:20px;padding:3px 10px;font-size:9px">● LIVE</div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px;margin-bottom:12px">
      <div style="background:#0f1c36;border:1px solid #1e355e;border-radius:12px;padding:10px"><div style="font-size:9px;color:#64748b">TOTAL VALUE</div><div style="font-size:16px;font-weight:900">KES """ + f"{total_val:,}" + """</div><div style="font-size:10px;color:#22c55e">""" + f"{pnl:+,} PnL" + """</div></div>
      <div style="background:#0f1c36;border:1px solid #1e355e;border-radius:12px;padding:10px"><div style="font-size:9px;color:#64748b">CAPITAL</div><div style="font-size:16px;font-weight:900">KES """ + f"{total_cap:,}" + """</div></div>
      <div style="background:#0f1c36;border:1px solid #1e355e;border-radius:12px;padding:10px"><div style="font-size:9px;color:#64748b">MONTHLY INCOME</div><div style="font-size:16px;font-weight:900;color:#facc15">KES """ + f"{total_inc:,}" + """</div></div>
      <div style="background:#0f1c36;border:1px solid #1e355e;border-radius:12px;padding:10px"><div style="font-size:9px;color:#64748b">GROWTH</div><div style="font-size:16px;font-weight:900">""" + f"{growth:+.1f}%" + """</div></div>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">""" + cards_html + """</div>
    <div style="text-align:center;color:#334155;font-size:10px;margin:20px">Elshaddai's Enterprises • """ + datetime.now().strftime('%d %b %Y') + """ • Built with Meta AI</div>
    </body></html>
    """
    return HTMLResponse(html)
