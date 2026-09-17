from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime

app = FastAPI(title="Tilisi Command Center")

units = [
    {"id": "T-01", "type": "2BR", "tenant": "John Kamau", "rent": 35000, "status": "Occupied", "paid": True},
    {"id": "T-02", "type": "2BR", "tenant": "Mary Wanjiku", "rent": 35000, "status": "Occupied", "paid": False},
    {"id": "T-03", "type": "1BR", "tenant": "", "rent": 25000, "status": "Vacant", "paid": False},
    {"id": "T-04", "type": "3BR", "tenant": "David Ochieng", "rent": 45000, "status": "Occupied", "paid": True},
    {"id": "T-05", "type": "2BR", "tenant": "Grace Akinyi", "rent": 35000, "status": "Occupied", "paid": True},
]

payments = [
    {"date": "2026-09-10", "unit": "T-01", "tenant": "John Kamau", "amount": 35000, "method": "M-Pesa", "code": "QJ8K2L9M"},
    {"date": "2026-09-12", "unit": "T-04", "tenant": "David Ochieng", "amount": 45000, "method": "M-Pesa", "code": "QJ8K3M1N"},
]

def get_stats():
    total = len(units)
    occ = len([u for u in units if u["status"]=="Occupied"])
    exp = sum(u["rent"] for u in units if u["status"]=="Occupied")
    coll = sum(u["rent"] for u in units if u["status"]=="Occupied" and u["paid"])
    rate = int((coll/exp*100) if exp else 0)
    return total, occ, total-occ, exp, coll, rate

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    total, occ, vac, exp, coll, rate = get_stats()
    rows = "".join([f"<tr><td><b>{u['id']}</b> {u['type']}</td><td>{u['tenant'] or 'Vacant'}</td><td>{u['rent']:,}</td><td>{u['status']}</td><td>{'Paid' if u['paid'] else 'Due'}</td></tr>" for u in units])
    pays = "".join([f"<tr><td>{p['date']}</td><td>{p['unit']} {p['tenant']}</td><td>{p['amount']:,}</td><td>{p['code']}</td></tr>" for p in payments])
    html = f"""
    <html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
    <title>Tilisi Command Center</title>
    <style>body{{background:#0f172a;color:#fff;font-family:sans-serif;padding:16px}}
    .card{{background:#1e293b;border-radius:16px;padding:16px;margin:8px 0}}
    .grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
    .val{{font-size:26px;font-weight:800}} td,th{{padding:8px;border-top:1px solid #334155;font-size:13px}}
    th{{color:#94a3b8;font-size:11px;text-align:left}}</style></head><body>
    <h2>TILISI<span style='color:#38bdf8'>.COMMAND</span> - LIVE 🟢</h2>
    <div class='grid'><div class='card'><div>Total Units</div><div class='val'>{total}</div><div>{occ} Occupied / {vac} Vacant</div></div>
    <div class='card'><div>Collection</div><div class='val'>{rate}%</div><div>Sep 2026</div></div>
    <div class='card'><div>Expected</div><div class='val'>KES {exp:,}</div></div>
    <div class='card'><div>Collected</div><div class='val'>KES {coll:,}</div></div></div>
    <div class='card'><h3>UNITS - TILISI</h3><table><tr><th>Unit</th><th>Tenant</th><th>Rent</th><th>Status</th><th>Paid</th></tr>{rows}</table></div>
    <div class='card'><h3>PAYMENTS M-PESA</h3><table><tr><th>Date</th><th>Unit</th><th>Amount</th><th>Code</th></tr>{pays}</table></div>
    <div style='text-align:center;color:#475569;font-size:11px;margin-top:20px'>Tilisi Command Center - {datetime.now().strftime('%d %b %Y')} - LIVE</div>
    </body></html>"""
    return HTMLResponse(html)

@app.get("/api/stats")
async def stats():
    t,o,v,e,c,r = get_stats()
    return {"total":t,"occupied":o,"vacant":v,"expected":e,"collected":c,"rate":r,"units":units}
