const fs=require('fs');
const ids=['48528371','48537165','48526633','48528029','48533101'];
function clean(t){return t.replace(/<[^>]*>/g,'').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/&gt;/g,'>').replace(/&lt;/g,'<').replace(/&#x2F;/g,'/').replace(/&amp;/g,'&').replace(/&#62;/g,'>').replace(/\s+/g,' ').trim();}
function walk(node,arr){if(node.text)arr.push({t:clean(node.text),p:node.points||0,a:node.author});(node.children||[]).forEach(c=>walk(c,arr));}
for(const id of ids){
  const d=JSON.parse(fs.readFileSync('.hl-cache/hn-'+id+'.json','utf8'));
  const arr=[];(d.children||[]).forEach(c=>walk(c,arr));
  const good=arr.filter(x=>x.t.length>200).sort((a,b)=>b.p-a.p);
  const top=good[0]||{t:'(no substantive comment)',a:'-'};
  console.log('### '+id+': '+d.title+' ('+d.points+'pts/'+(d.num_comments||'?')+'c)');
  console.log('TOP(@'+top.a+'): '+top.t.slice(0,440));
  console.log('---');
}
