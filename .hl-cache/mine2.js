const fs=require('fs');
function clean(t){return t.replace(/<[^>]*>/g,'').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/&gt;/g,'>').replace(/&lt;/g,'<').replace(/&#x2F;/g,'/').replace(/&amp;/g,'&').replace(/\s+/g,' ').trim();}
function walk(node,arr){if(node.text)arr.push({t:clean(node.text),p:node.points||0,a:node.author});(node.children||[]).forEach(c=>walk(c,arr));}
for(const id of ['48528029','48537165']){
  const d=JSON.parse(fs.readFileSync('.hl-cache/hn-'+id+'.json','utf8'));
  const arr=[];(d.children||[]).forEach(c=>walk(c,arr));
  const good=arr.filter(x=>x.t.length>200 && !/porn|lora|abliterated/i.test(x.t)).sort((a,b)=>b.p-a.p);
  console.log('### '+id+': '+d.title);
  good.slice(0,3).forEach((c,i)=>console.log('['+i+' @'+c.a+' '+c.p+'p]: '+c.t.slice(0,400)+'\n'));
  console.log('---');
}
