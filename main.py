from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(title="Elshaddai's Enterprises")

# YOUR FULL EMPIRE PORTFOLIO
ventures = [
    {"id":"RENTALS","name":"Majengo Rentals","type":"Real Estate","location":"Eldoret","capital":2500000,"value":3100000,"status":"Active","icon":"🏠","income":140000},
    {"id":"KAHAWA","name":"Kahawa Farming","type":"Agribusiness","location":"Nandi Hills","capital":800000,"value":950000,"status":"Growing","icon":"☕","income":120000},
    {"id":"HARDWARE","name":"Hardware Store","type":"Retail","location":"Eldoret CBD","capital":1200000,"value":1450000,"status":"Active","icon":"🔧","income":200000},
    {"id":"FISH","name":"Kandahari Fish Pond","type":"Aquaculture","location":"Kandahari","capital":450000,"value":600000,"status":"Active","icon":"🐟","income":85000},
    {"id":"KUKU","name":"Kuku Project","type":"Poultry","location":"Majengo","capital":300000,"value":420000,"status":"Active","icon":"🐔","income":65000},
    {"id":"BANANA","name":"Banana Plantation","type":"Agribusiness","location":"Bunyore","capital":600000,"value":780000,"status":"Growing","icon":"🍌","income":90000},
    {"id":"SUGAR","name":"Majengo Sugarcane","type":"Agribusiness","location":"Majengo","capital":900000,"value":1100000,"status":"Harvesting","icon":"🎋","income":150000},
    {"id":"POSHO","name":"Bunyore PoshoMill","type":"Manufacturing","location":"Bunyore","capital":500000,"value":650000,"status":"Active","icon":"🌽","income":110000},
    {"id":"PLASTIC","name":"Plastic Recycling Plant","type":"Green Energy","location":"Eldoret","capital":1500000,"value":1800000,"status":"Active","icon":"♻️","income":180000},
    {"id":"CHURCH","name":"St. Jordan Church Construction","type":"Contract","location":"St. Jordan","capital":2000000,"value":2200000,"status":"In Progress","icon":"⛪","income":0},
    {"id":"GREEN","name":"Green House Production","type":"Horticulture","location":"Eldoret","capital":700000,"value":900000,"status":"Active","icon":"🌱","income":95000},
    {"id":"DAIRY","name":"Dairy Production","type":"Livestock","location":"Bunyore","capital":850000,"value":1050000,"status":"Active","icon":"🐄","income":130000},
    {"id":"PIG","name":"Pig Farming","type":"Livestock","location":"Kandahari","capital":400000,"value":550000,"status":"Active","icon":"🐖","income":75000},
    {"id":"PHARMA","name":"Pharmacy","type":"Health","location":"Eldoret","capital":1000000,"value":1350000,"status":"Active","icon":"💊","income":160000},
]

def get_stats():
    total_cap = sum(v["capital"] for v in ventures)
    total_val = sum(v["value"] for v in ventures)
    total_inc = sum(v["income"] for v in ventures)
    pnl = total_val - total_cap
    active = len([v for v in ventures if v["status"]=="Active"])
    return total_cap, total_val, total_inc, pnl, active

@app.get("/", response_class=HTMLResponse)
def dashboard():
    cap, val, inc, pnl, active = get_stats()
    cards = "".join([f"""
    <div class="card">
      <div class="c-head"><span>{v['icon']} {v['id']}</span><span class="badge {v['status'].lower().replace(' ','')}">{v['status']}</span></div>
      <div class="c-title">{v['name']}</div>
      <div class="c-loc">📍 {v['location']} • {v['type']}</div>
      <div class="c-grid"><div><div class="lbl">Value</div><div class="val">KES {v['value']:,}</div></div><div><div class="lbl">Monthly Income</div><div class="inc">KES {v['income']:,}</div></div></div>
      <div class="bar"><div class="fill" style="width:{min(100, v['value']/v['capital']*70)}%"></div></div>
      <div class="pnl">{v['value']-v['capital']:+,} PnL • {((v['value']/v['capital']-1)*100):+.1f}%</div>
    </div>""" for v in ventures])

    return f"""
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Elshaddai's Enterprises</title>
<style>
*{{box-sizing:border-box;margin:0;font-family:Inter,system-ui}}
body{{background:#060d1e;color:#e2e8f0;padding:12px}}
.header{{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid #1e293b;margin-bottom:12px}}
.logo{{font-weight:900;letter-spacing:.05em}} .logo span{{color:#facc15}}
.live{{border:1px solid #22c55e;color:#22c55e;border-radius:20px;padding:3px 10px;font-size:9px;font-weight:800}}
.stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:12px}} @media(max-width:700px){{.stats{{grid-template-columns:1fr 1fr}}}}
.stat{{background:#0f1c36;border:1px solid #1e355e;border-radius:12px;padding:12px}} .stat .lbl{{font-size:9px;color:#64748b;letter-spacing:.1em;font-weight:800}} .stat .big{{font-size:18px;font-weight:900;margin-top:4px}}
.grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}} @media(max-width:900px){{.grid{{grid-template-columns:repeat(2,1fr)}}} @media(max-width:600px){{.grid{{grid-template-columns:1fr}}}}
.card{{background:#0e1c36;border:1px solid #1e355e;border-radius:14px;padding:12px}} .c-head{{display:flex;justify-content:space-between;font-size:10px;font-weight:800;color:#94a3b8}}
.badge{{padding:2px 6px;border-radius:6px;font-size:8px}} .active{{background:#052e16;color:#22c55e}} .growing{{background:#422006;color:#facc15}} .harvesting{{background:#042f2e;color:#2dd4bf}} .in{{background:#1e1b4b;color:#a5b4fc}}
.c-title{{font-weight:800;margin:6px 0;font-size:14px}} .c-loc{{font-size:10px;color:#64748b;margin-bottom:8px}} .c-grid{{display:grid;grid-template-columns:1fr 1fr;gap:6px}} .lbl{{font-size:8px;color:#64748b}} .val{{font-size:13px;font-weight:800}} .inc{{font-size:13px;font-weight:800;color:#facc15}}
.bar{{height:4px;background:#0b1428;border-radius:4px;margin:8px 0;overflow:hidden}} .fill{{height:100%;background:linear-gradient(90deg,#facc15,#22c55e)}}
.pnl{{font-size:10px;color:#94a3b8}}
</style></head><body>
<div class="header"><div class="logo">ELSHADDAI'S <span>ENTERPRISES</span> • HQ</div><div class="live">● LIVE EMPIRE</div></div>
<div class="stats">
<div class="stat"><div class="lbl">TOTAL PORTFOLIO VALUE</div><div class="big">KES {val:,}</div><div style="font-size:10px;color:#22c55e">{pnl:+,} PnL</div></div>
<div class="stat"><div class="lbl">TOTAL CAPITAL DEPLOYED</div><div class="big">KES {cap:,}</div><div style="font-size:10px;color:#64748b">{active} Active ventures</div></div>
<div class="stat"><div class="lbl">MONTHLY INCOME</div><div class="big" style="color:#facc15">KES {inc:,}</div><div style="font-size:10px;color:#64748b">From 14 ventures</div></div>
<div class="stat"><div class="lbl">EMPIRE GROWTH</div><div class="big">{((val/cap-1)*100):+.1f}%</div><div style="font-size:10px;color:#22c55e">Since inception</div></div>
</div>
<div class="grid">{cards}</div>
<div style="text-align:center;color:#334155;font-size:10px;margin:20px">Elshaddai's Enterprises • {datetime.now().strftime('%d %b %Y')} • Ahero - Eldoret - Bunyore - Nandi • Built with Meta AI</div>
</body></html>
"""

@app.get("/api/portfolio")
def api(): cap,val,inc,pnl,active=get_stats(); return {"capital":cap,"value":val,"income":inc,"pnl":pnl,"ventures":ventures}
