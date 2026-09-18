from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI(title="Elshaddai's Enterprises")

html_page = """
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Elshaddai's Enterprises</title>
<style>
body{background:#060d1e;color:#e2e8f0;font-family:system-ui;padding:10px;margin:0}
.header{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #1e293b;padding:12px 0;flex-wrap:wrap;gap:8px}
.logo{font-weight:900;font-size:15px}.logo span{color:#facc15}
.live{border:1px solid #22c55e;color:#22c55e;border-radius:20px;padding:4px 10px;font-size:10px;font-weight:800}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:12px 0} @media(max-width:700px){.stats{grid-template-columns:1fr 1fr}}
.stat{background:#0f1c36;border:1px solid #1e355e;border-radius:10px;padding:10px}
.s-lbl{font-size:8px;color:#64748b;font-weight:800;letter-spacing:.08em}.s-val{font-weight:900;margin-top:4px;font-size:14px}
.btn{background:#facc15;color:#000;border:none;border-radius:8px;padding:10px 16px;font-weight:900;cursor:pointer}
.btn-sm{padding:5px 8px;font-size:11px;border-radius:6px;margin:2px;cursor:pointer;border:1px solid #1e355e;background:#0f1c36;color:#fff}
.btn-sm.green{border-color:#22c55e;color:#22c55e}.btn-sm.red{border-color:#ef4444;color:#ef4444}
.row{background:#0e1c36;border:1px solid #1e355e;border-radius:12px;padding:12px;margin:8px 0;display:grid;grid-template-columns:2fr 1fr 1fr 1fr auto;gap:10px;align-items:center}
@media(max-width:850px){.row{grid-template-columns:1fr;}}
.badge{font-size:8px;padding:2px 6px;border-radius:6px;font-weight:800;margin-left:4px}
.Active{background:#052e16;color:#22c55e}.Growing{background:#422006;color:#facc15}.Harvesting{background:#042f2e;color:#2dd4bf}.In{background:#1e1b4b;color:#a5b4fc}
.prog{height:4px;background:#0b1428;border-radius:4px;margin-top:6px;overflow:hidden}.fill{height:100%;background:linear-gradient(90deg,#facc15,#22c55e)}
.modal{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.75);display:none;align-items:center;justify-content:center;z-index:99}
.modal-box{background:#0f1c36;border:1px solid #1e355e;border-radius:14px;padding:20px;width:92%;max-width:400px}
input,select{width:100%;padding:10px;margin:6px 0;border-radius:8px;border:1px solid #1e355e;background:#060d1e;color:#fff;box-sizing:border-box}
</style></head><body>
<div class="header">
  <div class="logo">ELSHADDAI'S <span>ENTERPRISES</span> • HQ</div>
  <div style="display:flex;gap:8px;align-items:center">
    <button class="btn" onclick="openAdd()">+ ADD VENTURE</button>
    <div class="live">● LIVE</div>
  </div>
</div>

<div class="stats" id="stats"></div>
<div id="list"></div>

<div class="modal" id="modal"><div class="modal-box">
<h3 id="mTitle" style="margin-bottom:8px">Add Venture</h3>
<input id="vName" placeholder="Name e.g. Elshaddai's Rentals">
<input id="vLoc" placeholder="Location e.g. Majengo / Eldoret">
<select id="vType"><option>Real Estate</option><option>Agribusiness</option><option>Retail</option><option>Livestock</option><option>Aquaculture</option><option>Manufacturing</option><option>Health</option><option>Contract</option><option>Green Energy</option><option>Poultry</option><option>Horticulture</option></select>
<input id="vCap" type="number" placeholder="Capital KES">
<input id="vVal" type="number" placeholder="Current Value KES">
<input id="vInc" type="number" placeholder="Monthly Income KES">
<select id="vStatus"><option>Active</option><option>Growing</option><option>Harvesting</option><option>In Progress</option></select>
<div style="display:flex;gap:8px;margin-top:12px"><button class="btn" onclick="saveVenture()" style="flex:1">SAVE</button><button class="btn-sm" onclick="closeModal()" style="flex:1;text-align:center;padding:10px">CANCEL</button></div>
</div></div>

<script>
// VERSION CONTROL - Ukibadilisha figures hapa chini, badilisha v4 kuja v5 ndio investors waone mpya
const APP_VERSION = 'v4';
const SERVER_DEFAULT = [
{id:"RENTALS",name:"Elshaddai's Rentals",loc:"Musembe",type:"Real Estate",cap:2500000,val:3100000,inc:140000,status:"Active",icon:"🏠"},
{id:"SUGAR",name:"Majengo Sugarcane",loc:"Majengo",type:"Agribusiness",cap:900000,val:1100000,inc:150000,status:"Harvesting",icon:"🎋"},
{id:"KAHAWA",name:"Kahawa Farming",loc:"home farm",type:"Agribusiness",cap:800000,val:950000,inc:120000,status:"Growing",icon:"☕"},
{id:"HARDWARE",name:"Hardware Store",loc:"Linemoja",type:"Retail",cap:1200000,val:1450000,inc:200000,status:"Active",icon:"🔧"},
{id:"FISH",name:"Kandahari Fish Pond",loc:"Kandahari",type:"Aquaculture",cap:450000,val:600000,inc:85000,status:"Active",icon:"🐟"},
{id:"KUKU",name:"Kuku Project",loc:"nyumbani",type:"Poultry",cap:300000,val:420000,inc:65000,status:"Active",icon:"🐔"},
{id:"BANANA",name:"Banana Plantation",loc:"home farm",type:"Agribusiness",cap:600000,val:780000,inc:90000,status:"Growing",icon:"🍌"},
{id:"POSHO",name:"Bunyore PoshoMill",loc:"Bunyore",type:"Manufacturing",cap:500000,val:650000,inc:110000,status:"Active",icon:"🌽"},
{id:"PLASTIC",name:"Plastic Recycling Plant",loc:"kona nzuri",type:"Green Energy",cap:1500000,val:1800000,inc:180000,status:"Active",icon:"♻️"},
{id:"CHURCH",name:"St. Jordan Catholic Church Construction",loc:"St. Jordan",type:"Contract",cap:2000000,val:2200000,inc:0,status:"In Progress",icon:"⛪"},
{id:"GREEN",name:"Green House Production",loc:"home farm",type:"Horticulture",cap:700000,val:900000,inc:95000,status:"Active",icon:"🌱"},
{id:"DAIRY",name:"Dairy Production",loc:"home",type:"Livestock",cap:850000,val:1050000,inc:130000,status:"Active",icon:"🐄"},
{id:"PIG",name:"Pig Farming",loc:"home",type:"Livestock",cap:400000,val:550000,inc:75000,status:"Active",icon:"🐖"},
{id:"PHARMA",name:"Pharmacy",loc:"Nairobi",type:"Health",cap:1000000,val:1350000,inc:160000,status:"Active",icon:"💊"}
];

// HAPA NDIO FIX YA INVESTORS: Kama version ni mpya, overwrite localStorage ya kila mtu
let savedVersion = localStorage.getItem('elshaddai_version');
let ventures;
if(savedVersion!== APP_VERSION){
  ventures = SERVER_DEFAULT;
  localStorage.setItem('elshaddai_v3', JSON.stringify(ventures));
  localStorage.setItem('elshaddai_version', APP_VERSION);
} else {
  ventures = JSON.parse(localStorage.getItem('elshaddai_v3') || 'null') || SERVER_DEFAULT;
}

let editId=null;
function persist(){localStorage.setItem('elshaddai_v3',JSON.stringify(ventures)); render();}
function render(){
  let cap=ventures.reduce((s,v)=>s+(v.cap||0),0), val=ventures.reduce((s,v)=>s+(v.val||0),0), inc=ventures.reduce((s,v)=>s+(v.inc||0),0), pnl=val-cap;
  let growth = cap>0? ((val/cap-1)*100) : 0;
  document.getElementById('stats').innerHTML=`
  <div class="stat"><div class="s-lbl">TOTAL VALUE</div><div class="s-val">KES ${val.toLocaleString()}</div><div style="font-size:10px;color:#22c55e">+${pnl.toLocaleString()} PnL</div></div>
  <div class="stat"><div class="s-lbl">CAPITAL DEPLOYED</div><div class="s-val">KES ${cap.toLocaleString()}</div><div style="font-size:9px;color:#64748b">${ventures.length} Ventures</div></div>
  <div class="stat"><div class="s-lbl">MONTHLY INCOME</div><div class="s-val" style="color:#facc15">KES ${inc.toLocaleString()}</div></div>
  <div class="stat"><div class="s-lbl">GROWTH</div><div class="s-val">${growth.toFixed(1)}%</div></div>`;
  let h='';
  ventures.forEach((v,i)=>{
    let diff=(v.val||0)-(v.cap||0);
    let perc= v.cap>0? ((v.val/v.cap-1)*100) : 0;
    let perf=perc>=30?'🔥 TOP':perc>=15?'✅ GOOD':perc>=0?'↗️ OK':'⚠️ WATCH';
    let statusText=v.val>=v.cap*1.3?'High Performer':v.val>=v.cap?'Break Even+':'Recovering';
    let width = v.cap>0? Math.min(100, (v.val/v.cap)*70) : 0;
    h+=`<div class="row">
      <div><div style="font-weight:800">${v.icon} ${v.name}</div><div style="font-size:10px;color:#64748b">📍 ${v.loc} • ${v.type} <span class="badge ${v.status.replace(' ','')}">${v.status}</span> <span style="margin-left:6px;font-weight:800">${perf}</span></div><div class="prog"><div class="fill" style="width:${width}%"></div></div></div>
      <div><div class="s-lbl">CAPITAL</div><div style="font-weight:800">KES ${(v.cap||0).toLocaleString()}</div><div class="s-lbl" style="margin-top:4px">VALUE</div><div style="font-weight:800">KES ${(v.val||0).toLocaleString()}</div></div>
      <div><div class="s-lbl">PnL / GROWTH</div><div style="color:${diff>=0?'#22c55e':'#ef4444'};font-weight:800">${diff>=0?'+':''}${diff.toLocaleString()} (${perc.toFixed(1)}%)</div><div class="s-lbl" style="margin-top:4px">INCOME</div><div style="font-weight:800;color:#facc15">KES ${(v.inc||0).toLocaleString()}/mo</div></div>
      <div><div class="s-lbl">INVESTMENT STATUS</div><div style="font-size:12px;font-weight:700;margin-top:4px">${statusText}</div><div class="s-lbl" style="margin-top:6px">PERFORMANCE BUDGE</div><div style="font-size:12px">${perf}</div></div>
      <div style="display:flex;flex-direction:column"><button class="btn-sm green" onclick="modCap(${i},1)">+ Capital</button><button class="btn-sm red" onclick="modCap(${i},-1)">- Capital</button><button class="btn-sm" onclick="editV(${i})">Edit</button><button class="btn-sm" onclick="delV(${i})">Delete</button></div>
    </div>`;
  });
  document.getElementById('list').innerHTML=h;
}
function modCap(i,dir){
  let amt=parseInt(prompt(dir>0?'Add how much capital? (KES)':'Subtract how much? (KES)','50000'));
  if(!amt || isNaN(amt)) return;
  if(dir>0){ ventures[i].cap+=amt; ventures[i].val+=amt; } else { ventures[i].cap=Math.max(0,ventures[i].cap-amt); ventures[i].val=Math.max(0,ventures[i].val-amt); }
  persist();
}
function openAdd(){editId=null; document.getElementById('mTitle').innerText='Add New Venture'; document.getElementById('vName').value=''; document.getElementById('vLoc').value=''; document.getElementById('vCap').value=''; document.getElementById('vVal').value=''; document.getElementById('vInc').value=''; document.getElementById('modal').style.display='flex';}
function editV(i){editId=i; let v=ventures[i]; vName.value=v.name; vLoc.value=v.loc; vType.value=v.type; vCap.value=v.cap; vVal.value=v.val; vInc.value=v.inc; vStatus.value=v.status; document.getElementById('mTitle').innerText='Edit '+v.name; document.getElementById('modal').style.display='flex';}
function closeModal(){document.getElementById('modal').style.display='none';}
function saveVenture(){
  let obj={id:(vName.value.slice(0,4).toUpperCase()||'NEW')+Date.now().toString().slice(-3), name:vName.value, loc:vLoc.value, type:vType.value, cap:parseInt(vCap.value)||0, val:parseInt(vVal.value)||0, inc:parseInt(vInc.value)||0, status:vStatus.value, icon:"📦"};
  if(!obj.name) return alert('Name required');
  if(editId!==null){obj.id=ventures[editId].id; obj.icon=ventures[editId].icon; ventures[editId]=obj;} else ventures.push(obj);
  closeModal(); persist();
}
function delV(i){if(confirm('Delete '+ventures[i].name+'?')){ ventures.splice(i,1); persist(); }}
render();
</script></body></html>
"""

@app.get("/")
def home():
    return HTMLResponse(html_page)
