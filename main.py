from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_page = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Elshaddai Ventures</title>
<style>
body{font-family:system-ui;background:#f6f7fb;padding:12px}
.card{background:white;border-radius:14px;padding:12px;margin-bottom:10px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{padding:8px;border-bottom:1px solid #eee;text-align:left}
.badge{padding:3px 8px;border-radius:20px;background:#eef;font-size:11px}
input{width:90px;padding:5px;border:1px solid #ddd;border-radius:6px}
</style>
</head>
<body>
<h2>🌾 Elshaddai Ventures - Live</h2>
<div id="app"></div>

<script>
// HIZI NDIZO FIGURES ZITAKAZOONEKANA KWA KILA MTU - INVESTOR NA WEWE
// Ukitaka ku-edit tena, edit hapa tu kwa code, usi-edit kwa browser
const SERVER_VENTURES = [
  {id:1, icon:"🏠", name:"Elshaddai's Rentals", cap:3000000, val:3100000, inc:14000, exp:5000},
  {id:2, icon:"🌿", name:"Majengo Sugarcane", cap:150000, val:160000, inc:150000, exp:20000},
  {id:3, icon:"🏡", name:"home farm", cap:50000, val:52000, inc:1000, exp:500},
  {id:4, icon:"📍", name:"Linemoja", cap:20000, val:21000, inc:2000, exp:800},
  {id:5, icon:"🏠", name:"nyumbani", cap:10000, val:10000, inc:0, exp:0},
  {id:6, icon:"⭐", name:"kona nzuri", cap:10000, val:11000, inc:0, exp:0},
  {id:7, icon:"🌾", name:"Musembe Farm", cap:80000, val:85000, inc:12000, exp:3000},
  {id:8, icon:"🐄", name:"Dairy Unit", cap:120000, val:125000, inc:18000, exp:6000},
  {id:9, icon:"🐓", name:"Poultry", cap:30000, val:32000, inc:8000, exp:3000},
  {id:10, icon:"🏪", name:"Duka", cap:60000, val:65000, inc:15000, exp:5000},
  {id:11, icon:"🚜", name:"Tractor Hire", cap:200000, val:210000, inc:20000, exp:5000},
  {id:12, icon:"💧", name:"Maji Project", cap:40000, val:42000, inc:5000, exp:1000},
  {id:13, icon:"🌽", name:"Maize Store", cap:90000, val:95000, inc:10000, exp:2000},
  {id:14, icon:"🏗️", name:"Plots", cap:500000, val:550000, inc:0, exp:0}
];

// FIX KUBWA: Force kila mtu kuona SERVER_VENTURES, si localStorage yake
localStorage.setItem('elshaddai_v3', JSON.stringify(SERVER_VENTURES));
let ventures = SERVER_VENTURES;

function render(){
  let html = `<div class="card"><table><tr><th>Venture</th><th>Daily</th><th>PnL</th><th>Growth</th><th>Income</th></tr>`;
  ventures.forEach(v=>{
    let daily = v.inc/30;
    let pnl = v.val - v.cap;
    // FIX ya Infinity% - kama cap ni 0, growth ni 0%
    let perc = v.cap > 0 ? ((v.val/v.cap - 1)*100) : 0;
    html += `<tr>
      <td>${v.icon} ${v.name}</td>
      <td>KES ${Math.round(daily).toLocaleString()}</td>
      <td>KES ${pnl.toLocaleString()}</td>
      <td><span class="badge">${perc.toFixed(1)}%</span></td>
      <td><input type="number" value="${v.inc}" onchange="updateInc(${v.id}, this.value)"></td>
    </tr>`;
  });
  html += `</table></div>`;
  html += `<div class="card"><b>Total Daily: KES ${Math.round(ventures.reduce((s,v)=>s+v.inc/30,0)).toLocaleString()}</b><br>
  <small>Figures hizi ndizo investors wataona - same kwa kila mtu</small></div>`;
  document.getElementById('app').innerHTML = html;
}
function updateInc(id, val){
  let v = ventures.find(x=>x.id==id);
  v.inc = parseInt(val)||0;
  localStorage.setItem('elshaddai_v3', JSON.stringify(ventures));
  render();
}
render();
</script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return html_page
